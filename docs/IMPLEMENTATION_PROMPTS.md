# RepoTutor – Implementierungs-Prompts

Diese Prompts sind für Claude Code gedacht. Sie sollen verhindern, dass der Agent zu breit baut.

## Prompt 1 – Verstehen und planen

```text
Lies diese Dateien:
- CLAUDE.md
- AGENTS.md
- docs/CONCEPT.md
- docs/BUILD_PLAN.md
- docs/FIRST_SESSION.md
- docs/phases/phase_01_agent_to_scaffold.md

Fasse zusammen:
1. Was soll RepoTutor werden?
2. Was ist ausdrücklich nicht Teil von V1?
3. Welche Phase ist als erstes erlaubt?
4. Welche Dateien dürfen in Phase 1 erstellt werden?
5. Welche Tests/Checks müssen danach laufen?

Erstelle danach nur einen Plan für Phase 1.
Ändere noch keine Dateien.
```

## Prompt 2 – Plan streng prüfen

```text
Prüfe deinen Phase-1-Plan streng gegen:
- docs/BUILD_PLAN.md
- docs/phases/phase_01_agent_to_scaffold.md
- docs/VERIFICATION.md
- docs/QUALITY_GATES.md

Suche:
- Scope-Creep
- fehlende Tests
- zu frühe UI
- zu frühe API-Anbindung
- schwammige Schritte
- unnötige Abhängigkeiten

Liefere danach eine korrigierte Fassung des Plans.
Ändere noch keine Dateien.
```

## Prompt 3 – Go für Phase 1

```text
Go für Phase 1.

Setze ausschließlich um:
- docs/phases/phase_01_agent_to_scaffold.md
- Phase 1 aus docs/BUILD_PLAN.md

Nicht bauen:
- keine Textual UI
- keine echte z.ai API
- kein Streaming
- kein Scanner-Komplettbau
- kein Indexer-Komplettbau
- kein Packaging
- kein OpenRouter

Am Ende ausführen, falls möglich:
- python --version
- python main.py --help
- pytest -q
- ruff check .

Berichte:
- geänderte Dateien
- ausgeführte Kommandos
- Ergebnis
- bekannte Grenzen
- nächster sinnvoller Schritt
```

## Prompt 4 – Nachkontrolle

```text
Nutze den Skill test-audit.
Prüfe die Umsetzung gegen:
- docs/VERIFICATION.md
- docs/QUALITY_GATES.md
- docs/phases/phase_01_agent_to_scaffold.md

Suche besonders nach:
- leeren Tests
- Fake-Implementierungen
- falscher Doku
- Scope-Creep
- nicht ausgeführten Prüfungen

Liefere konkrete Fixes, aber ändere noch keine Dateien.
```

## Prompt 5 – Phase 2 planen

Erst nach abgeschlossener Phase 1:

```text
Lies docs/BUILD_PLAN.md und docs/phases/phase_02_core_analysis.md.
Plane Phase 2: Scanner, Cache und Indexer.
Ändere noch keine Dateien.
```

## Prompts, die nicht genutzt werden sollten

Schlecht:

```text
Bau das komplette Tool fertig.
```

```text
Mach alles best practices.
```

```text
Setz einfach um.
```

Warum schlecht:

- zu breit
- nicht prüfbar
- lädt Scope-Creep ein
- Agent baut wahrscheinlich UI/API zu früh
