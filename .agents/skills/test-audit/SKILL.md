---
name: test-audit
description: Prüfe Tests, Lint und Dokumentationswahrheit für RepoTutor ohne neue Features.
---

# Skill: test-audit

## Eingangsbedingungen

- Es gibt eine abgeschlossene oder zu prüfende Umsetzung.
- `AGENTS.md`, `docs/VERIFICATION.md` und `docs/QUALITY_GATES.md` sind die verbindliche Prüfbasis.

## Prüfen

1. Lies `AGENTS.md`, `docs/VERIFICATION.md`, `docs/QUALITY_GATES.md` und die relevante Phase- oder Issue-Doku.
2. Prüfe, ob Tests echte Assertions enthalten und keine Scheinerfolge sind.
3. Führe die vorgesehenen Prüfungen aus, typischerweise `pytest -q` und `ruff check .`, sofern die Tools verfügbar sind.
4. Prüfe, ob die Dokumentation dem tatsächlichen Stand entspricht.
5. Markiere fehlende Tools, übersprungene Checks und verbleibende Risiken ausdrücklich.

## Ausgabeformat

```markdown
# Test-Audit

## Ausgeführte Kommandos
## Ergebnis
## Fehler
## Lücken
## Fix-Plan
```

## Nicht tun

- Keine neuen Features bauen.
- Keine Tests als bestanden melden, wenn sie nicht ausgeführt wurden.
- Keine Lint-Lücken verschweigen.
