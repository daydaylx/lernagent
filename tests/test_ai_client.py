import inspect
from unittest.mock import MagicMock, patch

import pytest

from app.ai_client import _parse_sse_line, stream_response
from app.config import DEFAULT_CONFIG, ProviderConfig, get_api_key


def _cfg() -> ProviderConfig:
    return ProviderConfig(
        model="glm-5.1",
        base_url="https://api.z.ai/api/coding/paas/v4",
        api_key_env="ZAI_API_KEY",
        stream=True,
    )


def _mock_client(lines: list[str]) -> MagicMock:
    mock_resp = MagicMock()
    mock_resp.iter_lines.return_value = iter(lines)
    mock_resp.raise_for_status = MagicMock()
    mock_resp.__enter__ = lambda s: s
    mock_resp.__exit__ = MagicMock(return_value=False)

    mock_client = MagicMock()
    mock_client.stream.return_value = mock_resp
    mock_client.__enter__ = lambda s: s
    mock_client.__exit__ = MagicMock(return_value=False)
    return mock_client


def test_get_api_key_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ZAI_API_KEY", raising=False)
    with pytest.raises(EnvironmentError, match="ZAI_API_KEY"):
        get_api_key(_cfg())


def test_get_api_key_returns_value(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ZAI_API_KEY", "test-key-123")
    assert get_api_key(_cfg()) == "test-key-123"


def test_parse_sse_content() -> None:
    line = 'data: {"choices": [{"delta": {"content": "Hallo"}}]}'
    assert _parse_sse_line(line) == "Hallo"


def test_parse_sse_done() -> None:
    assert _parse_sse_line("data: [DONE]") is None


def test_parse_sse_non_data_line() -> None:
    assert _parse_sse_line("event: ping") is None
    assert _parse_sse_line("") is None


def test_parse_sse_empty_delta() -> None:
    line = 'data: {"choices": [{"delta": {}}]}'
    assert _parse_sse_line(line) is None


def test_parse_sse_malformed_json() -> None:
    assert _parse_sse_line("data: {broken json}") is None


def test_stream_response_mock(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ZAI_API_KEY", "test-key")
    sse_lines = [
        'data: {"choices": [{"delta": {"content": "Hallo"}}]}',
        'data: {"choices": [{"delta": {"content": " Welt"}}]}',
        "data: [DONE]",
    ]
    with patch("app.ai_client.httpx.Client", return_value=_mock_client(sse_lines)):
        chunks = list(stream_response("Erkläre print().", _cfg()))
    assert chunks == ["Hallo", " Welt"]


def test_stream_raises_before_http_on_missing_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ZAI_API_KEY", raising=False)
    with patch("app.ai_client.httpx.Client") as mock_cls:
        with pytest.raises(EnvironmentError):
            list(stream_response("Prompt", _cfg()))
        mock_cls.assert_not_called()


def test_no_forbidden_http_imports() -> None:
    import app.ai_client as module

    source = inspect.getsource(module)
    for forbidden in ("requests", "urllib.request", "http.client"):
        assert forbidden not in source, f"Verbotener Import: {forbidden!r}"


def test_default_config_values() -> None:
    assert DEFAULT_CONFIG.model == "glm-5.1"
    assert DEFAULT_CONFIG.base_url == "https://api.z.ai/api/coding/paas/v4"
    assert DEFAULT_CONFIG.api_key_env == "ZAI_API_KEY"
    assert DEFAULT_CONFIG.stream is True
