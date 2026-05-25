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

Ausgeführt (2026-05-25):

```bash
python --version        # Python 3.12.3
python main.py --help   # Exit 0, "RepoTutor" in Ausgabe
pytest -q               # 2 passed in 0.07s
ruff check .            # All checks passed
```

## Phase 2 – Scanner, Cache, Indexer

Abgeschlossen (2026-05-25):

```bash
pytest -q               # 23 passed
ruff check .            # All checks passed
```

Geprüft:

- Scanner ignoriert node_modules, **pycache**, .venv usw.
- Scanner findet .py, .ts, .tsx, .js, .jsx, .md, .json, .yaml, .yml, .toml, .css, .scss
- Cache erkennt neue, unveränderte und geänderte Dateien per SHA-256
- Indexer erkennt Sprache, Python-Imports via ast, TS/JS-Imports/-Exports via Regex
- probable_role wird heuristisch gesetzt

## Phase 3 – Explainer / Prompt-Builder

Abgeschlossen (2026-05-25):

```bash
pytest -q               # 34 passed (23 bestehende + 11 neue)
ruff check .            # All checks passed
```

Geprüft:

- Prompt enthält Dateipfad
- Prompt enthält Dateiinhalt
- Prompt enthält Sprache aus FileIndex
- Prompt enthält Imports und Exports
- Modus-Label erscheint in Überschrift
- Deutschen Abschnittsüberschriften im Modus `normal`
- Inhalt > 25 000 Zeichen wird gekürzt mit Warnung
- Unbekannter Modus wirft ValueError
- explainer.py enthält keine Netzwerk-Imports

## Phase 4 – z.ai GLM 5.1 + Streaming

Abgeschlossen (2026-05-25):

```bash
pytest -q               # 45 passed (34 bestehende + 11 neue)
ruff check .            # All checks passed
```

Geprüft:

- Fehlender API-Key → EnvironmentError mit Key-Namen im Text
- API-Key aus Umgebungsvariable korrekt gelesen
- SSE-Zeilenparser: content extrahiert, [DONE] ignoriert, kaputtes JSON toleriert
- Mock-Streaming liefert Chunks in korrekter Reihenfolge
- Kein HTTP-Call bei fehlendem Key
- ai_client.py enthält keine requests/urllib-Imports
- DEFAULT_CONFIG-Werte stimmen mit Spezifikation überein

## Keine Scheinerfolge

Nicht akzeptiert:

- "Tests laufen" ohne Testausgabe.
- "Fertig" ohne geänderte Dateien.
- "Implementiert" bei leeren Funktionen.
- "Kein Problem" bei übersprungenen Qualitätsprüfungen.
