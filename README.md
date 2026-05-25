# Lernagent / RepoTutor Agent Setup

Dieses Repository ist zunächst **nur eine Vorbereitung für Claude Code**.

Es enthält keine App-Implementierung. Ziel ist, Claude Code vor dem ersten echten Build sauber zu steuern:

- klare Projektabsicht
- harte Scope-Grenzen
- Phasenverträge
- Review-Regeln
- konkrete Verifikationskriterien
- Sicherheitsregeln
- wiederverwendbare Skills
- optionaler Review-Subagent

## Status

Noch kein Tool. Noch kein Code. Noch kein Prototyp.

## Ziel des späteren Projekts

RepoTutor soll ein privates lokales Lernwerkzeug werden, das Softwareprojekte einliest und Dateien in einfacher deutscher Sprache erklärt.

## Erster Prompt

```text
Lies CLAUDE.md, AGENTS.md, docs/FIRST_SESSION.md und docs/PROJECT_BRIEF.md.
Fasse zusammen, was du verstanden hast.
Erstelle danach nur einen Plan für Phase 1.
Ändere noch keine Dateien.
```

## Wichtiger Grundsatz

Claude Code soll nicht direkt bauen. Erst erkunden, dann planen, dann nach explizitem Go implementieren.
