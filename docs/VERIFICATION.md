# Verification

## Grundregel

Claude muss seine Arbeit prüfen können. Ohne Verifikation gilt eine Phase nicht als fertig.

## Phase 0 – Agenten-Setup

Prüfen:

```bash
git status
ls -la
ls .claude/rules
ls .claude/skills
ls docs/phases
```

Erwartung:

- `CLAUDE.md` existiert.
- `AGENTS.md` existiert.
- `.claude/settings.json` existiert.
- `.claude/rules/` enthält Scope, Workflow, Qualität, Security, Provider und Kontext.
- `.claude/skills/` enthält Plan, Review, Implementation, Test-Audit und Scope-Audit.
- `docs/phases/phase_01_agent_to_scaffold.md` existiert.

## Phase 1 – Python-Scaffold

Später prüfen:

```bash
python --version
python main.py --help
pytest -q
ruff check .
```

Wenn ein Befehl noch nicht existiert, muss Claude erklären, ob das laut Phase erlaubt ist.

## Keine Scheinerfolge

Nicht akzeptiert:

- "Tests laufen" ohne Testausgabe.
- "Fertig" ohne geänderte Dateien.
- "Implementiert" bei leeren Funktionen.
- "Kein Problem" bei übersprungenen Qualitätsprüfungen.
