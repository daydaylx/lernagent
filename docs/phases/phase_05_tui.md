# Phase 05 – Textual TUI

## Voraussetzungen

- Phasen 1–4 stabil und verifiziert. ✓ (erfüllt)
- Decision Gate (siehe unten) vollständig beantwortet.
- Explizites Go nach UI-Richtungsentscheid.

## Decision Gate – vor jeder Implementierung

Alle folgenden Punkte müssen vom Nutzer beantwortet sein, bevor Phase 5 beginnt. Wenn Punkte offen sind, erstellt der Agent zuerst einen UI-Optionsvorschlag (Format: `docs/DECISION_POLICY.md`).

| Entscheidungspunkt                                      | Status |
| ------------------------------------------------------- | ------ |
| Layout-Basisstruktur (Single-View / Split-View / Panel) | offen  |
| Navigationsprinzip (Tastatur / Maus / beides)           | offen  |
| Informationshierarchie (was ist prominent?)             | offen  |
| Kompaktheitsgrad (minimalistisch / informationsdicht)   | offen  |
| Interaktionsfluss (Reihenfolge der Schritte)            | offen  |
| Lernmodus- vs. Analysemodus-Anteil                      | offen  |
| Placement von Projektbaum, Erklärung, Q&A               | offen  |
| Fehlerdarstellung (inline / Statusleiste / Modal)       | offen  |

## Layout-Referenz (aus BUILD_PLAN.md)

```text
┌─────────────────┬──────────────────────────────────┐
│ Projektbaum     │ Erklärung / Ausgabe              │
│                 │                                  │
│ src/            │ # Kurz gesagt                    │
│ components/     │ Diese Datei zeigt ...            │
├─────────────────┴──────────────────────────────────┤
│ > Rückfrage eingeben...                            │
└────────────────────────────────────────────────────┘
```

Dies ist eine Idee, kein verbindliches Design. Erst nach Decision Gate festlegen.

## Erlaubt (nach Go)

- `app/ui.py` – Textual TUI-Implementierung
- Integration in `main.py` (Projektpfad übergeben, TUI starten)
- UI-Tests mit Textual-Testrunner
- YAML-Config-Parsing (falls für UI-Flow nötig)

## Nicht erlaubt

- UI bauen, um fehlende Core-Logik zu kaschieren
- Neue Provider-Architektur
- Packaging (deb, AppImage, PyPI)
- Phase 5 vor beantwortetem Decision Gate

## Funktionen nach Go

- Projektpfad auswählen oder eingeben
- Projektbaum anzeigen
- Datei auswählen
- Erklärungsmodus auswählen (simple, normal, context, quiz)
- Erklärung gestreamt anzeigen
- Rückfrage eingeben
- Fehler sichtbar anzeigen

## Erwartete Verifikation

```bash
textual run app/ui.py          # TUI startet ohne Absturz
pytest -q                      # alle Tests weiterhin passing
ruff check .                   # clean
python main.py --help          # Exit 0
```
