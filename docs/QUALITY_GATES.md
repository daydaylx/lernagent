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

Später bestanden, wenn:
- Python-Projektstruktur existiert
- `python main.py --help` funktioniert oder bewusst begründet noch nicht existiert
- Tests existieren
- `pytest -q` läuft
- `ruff check .` läuft

## Gate 2 – Core

Später bestanden, wenn:
- Scanner testbar
- Cache testbar
- Indexer testbar
- Explainer als Prompt-Builder testbar
