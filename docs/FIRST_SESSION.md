# Erste Claude-Code-Session

## Ziel

Claude soll zuerst verstehen und planen. Nicht bauen.

## Prompt 1

```text
Lies CLAUDE.md, AGENTS.md und docs/PROJECT_BRIEF.md.
Fasse zusammen:
1. Was soll RepoTutor werden?
2. Was soll ausdrücklich nicht gebaut werden?
3. Welche Phase ist als erstes sinnvoll?
Ändere noch keine Dateien.
```

## Prompt 2

```text
Nutze den Skill plan-phase für Phase 1.
Plane nur die erste Phase.
Keine Dateiänderungen.
```

## Prompt 3 nach Prüfung

```text
Go für Phase 1.
Setze nur docs/phases/phase_01_agent_to_scaffold.md um.
Keine UI, keine echte LLM-API, kein Streaming, kein Packaging.
```

## Nach Umsetzung

```text
Nutze den Skill test-audit. Prüfe gegen docs/VERIFICATION.md und docs/phases/phase_01_agent_to_scaffold.md.
```
