@AGENTS.md

# CLAUDE.md – Claude-Code-spezifische Regeln

## Aktueller Zustand

Dieses Repo ist ein Agenten-Setup. Es enthält noch keine App-Implementierung.

Wenn du Code erzeugst, darf das nur nach explizitem Go für eine konkrete Phase passieren.

## Kontext-Regel

Halte diese Datei kurz. Details liegen in `docs/`, `.claude/rules/`, `.claude/skills/` und `.claude/agents/`.

## Startverhalten

Beim Start einer neuen Session:

1. Lies `docs/FIRST_SESSION.md`.
2. Prüfe den aktuellen Dateistand.
3. Fasse Ziel, Nicht-Ziele und aktuelle Phase zusammen.
4. Frage nicht nach Dingen, die bereits in den Dokumenten stehen.
5. Implementiere nichts, solange nur Analyse oder Planung verlangt ist.

## Geplanter Provider

Später soll z.ai GLM Coding Plan mit `glm-5.1` genutzt werden.

Aber:
- Keine echte LLM-Anbindung in Phase 1.
- Keine OpenRouter-Integration als Default.
- Provider-Logik erst nach Core, Indexer und Prompt-Builder.

## Verifikation

Nach jeder Implementierung gelten `docs/VERIFICATION.md` und die passende Datei in `docs/phases/`.

## Stop-Regel

Wenn eine Aufgabe außerhalb der aktuellen Phase liegt, markiere sie als Scope-Creep und schlage eine kleinere Alternative vor.
