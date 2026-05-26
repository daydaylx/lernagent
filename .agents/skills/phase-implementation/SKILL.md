---
name: phase-implementation
description: Setze eine ausdrücklich freigegebene RepoTutor-Phase oder Adapter-Aufgabe ohne Scope-Creep um.
---

# Skill: phase-implementation

## Voraussetzung

Diesen Workflow nur nutzen, wenn der Nutzer ausdrücklich Go für eine konkrete Phase, ein Issue oder eine klar begrenzte Adapter-Aufgabe gegeben hat.

## Vorgehen

1. Lies `AGENTS.md`, den freigegebenen Plan und die relevante Phase- oder Issue-Doku.
2. Ändere nur die erlaubten Dateien.
3. Halte App-Code, Doku und Adapter strikt getrennt.
4. Schreibe oder aktualisiere Tests nur, wenn der freigegebene Umfang das verlangt.
5. Führe `pytest -q` und `ruff check .` aus, sofern verfügbar.
6. Berichte geänderte Dateien, ausgeführte Prüfungen, Grenzen und verbleibende Risiken.

## Verboten

- Zusätzliche Features außerhalb des freigegebenen Umfangs.
- Provider/API, UI, MCP, Hooks oder Packaging, wenn sie nicht Teil der freigegebenen Phase sind.
- Echte Secrets oder lokale persönliche Configs.
- Commit oder Push ohne ausdrücklichen Auftrag.
