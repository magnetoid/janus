"""Tests for Self-Challenge (agent/self_challenge.py)."""
import json
import os
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


def test_generate_rejects_empty_value_checks():
    # Empty 'contains' would match ANY response -> false-positive pass. Must reject.
    reply = json.dumps({"instruction": "x", "checks": [{"type": "contains", "value": "  "}]})
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_llm(reply)) is None


def test_generate_rejects_non_dict_check_item():
    reply = json.dumps({"instruction": "x", "checks": ["nope", {"type": "contains", "value": "ok"}]})
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_llm(reply)) is None


def test_generate_rejects_regex_check_type():
    # regex is excluded from the allowlist (ReDoS via model-generated patterns).
    reply = json.dumps({"instruction": "x", "checks": [{"type": "regex", "value": ".*"}]})
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_llm(reply)) is None


def test_generate_rejects_bad_length_value():
    reply = json.dumps({"instruction": "x", "checks": [{"type": "min_length", "value": "ten"}]})
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_llm(reply)) is None


def test_generate_accepts_valid_length_check():
    reply = json.dumps({"instruction": "write a long answer",
                        "checks": [{"type": "min_length", "value": 50}]})
    ch = sc.generate_challenge({"topic": "t"}, llm_caller=_llm(reply))
    assert ch is not None and ch["checks"][0]["value"] == 50


def test_default_runner_pins_terminal_env_to_isolated_backend(monkeypatch):
    # The terminal backend comes from $TERMINAL_ENV, so the runner MUST set it to the
    # resolved isolated backend (else execution falls back to host 'local').
    seen = {}

    class _FakeAgent:
        def __init__(self, **kw):
            seen["env"] = os.environ.get("TERMINAL_ENV")

        def run_conversation(self, instr):
            return {"final_response": "", "messages": []}

    monkeypatch.setenv("TERMINAL_ENV", "local")
    monkeypatch.setattr("run_agent.AIAgent", _FakeAgent)
    sc._default_attempt_runner("do it", config={"self_challenge": {"sandbox": "docker"}})
    assert seen["env"] == "docker"
    assert os.environ.get("TERMINAL_ENV") == "local"  # restored afterwards


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


def test_default_runner_refuses_without_isolated_sandbox():
    # Safe-by-default: no isolated backend -> never executes self-generated code.
    assert sc._default_attempt_runner("rm -rf /", config={}) == {"final_response": "", "messages": []}
    assert sc._default_attempt_runner("x", config={"self_challenge": {"sandbox": "local"}})["final_response"] == ""
    assert sc._default_attempt_runner("x", config={"terminal": {"backend": "local"}})["final_response"] == ""


def test_resolve_sandbox_backend():
    assert sc._resolve_sandbox_backend({"self_challenge": {"sandbox": "docker"}}) == "docker"
    assert sc._resolve_sandbox_backend({"self_challenge": {"sandbox": "none"}}) is None
    # auto defers to terminal.backend, only when isolated
    assert sc._resolve_sandbox_backend(
        {"self_challenge": {"sandbox": "auto"}, "terminal": {"backend": "modal"}}) == "modal"
    assert sc._resolve_sandbox_backend(
        {"self_challenge": {"sandbox": "auto"}, "terminal": {"backend": "local"}}) is None


def test_best_effort_never_raises():
    assert isinstance(sc.run_self_challenge(config={}), dict)

    def _boom(**kw):
        raise RuntimeError("x")
    assert sc.generate_challenge({"topic": "t"}, llm_caller=_boom) is None
