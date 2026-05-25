# RepoTutor – Konzept

## Kurzbeschreibung

RepoTutor ist ein privates lokales Lern- und Analyse-Tool. Es soll ein Softwareprojekt auf dem eigenen Rechner einlesen, die Projektstruktur verständlich zusammenfassen und einzelne Dateien in einfacher deutscher Sprache erklären.

Das Tool ist kein öffentliches Produkt, keine SaaS-Anwendung und kein autonomer Coding-Agent. Es ist ein persönliches Werkzeug, um eigenen Code und KI-generierten Code besser zu verstehen.

> RepoTutor erklärt, was in einer Datei passiert, warum sie existiert, womit sie zusammenhängt und welche Stellen schwierig oder fehleranfällig sind.

## Hauptziel

Das Ziel ist echtes Codeverständnis, nicht nur eine hübsche Zusammenfassung.

RepoTutor soll beantworten können:

- Was ist das für ein Projekt?
- Welche Dateien sind wichtig?
- Was macht eine bestimmte Datei?
- Welche Funktionen, Komponenten oder Klassen sind relevant?
- Was passiert Schritt für Schritt?
- Welche anderen Dateien hängen damit zusammen?
- Welche Fachbegriffe muss ich verstehen?
- Was ist an der Datei potenziell problematisch?
- Habe ich die Datei wirklich verstanden?

## Zielgruppe

RepoTutor ist für private Nutzung gedacht.

Konkrete Anwendungsfälle:

- eigene Projekte nach einer Pause wieder verstehen
- KI-generierten Code prüfen, bevor er übernommen wird
- fremde Repos analysieren, ohne direkt alles ändern zu lassen
- schrittweise Codeverständnis bei größeren Projekten aufbauen

Kein Multi-User-Support, keine Authentifizierung, keine Cloud-Pflicht.

## Grundprinzipien

### Erst Fakten sammeln, dann KI nutzen

Das Tool darf nicht sofort ein komplettes Repo an ein Modell schicken.

Stattdessen:

1. Projekt lokal scannen.
2. Dateien und Struktur erfassen.
3. Imports, Exports und Einstiegspunkte erkennen.
4. Einen Projektindex erzeugen.
5. Erst danach gezielte KI-Erklärungen für einzelne Dateien generieren.

Das reduziert Halluzinationen, spart Kontext und macht die Antworten belastbarer.

### Kein Repo-Müll

Standardmäßig ignorieren:

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
*.lock
*.log
.DS_Store
```

### Erklärungen müssen belegbar sein

RepoTutor soll keine freien Behauptungen ausgeben. Gute Erklärungen beziehen sich auf konkrete Codebereiche:

- Dateiabschnitt
- Funktion
- Komponente
- Klasse
- Import
- Export
- Aufrufkette

Wenn etwas unklar ist, muss das Tool das offen sagen.

### Einfache Sprache

Schlecht:

```text
Die Komponente kapselt einen controlled input stateful über einen Hook und delegiert die Mutation an einen upstream handler.
```

Besser:

```text
Diese Komponente zeigt ein Eingabefeld. Der eingegebene Text wird gespeichert. Wenn du auf Senden drückst, wird der Text an eine Funktion von außen weitergegeben.
```

Fachbegriffe dürfen verwendet werden, müssen aber im Kontext erklärt werden.

### Streaming ist Pflicht, wenn KI genutzt wird

KI-Erklärungen können mehrere Sekunden dauern. Deshalb muss die spätere Modellantwort gestreamt und sichtbar fortlaufend angezeigt werden.

Kein blockierendes Warten auf eine komplette Antwort.

## Hauptfunktionen V1

### Projekt öffnen

Der Nutzer gibt einen lokalen Projektpfad an.

RepoTutor prüft:

- existiert der Pfad?
- ist es ein Ordner?
- enthält er relevante Projektdateien?
- ist es wahrscheinlich ein Git-Repo?
- welche Sprache oder Frameworks sind erkennbar?

### Projektstruktur anzeigen

Bereinigte Baumansicht ohne Müllordner.

Beispiel:

```text
Disa_Ai/
  src/
    components/
    pages/
    hooks/
    providers/
    services/
  public/
  package.json
  vite.config.ts
