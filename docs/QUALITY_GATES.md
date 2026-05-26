# Quality Gates

## Gate 0 – Agenten-Setup

Bestanden, wenn:

- CLAUDE.md existiert
- AGENTS.md existiert
- `.claude/settings.json` existiert
- Regeln existieren
- Skills existieren
- Phase 1 dokumentiert ist
- Verifikationsdokument existiert
- Review-Subagent existiert oder bewusst begründet fehlt

## Gate 1 – Erster Scaffold

Bestanden (Phase 1, 2026-05-25):

- Python-Projektstruktur existiert (`main.py`, `app/`, `tests/`)
- `python main.py --help` → Exit 0, "RepoTutor" in Ausgabe
- Tests existieren (`test_scaffold_imports.py`, `test_main_cli.py`)
- `pytest -q` → 2 passed
- `ruff check .` → All checks passed

## Gate 2 – Core

Bestanden, wenn:

- Scanner testbar
- Cache testbar
- Indexer testbar
- Explainer als Prompt-Builder testbar

## Gate 3 – Multi-Agent-Adapter

Bestanden, wenn:

- `AGENTS.md` die gemeinsame agentenübergreifende Wahrheit bleibt
- `docs/MULTI_AGENT_USAGE.md`, `docs/CODEX_USAGE.md` und `docs/OPENCODE_USAGE.md` existieren
- `.agents/skills/` mindestens `plan-phase`, `test-audit`, `scope-audit` und `context-reset` enthält
- `.codex/config.toml.example` und Codex-Subagents existieren
- `opencode.json.example`, `.opencode/commands/` und `.opencode/agents/repo-reviewer.md` existieren
- keine echten API-Keys, keine OpenRouter-Integration, kein MCP und keine aktiven Hooks ergänzt wurden
- `pytest -q` läuft
- `ruff check .` läuft oder ein fehlendes lokales Tool wird klar als Verifikationslücke gemeldet
