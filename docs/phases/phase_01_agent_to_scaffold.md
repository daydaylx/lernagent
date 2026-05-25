# Phase 01 – Vom Agenten-Setup zum Python-Scaffold

**Status: abgeschlossen (2026-05-25)**

## Ziel

Erzeuge die erste minimale Python-Projektstruktur.

## Erlaubt

- `main.py`
- `app/__init__.py`
- `app/config.py`
- leere Moduldateien mit klaren TODOs
- `tests/`
- `pyproject.toml`
- `requirements.txt`
- minimale Tests für Importierbarkeit

## Nicht erlaubt

- Textual UI
- echte LLM-API
- Streaming
- Scanner-Komplettbau
- Indexer-Komplettbau
- Packaging
- OpenRouter

## Muss danach funktionieren

```bash
python --version
pytest -q
ruff check .
```

Wenn `python main.py --help` angelegt wird, muss es funktionieren.

## Definition of Done

- Struktur existiert
- Module importierbar
- Tests sind nicht leer
- Docs sagen weiterhin ehrlich, dass noch kein Tool fertig ist
- `docs/VERIFICATION.md` ist für Phase 1 erfüllt oder Abweichungen sind begründet
