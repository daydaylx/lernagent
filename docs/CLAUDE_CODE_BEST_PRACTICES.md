# Claude Code Best Practices – Umsetzung im Repo

Dieses Dokument übersetzt die offiziellen Claude-Code-Best-Practices in konkrete Repo-Regeln.

## 1. Claude muss seine Arbeit prüfen können

Umgesetzt durch:

- `docs/VERIFICATION.md`
- `docs/QUALITY_GATES.md`
- Skill `test-audit`

Jede Phase muss prüfbare Kommandos oder begründete manuelle Checks haben.

## 2. Erst erkunden, dann planen, dann codieren

Umgesetzt durch:

- `.claude/settings.json` mit `permissions.defaultMode: plan`
- `docs/FIRST_SESSION.md`
- Skill `plan-phase`
- Phasenverträge in `docs/phases/`

## 3. Spezifischer Kontext statt schwammiger Prompts

Umgesetzt durch:

- `prompts/first_agent_prompt.md`
- `prompts/go_phase_01.md`
- `docs/phases/phase_01_agent_to_scaffold.md`

## 4. CLAUDE.md kurz halten

Umgesetzt durch:

- kurze `CLAUDE.md`
- allgemeine Regeln in `AGENTS.md`
- Details in `docs/`, `.claude/rules/`, `.claude/skills/`

## 5. Permissions gezielt konfigurieren

Umgesetzt durch:

- `.claude/settings.json`
- Deny-Regeln für `.env`, Secrets, `sudo`, `curl`, `wget`, `git push`
- Ask-Regeln für riskante lokale Befehle

## 6. Skills für wiederverwendbare Workflows

Umgesetzt durch:

- `plan-phase`
- `review-plan`
- `phase-implementation`
- `test-audit`
- `scope-audit`
- `context-reset`

## 7. Hooks nur, wenn wirklich nötig

Umgesetzt durch:

- `.claude/hooks/README.md`
- keine aktiven Hooks im Startzustand

## 8. Subagents für isolierte Reviews

Umgesetzt durch:

- `.claude/agents/repo-reviewer.md`

## 9. Kontext aggressiv verwalten

Umgesetzt durch:

- `.claude/rules/07-context.md`
- `docs/SESSION_MANAGEMENT.md`
- Skill `context-reset`
