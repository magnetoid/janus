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


# --- measurement spine (move 2): pass^k, kinds, noise floor, jump ------------

def _flaky_b_runner():
    """Fails eval "b" on its every 2nd invocation (per-spec counter); "a" always passes."""
    seen = {"b": 0}
    def run(spec):
        if spec.name == "b":
            seen["b"] += 1
            if seen["b"] % 2 == 0:
                return {"final_response": "", "messages": []}
        return {"final_response": spec.checks[0]["value"], "messages": []}
    return run


def test_run_trend_pass_k_records_fractions():
    # "b" passes trial 1 and fails trial 2 -> fraction 0.5; pass^k marks it
    # failed; "a" passes both -> 1.0.
    rec = et.run_trend(specs=_specs(), agent_runner=_flaky_b_runner(), trials=2)
    assert rec["trials"] == 2
    assert rec["per_eval"]["a"] == 1.0 and rec["per_eval"]["b"] == 0.5
    assert rec["passed"] == 1 and rec["pass_rate"] == 0.5  # pass^k: b is not reliable
    assert rec["kinds"] == {"a": "regression", "b": "regression"}


def test_learning_curve_noise_floor_flaky_neither_learned_nor_regressed():
    s = _specs()
    # Point 1: both reliably pass. Point 2: "b" flaky (0.5) — not a regression.
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}), trials=1)
    et.run_trend(specs=s, agent_runner=_flaky_b_runner(), trials=2)
    lc = et.learning_curve()
    assert lc["regressed"] == [] and lc["learned"] == []
    assert lc["flaky"] == ["b"]
    # Point 3: "b" reliably fails -> now it IS a regression.
    et.run_trend(specs=s, agent_runner=_runner({"a"}), trials=2)
    lc = et.learning_curve()
    assert lc["regressed"] == ["b"] and lc["flaky"] == []


def test_gate_capability_churn_does_not_fail(monkeypatch):
    specs = [
        EvalSpec(name="core", prompt="p", checks=[{"type": "contains", "value": "x"}]),
        EvalSpec(name="moonshot", prompt="p",
                 checks=[{"type": "contains", "value": "y"}], kind="capability"),
    ]
    et.run_trend(specs=specs, agent_runner=_runner({"core", "moonshot"}), trials=1)
    et.run_trend(specs=specs, agent_runner=_runner({"core"}), trials=1)
    gate = et.regression_gate()
    assert gate["ok"] is True                       # capability churn is soft
    assert gate["capability_churn"] == ["moonshot"]
    assert "capability eval(s) churned" in gate["message"]


def test_gate_jump_is_advisory_not_a_failure():
    # A genuine win (learn both evals) jumps the pass rate but MUST NOT fail
    # the gate or freeze the loop — the jump is advisory only.
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner(set()), trials=1)       # 0.0
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}), trials=1)  # 1.0 (+1.0)
    gate = et.regression_gate()
    assert gate["ok"] is True                       # genuine learning is not blocked
    assert gate["jump"] == 1.0
    assert gate["warnings"] and "advisory" in gate["message"]


def test_learned_then_regressed_is_caught():
    # 0 -> 1 -> 0: the eval was learned mid-window then broke. First-vs-last
    # (first=0, last=0) would miss it; the per-eval series catches it.
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner({"a"}), trials=1)        # b fails
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}), trials=1)   # b learned
    et.run_trend(specs=s, agent_runner=_runner({"a"}), trials=1)        # b broke again
    gate = et.regression_gate()
    assert gate["ok"] is False and gate["regressed"] == ["b"]


def test_sustained_mid_band_degradation_regresses():
    # Reliable (1.0) then two consecutive sub-reliable points -> regression,
    # even though it never hits 0 (a loop can't park a regression at ~2/3).
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}), trials=1)   # b=1.0
    et.run_trend(specs=s, agent_runner=_flaky_b_runner(), trials=3)     # b=1/3 or 2/3
    et.run_trend(specs=s, agent_runner=_flaky_b_runner(), trials=3)     # b sub-reliable again
    lc = et.learning_curve()
    assert "b" in lc["regressed"]


def test_single_noisy_dip_is_flaky_not_regressed():
    # One sub-reliable point after a reliable one is tolerated (k=3 noise).
    s = _specs()
    et.run_trend(specs=s, agent_runner=_runner({"a", "b"}), trials=1)   # b=1.0
    et.run_trend(specs=s, agent_runner=_flaky_b_runner(), trials=3)     # b sub-reliable once
    lc = et.learning_curve()
    assert lc["regressed"] == [] and "b" in lc["flaky"]


def test_kind_flip_resets_suite_hash():
    # Flipping an eval's kind must change suite_hash — otherwise a failing
    # regression eval could be silently exempted by relabelling it.
    reg = EvalSpec(name="x", prompt="p", checks=[{"type": "contains", "value": "y"}])
    cap = EvalSpec(name="x", prompt="p", checks=[{"type": "contains", "value": "y"}],
                   kind="capability")
    assert et._suite_hash([reg]) != et._suite_hash([cap])


def test_gate_fail_closed_without_history(monkeypatch):
    monkeypatch.setattr(et, "learning_curve", lambda window=None: {
        "regressed": [], "learned": [], "flaky": [], "points": [], "suite_hash": None})
    assert et.regression_gate()["ok"] is True                    # cron: fail-open
    assert et.regression_gate(fail_closed=True)["ok"] is False   # CI: fail-closed


def test_gate_fail_closed_on_empty_suite():
    # Spec dir emptied/archived -> load returns [] -> total 0 points. fail-open
    # passes, but --fail-closed catches the broken harness.
    et.run_trend(specs=[], agent_runner=_runner(set()))
    et.run_trend(specs=[], agent_runner=_runner(set()))
    assert et.regression_gate()["ok"] is True
    assert et.regression_gate(fail_closed=True)["ok"] is False


def test_spec_kind_validation():
    import pytest
    from agent.evals import _spec_from_dict
    ok = _spec_from_dict({"name": "n", "prompt": "p", "kind": "capability",
                          "checks": [{"type": "contains", "value": "x"}]})
    assert ok.kind == "capability"
    default = _spec_from_dict({"name": "n", "prompt": "p",
                               "checks": [{"type": "contains", "value": "x"}]})
    assert default.kind == "regression"
    with pytest.raises(ValueError):
        _spec_from_dict({"name": "n", "prompt": "p", "kind": "vibes",
                         "checks": [{"type": "contains", "value": "x"}]})


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