```

### Projekt grob einordnen

Soweit möglich erkennen:

- Projekttyp
- Framework
- Paketmanager
- Einstiegspunkte
- wichtige Konfigurationsdateien
- Test-Setup
- Build-System

Beispiel:

```text
Projektart: React-App mit Vite und TypeScript
Einstieg:   src/main.tsx
Layout:     src/App.tsx
State:      src/providers/ + src/hooks/
Styling:    Tailwind CSS
```

### Datei auswählen

Unterstützte Dateitypen für V1:

```text
.ts .tsx .js .jsx .py .json .md .css .html .yml .yaml
```

Priorität:

1. TypeScript / React
2. Python
3. Config-Dateien
4. Markdown-Dokumentation

### Datei erklären

Eine Dateierklärung hat feste Struktur:

1. Kurz gesagt
2. Warum gibt es diese Datei?
3. Wichtige Bestandteile
4. Ablauf Schritt für Schritt
5. Wichtige Fachbegriffe
6. Zusammenhänge mit anderen Dateien
7. Schwierige oder riskante Stellen
8. Merksatz

### Erklärungsmodi V1

| Modus | Zweck |
|---|---|
| Einfach | Sehr verständlich, ohne unnötige Fachsprache |
| Normal | Technisch genauer, aber noch lesbar |
| Zusammenhang | Fokus auf Imports, Exports und Nachbardateien |
| Lernfragen | Mini-Quiz zum Prüfen des Verständnisses |

Zeile-für-Zeile-Erklärung und tiefere Risikoanalyse kommen erst nach stabiler V1.

### Rückfragen zur Datei

Nach einer Erklärung kann der Nutzer Rückfragen stellen:

- Warum wird hier `useEffect` benutzt?
- Was passiert, wenn diese Funktion fehlschlägt?
- Welche Datei ruft diese Komponente auf?
- Was müsste ich verstehen, bevor ich diese Datei ändere?

Die Antwort nutzt ausgewählte Datei, Projektindex und relevante Nachbardateien.

### Lernfragen

RepoTutor kann Lernfragen erzeugen, zum Beispiel:

```text
1. Welche Hauptaufgabe hat diese Datei?
2. Welche Funktion wird ausgelöst, wenn der Nutzer auf Senden klickt?
3. Welche importierte Datei scheint besonders wichtig zu sein?
4. Was könnte passieren, wenn der Ladezustand nicht korrekt gesetzt wird?
5. Welche Stelle würdest du dir genauer ansehen, bevor du etwas änderst?
```

## Empfohlene technische Richtung

- Python als Hauptsprache
- Textual für Terminal-Oberfläche
- Standardbibliothek für Dateiscan, Hashing und Basislogik
- `ast` für Python-Importanalyse
- Regex für einfache TS/JS-Importanalyse in V1
- `tree-sitter` frühestens V2
- z.ai GLM Coding Plan mit `glm-5.1` erst nach stabiler Core-Logik
- Markdown-Ausgabe für Erklärungen
- Streaming für Modellantworten

## Start und Verteilung

Da es ein privates Tool ist:

```bash
python main.py
```

Später optional mit Shell-Alias.

Kein Packaging in V1. Kein `.deb`, kein AppImage, kein PyPI.

## Harte Nicht-Ziele V1

Nicht bauen:

- autonomer Coding-Agent
- automatische Codeänderungen
- GitHub-Issue-/PR-Automation
- Web-App
- SaaS
- Multi-User/Auth
- Packaging
- MCP-Integration
- Plugin-System
- Datenbankpflicht

## Wichtigster Satz

> Erst verstehen, dann ändern.

Das ist der eigentliche Wert von RepoTutor.
