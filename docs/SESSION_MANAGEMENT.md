# Session Management

## Ziel

Claude-Code-Sessions sollen klein und fokussiert bleiben.

## Regeln

- Eine Session = eine Phase oder ein klar begrenzter Review.
- Nach abgeschlossener Phase Handoff erzeugen.
- Bei Kontextvermüllung `/clear` nutzen.
- Bei Zwischenständen `/compact` mit klarer Instruktion nutzen.
- Bei Fehlrichtung früh stoppen und korrigieren.

## Compact-Instruktion

```text
/compact Bewahre unbedingt: aktuelle Phase, geänderte Dateien, Testergebnisse, offene Fehler, explizite Nutzerentscheidungen und nächste erlaubte Phase.
```

## Handoff-Prompt

```text
Nutze den Skill context-reset und erstelle eine kompakte Übergabe für eine neue Session.
```
