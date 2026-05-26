# Lernagent / RepoTutor Agent Setup

RepoTutor ist ein privates lokales Lernwerkzeug in Entwicklung – kein fertiges Endnutzer-Tool.

Die Core-Implementierungen aus Phase 1–4 sind vorhanden: Scanner, Cache, Indexer, Explainer, z.ai-Streaming-Client und Tests. Noch nicht vorhanden sind Textual UI, vollständiger `main.py`-Nutzerflow und YAML-Config-Parsing. Phase 5 darf erst nach dem UI-Decision-Gate beginnen (siehe `docs/phases/phase_05_tui.md`).

## Status

- Phase 0 – Agenten-Setup: abgeschlossen.
- Phase 1 – Python-Scaffold: abgeschlossen.
- Phase 2 – Scanner, Cache, Indexer: abgeschlossen.
- Phase 3 – Explainer / Prompt-Builder: abgeschlossen.
- Phase 4 – z.ai GLM 5.1 Streaming-Client: abgeschlossen.
- Multi-Agent-Adapter (Claude Code, Codex, opencode): abgeschlossen.

Vorhanden: `main.py`, `app/scanner.py`, `app/cache.py`, `app/indexer.py`, `app/explainer.py`, `app/ai_client.py`, `app/config.py`, `tests/` (45 passing), `pyproject.toml`, `requirements.txt`, Multi-Agent-Adapter-Dateien.

Nicht vorhanden: keine Textual UI, kein vollständiger `main.py`-Nutzerflow, kein YAML-Config-Parsing.

Nächste Phase: Phase 5 – Textual TUI, erst nach explizitem UI-Richtungsentscheid (siehe `docs/DECISION_POLICY.md` und `docs/phases/phase_05_tui.md`).

## Ziel des Projekts

RepoTutor ist ein privates lokales Lernwerkzeug, das Softwareprojekte einliest und Dateien in einfacher deutscher Sprache erklärt.

## Startprompt für neue Sessions

```text
Lies CLAUDE.md, AGENTS.md, docs/FIRST_SESSION.md.
Fasse zusammen: aktueller Phasenstand, was vorhanden ist, was noch fehlt.
Ändere noch keine Dateien.
```

## Wichtiger Grundsatz

Claude Code soll nicht direkt bauen. Erst erkunden, dann planen, dann nach explizitem Go implementieren.
