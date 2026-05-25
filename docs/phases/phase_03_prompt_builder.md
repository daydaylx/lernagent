# Phase 03 – Prompt-Builder

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

## Erwartete Verifikation

- Prompt enthält Dateiinhalt.
- Prompt enthält Projektkontext.
- Prompt enthält Modus.
- Große Dateien werden begrenzt.
