# Codex Usage

## Grundsatz

Codex soll RepoTutor über `AGENTS.md` und die vorhandenen `docs/` bearbeiten. `.codex/` ist nur ein Adapter für Codex-spezifische Beispiele und Subagents.

## Start-Workflow

1. Lies `AGENTS.md`.
2. Lies `docs/CONCEPT.md`, `docs/BUILD_PLAN.md`, `docs/VERIFICATION.md`, `docs/QUALITY_GATES.md` und die passende Phase-Datei oder Issue-Beschreibung.
3. Prüfe den aktuellen Dateistand.
4. Schreibe einen Plan mit Dateien, Reihenfolge, Risiken, Nicht-Zielen und Verifikation.
5. Ändere Dateien erst nach ausdrücklichem Go.

## Konfiguration

- `.codex/config.toml.example` ist nur eine Vorlage.
- Kopiere sie nur nach `.codex/config.toml`, wenn dieses Repository bewusst vertraut wurde.
- Empfohlen ist `approval_policy = "on-request"` und ein begrenztes Permission-Profil ohne automatische Netzwerknutzung.
- `danger-full-access` wird für dieses Repository nicht empfohlen.
- Keine echten Secrets, keine API-Keys, kein MCP-Setup und keine aktiven Hooks in diesem Adapter.

## Subagents

Die Dateien unter `.codex/agents/` sind read-only oder planend:

- `repo-reviewer.toml`: kritischer Review auf Scope, Tests, Doku, Security und zu frühe UI/API-Arbeit.
- `phase-planner.toml`: Planungsagent vor ausdrücklichem Go.
- `scope-auditor.toml`: Vergleich von Änderungen gegen `AGENTS.md`, Bauplan und freigegebenen Umfang.

Subagents dürfen `AGENTS.md` nicht abschwächen. Für wiederverwendbare Workflows sind die neutralen Skills unter `.agents/skills/` maßgeblich.

## Verifikation

Nach Adapter- oder Doku-Änderungen prüfen:

```bash
python --version
pytest -q
ruff check .
python -m json.tool opencode.json.example
python - <<'PY'
import pathlib
import tomllib

paths = list(pathlib.Path(".codex").rglob("*.toml"))
paths += list(pathlib.Path(".codex").rglob("*.toml.example"))

for path in paths:
    tomllib.loads(path.read_text())
    print(path)
PY
git diff --check
```

Wenn `ruff` lokal fehlt, darf das nicht als bestandener Lint verkauft werden.

## Offizielle Quellen

- Codex `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md
- Codex Best Practices: https://developers.openai.com/codex/learn/best-practices
- Codex Config: https://developers.openai.com/codex/config-basic
- Codex Permissions: https://developers.openai.com/codex/permissions
- Codex Subagents: https://developers.openai.com/codex/subagents
- Codex Skills: https://developers.openai.com/codex/skills
