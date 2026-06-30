"""Longitudinal eval runner: records a pass-rate point per run."""
from agent import eval_trend as et
from agent.evals import EvalSpec


def _specs():
    return [
        EvalSpec(name="a", prompt="p", checks=[{"type": "contains", "value": "x"}]),
        EvalSpec(name="b", prompt="p", checks=[{"type": "contains", "value": "y"}]),
    ]


def _runner(passing_names):
    def run(spec):
        text = ""
        if spec.name in passing_names:
            text = spec.checks[0]["value"]
        return {"final_response": text, "messages": []}
    return run


def test_run_trend_records_point():
    rec = et.run_trend(specs=_specs(), agent_runner=_runner({"a", "b"}))
    assert rec["pass_rate"] == 1.0
    assert rec["total"] == 2 and rec["passed"] == 2
    assert rec["per_eval"] == {"a": True, "b": True}
    assert rec["suite_hash"]
    assert len(et._load_trend()) == 1


def test_run_trend_partial():
    rec = et.run_trend(specs=_specs(), agent_runner=_runner({"a"}))
    assert rec["pass_rate"] == 0.5
    assert rec["per_eval"] == {"a": True, "b": False}


def test_run_trend_no_specs_is_best_effort():
    rec = et.run_trend(agent_runner=_runner(set()))
    assert rec.get("error")


def test_learning_curve_detects_flips():
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner({"a"}))       # b fails
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}))  # b now passes
    curve = et.learning_curve()
    assert len(curve["points"]) == 2
    assert curve["learned"] == ["b"]
    assert curve["regressed"] == []


def test_learning_curve_detects_regression():
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}))
    et.run_trend(specs=s, agent_runner=_runner({"a"}))
    curve = et.learning_curve()
    assert curve["regressed"] == ["b"]
    assert curve["learned"] == []


def test_learning_curve_empty():
    assert et.learning_curve()["points"] == []


import os


def test_compare_feature_reports_delta():
    s = _specs()

    def flag_sensitive_runner(spec):
        on = os.environ.get("JANUS_FLAG_MEMORY__WRITE_TIME_RECONCILE") == "1"
        passing = {"a", "b"} if on else {"a"}
        text = spec.checks[0]["value"] if spec.name in passing else ""
        return {"final_response": text, "messages": []}

    out = et.compare_feature(
        "memory.write_time_reconcile", specs=s, agent_runner=flag_sensitive_runner
    )
    assert out["pass_rate_on"] == 1.0
    assert out["pass_rate_off"] == 0.5
    assert out["delta"] == 0.5
    assert out["per_eval_delta"]["b"] == 1


def test_compare_feature_restores_env(monkeypatch):
    monkeypatch.setenv("JANUS_FLAG_MEMORY__WRITE_TIME_RECONCILE", "preset")
    et.compare_feature(
        "memory.write_time_reconcile", specs=_specs(),
        agent_runner=_runner({"a"}),
    )
    assert os.environ["JANUS_FLAG_MEMORY__WRITE_TIME_RECONCILE"] == "preset"


import yaml
from janus_constants import get_janus_home


def _enable_trend(interval_hours=24):
    home = get_janus_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "config.yaml").write_text(
        yaml.safe_dump({"evals": {"trend": {"enabled": True, "interval_hours": interval_hours}}}),
        encoding="utf-8",
    )


def test_maybe_run_trend_skips_when_disabled():
    assert et.maybe_run_trend(agent_runner=_runner({"a"})) is None


def test_maybe_run_trend_runs_when_due_then_skips():
    _enable_trend()
    from agent.evals import evals_dir
    d = evals_dir(); d.mkdir(parents=True, exist_ok=True)
    (d / "s.yaml").write_text(
        "name: a\nprompt: p\nchecks:\n  - type: contains\n    value: x\n", encoding="utf-8"
    )
    first = et.maybe_run_trend(agent_runner=lambda spec: {"final_response": "x", "messages": []})
    assert first is not None and first.get("pass_rate") == 1.0
    assert et.maybe_run_trend(agent_runner=lambda spec: {"final_response": "x", "messages": []}) is None


# --- regression gate (B-PR3) ------------------------------------------------

def test_regression_gate_fails_on_regression(monkeypatch):
    monkeypatch.setattr(et, "learning_curve", lambda window=None: {
        "regressed": ["a"], "learned": [], "points": [{"pass_rate": 0.5}], "suite_hash": "h"})
    g = et.regression_gate()
    assert g["ok"] is False
    assert g["regressed"] == ["a"]
    assert "REGRESSION" in g["message"]


def test_regression_gate_ok_when_clean(monkeypatch):
    monkeypatch.setattr(et, "learning_curve", lambda window=None: {
        "regressed": [], "learned": ["b"],
        "points": [{"pass_rate": 0.9}, {"pass_rate": 1.0}], "suite_hash": "h"})
    g = et.regression_gate()
    assert g["ok"] is True and g["pass_rate"] == 1.0


def test_regression_gate_ok_without_history(monkeypatch):
    monkeypatch.setattr(et, "learning_curve", lambda window=None: {
        "regressed": [], "learned": [], "points": [], "suite_hash": None})
    assert et.regression_gate()["ok"] is True
