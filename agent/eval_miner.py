"""Failure -> draft regression-pin eval (the self-growing benchmark).

When a session is classified a failure and a lesson is distilled, also draft a
deterministic eval that pins the behavior the agent should exhibit next time.
Drafts are quarantined in $JANUS_HOME/evals/.drafts/ (NOT the live suite) for
user review — so the agent can never inflate its own learning curve.

Reuses agent/evals.py's EvalSpec + check-type validation. Best-effort,
injectable llm_caller; never raises.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

_SYSTEM = (
    "You write a single regression test for an AI agent that just FAILED a task. "
    "Produce a deterministic eval: a prompt that recreates the situation and "
    "checks that would PASS only if the agent now behaves correctly. Use only "
    "deterministic checks (string/tool presence), never subjective judgment."
)


def _build_prompt(transcript: str, lesson: str) -> str:
    return (
        "From this failed session" + (f" and its lesson ({lesson})" if lesson else "") +
        ", write ONE eval as JSON:\n"
        '  {"name": "<kebab-case-id>", "prompt": "<prompt that recreates the '
        'task>", "checks": [{"type": "<contains|not_contains|regex|tool_called|'
        'tool_not_called|min_length|max_length>", "value": "<value>"}]}\n'
        "Return ONLY the JSON object.\n\nSESSION:\n" + transcript
    )


def _drafts_dir() -> Path:
    from agent.evals import evals_dir
    return evals_dir() / ".drafts"


def _slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(name).strip().lower()).strip("-")
    return s or "regression-pin"


def draft_eval_from_failure(
    messages: List[Dict[str, Any]], *, lesson: str = "",
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
):
    """Draft an EvalSpec pinning correct behavior. None if nothing valid. Best-effort."""
    try:
        from agent.evals import _spec_from_dict
        from agent.memory_miner import _render_transcript
        transcript = _render_transcript(messages, max_chars=6000)
        if not transcript.strip():
            return None
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        resp = llm_caller(
            task="eval_pin", provider=provider, model=model,
            messages=[{"role": "system", "content": _SYSTEM},
                      {"role": "user", "content": _build_prompt(transcript, lesson)}],
            temperature=0, max_tokens=300,
        )
        raw = resp.choices[0].message.content or ""
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if not m:
            return None
        data = json.loads(m.group(0))
        data["name"] = _slug(data.get("name", ""))
        return _spec_from_dict(data, source_file="(draft)")
    except Exception as exc:
        logger.debug("eval pin draft failed: %s", exc)
        return None


def write_eval_draft(spec, drafts_dir: Optional[Path] = None) -> Path:
    """Write the spec as quarantined YAML in evals/.drafts/ (auto-suffix on clash)."""
    import yaml
    drafts_dir = drafts_dir or _drafts_dir()
    drafts_dir.mkdir(parents=True, exist_ok=True)
    base = spec.name
    target = drafts_dir / f"{base}.yaml"
    n = 2
    while target.exists():
        target = drafts_dir / f"{base}-{n}.yaml"
        n += 1
    target.write_text(
        yaml.safe_dump({"name": spec.name, "prompt": spec.prompt, "checks": spec.checks},
                       sort_keys=False),
        encoding="utf-8",
    )
    return target
