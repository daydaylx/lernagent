from __future__ import annotations

from pathlib import Path
from typing import Iterable

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.message import Message
from textual.screen import Screen
from textual.widgets import (
    DirectoryTree,
    Footer,
    Header,
    Input,
    Label,
    RadioButton,
    RadioSet,
    Static,
)

from app.ai_client import stream_response
from app.config import DEFAULT_CONFIG
from app.explainer import ExplainContext, build_prompt
from app.indexer import index_file
from app.scanner import SUPPORTED_EXTENSIONS

_MODES = ("simple", "normal", "context", "quiz")


class _TutorTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [p for p in paths if p.is_dir() or p.suffix.lower() in SUPPORTED_EXTENSIONS]


class _PathChosen(Message):
    def __init__(self, path: Path) -> None:
        super().__init__()
        self.path = path


class PathInputScreen(Screen):
    DEFAULT_CSS = """
    PathInputScreen {
        align: center middle;
    }
    PathInputScreen Label {
        padding: 1 0;
        text-style: bold;
    }
    PathInputScreen Input {
        width: 64;
    }
    """
    BINDINGS = [Binding("escape", "app.quit", "Beenden")]

    def compose(self) -> ComposeResult:
        yield Label("RepoTutor – Projektpfad eingeben:")
        yield Input(placeholder="/pfad/zum/projekt", id="path-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        raw = event.value.strip()
        if not raw:
            return
        path = Path(raw).expanduser().resolve()
        if not path.is_dir():
            inp = self.query_one("#path-input", Input)
            inp.value = ""
            inp.placeholder = f"Kein Verzeichnis: {raw} – bitte erneut eingeben"
            return
        self.post_message(_PathChosen(path))


class RepoTutorApp(App):
    CSS = """
    #main-horizontal {
        height: 1fr;
    }
    #left-panel {
        width: 30%;
        min-width: 22;
        height: 100%;
        border-right: tall $panel;
    }
    #tree-container {
        height: 1fr;
        width: 100%;
    }
    #tree {
        height: 100%;
    }
    #mode-select {
        height: auto;
        padding: 0 1;
        border-top: solid $panel;
    }
    #output-scroll {
        width: 1fr;
        height: 100%;
    }
    #output-static {
        padding: 1 2;
        width: 100%;
    }
    #status-bar {
        height: 1;
        background: $panel;
        color: $text-muted;
        padding: 0 1;
    }
    #followup-input {
        height: 3;
    }
    """

    BINDINGS = [Binding("ctrl+q", "quit", "Beenden")]

    def __init__(self, project_path: str | Path | None = None) -> None:
        super().__init__()
        self._project_path: Path | None = (
            Path(project_path).expanduser().resolve() if project_path else None
        )
        self._selected_file: Path | None = None
        self._current_mode: str = "normal"
        self._output_text: str = ""
        self._stream_id: int = 0

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="main-horizontal"):
            with Vertical(id="left-panel"):
                yield Container(id="tree-container")
                with RadioSet(id="mode-select"):
                    yield RadioButton("simple")
                    yield RadioButton("normal", value=True)
                    yield RadioButton("context")
                    yield RadioButton("quiz")
            with VerticalScroll(id="output-scroll"):
                yield Static(
                    "Datei im Projektbaum auswählen, um eine Erklärung zu starten.",
                    id="output-static",
                )
        yield Static("", id="status-bar")
        yield Input(placeholder="> Rückfrage eingeben...", id="followup-input")
        yield Footer()

    def on_mount(self) -> None:
        if self._project_path:
            self._mount_tree(self._project_path)
            self._update_status()
        else:
            self.push_screen(PathInputScreen())

    def on__path_chosen(self, event: _PathChosen) -> None:
        self.pop_screen()
        self._project_path = event.path
        self._mount_tree(event.path)
        self._update_status()

    def _mount_tree(self, path: Path) -> None:
        container = self.query_one("#tree-container", Container)
        container.mount(_TutorTree(path, id="tree"))

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        self._selected_file = event.path
        self._clear_output()
        self._update_status()
        self._trigger_explanation()

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self._current_mode = _MODES[event.index]
        if self._selected_file:
            self._clear_output()
            self._trigger_explanation()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        question = event.value.strip()
        if not question:
            return
        event.input.clear()
        if not self._selected_file:
            self._set_status("Erst eine Datei im Projektbaum auswählen.")
            return
        self._stream_followup(question)

    def _clear_output(self) -> None:
        self._output_text = ""
        self.query_one("#output-static", Static).update("")

    def _trigger_explanation(self) -> None:
        if not self._selected_file or not self._project_path:
            return
        try:
            relative = self._selected_file.relative_to(self._project_path)
            idx = index_file(self._selected_file, str(relative))
            content = self._selected_file.read_text(encoding="utf-8", errors="replace")
            ctx = ExplainContext(
                filepath=str(relative),
                content=content,
                index=idx,
                project_name=self._project_path.name,
            )
            prompt = build_prompt(ctx, self._current_mode)
        except Exception as exc:
            self._set_status(f"Fehler beim Erstellen des Prompts: {exc}")
            return
        self._set_status(f"Erkläre [{self._current_mode}] ...")
        self._start_stream(prompt)

    def _stream_followup(self, question: str) -> None:
        if not self._selected_file or not self._project_path:
            return
        relative = self._selected_file.relative_to(self._project_path)
        prompt = (
            f"Kontext: Ich habe gerade die Datei `{relative}` "
            f"im Modus `{self._current_mode}` erklärt.\n\n"
            f"Frage: {question}\n\n"
            "Antworte auf Deutsch, kurz und präzise."
        )
        self._output_text += f"\n\n---\n**Rückfrage:** {question}\n\n"
        self.query_one("#output-static", Static).update(self._output_text)
        self._set_status("Rückfrage wird beantwortet ...")
        self._start_stream(prompt)

    def _start_stream(self, prompt: str) -> None:
        self._stream_id += 1
        sid = self._stream_id
        self.run_worker(
            lambda: self._do_stream(prompt, sid),
            group="stream",
            exclusive=True,
            thread=True,
        )

    def _do_stream(self, prompt: str, sid: int) -> None:
        try:
            for chunk in stream_response(prompt, DEFAULT_CONFIG):
                if self._stream_id != sid:
                    return
                self.call_from_thread(self._append_chunk, chunk, sid)
            if self._stream_id == sid:
                self.call_from_thread(self._on_stream_done)
        except Exception as exc:
            if self._stream_id == sid:
                self.call_from_thread(self._set_status, f"Fehler: {exc}")
                self.call_from_thread(self._on_stream_done)

    def _append_chunk(self, chunk: str, sid: int) -> None:
        if self._stream_id != sid:
            return
        self._output_text += chunk
        self.query_one("#output-static", Static).update(self._output_text)
        self.query_one("#output-scroll", VerticalScroll).scroll_end(animate=False)

    def _on_stream_done(self) -> None:
        self._update_status()

    def _update_status(self) -> None:
        path_str = str(self._project_path) if self._project_path else "kein Pfad"
        file_str = self._selected_file.name if self._selected_file else "keine Datei"
        self._set_status(
            f"Pfad: {path_str}  |  Datei: {file_str}  |  Modus: {self._current_mode}"
        )

    def _set_status(self, text: str) -> None:
        self.query_one("#status-bar", Static).update(text)


if __name__ == "__main__":
    RepoTutorApp().run()
