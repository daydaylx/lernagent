import json
from pathlib import Path

from app.cache import update
from app.scanner import ScannedFile


def _make_file(root: Path, name: str, content: str = "hello") -> ScannedFile:
    p = root / name
    p.write_text(content)
    return ScannedFile(path=name, size=p.stat().st_size, extension=Path(name).suffix)


def test_new_file_status(tmp_path: Path) -> None:
    f = _make_file(tmp_path, "a.py")
    results = update(tmp_path, [f])
    assert results[0].status == "new"


def test_unchanged_status(tmp_path: Path) -> None:
    f = _make_file(tmp_path, "a.py")
    update(tmp_path, [f])
    results = update(tmp_path, [f])
    assert results[0].status == "unchanged"


def test_changed_status(tmp_path: Path) -> None:
    f = _make_file(tmp_path, "a.py", "v1")
    update(tmp_path, [f])
    (tmp_path / "a.py").write_text("v2")
    results = update(tmp_path, [f])
    assert results[0].status == "changed"


def test_cache_file_created(tmp_path: Path) -> None:
    f = _make_file(tmp_path, "a.py")
    update(tmp_path, [f])
    assert (tmp_path / ".repo_tutor" / "file_cache.json").exists()


def test_cache_stores_no_source(tmp_path: Path) -> None:
    content = "secret source content"
    f = _make_file(tmp_path, "a.py", content)
    update(tmp_path, [f])
    cache_json = (tmp_path / ".repo_tutor" / "file_cache.json").read_text()
    data = json.loads(cache_json)
    assert content not in cache_json
    assert all(len(v) == 64 for v in data.values()), "values must be sha256 hex strings"
