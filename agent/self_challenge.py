"""Self-Challenge — verifiable self-play that grows the skill graph.

During the offline sleep cycle, Janus generates verifiable practice tasks aimed at
its KNOWN weaknesses (``gap_seeker``), attempts them in a restricted sandboxed
subagent, verifies the result with DETERMINISTIC checks (the *verifiable reward* —
no LLM judge), and turns successes into QUARANTINED skill drafts that flow through
the existing verifiable-reward + dialectic admission gate. This is the SCA /
AgentEvolver "Code-as-Task" pattern, fit to Janus's safety model.

Config-gated (default OFF), capped, best-effort, never raises. The heavy/risky
sandboxed *attempt* is an INJECTABLE callable (``attempt_runner``) so the
orchestration is fully testable without a live model or a live sandbox.
"""
from __future__ import annotations

import json
import logging
import os
import re
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

# Deterministic check types we accept — the eval framework's verifiable assertions.
# Anything else (e.g. an LLM-judge) is rejected: the reward must be deterministic.
# NOTE: ``regex`` is deliberately excluded — a model-generated pattern is untrusted
# and could trigger catastrophic backtracking (ReDoS) in the offline sleep cycle.
_CHECK_TYPES = frozenset({
    "contains", "not_contains", "min_length", "max_length",
    "tool_called", "tool_not_called",
})
_LENGTH_CHECKS = frozenset({"min_length", "max_length"})

_GEN_SYSTEM = (
    "You design ONE small, self-contained practice task to help an AI coding agent "
    "improve at a topic it keeps struggling with. The task MUST be checkable "
    "DETERMINISTICALLY — never by human or model judgment. Return ONLY JSON: "
    '{"instruction": "<the task for the agent>", "checks": [{"type": "...", '
    '"value": "..."}]}. Allowed check types (pick what verifies success): '
    "contains, not_contains, min_length, max_length, tool_called, tool_not_called. "
    "String-valued checks (contains/not_contains/tool_called/tool_not_called) need a "
    "non-empty value; length checks need a non-negative integer. Provide at least one "
    "check. The instruction must be solvable in a sandbox without network or secrets."
)


def enabled(config: Optional[Dict[str, Any]] = None) -> bool:
    """True when self-challenge is on (default OFF — opt-in, it runs real self-play)."""
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        sc = (config.get("self_challenge", {}) or {}) if isinstance(config, dict) else {}
        return bool(sc.get("enabled", False))
    except Exception:
        return False


def _cfg(config: Optional[Dict[str, Any]], key: str, default: Any) -> Any:
    try:
        sc = (config.get("self_challenge", {}) or {}) if isinstance(config, dict) else {}
        val = sc.get(key, default)
        return val if val is not None else default
    except Exception:
        return default


