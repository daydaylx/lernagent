---
description: Prüfe Tests, Lint und Dokumentationsstand ohne neue Features.
agent: plan
---

Lies zuerst `AGENTS.md`, `docs/VERIFICATION.md`, `docs/QUALITY_GATES.md` und die relevante Phase- oder Issue-Doku.

Prüfe streng:

- echte Tests statt Fake-Tests
- echte Assertions
- Dokumentation gegen tatsächlichen Stand
- Scope-Creep
- Security- und Secret-Risiken

Führe, sofern verfügbar und angemessen, diese Prüfungen aus:

- `pytest -q`
- `ruff check .`

Berichte:

- ausgeführte Kommandos
- Ergebnis
- Fehler
- Lücken
- konkreten Fix-Plan

Baue keine neuen Features.
