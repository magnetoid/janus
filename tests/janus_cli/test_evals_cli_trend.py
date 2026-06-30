"""`janus evals trend` records a curve point and prints it."""
import argparse

from janus_cli import evals as ev
from agent.evals import evals_dir
from agent import eval_trend as et


def _setup_specs():
    d = evals_dir(); d.mkdir(parents=True, exist_ok=True)
    (d / "s.yaml").write_text(
        "name: a\nprompt: p\nchecks:\n  - type: contains\n    value: x\n", encoding="utf-8")


def test_register_adds_trend_and_ab():
    parent = argparse.ArgumentParser()
    ev.register_cli(parent)
    ns = parent.parse_args(["trend"])
    assert hasattr(ns, "func")
    ns2 = parent.parse_args(["ab", "memory.write_time_reconcile"])
    assert ns2.flag == "memory.write_time_reconcile"


def test_cmd_trend_runs(monkeypatch, capsys):
    _setup_specs()
    monkeypatch.setattr(et, "run_trend",
                        lambda **k: {"pass_rate": 1.0, "total": 1, "passed": 1,
                                     "per_eval": {"a": True}, "suite_hash": "h"})
    args = argparse.Namespace(path=None)
    rc = ev._cmd_trend(args)
    assert rc == 0
    assert "pass_rate" in capsys.readouterr().out


def test_register_adds_gate():
    parent = argparse.ArgumentParser()
    ev.register_cli(parent)
    ns = parent.parse_args(["gate", "--window", "5"])
    assert ns.window == 5 and hasattr(ns, "func")


def test_cmd_gate_exit_codes(monkeypatch, capsys):
    # regression → exit 1 (CI fails)
    monkeypatch.setattr(et, "regression_gate", lambda **k: {
        "ok": False, "regressed": ["a"], "learned": [], "pass_rate": 0.5,
        "suite_hash": "h", "message": "REGRESSION — 1 eval(s) went pass→fail: a"})
    rc = ev._cmd_gate(argparse.Namespace(run=False, path=None, window=None))
    assert rc == 1
    assert "REGRESSION" in capsys.readouterr().out
    # clean → exit 0
    monkeypatch.setattr(et, "regression_gate", lambda **k: {
        "ok": True, "regressed": [], "learned": ["b"], "pass_rate": 1.0,
        "suite_hash": "h", "message": "OK — no regressions (1 learned)"})
    assert ev._cmd_gate(argparse.Namespace(run=False, path=None, window=None)) == 0
