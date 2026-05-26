# UI-Entscheidungsregel

Vor Phase 5 müssen alle Punkte aus dem Decision Gate in `docs/phases/phase_05_tui.md` vom Nutzer beantwortet sein.

## UI-Fragen, die immer gestellt werden müssen

Bevor Phase 5 beginnt, müssen diese Punkte geklärt sein:

- Layout-Basisstruktur: Single-View, Split-View oder Panel-Struktur?
- Navigationsprinzip: Tastaturnavigation, Mausklick oder beides gleichwertig?
- Informationshierarchie: Was ist prominent – Projektbaum, Erklärung oder Eingabe?
- Kompaktheitsgrad: Minimalistisch oder informationsdicht?
- Interaktionsfluss: Datei wählen → Modus wählen → Erklärung, oder anders?
- Lernmodus- vs. Analysemodus-Anteil: Was steht im Vordergrund?
- Placement: Wo erscheinen Projektbaum, Erklärung und Q&A?
- Fehlerdarstellung: Inline, Statusleiste oder Modal?

## Verhalten bei offenen Punkten

Wenn eines der obigen Punkte unklar ist, muss der Agent zuerst einen UI-Optionsvorschlag erstellen:

- 2–3 Varianten mit konkreten ASCII-Mockups
- Vor- und Nachteile je Variante
- Aufwandsschätzung
- Empfehlung mit Begründung
- Konkrete Frage an den Nutzer

Phase 5 darf erst nach explizitem Go beginnen.

## Verboten

- UI still bauen und Designrichtung im Code festlegen
- Interaktionsmuster ohne Abstimmung implementieren
- Phase 5 starten, wenn Decision Gate offen ist
- Comfort-Features vor Core-Interaktion einbauen

## Verweis

Siehe auch: `docs/DECISION_POLICY.md`, `docs/phases/phase_05_tui.md`.
