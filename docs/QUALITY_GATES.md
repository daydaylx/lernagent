# Quality Gates

## Gate 0 – Agenten-Setup

Bestanden, wenn:

- CLAUDE.md existiert
- AGENTS.md existiert
- `.claude/settings.json` existiert
- Regeln existieren
- Skills existieren
- Phase 1 dokumentiert ist
- Verifikationsdokument existiert
- Review-Subagent existiert oder bewusst begründet fehlt

## Gate 1 – Erster Scaffold

Bestanden (Phase 1, 2026-05-25):

- Python-Projektstruktur existiert (`main.py`, `app/`, `tests/`)
- `python main.py --help` → Exit 0, "RepoTutor" in Ausgabe
- Tests existieren (`test_scaffold_imports.py`, `test_main_cli.py`)
- `pytest -q` → 2 passed
- `ruff check .` → All checks passed

## Gate 2 – Core

Bestanden (Phase 2–3, 2026-05-25):

- Scanner testbar ✓
- Cache testbar ✓
- Indexer testbar ✓
- Explainer als Prompt-Builder testbar ✓
- `pytest -q` → 34 Tests passing (nach Phase 3) ✓
- `ruff check .` → clean ✓

## Gate 3 – Multi-Agent-Adapter

Bestanden (Multi-Agent-Adapter, 2026-05-26):

- `AGENTS.md` die gemeinsame agentenübergreifende Wahrheit bleibt ✓
- `docs/MULTI_AGENT_USAGE.md`, `docs/CODEX_USAGE.md` und `docs/OPENCODE_USAGE.md` existieren ✓
- `.agents/skills/` enthält `plan-phase`, `test-audit`, `scope-audit`, `context-reset`, `review-plan`, `phase-implementation` ✓
- `.codex/config.toml.example` und Codex-Subagents existieren ✓
- `opencode.json.example`, `.opencode/commands/` und `.opencode/agents/repo-reviewer.md` existieren ✓
- keine echten API-Keys, keine OpenRouter-Integration, kein MCP und keine aktiven Hooks ergänzt ✓
- `pytest -q` → 45 Tests passing ✓
- `ruff check .` → clean ✓

## Gate 4 – UI-Entscheidungstor

Bestanden, wenn:

- `docs/DECISION_POLICY.md` existiert
- `.claude/rules/08-ui-decisions.md` existiert
- `docs/phases/phase_05_tui.md` mit Decision Gate existiert
- alle offenen UI-Richtungsfragen aus phase_05_tui.md vom Nutzer beantwortet wurden
- Phase 5 wurde noch nicht implementiert
