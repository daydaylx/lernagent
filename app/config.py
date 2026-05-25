from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class ProviderConfig:
    model: str
    base_url: str
    api_key_env: str
    stream: bool


DEFAULT_CONFIG = ProviderConfig(
    model="glm-5.1",
    base_url="https://api.z.ai/api/coding/paas/v4",
    api_key_env="ZAI_API_KEY",
    stream=True,
)


def get_api_key(config: ProviderConfig) -> str:
    key = os.environ.get(config.api_key_env, "")
    if not key:
        raise EnvironmentError(
            f"API-Key fehlt. Setze die Umgebungsvariable {config.api_key_env!r}."
        )
    return key
