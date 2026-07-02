"""Tests for governed self-improvement / DGM-lite (agent/self_improve.py).

The guardrails are the whole point, so they get the most coverage: no core-code
targets, no escapes, and a promotion gate that refuses unless EVERY safety
condition holds. The isolated JANUS_HOME autouse fixture gives each test a clean
archive + artifact tree.
"""
import pytest

from agent import self_improve as si


@pytest.fixture(autouse=True)
def _enabled(monkeypatch):
    # Feature is off by default; turn it on for the lifecycle tests. Individual
    # tests re-patch to exercise the disabled path.
    monkeypatch.setattr(si, "enabled", lambda config=None: True)
    monkeypatch.setattr(si, "require_human_approval", lambda config=None: True)


# --- guardrail 1: target allowlist (self-artifacts only, never core) --------

def test_resolve_target_refuses_core_and_escapes():
    assert si.resolve_target("../run_agent.py") is None          # repo/core
    assert si.resolve_target("/etc/passwd") is None              # absolute
    assert si.resolve_target("../../etc/passwd") is None         # escape
    assert si.resolve_target("config.yaml") is None             # janus_home root, not allowlisted
    assert si.resolve_target("memory/USER.md") is None          # other janus dir
    assert si.resolve_target("") is None
    assert si.resolve_target("skills/active/x/SKILL.md") is None  # active skills, not .drafts


def test_resolve_target_accepts_self_artifacts():
    assert si.resolve_target("skills/.drafts/foo/SKILL.md") is not None
    assert si.resolve_target("prompts/frag.txt") is not None
    assert si.resolve_target("policies/curation.yaml") is not None


def test_propose_refuses_bad_target_kind_and_disabled(monkeypatch):
    assert si.propose("skill", "../core.py", "x") is None        # core target
    assert si.propose("core_patch", "skills/.drafts/a/SKILL.md", "x") is None  # bad kind
    monkeypatch.setattr(si, "enabled", lambda config=None: False)
    assert si.propose("skill", "skills/.drafts/a/SKILL.md", "x") is None       # disabled


# --- lifecycle + lineage ----------------------------------------------------

def _propose():
    return si.propose("skill", "skills/.drafts/demo/SKILL.md", "# Demo\nbody",
                      rationale="worth trying")


def test_propose_and_lineage():
    a = _propose()
    assert a["status"] == "proposed" and a["id"] == "si-0001"
    b = si.propose("skill", "skills/.drafts/demo/SKILL.md", "# Demo v2",
                   parent_id=a["id"])
    chain = si.lineage(b["id"])
    assert [c["id"] for c in chain] == [a["id"], b["id"]]


def test_approve_only_from_evaluated():
    a = _propose()
    assert si.approve(a["id"]) is None                # proposed, not evaluated
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.7)
    assert si.approve(a["id"])["status"] == "approved"


def test_record_evaluation_requires_strict_improvement():
    a = _propose()
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.7)   # improved
    assert si.get(a["id"])["gate_ok"] is True
    b = si.propose("skill", "skills/.drafts/two/SKILL.md", "x")
    si.record_evaluation(b["id"], score_before=0.9, score_after=0.6)   # regressed
    assert si.get(b["id"])["gate_ok"] is False
    # a no-op / fabricated 0→0 (or equal) pair does NOT pass — no measured gain
    c = si.propose("skill", "skills/.drafts/three/SKILL.md", "x")
    si.record_evaluation(c["id"], score_before=0.0, score_after=0.0)
    assert si.get(c["id"])["gate_ok"] is False


def test_cannot_re_evaluate_promoted_proposal():
    # Guards the backup: re-eval→re-promote must not clobber the original.
    target = si.resolve_target("skills/.drafts/keep/SKILL.md")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("ORIGINAL", encoding="utf-8")
    a = si.propose("skill", "skills/.drafts/keep/SKILL.md", "V1")
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.9)
    si.approve(a["id"])
    assert si.promote(a["id"])["promoted"] is True
    # attempt to re-evaluate the promoted proposal → refused
    assert si.record_evaluation(a["id"], score_before=0.9, score_after=0.95) is None
    assert si.get(a["id"])["status"] == "promoted"
    # rollback still restores the true original, not V1
    si.rollback(a["id"])
    assert target.read_text(encoding="utf-8") == "ORIGINAL"


# --- the promotion gate matrix ----------------------------------------------

def test_gate_refuses_until_all_conditions_hold(monkeypatch):
    a = _propose()
    assert si.can_promote(a["id"])[0] is False        # not evaluated
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.8)
    assert si.can_promote(a["id"])[0] is False        # awaiting approval
    si.approve(a["id"])
    ok, reason = si.can_promote(a["id"])
    assert ok is True and reason == "ok"


