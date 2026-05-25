# Sicherheitsregel

## Secrets

Nicht lesen, nicht ausgeben, nicht speichern:
- `.env`
- `.env.*`
- API-Keys
- Tokens
- Credentials
- private Schlüssel

## Git

Kein Push.
Kein Commit ohne explizites Go.
Kein Reset/Clean ohne explizites Go.

## Permissions

Projektsettings dürfen Routineprüfungen erleichtern, aber keine riskanten Schreib-/Netzwerkaktionen automatisch erlauben.
