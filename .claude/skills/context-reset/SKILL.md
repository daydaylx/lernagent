---
name: context-reset
description: Erstelle eine kompakte Übergabe, bevor eine neue Claude-Code-Session gestartet wird.
disable-model-invocation: true
---

# Skill: context-reset

## Ziel

Kontext sauber halten und eine neue Session vorbereiten.

## Ausgabe

```markdown
# Session-Handoff

## Aktuelle Phase
## Geänderte Dateien
## Ausgeführte Tests
## Offene Probleme
## Explizite Nutzerentscheidungen
## Nächster sinnvoller Prompt
```

## Regel

Keine neuen Features und keine Dateiänderungen, außer der Nutzer fordert explizit eine Handoff-Datei.
