# explain_project – Referenz-Template

Dieses Dokument beschreibt, welche Projektkontext-Daten in den Prompt einfließen.

## Projektkontext-Felder

| Feld            | Quelle           | Pflicht |
| --------------- | ---------------- | ------- |
| `project_name`  | `ExplainContext` | nein    |
| `related_files` | `ExplainContext` | nein    |

## Verhalten bei fehlenden Daten

- `project_name` leer → "(nicht angegeben)"
- `related_files` leer → "(keine angegeben)"

## Zukünftige Erweiterung (Phase 6+)

- Datei-Abhängigkeitsgraph
- Gesamtstruktur des Projekts
- Zusammenfassung aus mehreren FileIndex-Einträgen
