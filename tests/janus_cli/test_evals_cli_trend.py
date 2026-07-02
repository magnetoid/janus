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


def test_gate_exit_code_propagates_through_real_cli(tmp_path):
    # Regression: main.py used to discard args.func's return value, so the
    # gate printed FAIL but the PROCESS exited 0 — invisible to in-process
    # tests, fatal for CI. Drive the real entry point in a subprocess.
    import os
    import subprocess
    import sys as _sys
    home = tmp_path / ".janus"
    home.mkdir(parents=True)
    env = dict(os.environ, JANUS_HOME=str(home))
    r = subprocess.run(
        [_sys.executable, "-m", "janus_cli.main", "evals", "gate", "--fail-closed"],
        capture_output=True, text=True, env=env, timeout=120)
    assert r.returncode == 1, r.stdout + r.stderr
    assert "FAIL-CLOSED" in r.stdout
    r = subprocess.run(
        [_sys.executable, "-m", "janus_cli.main", "evals", "gate"],
        capture_output=True, text=True, env=env, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr


def test_register_adds_horizon():
    parent = argparse.ArgumentParser()
    ev.register_cli(parent)
    ns = parent.parse_args(["horizon"])
    assert hasattr(ns, "func")


def test_cmd_horizon_reports_scalar(monkeypatch, capsys):
    monkeypatch.setattr(et, "learning_curve", lambda *a, **k: {"points": [
        {"ts": "t1", "pass_rate": 0.5, "horizon_minutes": 15.0},
        {"ts": "t2", "pass_rate": 0.9, "horizon_minutes": 60.0},
    ]})
    rc = ev._cmd_horizon(argparse.Namespace())
    out = capsys.readouterr().out
    assert rc == 0
    assert "1h" in out and "15m" in out and "↑" in out   # rose 15m -> 1h


def test_cmd_horizon_no_data(monkeypatch, capsys):
    monkeypatch.setattr(et, "learning_curve", lambda *a, **k: {"points": []})
    assert ev._cmd_horizon(argparse.Namespace()) == 0
    assert "no horizon data" in capsys.readouterr().out


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
