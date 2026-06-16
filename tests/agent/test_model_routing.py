"""Tests for consensus model routing (agent/model_routing.py)."""
from agent import model_routing as mr


def _cfg(**overrides):
    base = {
        "enabled": True,
        "complexity_mode": "heuristic",
        "model_tiers": {
            "cheap": {"provider": "p", "model": "cheap-m"},
            "mid": {"provider": "p", "model": "mid-m"},
            "smart": {"provider": "p", "model": "smart-m"},
        },
        "ensemble": {"enabled": False, "min_complexity": "hard", "member_count": 3},
    }
    base.update(overrides)
    return {"consensus": base}


_HARD = "Design and prove a distributed lock; analyze the tradeoffs step by step."


def test_enabled_reads_config():
    assert mr.enabled({"consensus": {"enabled": True}}) is True
    assert mr.enabled({"consensus": {"enabled": False}}) is False
    assert mr.enabled({}) is False


def test_simple_routes_to_cheap():
    d = mr.route("what is the capital of France?", config=_cfg(), main_model="main")
    assert d["complexity"] == "simple"
    assert d["tier"] == "cheap" and d["model"] == "cheap-m"
    assert d["ensemble"] is False


def test_hard_routes_to_smart():
    d = mr.route(_HARD, config=_cfg(), main_model="main")
    assert d["complexity"] == "hard"
    assert d["tier"] == "smart" and d["model"] == "smart-m"


def test_empty_tier_falls_back_to_main_model():
    cfg = _cfg(model_tiers={"cheap": {"provider": "", "model": ""}, "mid": {}, "smart": {}})
    d = mr.route("what is 2 plus 2", config=cfg, main_model="main-m", main_provider="mp")
    assert d["model"] == "main-m" and d["provider"] == "mp"


def test_hard_ensemble_when_enabled(monkeypatch):
    monkeypatch.setattr("agent.model_strengths.best_models_for",
                        lambda task, available=None, n=4: ["a", "b", "c", "d"][:n])
    cfg = _cfg(ensemble={"enabled": True, "min_complexity": "hard", "member_count": 3})
    d = mr.route(_HARD, task="coding", config=cfg, main_model="main")
    assert d["ensemble"] is True
    assert d["members"] == ["a", "b", "c"]


def test_simple_never_ensembles_even_when_enabled(monkeypatch):
    monkeypatch.setattr("agent.model_strengths.best_models_for",
                        lambda task, available=None, n=4: ["a", "b", "c"])
    cfg = _cfg(ensemble={"enabled": True, "min_complexity": "hard", "member_count": 3})
    d = mr.route("what is the capital of France?", config=cfg, main_model="main")
    assert d["ensemble"] is False and d["members"] == []


def test_consensus_members_reuses_kb(monkeypatch):
    monkeypatch.setattr("agent.model_strengths.best_models_for",
                        lambda task, available=None, n=4: ["x", "y"])
    assert mr.consensus_members("math", n=2) == ["x", "y"]


def test_route_best_effort_on_bad_config():
    d = mr.route("hello", config={"consensus": "not-a-dict"}, main_model="m")
    assert d["model"] == "m"
    assert d["complexity"] in ("simple", "mid", "hard")
