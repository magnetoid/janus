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
