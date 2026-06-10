"""Tests for agent/deliberation.py and the dialectic learning gates."""

import json
from types import SimpleNamespace

import pytest
import yaml

from agent.deliberation import (
    _extract_json,
    apply_verdicts,
    deliberate,
    dialectic_enabled,
    quorum_classify,
    red_team_claims,
)
from janus_constants import get_janus_home


class _Resp:
    def __init__(self, content):
        self.choices = [SimpleNamespace(message=SimpleNamespace(content=content))]


def make_caller(by_task):
    """Scripted llm_caller keyed by aux task name.

    A list value is consumed sequentially (for tasks called more than once).
    Records the task of every call in ``calls``.
    """
    calls = []

    def caller(task=None, **kwargs):
        calls.append(task)
        val = by_task[task]
        content = val.pop(0) if isinstance(val, list) else val
        return _Resp(content)

    return caller, calls


def _enable_dialectic(**overrides):
    cfg_path = get_janus_home() / "config.yaml"
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    dialectic = {"enabled": True, **overrides}
    cfg_path.write_text(
        yaml.safe_dump({"learning": {"dialectic": dialectic}}), encoding="utf-8"
    )


class TestExtractJson:
    def test_object_amid_prose(self):
        raw = 'Here is my ruling:\n{"answer": "yes", "nested": {"a": 1}}\nthanks'
        assert _extract_json(raw, "{", "}") == {"answer": "yes", "nested": {"a": 1}}

    def test_array(self):
        assert _extract_json('x [1, 2] y', "[", "]") == [1, 2]

    def test_garbage_returns_none(self):
        assert _extract_json("no json here", "{", "}") is None
        assert _extract_json("{broken", "{", "}") is None


class TestDeliberate:
    def _synth(self, **kw):
        base = {
            "answer": "synthesized", "confidence": "high",
            "frame_dependent": False, "crux": "the crux", "dissent": "",
        }
        base.update(kw)
        return json.dumps(base)

    def test_three_calls_and_verdict(self):
        caller, calls = make_caller({
            "dialectic_advocate": "the case",
            "dialectic_skeptic": "the rebuttal",
            "dialectic_arbiter": self._synth(),
        })
        res = deliberate("is it so?", llm_caller=caller)
        assert res["error"] is None
        assert res["answer"] == "synthesized"
        assert res["confidence"] == "high"
        assert res["crux"] == "the crux"
        assert res["calls"] == 3
        assert calls == ["dialectic_advocate", "dialectic_skeptic", "dialectic_arbiter"]

    def test_frame_dependent_surfaces(self):
        caller, _ = make_caller({
            "dialectic_advocate": "half full",
            "dialectic_skeptic": "half empty",
            "dialectic_arbiter": self._synth(
                frame_dependent=True,
                answer="both: full if you value what's there, empty if you track what's missing",
            ),
        })
        res = deliberate("glass half full?", llm_caller=caller)
        assert res["frame_dependent"] is True
        assert "full" in res["answer"] and "empty" in res["answer"]

    def test_concession_recorded(self):
        caller, _ = make_caller({
            "dialectic_advocate": "2+2=4",
            "dialectic_skeptic": "CONCEDE — arithmetic identity, no honest counter-case.",
            "dialectic_arbiter": self._synth(answer="4"),
        })
        res = deliberate("what is 2+2?", llm_caller=caller)
        assert res["conceded"] is True

    def test_unparseable_synth_preserves_advocate_answer(self):
        caller, _ = make_caller({
            "dialectic_advocate": "best available answer",
            "dialectic_skeptic": "rebuttal",
            "dialectic_arbiter": "I refuse to emit JSON",
        })
        res = deliberate("q", llm_caller=caller)
        assert res["error"]
        assert res["answer"] == "best available answer"

    def test_exception_never_raises(self):
        def boom(**kw):
            raise RuntimeError("provider down")

        res = deliberate("q", llm_caller=boom)
        assert res["error"] == "provider down"

    def test_empty_question(self):
        res = deliberate("  ")
        assert res["error"] == "empty question"


