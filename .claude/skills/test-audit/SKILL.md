---
name: test-audit
description: Prüfe Tests und Qualität ohne neue Features.
disable-model-invocation: true
---

# Skill: test-audit

## Prüfen

- Sind Tests leer oder echt?
- Gibt es echte Assertions?
- Laufen `pytest -q` und `ruff check .`?
- Stimmen Docs und Stand überein?
- Gibt es Fake-Implementierungen?
- Wurde `docs/VERIFICATION.md` erfüllt?

## Ausgabe

```markdown
# Test-Audit

## Ausgeführte Kommandos
## Ergebnis
## Fehler
## Lücken
## Fix-Plan
```
