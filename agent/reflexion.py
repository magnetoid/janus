"""Reflexion — deliberate plan→attempt→self-critique→retry reasoning.

Where Mixture-of-Agents gives BREADTH (many models, one pass, aggregate), this
gives DEPTH: a single model iterates on a hard problem, critiquing its own
answer and retrying with the critique as feedback until a verifier approves or
an iteration cap is hit (the Reflexion pattern — intra-task self-improvement,
complementing the post-hoc session mining).

The core ``reflect_and_solve`` takes injectable ``solver`` and ``critic``
callables, so the control flow is fully testable without a model. The
agent-facing ``deep_reason`` tool wires in the auxiliary model for both.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


def reflect_and_solve(
    task: str, *,
    solver: Callable[[str, Optional[str], Optional[str]], str],
    critic: Callable[[str, str], Dict[str, Any]],
    max_iterations: int = 3,
) -> Dict[str, Any]:
    """Iterate solve→critique→retry until the critic approves or the cap is hit.

    ``solver(task, prev_attempt, feedback) -> str`` (prev/feedback are None on
    the first attempt). ``critic(task, attempt) -> {"ok": bool, "critique": str}``.
    Returns ``{answer, iterations, converged, history}``. Never raises.
    """
    history: List[Dict[str, Any]] = []
    try:
        attempt = solver(task, None, None)
        for i in range(1, max_iterations + 1):
            verdict = critic(task, attempt) or {}
            ok = bool(verdict.get("ok"))
            critique = str(verdict.get("critique", "")).strip()
            history.append({"iteration": i, "attempt": attempt, "ok": ok, "critique": critique})
            if ok:
                return {"answer": attempt, "iterations": i, "converged": True, "history": history}
            if i < max_iterations:
                attempt = solver(task, attempt, critique)
        return {"answer": attempt, "iterations": max_iterations, "converged": False, "history": history}
    except Exception as exc:  # deliberate reasoning must degrade, not crash
        logger.debug("reflexion failed: %s", exc)
        best = history[-1]["attempt"] if history else ""
        return {"answer": best, "iterations": len(history), "converged": False,
                "history": history, "error": str(exc)}


# --- default LLM-backed solver + critic -------------------------------------

_SOLVE_SYSTEM = (
    "You solve a hard problem carefully and completely. Think step by step, then "
    "give the final answer. If given feedback on a previous attempt, address every "
    "point it raised."
)

_CRITIC_SYSTEM = (
    "You are a rigorous critic. Judge whether an answer is CORRECT and COMPLETE for "
    "the task. Be skeptical: look for errors, missing cases, and unsupported claims. "
    'Respond with ONLY JSON: {"ok": true|false, "critique": "<specific issues, or '
    'empty if ok>"}.'
)


def make_llm_solver(llm_caller: Callable[..., Any], *, provider=None, model=None):
    def _solve(task: str, prev_attempt: Optional[str], feedback: Optional[str]) -> str:
        user = task
        if prev_attempt and feedback:
            user = (
                f"TASK:\n{task}\n\nYOUR PREVIOUS ATTEMPT:\n{prev_attempt}\n\n"
                f"A critic found these issues:\n{feedback}\n\n"
                "Produce an improved answer that fixes them."
            )
        resp = llm_caller(
            task="reflexion_solve", provider=provider, model=model,
            messages=[{"role": "system", "content": _SOLVE_SYSTEM},
                      {"role": "user", "content": user}],
            temperature=0.3, max_tokens=2000,
        )
        return str(resp.choices[0].message.content or "").strip()
    return _solve


def _parse_verdict(raw: Optional[str]) -> Dict[str, Any]:
    if not raw:
        return {"ok": False, "critique": ""}
    m = re.search(r"\{.*\}", str(raw), re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(0))
            if isinstance(data, dict):
                return {"ok": bool(data.get("ok")), "critique": str(data.get("critique", "")).strip()}
        except (ValueError, TypeError):
            pass
    # fall back: treat an explicit "ok"/"correct" prose as approval
    low = str(raw).lower()
    return {"ok": "ok" in low[:20] and "not ok" not in low[:20], "critique": str(raw).strip()}


def make_llm_critic(llm_caller: Callable[..., Any], *, provider=None, model=None):
    def _critic(task: str, attempt: str) -> Dict[str, Any]:
        resp = llm_caller(
            task="reflexion_critic", provider=provider, model=model,
            messages=[{"role": "system", "content": _CRITIC_SYSTEM},
                      {"role": "user", "content": f"TASK:\n{task}\n\nANSWER:\n{attempt}\n\nIs it correct and complete?"}],
            temperature=0, max_tokens=500,
        )
        return _parse_verdict(resp.choices[0].message.content)
    return _critic


def deep_reason(
    task: str, *, max_iterations: int = 3,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Solve ``task`` with the reflexion loop using the auxiliary model. Best-effort."""
    try:
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        return reflect_and_solve(
            task,
            solver=make_llm_solver(llm_caller, provider=provider, model=model),
            critic=make_llm_critic(llm_caller, provider=provider, model=model),
            max_iterations=max(1, min(int(max_iterations), 6)),
        )
    except Exception as exc:
        logger.debug("deep_reason failed: %s", exc)
        return {"answer": "", "iterations": 0, "converged": False, "history": [], "error": str(exc)}
