"""Learned routing for delegated subtasks (Track D).

Unit tests for tools.delegate_tool._maybe_route_task_credentials — the
task-entry routing decision — and its config default. The helper must be
strictly opt-in, lose to every explicit override, and fall back to parent
inheritance on any failure.
"""
from types import SimpleNamespace

from agent import model_routing
from agent import model_strengths as ms
from tools import delegate_tool as dt


INHERIT = {"model": None, "provider": None, "base_url": None,
           "api_key": None, "api_mode": None}


def _parent(model="parent-big", provider="parentprov"):
    return SimpleNamespace(model=model, provider=provider)


def _route_to(model, provider, band="simple", tier="cheap"):
    return lambda goal, **kw: {
        "complexity": band, "tier": tier, "provider": provider, "model": model,
        "ensemble": False, "members": [], "task": None,
    }


def test_off_by_default():
    creds, info = dt._maybe_route_task_credentials("fix typo", {}, _parent(), dict(INHERIT))
    assert creds == INHERIT and info is None


def test_config_default_is_off():
    from janus_cli.config import DEFAULT_CONFIG
    assert DEFAULT_CONFIG["delegation"]["routing"] is False


def test_static_override_wins(monkeypatch):
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    static = dict(INHERIT, model="pinned-model")
    creds, info = dt._maybe_route_task_credentials(
        "task", {"routing": True}, _parent(), static)
    assert creds is static and info is None


def test_consensus_disabled_is_noop(monkeypatch):
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: False)
    creds, info = dt._maybe_route_task_credentials(
        "task", {"routing": True}, _parent(), dict(INHERIT))
    assert creds == INHERIT and info is None


def test_routes_same_provider_model_only(monkeypatch):
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    monkeypatch.setattr(model_routing, "route", _route_to("mini-1", "parentprov"))
    creds, info = dt._maybe_route_task_credentials(
        "fix typo", {"routing": True}, _parent(), dict(INHERIT))
    assert creds["model"] == "mini-1"
    # Same provider: only the model is overridden — credentials inherit.
    assert creds["provider"] is None and creds["base_url"] is None
    assert info == {"band": "simple", "model": "mini-1"}


def test_route_to_parent_model_is_plain_inherit(monkeypatch):
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    monkeypatch.setattr(model_routing, "route", _route_to("parent-big", "parentprov", band="mid"))
    creds, info = dt._maybe_route_task_credentials(
        "task", {"routing": True}, _parent(), dict(INHERIT))
    assert creds == INHERIT and info is None


def test_learned_distrust_unroutes(monkeypatch):
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    monkeypatch.setattr(model_routing, "route", _route_to("flaky-mini", "parentprov"))
    monkeypatch.setattr(ms, "outcome_score", lambda task, model: (0.1, 5))
    creds, info = dt._maybe_route_task_credentials(
        "task", {"routing": True}, _parent(), dict(INHERIT))
    assert creds == INHERIT and info is None


def test_distrust_needs_min_samples(monkeypatch):
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    monkeypatch.setattr(model_routing, "route", _route_to("young-mini", "parentprov"))
    monkeypatch.setattr(ms, "outcome_score", lambda task, model: (0.0, 2))  # < 3 samples
    creds, info = dt._maybe_route_task_credentials(
        "task", {"routing": True}, _parent(), dict(INHERIT))
    assert creds["model"] == "young-mini" and info is not None


def test_cross_provider_without_key_falls_back(monkeypatch):
    import janus_cli.runtime_provider as rp
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    monkeypatch.setattr(model_routing, "route", _route_to("other-mini", "otherprov"))
    monkeypatch.setattr(rp, "resolve_runtime_provider",
                        lambda **kw: {"api_key": "", "base_url": "https://x"})
    creds, info = dt._maybe_route_task_credentials(
        "task", {"routing": True}, _parent(), dict(INHERIT))
    assert creds == INHERIT and info is None


def test_cross_provider_with_key_resolves_bundle(monkeypatch):
    import janus_cli.runtime_provider as rp
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    monkeypatch.setattr(model_routing, "route", _route_to("other-mini", "otherprov", band="hard", tier="smart"))
    monkeypatch.setattr(rp, "resolve_runtime_provider", lambda **kw: {
        "provider": "otherprov", "api_key": "sk-x", "base_url": "https://o.example",
        "api_mode": "chat_completions",
    })
    creds, info = dt._maybe_route_task_credentials(
        "hard task", {"routing": True}, _parent(), dict(INHERIT))
    assert creds["model"] == "other-mini" and creds["provider"] == "otherprov"
    assert creds["api_key"] == "sk-x" and creds["api_mode"] == "chat_completions"
    assert info == {"band": "hard", "model": "other-mini"}


def test_route_failure_falls_back(monkeypatch):
    monkeypatch.setattr(model_routing, "enabled", lambda *a, **k: True)
    def boom(*a, **k):
        raise RuntimeError("classifier down")
    monkeypatch.setattr(model_routing, "route", boom)
    creds, info = dt._maybe_route_task_credentials(
        "task", {"routing": True}, _parent(), dict(INHERIT))
    assert creds == INHERIT and info is None
