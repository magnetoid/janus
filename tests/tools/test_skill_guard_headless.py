"""Agent-created-skill scanning defaults ON in headless contexts (gap G5 / R2).

An agent-created skill is arbitrary Python that later cron / kanban sessions
load and auto-run on the host. The scan was off by default on the rationale
that "the agent can already run code via terminal() anyway" — true with a human
present, but in a headless context terminal()/execute_code are themselves
BLOCKED by the approval gate, so an unscanned agent skill is the one unguarded
code path there. The guard therefore defaults ON when no human is present
(cron / headless), while an explicit config value still wins in both directions.
"""
from __future__ import annotations

import tools.skill_manager_tool as smt


def _clear_ctx(monkeypatch):
    for var in ("JANUS_INTERACTIVE", "JANUS_CRON_SESSION"):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setattr(smt, "_is_gateway_context", lambda: False)


def test_interactive_session_defaults_guard_off(monkeypatch):
    _clear_ctx(monkeypatch)
    monkeypatch.setenv("JANUS_INTERACTIVE", "1")
    monkeypatch.setattr("janus_cli.config.load_config", lambda: {})
    assert smt._guard_agent_created_enabled() is False


def test_cron_session_defaults_guard_on(monkeypatch):
    _clear_ctx(monkeypatch)
    monkeypatch.setenv("JANUS_CRON_SESSION", "1")
    monkeypatch.setattr("janus_cli.config.load_config", lambda: {})
    assert smt._guard_agent_created_enabled() is True


def test_headless_noninteractive_defaults_guard_on(monkeypatch):
    _clear_ctx(monkeypatch)  # no JANUS_INTERACTIVE, no gateway, no cron
    monkeypatch.setattr("janus_cli.config.load_config", lambda: {})
    assert smt._guard_agent_created_enabled() is True


def test_explicit_config_true_wins_even_interactive(monkeypatch):
    _clear_ctx(monkeypatch)
    monkeypatch.setenv("JANUS_INTERACTIVE", "1")
    monkeypatch.setattr("janus_cli.config.load_config",
                        lambda: {"skills": {"guard_agent_created": True}})
    assert smt._guard_agent_created_enabled() is True


def test_explicit_config_false_wins_even_headless(monkeypatch):
    _clear_ctx(monkeypatch)  # headless context
    monkeypatch.setattr("janus_cli.config.load_config",
                        lambda: {"skills": {"guard_agent_created": False}})
    assert smt._guard_agent_created_enabled() is False
