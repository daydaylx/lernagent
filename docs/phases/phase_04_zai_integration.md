# Phase 04 – z.ai Integration

Status: erledigt (2026-05-25). z.ai GLM 5.1 Streaming-Client ist implementiert und getestet.

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

## Verifikation (bestanden)

- Mock-Streaming funktioniert. ✓
- Fehlender API-Key wird verständlich gemeldet. ✓
- Keine echten API-Calls in Unit-Tests. ✓
- `pytest -q` → 45 Tests passing (Phase 4). ✓
- `ruff check .` → clean. ✓
