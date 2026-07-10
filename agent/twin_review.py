"""Twin-core adversarial review (Phase 2.2) — the second head, veto-only.

Janus is a two-headed agent. Phase 2.1 wired the FIRST head: a proposer core that
mines its own failing skills and records self-modification proposals. This module
is the SECOND head — a separate reviewer core that red-teams each proposal before
a human ever spends attention on it.

The design is deliberately ASYMMETRIC, and that asymmetry is the whole safety
argument:

  * The reviewer may VETO a proposal (reject it with the objection that mattered).
  * The reviewer may NOT approve one, set its eval gate, or advance it one inch
    toward promotion. Approval is a human act. Two LLMs signing off on each
    other's changes — "mutual approval" — is BANNED: it invites collusion,
    correlated blind spots, and poison propagation from one core into the other.

So this is proposer/approver SEPARATION, not a second rubber stamp. A proposal
that survives the veto still faces the full quadruple gate (measured eval
improvement + governor not frozen + autonomy floor clear + human approval) — the
review only ever subtracts trust, never adds it.

The reviewer's independence comes from a distinct profile: when
``learning.self_improve.twin_review_reviewer_home`` points at a second
``$JANUS_HOME``, the skeptic is fed THAT core's accumulated lessons as prior
knowledge, so its blind spots de-correlate from the proposer's. Unconfigured, it
degrades to an in-profile self-review that is still strictly veto-only.

Gated (``learning.self_improve.twin_review``, off by default) + governor + the
autonomy floor. Best-effort and offline; an infrastructure failure FAILS OPEN
(no veto) — a flaky reviewer must not silently kill every proposal, and the human
gate is still there regardless.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


def _si_cfg(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        si = ((config.get("learning") or {}).get("self_improve") or {})
        return si if isinstance(si, dict) else {}
    except Exception:
        return {}


def enabled(config: Optional[Dict[str, Any]] = None) -> bool:
    """``learning.self_improve.twin_review`` — off by default."""
    return bool(_si_cfg(config).get("twin_review", False))


def _reviewer_home(config: Optional[Dict[str, Any]] = None) -> Optional[Path]:
    raw = str(_si_cfg(config).get("twin_review_reviewer_home", "") or "").strip()
    if not raw:
        return None
    try:
        p = Path(raw).expanduser()
        return p if p.is_dir() else None
    except Exception:
        return None


def _reviewer_lessons(config: Optional[Dict[str, Any]] = None) -> str:
    """The OTHER core's lessons, recalled under its profile so the skeptic argues
    from independent experience. Empty string when no reviewer home is configured
    (degraded single-core review — still veto-only)."""
    home = _reviewer_home(config)
    if home is None:
        return ""
    token = None
    try:
        from janus_constants import reset_janus_home_override, set_janus_home_override
        token = set_janus_home_override(str(home))
        from agent.lessons import format_lessons_for_prompt, recall_lessons
        hits = recall_lessons("skill self-modification review guardrails", n=8)
        return format_lessons_for_prompt(hits) if hits else ""
    except Exception as exc:
        logger.debug("_reviewer_lessons failed: %s", exc)
        return ""
    finally:
        if token is not None:
            try:
                from janus_constants import reset_janus_home_override
                reset_janus_home_override(token)
            except Exception:
                pass


def _baseline_md(name: str) -> str:
    """The current live SKILL.md the variant would replace — the diff the
    reviewer judges. Empty string if it can't be resolved."""
    try:
        from agent.proposer import _resolve_skill_md
        md = _resolve_skill_md(name)
        if md is not None:
            return md.read_text(encoding="utf-8")
    except Exception as exc:
        logger.debug("_baseline_md failed for %s: %s", name, exc)
    return ""


