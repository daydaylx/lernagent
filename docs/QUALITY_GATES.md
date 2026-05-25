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

Später bestanden, wenn:

- Scanner testbar
- Cache testbar
- Indexer testbar
- Explainer als Prompt-Builder testbar
