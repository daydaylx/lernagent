from pathlib import Path

from app.scanner import scan

FIXTURE = Path(__file__).parent / "fixtures" / "sample_project"


def test_ignores_node_modules() -> None:
    files = scan(FIXTURE)
    paths = [f.path for f in files]
    assert not any("node_modules" in p for p in paths)


def test_ignores_pycache() -> None:
    files = scan(FIXTURE)
    paths = [f.path for f in files]
    assert not any("__pycache__" in p for p in paths)


def test_finds_python_files() -> None:
    files = scan(FIXTURE)
    extensions = {f.extension for f in files}
    assert ".py" in extensions


def test_finds_tsx_files() -> None:
    files = scan(FIXTURE)
    extensions = {f.extension for f in files}
    assert ".tsx" in extensions


def test_results_sorted() -> None:
    files = scan(FIXTURE)
    paths = [f.path for f in files]
    assert paths == sorted(paths)


def test_captures_size() -> None:
    files = scan(FIXTURE)
    py_files = [f for f in files if f.extension == ".py"]
    assert py_files, "no .py files found"
    assert all(f.size > 0 for f in py_files)
