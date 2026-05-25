import inspect

import pytest

from app.explainer import (
    SMALL_FILE_CHARS,
    ExplainContext,
    build_prompt,
)
from app.indexer import FileIndex


def _make_index(
    path: str = "app/foo.py",
    language: str = "python",
    imports: list[str] | None = None,
    exports: list[str] | None = None,
    probable_role: str = "Service",
) -> FileIndex:
    return FileIndex(
        path=path,
        language=language,
        imports=imports if imports is not None else ["os", "sys"],
        exports=exports if exports is not None else [],
        probable_role=probable_role,
    )


def _make_ctx(**kwargs: object) -> ExplainContext:
    defaults: dict = dict(
        filepath="app/foo.py",
        content="def hello():\n    pass\n",
        index=_make_index(),
        project_name="MeinProjekt",
        related_files=[],
    )
    defaults.update(kwargs)
    return ExplainContext(**defaults)


def test_prompt_contains_filepath() -> None:
    ctx = _make_ctx(filepath="src/utils/parser.py")
    prompt = build_prompt(ctx)
    assert "src/utils/parser.py" in prompt


def test_prompt_contains_content() -> None:
    ctx = _make_ctx(content="def greet(): return 'Hallo'")
    prompt = build_prompt(ctx)
    assert "def greet(): return 'Hallo'" in prompt


def test_prompt_contains_language() -> None:
    ctx = _make_ctx(index=_make_index(language="typescript"))
    prompt = build_prompt(ctx)
    assert "typescript" in prompt


def test_prompt_contains_imports() -> None:
    ctx = _make_ctx(index=_make_index(imports=["pathlib", "json"]))
    prompt = build_prompt(ctx)
    assert "pathlib" in prompt
    assert "json" in prompt


def test_prompt_contains_exports_or_placeholder() -> None:
    ctx_with = _make_ctx(index=_make_index(exports=["MyClass"]))
    assert "MyClass" in build_prompt(ctx_with)

    ctx_empty = _make_ctx(index=_make_index(exports=[]))
    assert "(keine)" in build_prompt(ctx_empty)


def test_mode_label_in_prompt() -> None:
    assert "Standarderklärung" in build_prompt(_make_ctx(), mode="normal")
    assert "Einfache Erklärung" in build_prompt(_make_ctx(), mode="simple")
    assert "Zusammenhang" in build_prompt(_make_ctx(), mode="context")
    assert "Lernfragen" in build_prompt(_make_ctx(), mode="quiz")


def test_german_output_structure_in_normal_mode() -> None:
    prompt = build_prompt(_make_ctx(), mode="normal")
    for heading in [
        "Kurz gesagt",
        "Warum gibt es diese Datei",
        "Wichtige Bestandteile",
        "Ablauf Schritt für Schritt",
        "Wichtige Fachbegriffe",
        "Zusammenhänge mit anderen Dateien",
        "Schwierige oder riskante Stellen",
        "Merksatz",
    ]:
        assert heading in prompt, f"Abschnitt fehlt: {heading!r}"


def test_large_file_truncated_with_warning() -> None:
    big_content = "x" * (SMALL_FILE_CHARS + 1)
    ctx = _make_ctx(content=big_content)
    prompt = build_prompt(ctx)
    assert "HINWEIS" in prompt or "WARNUNG" in prompt
    assert big_content not in prompt


def test_very_large_file_has_warning() -> None:
    huge_content = "y" * 90_001
    ctx = _make_ctx(content=huge_content)
    prompt = build_prompt(ctx)
    assert "WARNUNG" in prompt


def test_unknown_mode_raises_value_error() -> None:
    ctx = _make_ctx()
    with pytest.raises(ValueError, match="Unbekannter Modus"):
        build_prompt(ctx, mode="fantasy")


def test_no_network_imports() -> None:
    import app.explainer as explainer_module

    source = inspect.getsource(explainer_module)
    for forbidden in ("requests", "httpx", "urllib", "http.client", "socket"):
        assert forbidden not in source, f"Verbotener Import gefunden: {forbidden!r}"
