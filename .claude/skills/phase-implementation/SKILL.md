---
name: phase-implementation
description: Setze eine freigegebene Phase um, ohne Scope-Creep.
disable-model-invocation: true
---

# Skill: phase-implementation

## Voraussetzung

Nur nutzen, wenn der Nutzer explizit Go für eine Phase gegeben hat.

## Vorgehen

1. Phase-Datei lesen.
2. Nur erlaubte Dateien ändern.
3. Tests schreiben.
4. `pytest -q` ausführen.
5. `ruff check .` ausführen.
6. Ergebnis berichten.

## Verboten

- zusätzliche Features
- Provider/API, wenn nicht Phase
- UI, wenn nicht Phase
- Commit/Push ohne Auftrag
