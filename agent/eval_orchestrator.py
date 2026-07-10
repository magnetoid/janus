"""Eval orchestrator (Phase 2.1b) — turns a proposal into promotable evidence.

The proposer (agent/proposer.py) records skill-variant proposals but leaves them
without eval evidence, so ``self_improve.can_promote`` refuses them — a proposal
with no measured improvement can never pass the gate. This module is the missing
evaluate() seam the DGM-lite docstring anticipated: it runs the move-2 eval suite
twice —

  * BASELINE — the current skill, in an isolated throwaway copy of $JANUS_HOME.
  * VARIANT  — the same isolated copy with the proposed SKILL.md applied as the
    ACTIVE skill.

— and records the two pass-rates via ``self_improve.record_evaluation``, which
defaults ``gate_ok`` to a STRICT improvement (variant > baseline). The live
profile is NEVER touched: the variant is applied only inside a temp home behind
a context-local ``JANUS_HOME`` override, which is torn down afterward. This is
the "evaluate the variant in an isolated profile, never the live one" isolation
the audit requires before a self-modification can be promoted.

Gated (self_improve.enabled + governor not frozen + autonomy floor clear) and
best-effort. Promotion still requires the human approval gate on top of the eval
evidence this produces.
"""
from __future__ import annotations

import logging
import shutil
import tempfile
from pathlib import Path
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)


def _skill_name_from_target(target: str) -> Optional[str]:
    """``skills/.drafts/<name>/SKILL.md`` → ``<name>``, else None."""
    parts = Path(str(target)).parts
    try:
        i = parts.index(".drafts")
        return parts[i + 1] if i + 1 < len(parts) else None
    except ValueError:
        return None


def _pass_rate(summary: Dict[str, Any]) -> Optional[float]:
    total = int(summary.get("total", 0) or 0)
    if total <= 0:
        return None
    return round(int(summary.get("passed", 0) or 0) / total, 4)


def _run_isolated(live_home: Path, *, apply_variant: Optional[tuple],
                  agent_runner: Optional[Callable[..., Any]]) -> Optional[float]:
    """Copy the live home's skills + evals into a throwaway home, optionally
    overwrite one active skill with a variant body, run the eval suite there
    behind a JANUS_HOME override, and return the pass-rate. None if no specs."""
    from janus_constants import (
        reset_janus_home_override, set_janus_home_override,
    )
    tmp = Path(tempfile.mkdtemp(prefix="janus-eval-"))
    token = None
    try:
        for sub in ("skills", "evals"):
            src = live_home / sub
            if src.is_dir():
                shutil.copytree(src, tmp / sub)
        if apply_variant is not None:
            name, content = apply_variant
            sd = tmp / "skills" / name
            sd.mkdir(parents=True, exist_ok=True)
            (sd / "SKILL.md").write_text(str(content), encoding="utf-8")
        token = set_janus_home_override(str(tmp))
        from agent.evals import load_eval_specs, run_evals
        specs = load_eval_specs()
        if not specs:
            return None
        summary = run_evals(specs, agent_runner=agent_runner, save_results=False)
        return _pass_rate(summary)
    finally:
        if token is not None:
            reset_janus_home_override(token)
        shutil.rmtree(tmp, ignore_errors=True)


def evaluate_proposal(
    proposal_id: str, *,
    agent_runner: Optional[Callable[..., Any]] = None,
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Evaluate a skill-variant proposal against the eval suite and record the
    result. Returns a summary dict. Never raises.

    Gated: self_improve enabled + governor not frozen + autonomy floor clear.
    No-op (evaluated=False) when the proposal isn't an evaluable skill variant,
    or no eval specs exist to measure against."""
    out: Dict[str, Any] = {"evaluated": False, "reason": "",
                           "score_before": None, "score_after": None}
    try:
        from agent import self_improve
        if not self_improve.enabled(config):
            out["reason"] = "self_improve disabled"
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

        rec = self_improve.get(proposal_id)
        if rec is None:
            out["reason"] = "no such proposal"
            return out
        if rec.get("kind") != "skill":
            out["reason"] = f"not an evaluable kind ({rec.get('kind')})"
            return out
        if rec.get("status") not in ("proposed", "evaluated"):
            out["reason"] = f"not in an evaluable state ({rec.get('status')})"
            return out
        name = _skill_name_from_target(rec.get("target", ""))
        if not name:
            out["reason"] = "could not resolve skill name from target"
            return out

        from janus_constants import get_janus_home
        live = get_janus_home()
        before = _run_isolated(live, apply_variant=None, agent_runner=agent_runner)
        if before is None:
            out["reason"] = "no eval specs to measure against"
            return out
        after = _run_isolated(live, apply_variant=(name, rec.get("content", "")),
                              agent_runner=agent_runner)
        if after is None:
            out["reason"] = "no eval specs to measure against"
            return out

        self_improve.record_evaluation(proposal_id, score_before=before, score_after=after)
        out.update({"evaluated": True, "reason": "ok",
                    "score_before": before, "score_after": after})
        try:
            from agent.audit_log import append_event
            append_event("self_improve_evaluated",
                         {"proposal_id": proposal_id, "skill": name,
                          "score_before": before, "score_after": after})
        except Exception:
            pass
        return out
    except Exception as exc:
        logger.debug("evaluate_proposal failed: %s", exc)
        out["reason"] = f"error: {exc}"
        return out