def _extract_json(text: str) -> Optional[Dict[str, Any]]:
    """Best-effort: parse a JSON object out of a model reply (tolerates fences/prose)."""
    if not text:
        return None
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        pass
    m = re.search(r"\{.*\}", str(text), re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except (ValueError, TypeError):
            return None
    return None


def _valid_checks(checks: Any) -> Optional[List[Dict[str, Any]]]:
    """Keep only deterministic, well-formed checks; None if any entry is malformed.

    Any malformed entry disqualifies the WHOLE task (we never silently drop checks —
    a partial check set would weaken the verifiable reward). Rejects: non-dict items,
    unknown/subjective types, missing values, EMPTY string values (an empty
    ``contains`` matches everything → false-positive pass), and non-integer lengths.
    """
    if not isinstance(checks, list):
        return None
    out: List[Dict[str, Any]] = []
    for c in checks:
        if not isinstance(c, dict):
            return None
        ctype = c.get("type")
        if ctype not in _CHECK_TYPES or "value" not in c:
            return None
        value = c.get("value")
        if ctype in _LENGTH_CHECKS:
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                return None
        elif not (isinstance(value, str) and value.strip()):
            return None  # empty/whitespace string would trivially always pass/fail
        out.append({"type": ctype, "value": value,
                    "case_sensitive": bool(c.get("case_sensitive", False))})
    return out or None


def generate_challenge(
    gap: Dict[str, Any], *, llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """Generate a Code-as-Task ``{topic, instruction, checks}`` for a knowledge gap.

    ``checks`` are deterministic eval assertions. Returns None on any failure or if
    the model proposes no deterministic checks (we never accept subjective rewards).
    """
    try:
        topic = str((gap or {}).get("topic", "")).strip()
        why = str((gap or {}).get("why", "")).strip()
        if not topic or llm_caller is None:
            return None
        prompt = f"Topic the agent struggles with: {topic}"
        if why:
            prompt += f"\nWhy it keeps failing: {why}"
        kwargs: Dict[str, Any] = {
            "task": "self_challenge_generation",
            "messages": [{"role": "system", "content": _GEN_SYSTEM},
                         {"role": "user", "content": prompt}],
            "temperature": 0.4,
            "provider": provider,
            "model": model,
        }
        resp = llm_caller(**kwargs)
        content = resp.choices[0].message.content
        data = _extract_json(content)
        if not isinstance(data, dict):
            return None
        instruction = str(data.get("instruction", "")).strip()
        checks = _valid_checks(data.get("checks"))
        if not instruction or not checks:
            return None
        return {"topic": topic, "instruction": instruction, "checks": checks}
    except Exception as exc:
        logger.debug("generate_challenge failed: %s", exc)
        return None


def verify_result(result: Any, checks: List[Dict[str, Any]]) -> bool:
    """Deterministic verification (the verifiable reward). True iff EVERY check passes.

    An empty check list is never 'verified' — a success needs a real assertion.
    """
    try:
        if not checks:
            return False
        if isinstance(result, dict):
            final = str(result.get("final_response", ""))
            messages = result.get("messages")
        else:
            final, messages = str(result or ""), None
        from agent.evals import evaluate_checks
        results = evaluate_checks(checks, final, messages)
        return bool(results) and all(r.get("passed") for r in results)
    except Exception as exc:
        logger.debug("verify_result failed: %s", exc)
        return False


def _slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    return (s or "self-challenge")[:48]


def _draft_skill_from_success(challenge: Dict[str, Any], result: Any) -> Optional[str]:
    """Write a QUARANTINED skill draft from a verified-successful trajectory.

    Never auto-activates — it lands in ``skills/.drafts/`` and must pass the existing
    verifiable-reward + dialectic admission gate before promotion.
    """
    try:
        from agent.skill_miner import write_skill_draft
        final = result.get("final_response", "") if isinstance(result, dict) else str(result)
        proposal = {
            "name": "self-challenge-" + _slug(challenge.get("topic", "")),
            "description": "(self-challenge) " + str(challenge.get("instruction", ""))[:140],
            "steps": [
                "Restate the task: " + str(challenge.get("instruction", ""))[:200],
                "Apply the verified approach below.",
                "Check the result against the deterministic criteria before finishing.",
            ],
            "category": "self-challenge",
            "source": "self-challenge",
            "body": str(final)[:2000],
        }
        path = write_skill_draft(proposal)
        return str(path)
    except Exception as exc:
        logger.debug("_draft_skill_from_success failed: %s", exc)
        return None


def _record_fail_lesson(challenge: Dict[str, Any], result: Any) -> None:
    """A failed self-challenge is signal — record it as a lesson (best-effort)."""
    try:
        from agent.lessons import record_lesson
        record_lesson(
            f"Self-challenge on '{challenge.get('topic', '')}' was not solved: "
            f"{str(challenge.get('instruction', ''))[:160]}",
            task_type="self-challenge", source="self-challenge",
        )
    except Exception as exc:
        logger.debug("_record_fail_lesson failed: %s", exc)


# Execution backends that actually isolate a self-generated task from the host.
_ISOLATED_SANDBOXES = frozenset({"docker", "modal", "daytona", "singularity", "ssh", "e2b"})


def _resolve_sandbox_backend(config: Optional[Dict[str, Any]]) -> Optional[str]:
    """The isolated execution backend to use, or None if none is safe.

    ``self_challenge.sandbox`` of an isolated name forces it; ``none``/``off``
    disables; ``auto`` (default) defers to the configured ``terminal.backend`` and
    only permits execution when that backend is isolated (never ``local``).
    """
    sandbox = str(_cfg(config, "sandbox", "auto")).lower()
    if sandbox in _ISOLATED_SANDBOXES:
        return sandbox
    if sandbox in ("none", "off", "local"):
        return None
    try:
        backend = str(((config or {}).get("terminal", {}) or {}).get("backend", "local")).lower()
    except Exception:
        backend = "local"
    return backend if backend in _ISOLATED_SANDBOXES else None


def _default_attempt_runner(instruction: str, *, config: Optional[Dict[str, Any]] = None,
                            provider: Optional[str] = None, model: Optional[str] = None,
                            **_: Any) -> Dict[str, Any]:
    """Safe-by-default attempt backend.

    Tool-using self-play means executing a SELF-GENERATED task — only safe inside an
    isolated environment (the offline sleep cycle has no human to approve a shell
    command). Unless an isolated execution backend is configured (``terminal.backend``
    = docker/modal/daytona/… or an explicit ``self_challenge.sandbox``), this REFUSES
    to run rather than execute self-generated commands on the host: it returns a
    non-passing empty result (the round drafts nothing). To enable real self-play,
    configure an isolated backend or inject your own ``attempt_runner``.
    """
    backend = _resolve_sandbox_backend(config)
    if not backend:
        logger.info(
            "self-challenge: no isolated execution backend configured — skipping "
            "execution (set terminal.backend to %s, or self_challenge.sandbox, or "
            "inject an attempt_runner).", "/".join(sorted(_ISOLATED_SANDBOXES)))
        return {"final_response": "", "messages": []}
    # The terminal tool selects its backend from the TERMINAL_ENV env var (default
    # 'local'), NOT from the config dict — so gating on config alone is not enough.
    # Pin it to the resolved isolated backend for the duration of the attempt (then
    # restore), or the subagent would execute on the host despite the safety check.
    _prev_env = os.environ.get("TERMINAL_ENV")
    try:
        os.environ["TERMINAL_ENV"] = backend
        from run_agent import AIAgent
        agent = AIAgent(
            model=model or "",
            enabled_toolsets="development",
            # max_iterations bounds turns; a hard wall-clock timeout needs a sandbox
            # that enforces it (signal-based timeouts aren't thread/Windows-safe).
            max_iterations=int(_cfg(config, "max_iterations", 30)),
            quiet_mode=True,
            save_trajectories=False,
        )
        out = agent.run_conversation(str(instruction))
        return {"final_response": out.get("final_response", ""),
                "messages": out.get("messages", [])}
    except Exception as exc:
        logger.debug("_default_attempt_runner unavailable (%s) — self-challenge no-op", exc)
        return {"final_response": "", "messages": []}
    finally:
        if _prev_env is None:
            os.environ.pop("TERMINAL_ENV", None)
        else:
            os.environ["TERMINAL_ENV"] = _prev_env


def run_self_challenge(
    *, gaps: Optional[List[Dict[str, Any]]] = None,
    llm_caller: Optional[Callable[..., Any]] = None,
    attempt_runner: Optional[Callable[..., Any]] = None,
    config: Optional[Dict[str, Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Orchestrate one self-challenge round: seed → generate → attempt → verify →
    promote. Gated (default off), capped at ``max_per_cycle``, best-effort.

    Returns ``{attempted, passed, drafted, lessons, error}``.
    """
    report: Dict[str, Any] = {"attempted": 0, "passed": 0, "drafted": [],
                              "lessons": 0, "error": None}
    try:
        if config is None:
            try:
                from janus_cli.config import load_config
                config = load_config()
            except Exception:
                config = {}
        if not enabled(config):
            return report
        max_per = int(_cfg(config, "max_per_cycle", 2))
        if max_per <= 0:
            return report
        if gaps is None:
            try:
                from agent.gap_seeker import identify_gaps
                gaps = (identify_gaps(llm_caller=llm_caller, provider=provider,
                                      model=model) or {}).get("gaps", [])
            except Exception as exc:
                logger.debug("self_challenge seed failed: %s", exc)
                gaps = []
        runner = attempt_runner or _default_attempt_runner
        for gap in (gaps or []):
            if report["attempted"] >= max_per:
                break
            challenge = generate_challenge(gap, llm_caller=llm_caller,
                                           provider=provider, model=model)
            if not challenge:
                continue
            report["attempted"] += 1
            result = runner(challenge["instruction"], config=config,
                            provider=provider, model=model)
            if verify_result(result, challenge["checks"]):
                report["passed"] += 1
                path = _draft_skill_from_success(challenge, result)
                if path:
                    report["drafted"].append(path)
            else:
                _record_fail_lesson(challenge, result)
                report["lessons"] += 1
    except Exception as exc:
        logger.debug("run_self_challenge failed: %s", exc)
        report["error"] = str(exc)
    return report
