# Phase 03 – Prompt-Builder

Status: erledigt (2026-05-25). Explainer und Prompt-Templates sind implementiert und getestet.

## Ziel

Explainer baut Prompts aus Datei, Projektkontext und Modus.

## Erlaubt

- `app/explainer.py`
- `prompts/`
- Tests für Prompt-Building

## Nicht erlaubt

- echte API-Aufrufe
- Streaming
- UI

## Verifikation (bestanden)

- Prompt enthält Dateiinhalt. ✓
- Prompt enthält Projektkontext. ✓
- Prompt enthält Modus. ✓
- Große Dateien werden begrenzt (>25 KB Warnung, >80 KB starke Warnung). ✓
- `pytest -q` → 34 Tests passing (Phase 3). ✓
- `ruff check .` → clean. ✓
