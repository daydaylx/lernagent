# explain_file – Referenz-Template

Dieses Dokument beschreibt die Struktur, die `app/explainer.py` für Datei-Erklärungen erzeugt.

## Pflichtbestandteile des Prompts

- Dateipfad
- Sprache (python, typescript, javascript, …)
- Wahrscheinliche Rolle (UI-Komponente, Service, …)
- Imports
- Exports (oder Hinweis "keine")
- Dateiinhalt (ggf. gekürzt mit Hinweis)
- Projektname und verwandte Dateien
- Modus-spezifische Ausgabeanweisung

## Ausgabestruktur (Modus normal / context)

1. Kurz gesagt
2. Warum gibt es diese Datei?
3. Wichtige Bestandteile
4. Ablauf Schritt für Schritt
5. Wichtige Fachbegriffe
6. Zusammenhänge mit anderen Dateien
7. Schwierige oder riskante Stellen
8. Merksatz

## Größenbeschränkung

- ≤ 25 000 Zeichen: vollständiger Inhalt
- 25 001–80 000 Zeichen: Kürzung auf 25 000 + `[HINWEIS: Datei zu groß …]`
- > 80 000 Zeichen: Kürzung auf 25 000 + `[WARNUNG: Datei sehr groß …]`

## Pflichtanweisungen (in jedem Modus)

- Einfache deutsche Sprache
- Keine erfundenen Informationen
- Unsicherheit offen markieren
