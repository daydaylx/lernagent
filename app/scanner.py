import os
from dataclasses import dataclass
from pathlib import Path

IGNORE_DIRS = frozenset({
    "node_modules", ".git", "dist", "build", "coverage",
    ".cache", ".vite", ".next", ".nuxt", "venv", ".venv",
    "__pycache__", ".idea", ".vscode", ".repo_tutor",
})

SUPPORTED_EXTENSIONS = frozenset({
    ".py", ".ts", ".tsx", ".js", ".jsx",
    ".md", ".json", ".yaml", ".yml", ".toml", ".css", ".scss",
})


@dataclass
class ScannedFile:
    path: str
    size: int
    extension: str


def scan(root: Path) -> list[ScannedFile]:
    results: list[ScannedFile] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for filename in filenames:
            filepath = Path(dirpath) / filename
            ext = filepath.suffix.lower()
            if ext in SUPPORTED_EXTENSIONS:
                relative = str(filepath.relative_to(root))
                results.append(ScannedFile(
                    path=relative,
                    size=filepath.stat().st_size,
                    extension=ext,
                ))
    return sorted(results, key=lambda f: f.path)
