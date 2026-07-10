"""Governor hardening — fail-closed promotion + wider FROZEN scope (gap G7).

The governor is an advisory health read that deliberately fails OPEN on an
internal crash (a broken governor must not wedge the agent). But when that read
is used to GATE a promotion — an action that modifies the agent — the gate must
fail CLOSED: a crashed governor should block self-modification, not wave it
through. And a FROZEN governor should pause the durable learning write-backs
(what teaches future behavior), not just skill-draft promotion.
"""
from __future__ import annotations

from agent import self_improvement_governor as gov


def _enable(monkeypatch, **cfg):
    monkeypatch.setattr(gov, "governor_enabled", lambda: True)
    monkeypatch.setattr(gov, "_gov_cfg", lambda key, default: cfg.get(key, default))


# --------------------------------------------------------------------------
# fail-open stays the default; fail-closed is opt-in for promotion gates
# --------------------------------------------------------------------------

def test_internal_error_fails_open_by_default(monkeypatch):
    _enable(monkeypatch)
    # Force an internal crash inside assessment.
    monkeypatch.setattr(gov, "_eval_trend_freeze_reason",
                        lambda: (_ for _ in ()).throw(RuntimeError("boom")))
    r = gov.assess_admission_state({"sessions": 10})
    assert r["state"] == gov.STATE_OK  # advisory read → fail open
    assert gov.admission_allowed({"sessions": 10}) is True


def test_internal_error_fails_closed_when_requested(monkeypatch):
    _enable(monkeypatch)
    monkeypatch.setattr(gov, "_eval_trend_freeze_reason",
                        lambda: (_ for _ in ()).throw(RuntimeError("boom")))
    r = gov.assess_admission_state({"sessions": 10}, fail_closed=True)
    assert r["state"] == gov.STATE_FROZEN  # promotion gate → fail closed
    assert gov.admission_allowed({"sessions": 10}, fail_closed=True) is False


def test_healthy_metrics_allow_even_when_fail_closed(monkeypatch):
    _enable(monkeypatch)
    r = gov.assess_admission_state(
        {"sessions": 10, "forgetting": 0.0, "diversity_trend": 0.0,
         "forward_transfer": 0.05}, fail_closed=True)
    assert r["state"] == gov.STATE_OK
    assert gov.admission_allowed({"sessions": 10, "forgetting": 0.0,
                                  "diversity_trend": 0.0, "forward_transfer": 0.05},
                                 fail_closed=True) is True


# --------------------------------------------------------------------------
# learning_frozen(): the write-side pause signal
# --------------------------------------------------------------------------

def test_learning_frozen_true_when_governor_frozen(monkeypatch):
    _enable(monkeypatch)
    monkeypatch.setattr(gov, "assess_admission_state",
                        lambda *a, **k: {"state": gov.STATE_FROZEN, "reasons": [], "metrics": {}})
    assert gov.learning_frozen() is True


def test_learning_frozen_false_when_governor_disabled(monkeypatch):
    # Default (governor off) → never frozen → learning writes proceed.
    monkeypatch.setattr(gov, "governor_enabled", lambda: False)
    assert gov.learning_frozen() is False


def test_learning_frozen_false_on_error(monkeypatch):
    _enable(monkeypatch)
    monkeypatch.setattr(gov, "assess_admission_state",
                        lambda *a, **k: (_ for _ in ()).throw(RuntimeError("boom")))
    # A crash in the write-side signal must not itself block learning writes.
    assert gov.learning_frozen() is False


# --------------------------------------------------------------------------
# skill promotion path uses the fail-closed gate
# --------------------------------------------------------------------------

def test_auto_promote_blocks_on_governor_error(monkeypatch, tmp_path):
    """A crashing governor must BLOCK skill promotion, not wave it through."""
    from agent import skill_graph

    monkeypatch.setattr(gov, "governor_enabled", lambda: True)
    monkeypatch.setattr(gov, "_eval_trend_freeze_reason",
                        lambda: (_ for _ in ()).throw(RuntimeError("boom")))
    # learning_metrics also crashes → assessment would fail open to OK by default.
    monkeypatch.setattr("agent.outcome_tracker.learning_metrics",
                        lambda *a, **k: (_ for _ in ()).throw(RuntimeError("boom")))

    summary = skill_graph.auto_promote_drafts(dry_run=True)
    assert summary["blocked_by_governor"] is True
    assert summary["promoted"] == []
