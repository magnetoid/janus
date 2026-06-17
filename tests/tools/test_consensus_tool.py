"""Tests for the consensus tool (tools/consensus_tool.py)."""
from tools import consensus_tool as ct


def _cfg(ensemble_on=False):
    return {"consensus": {
        "enabled": True, "complexity_mode": "heuristic",
        "model_tiers": {
            "cheap": {"provider": "p", "model": "cheap-m"},
            "mid": {"provider": "p", "model": "mid-m"},
            "smart": {"provider": "p", "model": "smart-m"},
        },
        "ensemble": {"enabled": ensemble_on, "min_complexity": "hard", "member_count": 3},
    }}


_HARD = "Design and prove a distributed lock; analyze the tradeoffs step by step."


def test_simple_uses_single_cheap_model():
    calls = {}

    def single(provider, model, prompt):
        calls.update(provider=provider, model=model, prompt=prompt)
        return "cheap answer"

    def ensemble(p, m, t):
        raise AssertionError("simple prompt must not ensemble")

    out = ct.consensus_answer("what is the capital of France?", config=_cfg(),
                              single_caller=single, ensemble_caller=ensemble)
    assert out["error"] is None
    assert out["complexity"] == "simple" and out["tier"] == "cheap"
    assert out["ensemble"] is False and out["models"] == ["cheap-m"]
    assert out["answer"] == "cheap answer"
    assert calls["model"] == "cheap-m"


def test_hard_ensemble_dispatches_to_moa(monkeypatch):
    monkeypatch.setattr("agent.model_strengths.best_models_for",
                        lambda task, available=None, n=4: ["a", "b", "c", "d"][:n])
    seen = {}

    def single(p, m, prompt):
        raise AssertionError("hard prompt with ensemble must not use a single model")

    def ensemble(prompt, members, task):
        seen.update(members=members, task=task)
        return "synthesized"

    out = ct.consensus_answer(_HARD, task="coding", config=_cfg(ensemble_on=True),
                              single_caller=single, ensemble_caller=ensemble)
    assert out["ensemble"] is True
    assert out["models"] == ["a", "b", "c"]
    assert out["answer"] == "synthesized"
    assert seen["task"] == "coding"


def test_caller_error_is_captured():
    def single(p, m, prompt):
        raise RuntimeError("provider down")

    out = ct.consensus_answer("what is 2 plus 2", config=_cfg(),
                              single_caller=single, ensemble_caller=lambda *a: "x")
    assert out["error"] and "provider down" in out["error"]
    assert out["answer"] == ""


def test_check_fn_gates_on_config(monkeypatch):
    monkeypatch.setattr("agent.model_routing.enabled", lambda config=None: True)
    assert ct._consensus_enabled() is True
    monkeypatch.setattr("agent.model_routing.enabled", lambda config=None: False)
    assert ct._consensus_enabled() is False


def test_registered_in_registry():
    import tools.consensus_tool  # noqa: F401 — triggers registration
    from tools.registry import registry
    names = set(getattr(registry, "_tools", {}).keys())
    assert "consensus" in names