def test_gate_refuses_when_governor_frozen(monkeypatch):
    a = _propose()
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.8)
    si.approve(a["id"])
    monkeypatch.setattr("agent.self_improvement_governor.assess_admission_state",
                        lambda *a, **k: {"state": "frozen", "reasons": ["regression"]})
    ok, reason = si.can_promote(a["id"])
    assert ok is False and "FROZEN" in reason


def test_gate_refuses_when_autonomy_blocked(monkeypatch):
    a = _propose()
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.8)
    si.approve(a["id"])
    monkeypatch.setattr("agent.autonomy_guard.blocked_reason",
                        lambda *a, **k: "rolling 24h spend over cap")
    ok, reason = si.can_promote(a["id"])
    assert ok is False and "safety floor" in reason


def test_gate_refuses_regressed_variant():
    a = _propose()
    si.record_evaluation(a["id"], score_before=0.9, score_after=0.5)  # regressed
    si.approve(a["id"])
    ok, reason = si.can_promote(a["id"])
    assert ok is False and "improvement" in reason


def test_gate_refuses_when_live_suite_regressed(monkeypatch):
    a = _propose()
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.8)
    si.approve(a["id"])
    monkeypatch.setattr("agent.eval_trend.regression_gate",
                        lambda *a, **k: {"ok": False, "message": "REGRESSION — core_test"})
    ok, reason = si.can_promote(a["id"])
    assert ok is False and "live eval suite is regressed" in reason


def test_gate_fails_closed_when_safety_check_errors(monkeypatch):
    a = _propose()
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.8)
    si.approve(a["id"])
    def _boom(*a, **k):
        raise RuntimeError("governor import broke")
    monkeypatch.setattr("agent.self_improvement_governor.assess_admission_state", _boom)
    ok, reason = si.can_promote(a["id"])
    assert ok is False and "refusing" in reason        # fail CLOSED, not open


# --- apply / rollback -------------------------------------------------------

def test_promote_writes_file_and_rollback_removes_new_file():
    a = _propose()
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.9)
    si.approve(a["id"])
    res = si.promote(a["id"])
    target = si.resolve_target(a["target"])
    assert res["promoted"] is True and target.exists()
    assert target.read_text(encoding="utf-8") == "# Demo\nbody"
    # target didn't exist before → rollback removes it
    assert si.rollback(a["id"])["rolled_back"] is True
    assert not target.exists()


def test_promote_backs_up_and_rollback_restores_prior_content():
    target = si.resolve_target("skills/.drafts/exists/SKILL.md")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("ORIGINAL", encoding="utf-8")
    a = si.propose("skill", "skills/.drafts/exists/SKILL.md", "REPLACEMENT")
    si.record_evaluation(a["id"], score_before=0.5, score_after=0.9)
    si.approve(a["id"])
    assert si.promote(a["id"])["promoted"] is True
    assert target.read_text(encoding="utf-8") == "REPLACEMENT"
    si.rollback(a["id"])
    assert target.read_text(encoding="utf-8") == "ORIGINAL"   # prior content restored


def test_promote_refused_does_not_write():
    a = _propose()  # never evaluated/approved
    res = si.promote(a["id"])
    assert res["promoted"] is False
    assert not si.resolve_target(a["target"]).exists()


def test_safe_write_refuses_symlinked_path_component(tmp_path):
    # Second-layer defense: even if a symlink is planted inside the allowlisted
    # tree, the write refuses to traverse it (closes the TOCTOU window).
    from janus_constants import get_janus_home
    root = get_janus_home().resolve()
    drafts = root / "skills" / ".drafts"
    drafts.mkdir(parents=True, exist_ok=True)
    outside = tmp_path / "outside"
    outside.mkdir()
    (drafts / "evil").symlink_to(outside, target_is_directory=True)
    target = drafts / "evil" / "SKILL.md"
    assert si._has_symlink_component(target, root) is True
    with pytest.raises(OSError):
        si._safe_write(target, b"pwned", root)
    assert not (outside / "SKILL.md").exists()   # nothing written through the link


# --- config reading ---------------------------------------------------------

def test_enabled_and_approval_read_config(monkeypatch):
    monkeypatch.undo()  # drop the autouse patches; test the real config readers
    assert si.enabled({"learning": {"self_improve": {"enabled": True}}}) is True
    assert si.enabled({"learning": {"self_improve": {"enabled": False}}}) is False
    assert si.enabled({}) is False                                   # default off
    assert si.require_human_approval({}) is True                     # default ON
    assert si.require_human_approval(
        {"learning": {"self_improve": {"require_human_approval": False}}}) is False