def review_proposal(
    proposal_id: str, *,
    llm_caller: Optional[Callable[..., Any]] = None,
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Red-team one skill-variant proposal from the reviewer core. Never raises.

    Returns ``{"reviewed": bool, "verdict": "pass"|"veto"|"", "objection": str,
    "reason": str}``. A veto rejects the proposal; a pass records an inert review
    annotation and leaves the proposal exactly where it was (still needing human
    approval). Infra failure → ``reviewed=False`` (fail open, no veto)."""
    out: Dict[str, Any] = {"reviewed": False, "verdict": "", "objection": "", "reason": ""}
    try:
        if not enabled(config):
            out["reason"] = "twin_review disabled"
            return out
        try:
            from agent.self_improvement_governor import learning_frozen
            if learning_frozen():
                out["reason"] = "governor frozen"
                return out
        except Exception:
            pass
        try:
            from agent.autonomy_guard import blocked_reason
            br = blocked_reason(config)
            if br:
                out["reason"] = f"autonomy floor: {br}"
                return out
        except Exception:
            pass

        from agent import self_improve
        rec = self_improve.get(proposal_id)
        if rec is None:
            out["reason"] = "no such proposal"
            return out
        if rec.get("kind") != "skill":
            out["reason"] = f"not a reviewable kind ({rec.get('kind')})"
            return out
        if rec.get("status") not in ("proposed", "evaluated"):
            out["reason"] = f"not in a reviewable state ({rec.get('status')})"
            return out

        from agent.eval_orchestrator import _skill_name_from_target
        name = _skill_name_from_target(rec.get("target", "")) or "(unknown)"
        variant = str(rec.get("content", ""))
        baseline = _baseline_md(name)

        claim = {
            "id": proposal_id, "kind": "skill", "context": name,
            "content": (f"Adopt this agent-proposed revision of skill '{name}'. "
                        "It is a self-modification of the agent's own artifact."),
        }
        transcript = (f"CURRENT SKILL.md (baseline):\n{baseline or '(none)'}\n\n"
                      f"PROPOSED VARIANT:\n{variant}")
        existing = _reviewer_lessons(config)

        from agent.deliberation import red_team_claims
        result = red_team_claims([claim], transcript=transcript,
                                 existing=existing, llm_caller=llm_caller)
        verdicts = result.get("verdicts") or {}
        v = verdicts.get(str(proposal_id))
        if result.get("error") or v is None:
            # Fail open: no verdict is NOT a veto. The human gate still stands.
            out["reason"] = f"review unavailable (fail-open): {result.get('error') or 'no verdict'}"
            return out

        objection = (v.get("skeptic_objection") or v.get("crux") or "").strip()
        # reject OR revise both mean the skeptic found a real, load-bearing flaw
        # in a self-modification — block it. revised_content is intentionally NOT
        # applied: the reviewer critiques, it does not author.
        if v.get("verdict") in ("reject", "revise"):
            self_improve.record_review(proposal_id, verdict="veto", objection=objection)
            self_improve.reject(proposal_id, reason=f"twin-core veto: {objection}"[:500])
            out.update({"reviewed": True, "verdict": "veto",
                        "objection": objection, "reason": "vetoed"})
            _audit("self_improve_vetoed", proposal_id, name, objection)
            return out

        # accept → the second core did not object. Record it as INERT metadata;
        # status/gate_ok/approval are untouched. A human still approves.
        self_improve.record_review(proposal_id, verdict="pass", objection="")
        out.update({"reviewed": True, "verdict": "pass", "reason": "passed"})
        _audit("self_improve_review_passed", proposal_id, name, "")
        return out
    except Exception as exc:
        logger.debug("review_proposal failed: %s", exc)
        out["reason"] = f"error: {exc}"
        return out


def review_proposals(
    proposal_ids: List[str], *,
    llm_caller: Optional[Callable[..., Any]] = None,
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Review a batch of fresh proposals (sleep-cycle convenience). Returns
    ``{"vetoed": [...], "passed": [...], "reason": str}``. Never raises."""
    summary: Dict[str, Any] = {"vetoed": [], "passed": [], "reason": ""}
    if not enabled(config):
        summary["reason"] = "twin_review disabled"
        return summary
    for pid in proposal_ids or []:
        try:
            r = review_proposal(pid, llm_caller=llm_caller, config=config)
            if r.get("verdict") == "veto":
                summary["vetoed"].append(pid)
            elif r.get("verdict") == "pass":
                summary["passed"].append(pid)
        except Exception as exc:
            logger.debug("review_proposals: %s failed: %s", pid, exc)
    summary["reason"] = "ok"
    return summary


def _audit(kind: str, proposal_id: str, skill: str, objection: str) -> None:
    try:
        from agent.audit_log import append_event
        append_event(kind, {"proposal_id": proposal_id, "skill": skill,
                            "objection": objection})
    except Exception:
        pass
