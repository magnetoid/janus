"""Tests for Self-Challenge (agent/self_challenge.py)."""
import json
from types import SimpleNamespace

from agent import self_challenge as sc


def _llm(reply):
    def _c(**kw):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _c


def test_enabled_default_off():
    assert sc.enabled({}) is False
    assert sc.enabled({"self_challenge": {"enabled": True}}) is True


def test_generate_challenge_parses_code_as_task():
    reply = json.dumps({"instruction": "Write a function to reverse a string",
                        "checks": [{"type": "contains", "value": "def reverse"}]})
    ch = sc.generate_challenge({"topic": "string algorithms", "why": "keeps failing"},
                               llm_caller=_llm(reply))
    assert ch["instruction"].startswith("Write")
    assert ch["checks"][0]["type"] == "contains"
    assert ch["topic"] == "string algorithms"


def test_generate_rejects_when_no_deterministic_checks():
    reply = json.dumps({"instruction": "do x", "checks": []})
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_llm(reply)) is None


def test_generate_rejects_subjective_check_types():
    reply = json.dumps({"instruction": "do x", "checks": [{"type": "llm_judge", "value": "good"}]})
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_llm(reply)) is None


def test_verify_result_deterministic():
    checks = [{"type": "contains", "value": "hello"}]
    assert sc.verify_result({"final_response": "hello world"}, checks) is True
    assert sc.verify_result({"final_response": "bye"}, checks) is False
    assert sc.verify_result({"final_response": "x"}, []) is False  # no checks -> not verified


def test_run_self_challenge_gated_off():
    rep = sc.run_self_challenge(gaps=[{"topic": "t"}], llm_caller=_llm("{}"),
                                attempt_runner=lambda i, **k: {}, config={})
    assert rep["attempted"] == 0  # disabled -> no-op


def test_run_self_challenge_pass_drafts_quarantined_skill(monkeypatch):
    cfg = {"self_challenge": {"enabled": True, "max_per_cycle": 5}}
    reply = json.dumps({"instruction": "reverse a string",
                        "checks": [{"type": "contains", "value": "olleh"}]})
    drafted = {}
    monkeypatch.setattr("agent.skill_miner.write_skill_draft",
                        lambda proposal, **k: (drafted.setdefault("p", proposal), "skills/.drafts/x")[1])
    rep = sc.run_self_challenge(
        gaps=[{"topic": "strings", "why": "x"}], llm_caller=_llm(reply),
        attempt_runner=lambda instr, **k: {"final_response": "the answer is olleh"}, config=cfg)
    assert rep["attempted"] == 1 and rep["passed"] == 1 and len(rep["drafted"]) == 1
    assert drafted["p"]["source"] == "self-challenge"


def test_run_self_challenge_fail_records_lesson(monkeypatch):
    cfg = {"self_challenge": {"enabled": True, "max_per_cycle": 5}}
    reply = json.dumps({"instruction": "reverse", "checks": [{"type": "contains", "value": "olleh"}]})
    recorded = []
    monkeypatch.setattr("agent.lessons.record_lesson", lambda *a, **k: recorded.append(1))
    rep = sc.run_self_challenge(
        gaps=[{"topic": "t", "why": "y"}], llm_caller=_llm(reply),
        attempt_runner=lambda instr, **k: {"final_response": "wrong"}, config=cfg)
    assert rep["passed"] == 0 and rep["lessons"] == 1


def test_run_self_challenge_caps_per_cycle():
    cfg = {"self_challenge": {"enabled": True, "max_per_cycle": 1}}
    reply = json.dumps({"instruction": "x", "checks": [{"type": "contains", "value": "y"}]})
    calls = {"n": 0}

    def runner(i, **k):
        calls["n"] += 1
        return {"final_response": "y"}

    rep = sc.run_self_challenge(
        gaps=[{"topic": "a"}, {"topic": "b"}, {"topic": "c"}],
        llm_caller=_llm(reply), attempt_runner=runner, config=cfg)
    assert rep["attempted"] == 1 and calls["n"] == 1


def test_draft_skill_real_path_writes_quarantined_draft():
    # Exercises the REAL skill_miner.write_skill_draft to catch proposal-shape drift.
    # (_isolate_janus_home autouse fixture redirects the drafts dir under tmp.)
    path = sc._draft_skill_from_success(
        {"topic": "string reversal", "instruction": "reverse a string"},
        {"final_response": "use s[::-1]"})
    assert path is not None and ".drafts" in str(path)
    from pathlib import Path
    assert Path(path).exists()


def test_best_effort_never_raises():
    assert isinstance(sc.run_self_challenge(config={}), dict)

    def _boom(**kw):
        raise RuntimeError("x")
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_boom) is None
