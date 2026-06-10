"""Workflow memory — mine SUCCESSFUL multi-step sessions into reusable workflows.

The procedural-pipeline twin of skill mining. Where ``agent/skill_miner.py``
drafts a single skill, this drafts a declarative WORKFLOW (ordered steps for
``agent/workflow_engine.py``) from a session that SUCCEEDED — so a repeatable
multi-step task becomes a re-runnable pipeline. Only sessions the outcome
tracker classifies as a success are mined; drafts go to
``~/.janus/workflows/.drafts/`` for review (never auto-activated).

Pure + injectable ``llm_caller`` so it's fully testable without a model;
best-effort (never raises).
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from agent.memory_miner import _render_transcript
from agent.skill_miner import _slug

logger = logging.getLogger(__name__)

_SYSTEM = (
    "You extract a reusable WORKFLOW from a transcript of a multi-step task that "
    "SUCCEEDED — the ordered steps a future run would follow. Only propose a "
    "workflow when the task was genuinely multi-step and repeatable; ignore "
    "one-off chatter and trivial single actions."
)


def _build_prompt(transcript: str, existing_names: List[str]) -> str:
    existing = ", ".join(sorted(existing_names)) or "(none)"
    return (
        "From the transcript, extract reusable workflows as a JSON array. Each "
        "item is an object:\n"
        '  "name": kebab-case id (e.g. "ship-release")\n'
        '  "description": one short sentence\n'
        '  "steps": ordered array of objects, each:\n'
        '     {"name": "<step id>", "prompt": "<imperative instruction; may use '
        '{var} from an earlier step\'s output>", "output": "<optional var name '
        'to store this step\'s result>"}\n\n'
        "Only include workflows with 2+ genuine steps. Skip anything already "
        f"covered by these existing workflows: {existing}. If nothing qualifies, "
        "return []. Return ONLY the JSON array."
        f"\n\nTRANSCRIPT:\n{transcript}"
    )


def _parse_proposals(raw: Optional[str]) -> List[Dict[str, Any]]:
    """Parse the model's JSON array, tolerating code fences / incomplete items."""
    if not raw or not raw.strip():
        return []
    txt = raw.strip()
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\n?", "", txt)
        txt = re.sub(r"\n?```$", "", txt).strip()
    match = re.search(r"\[.*\]", txt, re.DOTALL)
    if match:
        txt = match.group(0)
    try:
        data = json.loads(txt)
    except (ValueError, TypeError):
        return []
    if not isinstance(data, list):
        return []
    out: List[Dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        raw_name = str(item.get("name", "")).strip()
        desc = str(item.get("description", "")).strip()
        raw_steps = item.get("steps", [])
        if not raw_name or not isinstance(raw_steps, list):
            continue
        name = _slug(raw_name)
        steps: List[Dict[str, str]] = []
        for i, s in enumerate(raw_steps, 1):
            if not isinstance(s, dict):
                continue
            prompt = str(s.get("prompt", "")).strip()
            if not prompt:
                continue
            step = {"name": _slug(s.get("name", "") or f"step{i}"), "prompt": prompt}
            if str(s.get("output", "")).strip():
                step["output"] = _slug(s["output"])
            steps.append(step)
        if len(steps) < 2:  # a workflow needs real multi-step structure
            continue
        out.append({"name": name, "description": desc, "steps": steps})
    return out


def render_workflow_yaml(proposal: Dict[str, Any]) -> str:
    """Render a proposal as workflow_engine-compatible YAML."""
    import yaml

    doc = {
        "name": proposal["name"],
        "description": proposal.get("description", "")
        or "Mined from a successful session — review before use.",
        "steps": [
            {k: v for k, v in step.items() if v}
            for step in proposal["steps"]
        ],
    }
    return yaml.safe_dump(doc, default_flow_style=False, sort_keys=False)


def write_workflow_draft(proposal: Dict[str, Any], drafts_dir: Optional[Path] = None) -> Path:
    """Write a draft workflow under workflows/.drafts/ (non-clobbering)."""
    if drafts_dir is None:
        from janus_constants import get_janus_home
        drafts_dir = get_janus_home() / "workflows" / ".drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)
    base = proposal["name"]
    target = drafts_dir / f"{base}.yaml"
    n = 2
    while target.exists():
        target = drafts_dir / f"{base}-{n}.yaml"
        n += 1
    target.write_text(render_workflow_yaml(proposal), encoding="utf-8")
    return target


def mine_session_workflow(
    messages: List[Dict[str, Any]],
    *,
    llm_caller: Optional[Callable[..., Any]] = None,
    existing_workflow_names: Optional[List[str]] = None,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    max_workflows: int = 2,
    write_drafts: bool = True,
    drafts_dir: Optional[Path] = None,
    classify: bool = True,
) -> Dict[str, Any]:
    """Mine reusable workflows from a SUCCESSFUL session. Returns {proposals, written, error}.

    When ``classify`` is True, the session is only mined if
    ``outcome_tracker.classify_session`` returns True — a failed or unclear
    session is skipped (returns empty). Never raises.
    """
    result: Dict[str, Any] = {"proposals": [], "written": [], "error": None}
    existing = {n.strip().lower() for n in (existing_workflow_names or []) if n}
    try:
        transcript = _render_transcript(messages)
        if not transcript.strip():
            return result
        if classify:
            from agent.outcome_tracker import classify_session
            if classify_session(messages, llm_caller=llm_caller, provider=provider, model=model) is not True:
                return result  # only mine genuine successes
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        response = llm_caller(
            task="workflow_mining",
            provider=provider,
            model=model,
            messages=[
                {"role": "system", "content": _SYSTEM},
                {"role": "user", "content": _build_prompt(transcript, sorted(existing))},
            ],
            temperature=0,
            max_tokens=1500,
        )
        raw = response.choices[0].message.content
        proposals = [
            p for p in _parse_proposals(raw) if p["name"].lower() not in existing
        ][:max_workflows]
        result["proposals"] = proposals
        if write_drafts:
            for p in proposals:
                try:
                    result["written"].append(str(write_workflow_draft(p, drafts_dir=drafts_dir)))
                except Exception as exc:
                    logger.debug("workflow draft write failed for %s: %s", p.get("name"), exc)
    except Exception as exc:  # mining must never break a session
        logger.debug("session workflow mining failed: %s", exc)
        result["error"] = str(exc)
    return result
