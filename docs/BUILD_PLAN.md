# RepoTutor – Bauplan

## Zweck dieses Plans

Dieser Plan beschreibt, wie aus dem aktuellen Agenten-Setup schrittweise ein funktionierendes RepoTutor-Tool entstehen soll.

Wichtig: Nicht alles auf einmal bauen. Jede Phase muss einzeln prüfbar sein.

## Gesamtstrategie

1. Agenten-Setup nutzen.
2. Phase planen lassen.
3. Plan prüfen.
4. Nur eine kleine Phase freigeben.
5. Umsetzung verifizieren.
6. Erst danach nächste Phase.

## Phase 0 – Agenten-Setup

Status: erledigt.

Ziel:

- Claude Code bekommt Projektziel, Scope-Grenzen, Regeln, Skills, Phasenverträge und Verification-Vorgaben.

Nicht enthalten:

- kein App-Code
- kein `main.py`
- kein `app/`
- keine Tests
- keine TUI
- keine API

## Phase 1 – Python-Scaffold

Ziel:

Erzeuge die minimale Python-Projektstruktur.

Erlaubt:

```text
main.py
app/__init__.py
app/config.py
app/scanner.py
app/cache.py
app/indexer.py
app/explainer.py
app/ai_client.py
app/ui.py
tests/
pyproject.toml
requirements.txt
config.yaml.example
```

Wichtig: Die Moduldateien dürfen noch minimal sein, aber sie müssen sauber importierbar sein.

Nicht erlaubt:

- keine echte TUI
- keine echte LLM-API
- kein Streaming
- kein kompletter Scanner
- kein kompletter Indexer
- kein Packaging
- keine OpenRouter-Integration

Muss danach funktionieren:

```bash
python --version
python main.py --help
pytest -q
ruff check .
```

Definition of Done:

- Projektstruktur existiert
- Module sind importierbar
- Tests sind nicht leer
- Doku behauptet nicht, dass das Tool schon fertig ist

## Phase 2 – Scanner, Cache, Indexer

Ziel:

Lokale Projektanalyse ohne KI.

### Scanner

Aufgaben:

- Projektordner rekursiv scannen
- Ignore-Regeln anwenden
- unterstützte Dateiendungen erkennen
- Dateigröße erfassen
- relative Pfade liefern
- stabile Sortierung

Ignorieren:

```text
node_modules
.git
dist
build
coverage
.cache
.vite
.next
.nuxt
venv
.venv
__pycache__
.idea
.vscode
```

### Cache

Aufgaben:

- SHA-256-Hash pro Datei
- `.repo_tutor/file_cache.json` lesen/schreiben
- Status erkennen:
  - neu
  - unverändert
  - geändert
- keine vollständigen Quelltexte speichern
- keine API-Keys speichern

### Indexer

Aufgaben:

- Sprache anhand Dateiendung erkennen
- Python-Imports via `ast`
- TS/JS/TSX/JSX-Imports via Regex
- einfache Exports erkennen
- `probable_role` heuristisch setzen

Beispiel für Rollen:

```text
components/ -> UI-Komponente
hooks/      -> Custom Hook
Provider    -> Zustandsmanagement
service     -> Service/Integrationslogik
config      -> Konfiguration
```

Muss danach funktionieren:

```bash
pytest -q
ruff check .
```

Tests müssen prüfen:

- Ignore-Ordner werden übersprungen
- relevante Dateien werden gefunden
- Python-Imports werden erkannt
- TSX-Imports werden erkannt
- Hash ändert sich bei Dateiänderung
- probable_role ist nachvollziehbar

## Phase 3 – Explainer als Prompt-Builder

Ziel:

Prompt-Building ohne echte API.

Erlaubt:

- `app/explainer.py`
- `prompts/explain_file.md`
- `prompts/explain_project.md`
- `prompts/generate_quiz.md`
- Tests für Prompt-Aufbau

Nicht erlaubt:

