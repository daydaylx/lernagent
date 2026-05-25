# CLI Usage Notes

## Grundsatz

CLI-Tools sind nützlich, aber nur, wenn sie kontrolliert genutzt werden.

## Erlaubte Routinebefehle

- `git status`
- `git diff`
- `python --version`
- `pytest -q`
- `ruff check .`
- `ruff format .`

## Nur nach Rückfrage

- `pip install ...`
- `python -m pip install ...`
- `rm ...`
- `git commit ...`
- `git reset ...`
- `git clean ...`

## Verboten ohne expliziten Auftrag

- `git push`
- `sudo ...`
- Secrets lesen
- `.env` ausgeben
- Netzwerkanfragen mit `curl`/`wget`
