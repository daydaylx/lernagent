# opencode Usage

## Grundsatz

opencode soll RepoTutor über `AGENTS.md` nutzen. `opencode.json.example` und `.opencode/` sind nur Adapter und dürfen die gemeinsamen Regeln nicht abschwächen.

## Start-Workflow

1. Lies `AGENTS.md`.
2. Lies `docs/CONCEPT.md`, `docs/BUILD_PLAN.md`, `docs/VERIFICATION.md`, `docs/QUALITY_GATES.md` und die passende Phase-Datei oder Issue-Beschreibung.
3. Plane zuerst und ändere Dateien erst nach ausdrücklichem Go.
4. Nutze `.opencode/commands/` nur als Workflow-Hilfe, nicht als Freigabe für automatische Umsetzung.

## z.ai GLM 5.1 Coding Plan

`opencode.json.example` bereitet den Provider `zai-coding/glm-5.1` vor:

- Base URL: `https://api.z.ai/api/coding/paas/v4`
- API-Key: `{env:ZAI_API_KEY}`
- Modell: `glm-5.1`

Wichtig:

- Kein echter API-Key im Repository.
- Kein OpenRouter als Default.
- Kein `/v1` an den z.ai Coding-Plan-Endpoint anhängen.
- Wenn opencode den Provider direkt anbietet, kann alternativ `/connect` genutzt und `Z.AI Coding Plan` ausgewählt werden.

## Permissions

Die Example-Konfiguration empfiehlt restriktive Permissions:

- `.env`, `.env.*`, `secrets/**` und secret/token/credential-Pfade blockieren.
- `sudo`, `git push`, `curl`, `wget`, `printenv` und `env` blockieren.
- Tests und Lint bleiben `ask`.
- Externe Verzeichnisse, Subagents, Skills, Webfetch und Websearch bleiben `ask`.

Permissions ersetzen keine Secret-Hygiene. Echte Secrets gehören nicht in den Arbeitsbaum.

## Commands und Agent

- `.opencode/commands/plan-phase.md`: Plan ohne Änderungen.
- `.opencode/commands/test-audit.md`: Tests, Lint und Doku-Wahrheit prüfen.
- `.opencode/commands/scope-audit.md`: Scope-Creep gegen `AGENTS.md` und Bauplan prüfen.
- `.opencode/commands/review-phase.md`: kritischer Review über `repo-reviewer`.
- `.opencode/agents/repo-reviewer.md`: read-only Review-Subagent.

Jeder Command verweist auf `AGENTS.md` und die relevanten `docs/`.

## Offizielle Quellen

- opencode Rules / `AGENTS.md`: https://opencode.ai/docs/rules/
- opencode Providers: https://opencode.ai/docs/providers/
- opencode Permissions: https://opencode.ai/docs/permissions/
- opencode Commands: https://opencode.ai/docs/commands/
- opencode Agents: https://opencode.ai/docs/agents/
- z.ai GLM 5.1 Coding Plan: https://docs.z.ai/devpack/using5.1
- z.ai Coding Plan Endpoint: https://docs.z.ai/devpack/tool/others
