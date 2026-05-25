---
name: scope-audit
description: Prüfe, ob Claude Code außerhalb des erlaubten Umfangs gearbeitet hat.
disable-model-invocation: true
---

# Skill: scope-audit

## Prüfen

- Wurde etwas außerhalb der aktuellen Phase gebaut?
- Wurde UI zu früh gebaut?
- Wurde LLM/API zu früh eingebaut?
- Wurde OpenRouter eingebaut?
- Wurden Secrets berührt?
- Wurden Docs übertrieben?

## Ausgabe

```markdown
# Scope-Audit

## Verstöße
## Risiko
## Was zurückgebaut werden sollte
## Was bleiben kann
```
