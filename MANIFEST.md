# Manifest

## Zweck

Agenten-Setup für Claude Code.

## Enthält

- CLAUDE.md
- AGENTS.md
- .claude/settings.json
- .claude/rules/
- .claude/skills/
- .claude/agents/
- .claude/hooks/README.md
- docs/
- prompts/
- main.py (Scaffold, CLI-Einstieg)
- app/ (7 Stub-Module: config, scanner, cache, indexer, explainer, ai_client, ui)
- tests/ (Importierbarkeits- und CLI-Tests)
- pyproject.toml, requirements.txt, config.yaml.example

## Enthält nicht

- kein funktionsfähiges Tool
- keine Scanner-/Cache-/Indexer-Implementierung
- keine Textual UI
- keine LLM-Anbindung

Das ist Absicht. Phase 1 ist Scaffold, nicht Funktionalität.
