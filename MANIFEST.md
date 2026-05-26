# Manifest

## Zweck

Agenten-Setup für Claude Code, Codex und opencode.

## Enthält

- CLAUDE.md
- AGENTS.md
- .claude/settings.json
- .claude/rules/
- .claude/skills/
- .claude/agents/
- .claude/hooks/README.md
- .codex/config.toml.example
- .codex/agents/
- opencode.json.example
- .opencode/commands/
- .opencode/agents/
- .agents/skills/
- docs/
- prompts/
- main.py (CLI-Einstieg)
- app/ (Core-Module: config, scanner, cache, indexer, explainer, ai_client, ui)
- tests/
- pyproject.toml, requirements.txt, config.yaml.example

## Enthält nicht

- keine Textual UI
- keine main.py-Integration für vollständige Nutzerflows
- keine lokalen persönlichen Codex- oder opencode-Konfigs
- keine echten API-Keys
- keine aktiven Hooks
- kein MCP

Das ist Absicht. Tool-spezifische Dateien sind Adapter; `AGENTS.md` bleibt die gemeinsame Wahrheit.
