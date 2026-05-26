# Decision Policy – RepoTutor

## Zweck

Diese Policy verhindert, dass Agenten offene Produkt-, UX- oder Architekturentscheide still selbst treffen.

## Wann der Agent selbst entscheiden darf

- Technische Details ohne Produktauswirkung (Variablennamen, Dateistruktur innerhalb einer Phase, Importreihenfolge)
- Formatierung und Lint-Korrekturen
- Offensichtliche Bugfixes mit eindeutiger Lösung
- Dokumentations-Alignment (bestehenden Stand korrekt beschreiben)
- Tests, die bestehendes Verhalten absichern
- Kleine Refactorings ohne Verhaltensänderung

## Wann der Agent fragen muss

- Offene UI/UX-Fragen (Layout, Navigation, Interaktionsfluss, Informationsdichte)
- Mehrere plausible Produktvarianten ohne klare Präferenz
- Langzeit-Architekturentscheide mit Auswirkung auf spätere Phasen
- Widersprüchliche Anforderungen
- Entscheide, die spätere Phasen einschränken oder vorwegnehmen
- Unklare Priorität zwischen Einfachheit, Flexibilität und Aufwand

## Pflichtformat für Optionsvorstellung

Wenn der Agent eine Frage stellt, muss er dieses Format verwenden:

```markdown
## Offener Entscheidungspunkt: [Titel]

**Kontext:** [Warum muss das jetzt entschieden werden?]

**Option A – [Name]**

- Vorteil: ...
- Nachteil: ...
- Aufwand: ...

**Option B – [Name]**

- Vorteil: ...
- Nachteil: ...
- Aufwand: ...

**Empfehlung:** Option [A/B], weil [Begründung].

**Frage:** [Konkrete, beantwortbare Frage]
```

## Verboten

- UI/UX-Richtung still setzen und erst im Code sichtbar machen
- Interaktionsmuster ohne Abstimmung festlegen
- Phase 5 beginnen, bevor alle Decision-Gate-Punkte aus `docs/phases/phase_05_tui.md` beantwortet sind
- Visuellen Stil einseitig wählen
- Comfort-Features vor Core-Interaktion priorisieren, ohne zu fragen

## Verweis

Siehe auch: `.claude/rules/08-ui-decisions.md`, `docs/phases/phase_05_tui.md`.
