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