class TestRedTeamClaims:
    CLAIMS = [
        {"id": "user-0", "kind": "fact", "content": "prefers tabs"},
        {"id": "user-1", "kind": "fact", "content": "use port 8080 always"},
        {"id": "memory-0", "kind": "fact", "content": "project uses pytest"},
    ]

    def _ruling(self):
        return json.dumps([
            {"id": "user-0", "verdict": "accept", "confidence": "high",
             "revised_content": None, "crux": "stated directly", "skeptic_objection": ""},
            {"id": "user-1", "verdict": "reject", "confidence": "medium",
             "revised_content": None, "crux": "session-specific",
             "skeptic_objection": "port was for this demo only"},
            {"id": "memory-0", "verdict": "revise", "confidence": "high",
             "revised_content": "janus project uses pytest via scripts/run_tests.sh",
             "crux": "true but underspecified", "skeptic_objection": ""},
        ])

    def test_batched_exactly_three_calls(self):
        caller, calls = make_caller({
            "dialectic_advocate": "cases",
            "dialectic_skeptic": "objections",
            "dialectic_arbiter": self._ruling(),
        })
        res = red_team_claims(self.CLAIMS, transcript="t", llm_caller=caller)
        assert res["error"] is None
        assert res["calls"] == 3
        assert len(calls) == 3

    def test_verdicts_parsed_and_applied(self):
        caller, _ = make_caller({
            "dialectic_advocate": "c", "dialectic_skeptic": "o",
            "dialectic_arbiter": self._ruling(),
        })
        res = red_team_claims(self.CLAIMS, llm_caller=caller)
        split = apply_verdicts(self.CLAIMS, res["verdicts"])
        accepted = {c["id"]: c["content"] for c in split["accepted"]}
        assert "user-0" in accepted
        assert accepted["memory-0"].startswith("janus project uses pytest")
        assert [c["id"] for c in split["rejected"]] == ["user-1"]
        assert "demo only" in split["rejected"][0]["objection"]

    def test_unknown_ids_and_bad_verdicts_ignored(self):
        ruling = json.dumps([
            {"id": "ghost", "verdict": "reject"},
            {"id": "user-0", "verdict": "obliterate"},
        ])
        caller, _ = make_caller({
            "dialectic_advocate": "c", "dialectic_skeptic": "o",
            "dialectic_arbiter": ruling,
        })
        res = red_team_claims(self.CLAIMS, llm_caller=caller)
        assert res["verdicts"] == {}

    def test_revise_without_content_becomes_accept(self):
        ruling = json.dumps([
            {"id": "user-0", "verdict": "revise", "revised_content": None},
        ])
        caller, _ = make_caller({
            "dialectic_advocate": "c", "dialectic_skeptic": "o",
            "dialectic_arbiter": ruling,
        })
        res = red_team_claims(self.CLAIMS, llm_caller=caller)
        assert res["verdicts"]["user-0"]["verdict"] == "accept"

    def test_unparseable_ruling_fails_open(self):
        caller, _ = make_caller({
            "dialectic_advocate": "c", "dialectic_skeptic": "o",
            "dialectic_arbiter": "no json",
        })
        res = red_team_claims(self.CLAIMS, llm_caller=caller)
        assert res["error"]
        assert res["verdicts"] == {}

    def test_unruled_claim_passes_through_accepted(self):
        split = apply_verdicts(self.CLAIMS, {})
        assert len(split["accepted"]) == 3
        assert split["rejected"] == []

    def test_empty_claims_no_calls(self):
        caller, calls = make_caller({})
        res = red_team_claims([], llm_caller=caller)
        assert res["calls"] == 0 and calls == []


class TestQuorumClassify:
    def test_agreement_yields_label(self):
        caller, _ = make_caller({"dialectic_arbiter": ["SUCCESS", "SUCCESS"]})
        res = quorum_classify("succeeded?", "transcript", llm_caller=caller)
        assert res["agreed"] is True and res["label"] is True

    def test_disagreement_is_contested(self):
        caller, _ = make_caller({"dialectic_arbiter": ["SUCCESS", "FAILURE"]})
        res = quorum_classify("succeeded?", "transcript", llm_caller=caller)
        assert res["agreed"] is False and res["label"] is None
        assert res["votes"] == [True, False]

    def test_junk_vote_not_agreed(self):
        caller, _ = make_caller({"dialectic_arbiter": ["SUCCESS", "perhaps"]})
        res = quorum_classify("succeeded?", "transcript", llm_caller=caller)
        assert res["agreed"] is False and res["label"] is None

    def test_error_never_raises(self):
        def boom(**kw):
            raise RuntimeError("down")

        res = quorum_classify("q", "t", llm_caller=boom)
        assert res["error"] and res["label"] is None


