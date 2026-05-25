# Phase 02 – Core-Analyse

## Ziel

Scanner, Cache und Indexer testbar machen.

## Erlaubt

- `app/scanner.py`
- `app/cache.py`
- `app/indexer.py`
- Tests und Fixtures

## Nicht erlaubt

- UI
- echte LLM-API
- Streaming
- Provider-Auswahl
- Codeänderungen in analysierten Projekten

## Erwartete Verifikation

- Scanner ignoriert Müllordner.
- Cache erkennt Dateiänderungen.
- Indexer erkennt einfache Imports/Exports.
- Tests laufen.
