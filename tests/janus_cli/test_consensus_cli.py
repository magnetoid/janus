"""Tests for the `janus consensus` CLI (janus_cli/consensus.py)."""
import argparse

from janus_cli import consensus as cc


def test_register_adds_subcommands():
    parent = argparse.ArgumentParser()
    cc.register_cli(parent)
    ns = parent.parse_args(["route", "design a distributed system"])
    assert hasattr(ns, "func") and ns.prompt
    ns2 = parent.parse_args(["status"])
    assert hasattr(ns2, "func")
    ns3 = parent.parse_args(["run", "hi", "--task", "coding"])
    assert ns3.task == "coding"


def test_cmd_route_prints_decision(capsys):
    rc = cc._cmd_route(argparse.Namespace(prompt="what is the capital of France?", task=None))
    out = capsys.readouterr().out
    assert rc == 0
    assert "complexity:" in out and "simple" in out


def test_cmd_status_runs(capsys):
    rc = cc._cmd_status(argparse.Namespace())
    out = capsys.readouterr().out
    assert rc == 0 and "consensus:" in out


def test_cmd_run_dispatches(monkeypatch, capsys):
    monkeypatch.setattr(
        "tools.consensus_tool.consensus_answer",
        lambda prompt, task=None: {
            "answer": "42", "error": None, "complexity": "simple",
            "tier": "cheap", "ensemble": False, "models": ["cheap-m"],
        },
    )
    rc = cc._cmd_run(argparse.Namespace(prompt="what is 6*7", task=None, verbose=False))
    assert rc == 0 and "42" in capsys.readouterr().out


def test_cmd_run_reports_error(monkeypatch, capsys):
    monkeypatch.setattr(
        "tools.consensus_tool.consensus_answer",
        lambda prompt, task=None: {"answer": "", "error": "boom", "complexity": "mid",
                                   "tier": "mid", "ensemble": False, "models": []},
    )
    rc = cc._cmd_run(argparse.Namespace(prompt="x", task=None, verbose=False))
    assert rc == 1
