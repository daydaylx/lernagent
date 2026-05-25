# Qualitätsregel

Keine Fake-Fertigstellung.

Nicht erlaubt:
- Tests ohne echte Assertions
- `pass` als angeblich fertige Funktion
- TODO-Kommentare als Implementierung verkaufen
- Dummy-Daten als echte Analyse ausgeben
- Docs, die nicht dem Stand entsprechen

Nach Implementierung:

```bash
pytest -q
ruff check .
```

Wenn diese Befehle noch nicht sinnvoll laufen können, muss der Grund explizit im Ergebnisbericht stehen.