class TestConfigGate:
    def test_default_off(self):
        assert dialectic_enabled("memory") is False

    def test_master_switch_enables_paths(self):
        _enable_dialectic()
        assert dialectic_enabled("memory") is True
        assert dialectic_enabled("outcomes") is True

    def test_per_path_override(self):
        _enable_dialectic(memory=False)
        assert dialectic_enabled("memory") is False
        assert dialectic_enabled("skills") is True


class _FakeStore:
    def __init__(self):
        self.user_entries = []
        self.memory_entries = []
        self.added = []

    def add(self, target, content):
        self.added.append((target, content))
        return {"success": True}


class TestMinerIntegration:
    MESSAGES = [
        {"role": "user", "content": "for this demo use port 8080; btw I always prefer tabs"},
        {"role": "assistant", "content": "done"},
    ]

    def test_memory_gate_blocks_rejected_fact(self):
        from agent.memory_miner import mine_session_memory

        _enable_dialectic()
        facts = json.dumps({"user": ["prefers tabs", "always use port 8080"], "memory": []})
        ruling = json.dumps([
            {"id": "user-0", "verdict": "accept"},
            {"id": "user-1", "verdict": "reject",
             "skeptic_objection": "demo-scoped instruction phrased as permanent"},
        ])
        caller, _ = make_caller({
            "memory_mining": facts,
            "dialectic_advocate": "c", "dialectic_skeptic": "o",
            "dialectic_arbiter": ruling,
        })
        store = _FakeStore()
        result = mine_session_memory(self.MESSAGES, store, llm_caller=caller)
        assert result["error"] is None
        assert store.added == [("user", "prefers tabs")]
        assert result["red_team"]["accepted"] == 1
        assert "demo-scoped" in result["red_team"]["rejected"][0]["objection"]

    def test_memory_gate_fails_open_on_arbiter_garbage(self):
        from agent.memory_miner import mine_session_memory

        _enable_dialectic()
        facts = json.dumps({"user": ["prefers tabs"], "memory": []})
        caller, _ = make_caller({
            "memory_mining": facts,
            "dialectic_advocate": "c", "dialectic_skeptic": "o",
            "dialectic_arbiter": "not json",
        })
        store = _FakeStore()
        result = mine_session_memory(self.MESSAGES, store, llm_caller=caller)
        assert store.added == [("user", "prefers tabs")]
        assert "red_team" not in result

    def test_memory_gate_disabled_makes_no_dialectic_calls(self):
        from agent.memory_miner import mine_session_memory

        facts = json.dumps({"user": ["prefers tabs"], "memory": []})
        caller, calls = make_caller({"memory_mining": facts})
        store = _FakeStore()
        mine_session_memory(self.MESSAGES, store, llm_caller=caller)
        assert calls == ["memory_mining"]
        assert store.added == [("user", "prefers tabs")]

    def test_skill_gate_flags_rejected_draft(self, tmp_path):
        from agent.skill_miner import mine_session_skills

        _enable_dialectic()
        proposals = json.dumps([{
            "name": "lucky-deploy", "description": "Deploys the app.",
            "when_to_use": "deploying", "steps": ["run deploy"],
        }])
        ruling = json.dumps([
            {"id": "lucky-deploy", "verdict": "reject",
             "skeptic_objection": "single lucky success, not a procedure"},
        ])
        caller, _ = make_caller({
            "skill_mining": proposals,
            "dialectic_advocate": "c", "dialectic_skeptic": "o",
            "dialectic_arbiter": ruling,
        })
        result = mine_session_skills(
            self.MESSAGES, llm_caller=caller, drafts_dir=tmp_path
        )
        assert result["error"] is None
        # Draft still written (drafts are the quarantine), but flagged
        assert len(result["written"]) == 1
        flags = [f for f in result["flagged"] if any("red-team" in i for i in f["issues"])]
        assert flags and "lucky success" in flags[0]["issues"][0]

    def test_outcome_quorum_disagreement_returns_none(self):
        from agent.outcome_tracker import classify_session

        _enable_dialectic()
        caller, _ = make_caller({"dialectic_arbiter": ["SUCCESS", "FAILURE"]})
        assert classify_session(self.MESSAGES, llm_caller=caller) is None

    def test_outcome_quorum_agreement_returns_label(self):
        from agent.outcome_tracker import classify_session

        _enable_dialectic()
        caller, _ = make_caller({"dialectic_arbiter": ["FAILURE", "FAILURE"]})
        assert classify_session(self.MESSAGES, llm_caller=caller) is False
