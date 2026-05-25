from __future__ import annotations

from dataclasses import dataclass, field

from app.indexer import FileIndex

SMALL_FILE_CHARS = 25_000
MEDIUM_FILE_CHARS = 80_000

_VALID_MODES = {"simple", "normal", "context", "quiz"}

_MODE_LABELS: dict[str, str] = {
    "simple": "Einfache Erklärung",
    "normal": "Standarderklärung",
    "context": "Zusammenhang und Einbettung",
    "quiz": "Lernfragen",
}

_GERMAN_STRUCTURE = """\
Struktur der Ausgabe:

1. Kurz gesagt
2. Warum gibt es diese Datei?
3. Wichtige Bestandteile
4. Ablauf Schritt für Schritt
5. Wichtige Fachbegriffe
6. Zusammenhänge mit anderen Dateien
7. Schwierige oder riskante Stellen
8. Merksatz"""


@dataclass
class ExplainContext:
    filepath: str
    content: str
    index: FileIndex
    project_name: str = ""
    related_files: list[str] = field(default_factory=list)


def build_prompt(ctx: ExplainContext, mode: str = "normal") -> str:
    if mode not in _VALID_MODES:
        raise ValueError(f"Unbekannter Modus: {mode!r}. Erlaubt: {sorted(_VALID_MODES)}")

    content_block, size_warning = _prepare_content(ctx.content)

    parts = [
        _build_header(ctx, mode),
        _build_file_section(ctx, content_block, size_warning),
        _build_project_section(ctx),
        _build_output_instructions(mode),
    ]
    return "\n\n".join(parts)


def _prepare_content(content: str) -> tuple[str, str]:
    chars = len(content)
    if chars <= SMALL_FILE_CHARS:
        return content, ""
    if chars <= MEDIUM_FILE_CHARS:
        excerpt = content[:SMALL_FILE_CHARS]
        warning = (
            f"[HINWEIS: Datei zu groß ({chars} Zeichen). "
            f"Erste {SMALL_FILE_CHARS} Zeichen angezeigt. Rest ausgeblendet.]"
        )
        return excerpt, warning
    excerpt = content[:SMALL_FILE_CHARS]
    warning = (
        f"[WARNUNG: Datei sehr groß ({chars} Zeichen, >{MEDIUM_FILE_CHARS}). "
        "Nur ein Ausschnitt verfügbar. Struktur und Imports bevorzugen.]"
    )
    return excerpt, warning


def _build_header(ctx: ExplainContext, mode: str) -> str:
    label = _MODE_LABELS[mode]
    return f"# RepoTutor – {label}\n\nDatei: `{ctx.filepath}`"


def _build_file_section(ctx: ExplainContext, content_block: str, size_warning: str) -> str:
    idx = ctx.index
    imports_str = "\n".join(f"- {i}" for i in idx.imports) if idx.imports else "- (keine)"
    exports_str = "\n".join(f"- {e}" for e in idx.exports) if idx.exports else "- (keine)"

    lines = [
        "## Dateiinformationen",
        f"- **Pfad:** `{ctx.filepath}`",
        f"- **Sprache:** {idx.language}",
        f"- **Wahrscheinliche Rolle:** {idx.probable_role}",
        "",
        "**Imports:**",
        imports_str,
        "",
        "**Exports:**",
        exports_str,
    ]
    if size_warning:
        lines += ["", size_warning]
    lines += ["", "## Dateiinhalt", "", f"```\n{content_block}\n```"]
    return "\n".join(lines)


def _build_project_section(ctx: ExplainContext) -> str:
    project = ctx.project_name if ctx.project_name else "(nicht angegeben)"
    lines = [
        "## Projektkontext",
        f"- **Projektname:** {project}",
    ]
    if ctx.related_files:
        lines += ["", "**Verwandte Dateien:**"]
        lines += [f"- `{f}`" for f in ctx.related_files]
    else:
        lines.append("- **Verwandte Dateien:** (keine angegeben)")
    return "\n".join(lines)


def _build_output_instructions(mode: str) -> str:
    base = (
        "## Aufgabe\n\n"
        "Erkläre die oben gezeigte Datei auf Deutsch. "
        "Schreibe in einfacher, klarer Sprache. "
        "Erfinde keine Informationen. "
        "Wenn du unsicher bist, markiere das offen."
    )

    if mode == "simple":
        return base + "\n\nHalte die Erklärung kurz und einfach. Nur das Wichtigste."

    if mode == "quiz":
        return (
            "## Aufgabe\n\n"
            "Erzeuge Lernfragen zur oben gezeigten Datei auf Deutsch.\n\n"
            "Schreibe in einfacher, klarer Sprache. "
            "Erfinde keine Informationen. "
            "Wenn du unsicher bist, markiere das offen.\n\n"
            "Format:\n\n"
            "1. [Frage]\n"
            "   Antwort: ...\n\n"
            "Mindestens 5 Fragen, maximal 10."
        )

    if mode == "context":
        return (
            base
            + "\n\n"
            + _GERMAN_STRUCTURE
            + "\n\nBetone besonders Abschnitt 6 (Zusammenhänge mit anderen Dateien)."
        )

    # normal
    return base + "\n\n" + _GERMAN_STRUCTURE
