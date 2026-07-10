"""Eval orchestrator (Phase 2.1b) — makes a proposal promotable.

The proposer generates skill-variant proposals but leaves them without eval
evidence, so ``can_promote`` refuses them. This orchestrator runs the move-2
eval suite twice — once against the current skill (baseline), once with the
variant applied in an ISOLATED throwaway home (never the live profile) — and
records the comparison via ``self_improve.record_evaluation``. A variant that
measurably helps then clears the eval half of the quadruple gate; a human still
approves and promotes.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from agent import eval_orchestrator, self_improve


def _write_skill(home: Path, name: str, body: str):
    d = home / "skills" / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: d\n---\n\n{body}", encoding="utf-8")


def _write_eval(home: Path):
    e = home / "evals"
    e.mkdir(parents=True, exist_ok=True)
    (e / "s.yaml").write_text(
        "name: uses-checklist\nprompt: do the flaky task\n"
        "checks:\n  - type: contains\n    value: checklist\n", encoding="utf-8")


@pytest.fixture()
def home(tmp_path, monkeypatch):
    h = tmp_path / ".janus"
    (h / "skills").mkdir(parents=True)
    monkeypatch.setenv("JANUS_HOME", str(h))
    _write_skill(h, "flaky", "old body without the magic word")
    _write_eval(h)
    monkeypatch.setattr(self_improve, "enabled", lambda config=None: True)
    return h


def _runner_reads_active_skill(spec):
    """Test agent_runner: 'passes' the eval iff the ACTIVE flaky skill body
    contains 'checklist' — so it distinguishes the baseline home from the
    variant home purely by what skill content is live in each isolated run."""
    from janus_constants import get_janus_home
    body = (get_janus_home() / "skills" / "flaky" / "SKILL.md").read_text(encoding="utf-8")
    resp = "checklist applied" if "checklist" in body else "no help"
    return {"final_response": resp, "messages": []}


def test_evaluate_records_improvement_for_a_better_variant(home, monkeypatch):
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    variant = "---\nname: flaky\ndescription: d\n---\n\nNow with a checklist step."
    rec = self_improve.propose("skill", "skills/.drafts/flaky/SKILL.md", variant)

    out = eval_orchestrator.evaluate_proposal(
        rec["id"], agent_runner=_runner_reads_active_skill)

    assert out["evaluated"] is True
    assert out["score_before"] == 0.0   # baseline skill lacks 'checklist'
    assert out["score_after"] == 1.0    # variant adds it
    updated = self_improve.get(rec["id"])
    assert updated["status"] == "evaluated"
    assert updated["gate_ok"] is True   # strict improvement


def test_live_profile_is_never_mutated(home, monkeypatch):
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    before = (home / "skills" / "flaky" / "SKILL.md").read_text(encoding="utf-8")
    variant = "---\nname: flaky\ndescription: d\n---\n\nNow with a checklist step."
    rec = self_improve.propose("skill", "skills/.drafts/flaky/SKILL.md", variant)
    eval_orchestrator.evaluate_proposal(rec["id"], agent_runner=_runner_reads_active_skill)
    after = (home / "skills" / "flaky" / "SKILL.md").read_text(encoding="utf-8")
    assert after == before   # the variant was applied only in a throwaway home


def test_no_eval_specs_is_a_clean_noop(home, monkeypatch):
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    import shutil
    shutil.rmtree(home / "evals")   # no suite to evaluate against
    rec = self_improve.propose("skill", "skills/.drafts/flaky/SKILL.md",
                               "---\nname: flaky\ndescription: d\n---\n\nx")
    out = eval_orchestrator.evaluate_proposal(rec["id"], agent_runner=_runner_reads_active_skill)
    assert out["evaluated"] is False
    assert "no eval" in out["reason"].lower()
    assert self_improve.get(rec["id"])["status"] == "proposed"  # unchanged


def test_gated_off_when_self_improve_disabled(home, monkeypatch):
    rec = self_improve.propose("skill", "skills/.drafts/flaky/SKILL.md",
                               "---\nname: flaky\ndescription: d\n---\n\nx")
    monkeypatch.setattr(self_improve, "enabled", lambda config=None: False)
    out = eval_orchestrator.evaluate_proposal(rec["id"], agent_runner=_runner_reads_active_skill)
    assert out["evaluated"] is False
    assert "disabled" in out["reason"]


def test_shaped_reward_lets_a_cleaner_variant_clear_the_gate(home, monkeypatch):
    """Phase 2.3: promotion consumes the shaped reward. Baseline and variant pass
    the SAME eval check, so a pass-rate-only gate would call it a no-op (blocked).
    But the variant reaches the pass with a clean tool trajectory while the
    baseline thrashes — the shaped score rises, so the gate opens."""
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    variant = "---\nname: flaky\ndescription: d\n---\n\nchecklist, done cleanly."

    def runner(spec):
        # Both bodies contain 'checklist' → both PASS the eval. The baseline body
        # (no 'cleanly') drives a failed tool call; the variant runs clean.
        from janus_constants import get_janus_home
        body = (get_janus_home() / "skills" / "flaky" / "SKILL.md").read_text(encoding="utf-8")
        thrash = "cleanly" not in body
        msgs = ([{"role": "tool", "content": '{"error": "x"}'}] if thrash
                else [{"role": "tool", "content": "ok"}])
        return {"final_response": "checklist applied", "messages": msgs}

    # baseline skill also passes the check, so pass-rate is identical (1.0 vs 1.0)
    _write_skill(home, "flaky", "checklist but messy")
    rec = self_improve.propose("skill", "skills/.drafts/flaky/SKILL.md", variant)
    out = eval_orchestrator.evaluate_proposal(rec["id"], agent_runner=runner)

    assert out["evaluated"] is True
    # baseline: pass with tfr=1.0 → shaped 0.5 ; variant: pass clean → shaped 1.0
    assert out["score_before"] == 0.5
    assert out["score_after"] == 1.0
    assert self_improve.get(rec["id"])["gate_ok"] is True   # shaped improvement


def test_worse_variant_records_no_improvement(home, monkeypatch):
    monkeypatch.setattr("agent.self_improvement_governor.learning_frozen", lambda: False)
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason", lambda config=None: None)
    # baseline already has the magic word; the variant removes it → regression.
    _write_skill(home, "flaky", "the checklist is already here")
    variant = "---\nname: flaky\ndescription: d\n---\n\nremoved the good part."
    rec = self_improve.propose("skill", "skills/.drafts/flaky/SKILL.md", variant)
    out = eval_orchestrator.evaluate_proposal(rec["id"], agent_runner=_runner_reads_active_skill)
    assert out["score_before"] == 1.0
    assert out["score_after"] == 0.0
    assert self_improve.get(rec["id"])["gate_ok"] is False   # not an improvement
