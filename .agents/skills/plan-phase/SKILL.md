---
name: plan-phase
description: Plane eine einzelne RepoTutor-Phase oder Adapter-Aufgabe, ohne Dateien zu ändern.
---

# Skill: plan-phase

## Eingangsbedingungen

- Es gibt eine konkrete Phase, ein Issue oder eine klar begrenzte Adapter-Aufgabe.
- Es liegt noch kein ausdrückliches Go zur Umsetzung vor.
- `AGENTS.md` ist die gemeinsame Regelbasis.

## Vorgehen

1. Lies `AGENTS.md`.
2. Lies die relevanten Dateien aus `docs/`, mindestens `docs/CONCEPT.md`, `docs/BUILD_PLAN.md`, `docs/VERIFICATION.md` und die passende Phase- oder Issue-Doku.
3. Prüfe den aktuellen Dateistand mit nicht-mutierenden Befehlen.
4. Erstelle einen konkreten Plan mit Dateien, Reihenfolge, Tests, Nicht-Zielen und Risiken.
5. Warte auf ein ausdrückliches Go, bevor Dateien geändert werden.

## Ausgabeformat

```markdown
# Plan: <Aufgabe>

## Ziel
## Aktueller Stand
## Dateien
## Schritte
## Tests
## Nicht-Ziele
## Risiken
## Definition of Done
```

## Nicht tun

- Keine Dateien ändern.
- Keine App-Features bauen.
- Keine Secrets lesen oder ausgeben.
- Keine Regeln vorschlagen, die `AGENTS.md` abschwächen.
