# Multi-Agent Usage

## Zweck

RepoTutor kann mit Claude Code, Codex und opencode bearbeitet werden. Die Regeln bleiben dabei agentenübergreifend konsistent: `AGENTS.md` ist die gemeinsame Wahrheit, tool-spezifische Dateien sind nur Adapter.

## Struktur

```text
AGENTS.md = gemeinsame Basis
CLAUDE.md = Claude-Code-Adapter
.codex/ = Codex-Adapter
opencode.json.example + .opencode/ = opencode-Adapter
.agents/skills/ = agentenneutrale wiederverwendbare Workflows
docs/ = Konzept, Plan, Phasen, Verifikation
```

## Gemeinsame Regeln

- Jeder Agent liest zuerst `AGENTS.md`.
- Adapter dürfen `AGENTS.md` nicht abschwächen oder widersprechen.
- Bei Widersprüchen gilt die strengere Regel.
- Erst erkunden, dann planen, dann nach ausdrücklichem Go ändern.
- Keine App-Implementierung, kein MCP, keine aktiven Hooks, keine echten API-Keys und keine lokalen persönlichen Configs erzwingen.
- `docs/CONCEPT.md`, `docs/BUILD_PLAN.md`, `docs/VERIFICATION.md` und die passende Phase-Datei bleiben die fachliche Arbeitsgrundlage.

## Adapter-Rollen

- Claude Code nutzt `CLAUDE.md`, `.claude/rules/`, `.claude/skills/` und `.claude/agents/`.
- Codex nutzt `AGENTS.md`, optionale Beispiele unter `.codex/` und wiederverwendbare Skills unter `.agents/skills/`.
- opencode nutzt `AGENTS.md`, optionale Beispiele aus `opencode.json.example` und Workflows unter `.opencode/`.
- `.agents/skills/` enthält neutrale Arbeitsabläufe. Tool-spezifische Skills oder Commands dürfen sie spiegeln, aber nicht verschärfende Regeln entfernen.

## Offizielle Quellen

- Claude Code Best Practices: https://code.claude.com/docs/en/best-practices
- Claude Code Skills: https://docs.anthropic.com/en/docs/claude-code/skills
- Codex `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md
- Codex Best Practices: https://developers.openai.com/codex/learn/best-practices
- Codex Config: https://developers.openai.com/codex/config-basic
- Codex Permissions: https://developers.openai.com/codex/permissions
- Codex Subagents: https://developers.openai.com/codex/subagents
- Codex Skills: https://developers.openai.com/codex/skills
- opencode Rules / `AGENTS.md`: https://opencode.ai/docs/rules/
- opencode Providers: https://opencode.ai/docs/providers/
- opencode Permissions: https://opencode.ai/docs/permissions/
- opencode Commands: https://opencode.ai/docs/commands/
- opencode Agents: https://opencode.ai/docs/agents/
- z.ai GLM 5.1 Coding Plan: https://docs.z.ai/devpack/using5.1
- z.ai Coding Plan Endpoint: https://docs.z.ai/devpack/tool/others
