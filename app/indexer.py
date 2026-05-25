import ast
import re
from dataclasses import dataclass, field
from pathlib import Path

LANGUAGE_MAP: dict[str, str] = {
    ".py": "python",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
}

_TS_IMPORT_RE = re.compile(r"""from\s+['"]([^'"]+)['"]""")
_TS_EXPORT_RE = re.compile(
    r"export\s+(?:default\s+)?(?:const|function|class|interface|type|enum)\s+(\w+)"
)


@dataclass
class FileIndex:
    path: str
    language: str
    imports: list[str] = field(default_factory=list)
    exports: list[str] = field(default_factory=list)
    probable_role: str = "Unbekannt"


def detect_language(extension: str) -> str:
    return LANGUAGE_MAP.get(extension, "unknown")


def extract_python_imports(source: str) -> list[str]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    return imports


def extract_ts_imports(source: str) -> list[str]:
    return _TS_IMPORT_RE.findall(source)


def extract_ts_exports(source: str) -> list[str]:
    return _TS_EXPORT_RE.findall(source)


def infer_role(path: str) -> str:
    normalized = path.replace("\\", "/").lower()
    stem = Path(path).stem.lower()
    if "components/" in normalized:
        return "UI-Komponente"
    if "hooks/" in normalized:
        return "Custom Hook"
    if "provider" in stem:
        return "Zustandsmanagement"
    if "service" in stem:
        return "Service"
    if stem in ("config", "settings", "configuration"):
        return "Konfiguration"
    return "Unbekannt"


def index_file(filepath: Path, relative_path: str) -> FileIndex:
    language = detect_language(filepath.suffix.lower())
    source = filepath.read_text(encoding="utf-8", errors="replace")
    if language == "python":
        imports = extract_python_imports(source)
        exports: list[str] = []
    elif language in ("typescript", "javascript"):
        imports = extract_ts_imports(source)
        exports = extract_ts_exports(source)
    else:
        imports = []
        exports = []
    return FileIndex(
        path=relative_path,
        language=language,
        imports=imports,
        exports=exports,
        probable_role=infer_role(relative_path),
    )
