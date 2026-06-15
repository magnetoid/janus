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
