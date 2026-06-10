"""Tests for workflow memory (agent/workflow_memory.py)."""
import json
from types import SimpleNamespace

import pytest

from agent import workflow_memory as wm


def _fake_llm(reply: str):
    def _caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return _caller


TRANSCRIPT = [
    {"role": "user", "content": "Ship the release"},
    {"role": "assistant", "content": "ran tests, bumped version, tagged, pushed — released"},
]

ONE_WF = json.dumps([{
    "name": "Ship Release",
    "description": "Test, bump, tag, push a release.",
    "steps": [
        {"name": "test", "prompt": "Run the full test suite", "output": "test_result"},
        {"name": "tag", "prompt": "Bump version and tag using {test_result}"},
    ],
}])


def test_parse_tolerates_code_fence_and_incomplete_workflows():
    raw = (
        "```json\n[" +
        '{"name":"ok","description":"d","steps":[{"name":"a","prompt":"x"},{"name":"b","prompt":"y"}]},' +
        '{"name":"one-step","steps":[{"name":"a","prompt":"x"}]},' +   # <2 steps -> dropped
        '{"name":"","steps":[{"prompt":"x"},{"prompt":"y"}]}' +        # no name -> dropped
        "]\n```"
    )
    out = wm._parse_proposals(raw)
    assert [p["name"] for p in out] == ["ok"]


def test_render_workflow_yaml_is_loadable(tmp_path, monkeypatch):
    monkeypatch.setenv("JANUS_HOME", str(tmp_path))
    p = wm._parse_proposals(ONE_WF)[0]
    path = wm.write_workflow_draft(p, drafts_dir=tmp_path / "wf")
    # round-trips through the real workflow engine loader
    from agent import workflow_engine as we
    loaded = we.load_workflow(str(path))
    assert loaded["name"] == "ship-release"
    assert [s["name"] for s in loaded["steps"]] == ["test", "tag"]


def test_mine_only_successful_sessions(monkeypatch, tmp_path):
    # success -> mines
    monkeypatch.setattr("agent.outcome_tracker.classify_session", lambda *a, **k: True)
    res = wm.mine_session_workflow(TRANSCRIPT, llm_caller=_fake_llm(ONE_WF), drafts_dir=tmp_path)
    assert len(res["proposals"]) == 1 and res["written"]

    # failure -> skipped
    monkeypatch.setattr("agent.outcome_tracker.classify_session", lambda *a, **k: False)
    assert wm.mine_session_workflow(TRANSCRIPT, llm_caller=_fake_llm(ONE_WF), drafts_dir=tmp_path)["proposals"] == []

    # unclear (None) -> skipped
    monkeypatch.setattr("agent.outcome_tracker.classify_session", lambda *a, **k: None)
    assert wm.mine_session_workflow(TRANSCRIPT, llm_caller=_fake_llm(ONE_WF), drafts_dir=tmp_path)["proposals"] == []


def test_mine_skips_single_step(monkeypatch, tmp_path):
    monkeypatch.setattr("agent.outcome_tracker.classify_session", lambda *a, **k: True)
    one_step = json.dumps([{"name": "x", "steps": [{"name": "a", "prompt": "only one"}]}])
    res = wm.mine_session_workflow(TRANSCRIPT, llm_caller=_fake_llm(one_step), drafts_dir=tmp_path)
    assert res["proposals"] == []


def test_mine_dedupes_existing(monkeypatch, tmp_path):
    monkeypatch.setattr("agent.outcome_tracker.classify_session", lambda *a, **k: True)
    res = wm.mine_session_workflow(
        TRANSCRIPT, llm_caller=_fake_llm(ONE_WF),
        existing_workflow_names=["ship-release"], drafts_dir=tmp_path)
    assert res["proposals"] == []


def test_mine_best_effort_on_llm_failure(monkeypatch, tmp_path):
    monkeypatch.setattr("agent.outcome_tracker.classify_session", lambda *a, **k: True)
    def boom(**kw):
        raise RuntimeError("model down")
    res = wm.mine_session_workflow(TRANSCRIPT, llm_caller=boom, drafts_dir=tmp_path)
    assert res["error"] is not None and res["proposals"] == []


def test_no_classify_bypasses_outcome_gate(tmp_path):
    res = wm.mine_session_workflow(TRANSCRIPT, llm_caller=_fake_llm(ONE_WF),
                                   classify=False, drafts_dir=tmp_path)
    assert len(res["proposals"]) == 1
