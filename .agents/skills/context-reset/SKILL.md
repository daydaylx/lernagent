---
name: context-reset
description: Erstelle eine kompakte RepoTutor-Session-Übergabe mit aktuellem Stand, Tests und offenen Entscheidungen.
---

# Skill: context-reset

## Ziel

Kontext klein halten und eine neue Agenten-Session ohne Informationsverlust vorbereiten.

## Eingangsbedingungen

- Eine Phase, ein Review oder eine Adapter-Aufgabe ist abgeschlossen, pausiert oder zu groß für den aktuellen Kontext.
- Die Übergabe soll keine neuen Features starten.

## Vorgehen

1. Lies `AGENTS.md`, `docs/SESSION_MANAGEMENT.md` und die relevante Phase- oder Issue-Doku.
2. Prüfe `git status --short`.
3. Sammle geänderte Dateien, ausgeführte Tests, offene Fehler und explizite Nutzerentscheidungen.
4. Formuliere den nächsten zulässigen Prompt eng am aktuellen Stand.

## Ausgabeformat

```markdown
# Session-Handoff

## Aktuelle Phase
## Geänderte Dateien
## Ausgeführte Tests
## Offene Probleme
## Explizite Nutzerentscheidungen
## Nächster sinnvoller Prompt
```

## Nicht tun

- Keine App-Funktionalität bauen.
- Keine persönlichen Secrets oder lokalen Config-Werte aufnehmen.
- Keine Handoff-Datei schreiben, außer der Nutzer fordert sie ausdrücklich.
