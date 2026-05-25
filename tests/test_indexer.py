from pathlib import Path

from app.indexer import (
    detect_language,
    extract_python_imports,
    extract_ts_exports,
    extract_ts_imports,
    index_file,
    infer_role,
)

FIXTURE = Path(__file__).parent / "fixtures" / "sample_project"


def test_python_imports() -> None:
    source = (FIXTURE / "main.py").read_text()
    imports = extract_python_imports(source)
    assert "os" in imports
    assert "pathlib" in imports
    assert "app.config" in imports


def test_python_syntax_error_safe() -> None:
    result = extract_python_imports("def broken(")
    assert result == []


def test_tsx_imports() -> None:
    source = (FIXTURE / "src" / "components" / "Button.tsx").read_text()
    imports = extract_ts_imports(source)
    assert "react" in imports


def test_tsx_exports() -> None:
    source = (FIXTURE / "src" / "components" / "Button.tsx").read_text()
    exports = extract_ts_exports(source)
    assert "Button" in exports


def test_probable_role_component() -> None:
    assert infer_role("src/components/Button.tsx") == "UI-Komponente"


def test_probable_role_hook() -> None:
    assert infer_role("src/hooks/useData.ts") == "Custom Hook"


def test_probable_role_config() -> None:
    assert infer_role("app/config.py") == "Konfiguration"


def test_language_detection() -> None:
    assert detect_language(".py") == "python"
    assert detect_language(".tsx") == "typescript"
    assert detect_language(".js") == "javascript"
    assert detect_language(".md") == "unknown"


def test_index_file_python(tmp_path: Path) -> None:
    f = tmp_path / "utils.py"
    f.write_text("import os\nfrom pathlib import Path\n")
    result = index_file(f, "utils.py")
    assert result.language == "python"
    assert "os" in result.imports
    assert result.probable_role == "Unbekannt"


def test_index_file_tsx() -> None:
    filepath = FIXTURE / "src" / "components" / "Button.tsx"
    result = index_file(filepath, "src/components/Button.tsx")
    assert result.language == "typescript"
    assert "react" in result.imports
    assert result.probable_role == "UI-Komponente"
