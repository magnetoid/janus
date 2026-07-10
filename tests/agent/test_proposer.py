"""The autonomous self-improvement proposer (Phase 2.1).

The missing generator half of the DGM-lite loop: self_improve.propose() had zero
production callers. This module detects persistently-failing AGENT-CREATED skills
and generates improved variants as GATED proposals for human review — it never
evaluates or promotes (promotion stays behind the quadruple gate + human
approval). Gated behind learning.self_improve.enabled, the governor, and the
autonomy floor, so a default install proposes nothing.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from agent import proposer, self_improve


def _enable_self_improve(monkeypatch):
    monkeypatch.setattr(self_improve, "enabled", lambda config=None: True)
    monkeypatch.setattr(self_improve, "require_human_approval", lambda config=None: True)


def _llm(reply: str):
    def caller(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=reply))])
    return caller


# --------------------------------------------------------------------------
# failing-skill detection
# --------------------------------------------------------------------------

def test_find_failing_skills_filters_by_rate_uses_and_provenance(monkeypatch):
    monkeypatch.setattr("agent.outcome_tracker.skill_stats", lambda: {
        "weak-agent-skill": {"uses": 8, "successes": 2, "success_rate": 0.25},
        "good-agent-skill": {"uses": 8, "successes": 7, "success_rate": 0.875},
        "rarely-used": {"uses": 1, "successes": 0, "success_rate": 0.0},
        "weak-bundled-skill": {"uses": 8, "successes": 1, "success_rate": 0.125},
    })
    # Only the agent-created ones are eligible (never propose over bundled skills).
    monkeypatch.setattr("tools.skill_usage.is_agent_created",
                        lambda name: name.endswith("agent-skill"))
    failing = proposer.find_failing_skills(min_uses=4, max_success_rate=0.5)
    names = {f["name"] for f in failing}
    assert names == {"weak-agent-skill"}


# --------------------------------------------------------------------------
# gating: proposes nothing unless fully enabled
# --------------------------------------------------------------------------

def test_noop_when_self_improve_disabled(monkeypatch):
    monkeypatch.setattr(self_improve, "enabled", lambda config=None: False)
    out = proposer.propose_skill_improvements(llm_caller=_llm("x"))
    assert out["proposed"] == []
    assert out["reason"] == "self_improve disabled"


def test_noop_when_governor_frozen(monkeypatch):
    _enable_self_improve(monkeypatch)
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: True)
    out = proposer.propose_skill_improvements(llm_caller=_llm("x"))
    assert out["proposed"] == []
    assert "frozen" in out["reason"]


def test_noop_when_autonomy_blocked(monkeypatch):
    _enable_self_improve(monkeypatch)
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason",
                        lambda config=None: "kill switch engaged")
    out = proposer.propose_skill_improvements(llm_caller=_llm("x"))
    assert out["proposed"] == []
    assert "kill switch" in out["reason"]


# --------------------------------------------------------------------------
# the generate → propose path
# --------------------------------------------------------------------------

def _wire_one_failing_skill(monkeypatch, tmp_path):
    """Set JANUS_HOME, write one agent-created skill, mark it failing + agent-made."""
    home = tmp_path / ".janus"
    (home / "skills" / "flaky").mkdir(parents=True)
    (home / "skills" / "flaky" / "SKILL.md").write_text(
        "---\nname: flaky\ndescription: does a flaky thing\n---\n\nOld body that fails.",
        encoding="utf-8")
    monkeypatch.setenv("JANUS_HOME", str(home))
    monkeypatch.setattr("agent.outcome_tracker.skill_stats", lambda: {
        "flaky": {"uses": 10, "successes": 2, "success_rate": 0.2}})
    monkeypatch.setattr("tools.skill_usage.is_agent_created", lambda name: True)
    return home


def test_generates_a_proposal_for_a_failing_skill(monkeypatch, tmp_path):
    _enable_self_improve(monkeypatch)
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    _wire_one_failing_skill(monkeypatch, tmp_path)

    variant = ("---\nname: flaky\ndescription: does a flaky thing\n---\n\n"
               "Revised body with a checklist that avoids the failure.")
    out = proposer.propose_skill_improvements(llm_caller=_llm(variant), max_proposals=3)

    assert len(out["proposed"]) == 1
    pid = out["proposed"][0]
    rec = self_improve.get(pid)
    assert rec is not None
    assert rec["kind"] == "skill"
    assert rec["status"] == "proposed"           # NEVER auto-promoted
    assert rec["target"] == "skills/.drafts/flaky/SKILL.md"
    assert "Revised body" in rec["content"]


def test_proposal_target_is_allowlisted_drafts_path(monkeypatch, tmp_path):
    """The generated target must survive self_improve's own allowlist so promote
    would be possible later — i.e. it lives under skills/.drafts."""
    _enable_self_improve(monkeypatch)
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    _wire_one_failing_skill(monkeypatch, tmp_path)
    out = proposer.propose_skill_improvements(
        llm_caller=_llm("---\nname: flaky\ndescription: d\n---\n\nbody"), max_proposals=1)
    pid = out["proposed"][0]
    rec = self_improve.get(pid)
    assert self_improve.resolve_target(rec["target"]) is not None


def test_unparseable_variant_is_skipped_not_proposed(monkeypatch, tmp_path):
    _enable_self_improve(monkeypatch)
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    _wire_one_failing_skill(monkeypatch, tmp_path)
    # LLM returns something without valid frontmatter → not a usable skill.
    out = proposer.propose_skill_improvements(llm_caller=_llm("no frontmatter here"),
                                              max_proposals=1)
    assert out["proposed"] == []
