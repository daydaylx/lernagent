---
description: Lasse eine freigegebene oder abgeschlossene Phase kritisch reviewen.
agent: repo-reviewer
subtask: true
---

Lies zuerst `AGENTS.md`.

Prüfe die letzte Umsetzung streng gegen:

- `docs/QUALITY_GATES.md`
- `docs/VERIFICATION.md`
- `docs/BUILD_PLAN.md`
- die passende Datei aus `docs/phases/`
- den freigegebenen Plan oder die betroffenen Issues

Suche:

- Scope-Creep
- Fake-Tests
- leere Implementierungen
- falsche oder übertriebene Doku
- Sicherheitsprobleme
- unnötige Komplexität
- zu frühe UI/API/Provider-Arbeit

Liefere:

- Urteil
- kritische Probleme
- mittlere Probleme
- kleine Probleme
- konkrete Fixes

Ändere keine Dateien.
