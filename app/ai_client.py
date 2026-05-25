from __future__ import annotations

import json
from collections.abc import Iterator

import httpx

from app.config import ProviderConfig, get_api_key

_CHAT_PATH = "/chat/completions"


def stream_response(prompt: str, config: ProviderConfig) -> Iterator[str]:
    api_key = get_api_key(config)
    url = config.base_url.rstrip("/") + _CHAT_PATH
    payload = {
        "model": config.model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": config.stream,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    with httpx.Client(timeout=60.0) as client:
        with client.stream("POST", url, json=payload, headers=headers) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                chunk = _parse_sse_line(line)
                if chunk:
                    yield chunk


def _parse_sse_line(line: str) -> str | None:
    if not line.startswith("data: "):
        return None
    data = line[6:]
    if data.strip() == "[DONE]":
        return None
    try:
        return json.loads(data)["choices"][0]["delta"].get("content", "") or None
    except (json.JSONDecodeError, KeyError, IndexError):
        return None
