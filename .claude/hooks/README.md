# Hooks

Aktuell sind bewusst keine aktiven Hooks eingerichtet.

Claude-Code-Hooks sind deterministischer als normale Anweisungen und sollten nur für Aktionen genutzt werden, die wirklich immer passieren müssen.

Für dieses Repo gilt:

- Keine automatischen Hooks vor Phase 1.
- Keine Hooks, die Git-Operationen ausführen.
- Keine Hooks, die Secrets lesen.
- Später höchstens Hooks für sichere Validierung wie `ruff check .` oder `pytest -q`, wenn die Projektstruktur existiert.
