# Erste Session / Neue Session

## Aktueller Stand

Phasen 0–4 sind abgeschlossen. Vorhanden:

- `main.py` (CLI-Einstieg, noch kein vollständiger Nutzerflow)
- `app/scanner.py`, `app/cache.py`, `app/indexer.py` – lokale Projektanalyse
- `app/explainer.py` – Prompt-Builder
- `app/ai_client.py` – z.ai GLM 5.1 Streaming-Client
- `app/config.py` – Provider-Konfiguration
- `tests/` – 45 Tests, alle passing
- Multi-Agent-Adapter für Claude Code, Codex und opencode

Noch nicht vorhanden: Textual UI, vollständiger `main.py`-Flow, YAML-Config-Parsing.

## Prompt 1 – Stand zusammenfassen

```text
Lies CLAUDE.md, AGENTS.md, docs/BUILD_PLAN.md und docs/QUALITY_GATES.md.
Fasse zusammen:
1. Welche Phasen sind abgeschlossen?
2. Was ist vorhanden, was fehlt noch?
3. Was ist die nächste erlaubte Phase?
Ändere noch keine Dateien.
```

## Prompt 2 – Phase 5 vorbereiten (erst nach Decision Gate)

```text
Lies docs/phases/phase_05_tui.md und docs/DECISION_POLICY.md.
Prüfe, ob alle UI-Entscheidungspunkte aus dem Decision Gate geklärt sind.
Wenn nicht: erstelle einen UI-Optionsvorschlag (2–3 Varianten, Vor-/Nachteile, Empfehlung, konkrete Frage).
Ändere noch keine Dateien.
```

## Prompt 3 – Go für Phase 5 (nur nach explizitem UI-Richtungsentscheid)

```text
Go für Phase 5.
Setze ausschließlich um, was in docs/phases/phase_05_tui.md beschrieben ist.
Decision Gate muss vorher bestätigt sein.
Keine neue Provider-Architektur, kein Packaging.
```

## Nach Umsetzung

```text
Nutze den Skill test-audit.
Prüfe gegen docs/VERIFICATION.md und docs/phases/phase_05_tui.md.
```
