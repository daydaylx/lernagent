# Phase 04 – z.ai Integration

## Ziel

z.ai GLM Coding Plan mit Streaming anbinden.

## Voraussetzungen

Erst nach Phase 1–3.

## Default

```text
model: glm-5.1
base_url: https://api.z.ai/api/coding/paas/v4
api_key_env: ZAI_API_KEY
```

## Nicht erlaubt

- OpenRouter als Default
- Secrets ausgeben
- echte API-Aufrufe in Unit-Tests
- UI als Hauptarbeit

## Erwartete Verifikation

- Mock-Streaming funktioniert.
- fehlender API-Key wird verständlich gemeldet.
- keine echten API-Calls in Unit-Tests.
