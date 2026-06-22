"""Regression tests for gateway runtime config env-var expansion."""

from __future__ import annotations

import json

import pytest

import gateway.run as gateway_run


def _write_config(home, body: str) -> None:
    (home / "config.yaml").write_text(body, encoding="utf-8")


@pytest.fixture
def gateway_env(monkeypatch, gateway_home):
    """Clear env vars that override the config-file path under test.

    ``gateway_home`` is the shared fixture from ``tests/gateway/conftest.py``: it
    redirects the import-cached ``_janus_home`` across ``gateway.run`` /
    ``gateway.runner`` / ``gateway.core`` (the runner methods resolve relative
    paths via ``gateway.runner._janus_home`` while ``_load_gateway_runtime_config``
    reads config through ``gateway.core._janus_home``) and returns the tmp home.
    Patching only ``gateway.run._janus_home`` left the real ``~/.janus`` in play.
    """
    monkeypatch.delenv("JANUS_PREFILL_MESSAGES_FILE", raising=False)
    monkeypatch.delenv("JANUS_EPHEMERAL_SYSTEM_PROMPT", raising=False)
    monkeypatch.delenv("JANUS_GATEWAY_BUSY_INPUT_MODE", raising=False)
    monkeypatch.delenv("JANUS_RESTART_DRAIN_TIMEOUT", raising=False)
    monkeypatch.delenv("JANUS_BACKGROUND_NOTIFICATIONS", raising=False)
    return gateway_home


def test_load_prefill_messages_expands_env_var_path(monkeypatch, gateway_env):
    prefill = [{"role": "system", "content": "few-shot"}]
    (gateway_env / "prefill.json").write_text(json.dumps(prefill), encoding="utf-8")
    _write_config(gateway_env, "prefill_messages_file: ${PREFILL_FILE}\n")
    monkeypatch.setenv("PREFILL_FILE", "prefill.json")

    assert gateway_run.GatewayRunner._load_prefill_messages() == prefill


def test_load_prefill_messages_accepts_legacy_agent_key(monkeypatch, gateway_env):
    prefill = [{"role": "system", "content": "legacy few-shot"}]
    (gateway_env / "prefill.json").write_text(json.dumps(prefill), encoding="utf-8")
    _write_config(gateway_env, "agent:\n  prefill_messages_file: prefill.json\n")

    assert gateway_run.GatewayRunner._load_prefill_messages() == prefill


def test_load_prefill_messages_prefers_top_level_over_legacy(monkeypatch, gateway_env):
    top_level = [{"role": "system", "content": "top-level"}]
    legacy = [{"role": "system", "content": "legacy"}]
    (gateway_env / "top.json").write_text(json.dumps(top_level), encoding="utf-8")
    (gateway_env / "legacy.json").write_text(json.dumps(legacy), encoding="utf-8")
    _write_config(
        gateway_env,
        "prefill_messages_file: top.json\n"
        "agent:\n"
        "  prefill_messages_file: legacy.json\n",
    )

    assert gateway_run.GatewayRunner._load_prefill_messages() == top_level


@pytest.mark.parametrize(
    ("config_body", "env_name", "env_value", "loader_name", "expected"),
    [
        (
            "agent:\n  system_prompt: ${GW_PROMPT}\n",
            "GW_PROMPT",
            "expanded prompt",
            "_load_ephemeral_system_prompt",
            "expanded prompt",
        ),
        (
            "agent:\n  reasoning_effort: ${REASONING_LEVEL}\n",
            "REASONING_LEVEL",
            "high",
            "_load_reasoning_config",
            {"enabled": True, "effort": "high"},
        ),
        (
            "agent:\n  service_tier: ${SERVICE_TIER}\n",
            "SERVICE_TIER",
            "priority",
            "_load_service_tier",
            "priority",
        ),
        (
            "display:\n  busy_input_mode: ${BUSY_MODE}\n",
            "BUSY_MODE",
            "steer",
            "_load_busy_input_mode",
            "steer",
        ),
        (
            "agent:\n  restart_drain_timeout: ${DRAIN_TIMEOUT}\n",
            "DRAIN_TIMEOUT",
            "12",
            "_load_restart_drain_timeout",
            12.0,
        ),
        (
            "display:\n  background_process_notifications: ${BG_MODE}\n",
            "BG_MODE",
            "error",
            "_load_background_notifications_mode",
            "error",
        ),
    ],
)
def test_gateway_runtime_loaders_expand_env_var_templates(
    monkeypatch,
    gateway_env,
    config_body,
    env_name,
    env_value,
    loader_name,
    expected,
):
    _write_config(gateway_env, config_body)
    monkeypatch.setenv(env_name, env_value)

    loader = getattr(gateway_run.GatewayRunner, loader_name)

    assert loader() == expected
