---
name: scope-audit
description: Prüfe RepoTutor-Änderungen gegen AGENTS.md, Bauplan und freigegebenen Umfang.
---

# Skill: scope-audit

## Eingangsbedingungen

- Es gibt eine Umsetzung oder einen Diff, der gegen einen freigegebenen Plan geprüft werden soll.
- `AGENTS.md` bleibt die höchste gemeinsame Regelbasis.

## Prüfen

1. Lies `AGENTS.md`, `docs/BUILD_PLAN.md` und die relevante Datei aus `docs/phases/` oder die betroffenen Issues.
2. Vergleiche die geänderten Dateien mit dem freigegebenen Umfang.
3. Markiere Scope-Creep, besonders zu frühe UI, zu frühe Provider/API-Arbeit, OpenRouter, MCP, Hooks, Secrets und unnötige Komplexität.
4. Unterscheide klar zwischen erlaubten Adapter-/Doku-Änderungen und unerlaubten App-Änderungen.

## Ausgabeformat

```markdown
# Scope-Audit

## Verstöße
## Risiko
## Was zurückgebaut werden sollte
## Was bleiben kann
```

## Nicht tun

- Keine Dateien ändern, außer der Nutzer fordert ausdrücklich einen Fix.
- Keine tool-spezifischen Regeln akzeptieren, die `AGENTS.md` abschwächen.