- keine echte z.ai API
- kein Streaming
- keine TUI als Hauptarbeit

Prompt muss enthalten:

- Projektkontext
- ausgewählte Datei
- Datei-Metadaten
- Imports/Exports
- Modus
- klare Ausgabestruktur

Große Dateien:

- bis 25 KB direkt
- 25–80 KB abschnittsweise vorbereiten
- über 80 KB Warnung und nur Struktur/Imports

## Phase 4 – z.ai GLM 5.1 + Streaming

Ziel:

z.ai GLM Coding Plan anbinden.

Default:

```text
model_provider: zai_coding_plan
model: glm-5.1
base_url: https://api.z.ai/api/coding/paas/v4
api_key_env: ZAI_API_KEY
stream: true
```

Nicht erlaubt:

- kein OpenRouter als Default
- kein `/v1` an den z.ai Coding-Endpunkt anhängen
- keine API-Keys im Code
- keine echten API-Calls in Unit-Tests

Tests:

- fehlender API-Key wird sauber gemeldet
- falscher Endpoint wird verständlich gemeldet
- Mock-Streaming funktioniert
- Timeout wird verständlich behandelt

## Phase 5 – Textual TUI

Ziel:

Terminal-Oberfläche auf stabile Core-Logik setzen.

Layout-Idee:

```text
┌─────────────────┬──────────────────────────────────┐
│ Projektbaum     │ Erklärung / Ausgabe              │
│                 │                                  │
│ src/            │ # Kurz gesagt                    │
│ components/     │ Diese Datei zeigt ...            │
├─────────────────┴──────────────────────────────────┤
│ > Rückfrage eingeben...                            │
└────────────────────────────────────────────────────┘
```

Funktionen:

- Projektpfad auswählen/eingeben
- Projektbaum anzeigen
- Datei auswählen
- Modus auswählen
- Erklärung gestreamt anzeigen
- Rückfrage eingeben
- Fehler sichtbar anzeigen

Nicht erlaubt:

- UI bauen, um fehlende Core-Logik zu kaschieren
- neue Provider-Architektur
- Packaging

## Phase 6 – Lernmodus

Ziel:

RepoTutor wird nicht nur Erklärer, sondern Lernhilfe.

Funktionen:

- Lernfragen erzeugen
- Antworten optional bewerten
- Fachbegriffe sammeln
- Datei-Zusammenhänge als Lernpfad darstellen

Nicht vor Phase 1–5.

## Phase 7 – spätere Erweiterungen

Nur nach stabiler V1:

- Zeile-für-Zeile-Erklärung
- Risikoanalyse
- Datei-Abhängigkeitsgraph
- Review-Modus für KI-generierte Änderungen
- Agenten-Prompts aus Analyse erzeugen

Nicht automatisch umsetzen.

## Reihenfolge, die nicht gebrochen werden darf

```text
Agenten-Setup
→ Python-Scaffold
→ Scanner/Cache/Indexer
→ Prompt-Builder
→ z.ai Streaming
→ Textual UI
→ Lernmodus
```

## Anti-Pattern

Nicht machen:

- zuerst UI bauen
- zuerst API-Client bauen
- alles in eine Datei werfen
- OpenRouter einbauen, obwohl z.ai geplant ist
- leere Tests als Qualität verkaufen
- Docs schreiben, die mehr versprechen als existiert
- komplette Repos an das Modell schicken

## Nächster sinnvoller Claude-Code-Prompt

```text
Lies CLAUDE.md, AGENTS.md, docs/CONCEPT.md, docs/BUILD_PLAN.md und docs/phases/phase_01_agent_to_scaffold.md.
Erstelle einen konkreten Plan für Phase 1.
Ändere noch keine Dateien.
```

Danach erst nach Prüfung:

```text
Go für Phase 1.
Setze nur docs/phases/phase_01_agent_to_scaffold.md und docs/BUILD_PLAN.md Phase 1 um.
Keine UI, keine echte LLM-API, kein Streaming, kein Packaging.
```
