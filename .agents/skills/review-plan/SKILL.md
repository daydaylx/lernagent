---
name: review-plan
description: Prüfe einen RepoTutor-Plan vor der Umsetzung kritisch auf Scope, Tests und Risiken.
---

# Skill: review-plan

## Eingangsbedingungen

- Es liegt ein Plan für eine Phase, ein Issue oder eine Adapter-Änderung vor.
- Noch keine Umsetzung wurde freigegeben oder die Umsetzung soll vorab geschärft werden.

## Prüfen

1. Lies `AGENTS.md`, `docs/BUILD_PLAN.md`, `docs/VERIFICATION.md` und die relevante Phase- oder Issue-Doku.
2. Prüfe, ob Ziel, Nicht-Ziele, betroffene Dateien, Reihenfolge, Tests, Risiken und Definition of Done konkret sind.
3. Markiere unklare Entscheidungen, übergroßen Umfang, Sicherheitsrisiken und fehlende Verifikation.
4. Schlage eine kleinere oder präzisere Variante vor, wenn der Plan zu breit ist.

## Ausgabeformat

```markdown
# Plan-Review

## Urteil
## Kritische Probleme
## Unklare Punkte
## Verbesserter Plan
```

## Nicht tun

- Keine Dateien ändern.
- Keine Umsetzung beginnen.
- Keine unprüfbaren Erfolgskriterien akzeptieren.
