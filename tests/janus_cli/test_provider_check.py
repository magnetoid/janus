"""Tests for janus_cli/provider_check.py — live credential verification.

These assert the *contract* setup relies on: a provider-confirmed rejection
is the only actionable failure; network trouble and unknown providers must
degrade to non-blocking statuses (unreachable/skip), never raise.
"""

from types import SimpleNamespace

import pytest

from janus_cli import provider_check
from janus_cli.provider_check import (
    INVALID,
    OK,
    SKIP,
    UNREACHABLE,
    live_check_provider,
    verify_telegram_token,
)


class _Resp:
    def __init__(self, status_code, json_data=None, text=""):
        self.status_code = status_code
        self._json = json_data
        self.text = text

    def json(self):
        if self._json is None:
            raise ValueError("no json")
        return self._json


def _patch_httpx_get(monkeypatch, fn):
    import httpx

    monkeypatch.setattr(httpx, "get", fn)


# ── verify_telegram_token ───────────────────────────────────────────────


def test_telegram_token_ok_returns_bot_info(monkeypatch):
    def fake_get(url, timeout):
        assert "/getMe" in url
        return _Resp(200, {"ok": True, "result": {"username": "my_janus_bot"}})

    _patch_httpx_get(monkeypatch, fake_get)
    status, info = verify_telegram_token("123:abc")
    assert status == OK
    assert info["username"] == "my_janus_bot"


def test_telegram_token_rejected(monkeypatch):
    _patch_httpx_get(monkeypatch, lambda url, timeout: _Resp(401, {"ok": False}))
    status, info = verify_telegram_token("123:bad")
    assert status == INVALID
    assert info == {}


def test_telegram_network_failure_is_unreachable_not_invalid(monkeypatch):
    def fake_get(url, timeout):
        raise OSError("no network")

    _patch_httpx_get(monkeypatch, fake_get)
    status, _ = verify_telegram_token("123:abc")
    assert status == UNREACHABLE


def test_telegram_empty_token_is_invalid():
    status, _ = verify_telegram_token("")
    assert status == INVALID


# ── live_check_provider ─────────────────────────────────────────────────


def test_no_provider_is_skip():
    assert live_check_provider(None).status == SKIP
    assert live_check_provider("").status == SKIP


def test_openrouter_without_key_is_skip(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    assert live_check_provider("openrouter").status == SKIP


def test_openrouter_ok_carries_latency(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
    seen = {}

    def fake_get(url, headers, timeout):
        seen["auth"] = headers.get("Authorization")
        return _Resp(200)

    _patch_httpx_get(monkeypatch, fake_get)
    result = live_check_provider("openrouter")
    assert result.status == OK
    assert result.latency_ms is not None and result.latency_ms >= 0
    assert seen["auth"] == "Bearer sk-or-test"


@pytest.mark.parametrize(
    "status_code,expected",
    [(401, INVALID), (403, INVALID), (402, INVALID), (429, OK), (500, UNREACHABLE)],
)
def test_openrouter_status_code_mapping(monkeypatch, status_code, expected):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
    _patch_httpx_get(monkeypatch, lambda url, headers, timeout: _Resp(status_code))
    assert live_check_provider("openrouter").status == expected


def test_anthropic_api_key_uses_x_api_key_header(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-api03-test")
    monkeypatch.setattr(
        "janus_cli.auth.get_anthropic_key", lambda: "sk-ant-api03-test"
    )
    seen = {}

    def fake_get(url, headers, timeout):
        seen.update(headers)
        return _Resp(200)

    _patch_httpx_get(monkeypatch, fake_get)
    assert live_check_provider("anthropic").status == OK
    assert seen.get("x-api-key") == "sk-ant-api03-test"
    assert "Authorization" not in seen


def test_anthropic_oauth_token_uses_bearer(monkeypatch):
    monkeypatch.setattr(
        "janus_cli.auth.get_anthropic_key", lambda: "sk-ant-oat01-test"
    )
    seen = {}

    def fake_get(url, headers, timeout):
        seen.update(headers)
        return _Resp(200)

    _patch_httpx_get(monkeypatch, fake_get)
    assert live_check_provider("anthropic").status == OK
    assert seen.get("Authorization") == "Bearer sk-ant-oat01-test"


def test_network_failure_never_raises(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")

    def fake_get(url, headers, timeout):
        raise OSError("dns down")

    _patch_httpx_get(monkeypatch, fake_get)
    assert live_check_provider("openai").status == UNREACHABLE


def test_unknown_provider_without_profile_is_skip(monkeypatch):
    import providers

    monkeypatch.setattr(providers, "get_provider_profile", lambda name: None)
    assert live_check_provider("definitely-not-a-provider").status == SKIP


def test_profile_provider_bearer_check(monkeypatch):
    import providers

    profile = SimpleNamespace(
        auth_type="api_key",
        supports_health_check=True,
        env_vars=("FAKEPROV_API_KEY", "FAKEPROV_BASE_URL"),
        models_url=None,
        base_url="https://api.fakeprov.test/v1",
    )
    monkeypatch.setattr(providers, "get_provider_profile", lambda name: profile)
    monkeypatch.setenv("FAKEPROV_API_KEY", "fk-123")
    seen = {}

    def fake_get(url, headers, timeout):
        seen["url"] = url
        seen["auth"] = headers.get("Authorization")
        return _Resp(200)

    _patch_httpx_get(monkeypatch, fake_get)
    assert live_check_provider("fakeprov").status == OK
    assert seen["url"] == "https://api.fakeprov.test/v1/models"
    # The base-URL env var must never be sent as the credential.
    assert seen["auth"] == "Bearer fk-123"


def test_oauth_profile_is_skip(monkeypatch):
    import providers

    profile = SimpleNamespace(auth_type="oauth", env_vars=("X_TOKEN",))
    monkeypatch.setattr(providers, "get_provider_profile", lambda name: profile)
    assert live_check_provider("some-oauth-prov").status == SKIP


def test_checker_exception_degrades_to_unreachable(monkeypatch):
    monkeypatch.setitem(
        provider_check._DEDICATED, "openrouter", lambda: 1 / 0
    )
    assert live_check_provider("openrouter").status == UNREACHABLE
