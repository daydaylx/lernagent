import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from app.scanner import ScannedFile

CACHE_FILE = Path(".repo_tutor") / "file_cache.json"


@dataclass
class CachedFile:
    path: str
    sha256: str
    status: str  # "new" | "unchanged" | "changed"


def compute_hash(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_cache(root: Path) -> dict[str, str]:
    cache_path = root / CACHE_FILE
    if not cache_path.exists():
        return {}
    with open(cache_path) as f:
        return json.load(f)


def save_cache(root: Path, data: dict[str, str]) -> None:
    cache_dir = root / ".repo_tutor"
    cache_dir.mkdir(exist_ok=True)
    with open(cache_dir / "file_cache.json", "w") as f:
        json.dump(data, f, indent=2)


def update(root: Path, files: list[ScannedFile]) -> list[CachedFile]:
    old = load_cache(root)
    new: dict[str, str] = {}
    results: list[CachedFile] = []
    for f in files:
        sha = compute_hash(root / f.path)
        new[f.path] = sha
        if f.path not in old:
            status = "new"
        elif old[f.path] == sha:
            status = "unchanged"
        else:
            status = "changed"
        results.append(CachedFile(path=f.path, sha256=sha, status=status))
    save_cache(root, new)
    return results
