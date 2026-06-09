"""Outcome-based reinforcement — learn from what WORKED, not just what was used.

The keystone of the learning loop: it records a success/failure signal per
session and attributes it to the skills used that session. With that reward
signal the system can promote skills/knowledge that correlate with success and
demote what correlates with failure — turning accumulation into getting smarter.

Store: ``~/.janus/learning/outcomes.json`` — append-only session records plus
derived per-skill aggregates computed on read.

Pure helpers with an injectable ``llm_caller`` so the classifier is testable
without a live model.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


def get_outcomes_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "outcomes.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def load() -> List[Dict[str, Any]]:
    path = get_outcomes_path()
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def _save(records: List[Dict[str, Any]]) -> None:
    path = get_outcomes_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def record_outcome(
    session_id: str, success: bool, *, skills: Optional[List[str]] = None, note: str = ""
) -> Dict[str, Any]:
    """Record a session's outcome attributed to the skills it used."""
    rec = {
        "session_id": session_id or "",
        "success": bool(success),
        "skills": sorted({s for s in (skills or []) if s}),
        "note": note,
        "ts": _now_iso(),
    }
    records = load()
    records.append(rec)
    _save(records)
    return rec


_SKILL_VIEW = re.compile(r"skill_view\s*\(\s*name\s*=\s*['\"]([\w./-]+)['\"]", re.I)


def skills_used_in(messages: List[Dict[str, Any]]) -> List[str]:
    """Best-effort: which skills were loaded this session (from skill_view calls)."""
    used: set = set()
    for m in messages:
        # tool_calls carry the structured call; content may carry the rendered text
        for tc in (m.get("tool_calls") or []):
            fn = (tc.get("function") or {}) if isinstance(tc, dict) else {}
            if fn.get("name") == "skill_view":
                try:
                    args = json.loads(fn.get("arguments") or "{}")
                    if args.get("name"):
                        used.add(str(args["name"]))
                except (ValueError, TypeError):
                    pass
        content = m.get("content")
        if isinstance(content, str):
            for hit in _SKILL_VIEW.findall(content):
                used.add(hit)
    return sorted(used)


def skill_stats() -> Dict[str, Dict[str, Any]]:
    """Per-skill aggregates: uses, successes, success_rate."""
    agg: Dict[str, Dict[str, Any]] = {}
    for rec in load():
        for skill in rec.get("skills", []):
            a = agg.setdefault(skill, {"uses": 0, "successes": 0})
            a["uses"] += 1
            if rec.get("success"):
                a["successes"] += 1
    for a in agg.values():
        a["success_rate"] = round(a["successes"] / a["uses"], 3) if a["uses"] else None
    return agg


def skill_success_rate(skill: str) -> Optional[float]:
    return skill_stats().get(skill, {}).get("success_rate")


def overall_stats() -> Dict[str, Any]:
    records = load()
    n = len(records)
    wins = sum(1 for r in records if r.get("success"))
    return {
        "sessions": n,
        "successes": wins,
        "success_rate": round(wins / n, 3) if n else None,
    }


def recent_success_rate(window: int = 20) -> Optional[float]:
    """Success rate over the most recent ``window`` sessions (trend signal)."""
    records = load()[-window:]
    if not records:
        return None
    wins = sum(1 for r in records if r.get("success"))
    return round(wins / len(records), 3)


# --- classification ---------------------------------------------------------

_CLASSIFY_SYSTEM = (
    "You judge whether an AI assistant SUCCEEDED at what the user asked in a "
    "conversation. Answer strictly with one word: SUCCESS, FAILURE, or UNCLEAR."
)


def classify_session(
    messages: List[Dict[str, Any]], *,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Optional[bool]:
    """Judge whether the session succeeded. Returns True/False, or None if unclear.

    Best-effort; never raises. Injectable ``llm_caller`` for tests.
    """
    try:
        # Render a compact transcript (reuse the memory miner's flattener).
        from agent.memory_miner import _render_transcript
        transcript = _render_transcript(messages, max_chars=8000)
        if not transcript.strip():
            return None
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        response = llm_caller(
            task="outcome_classify",
            provider=provider, model=model,
            messages=[
                {"role": "system", "content": _CLASSIFY_SYSTEM},
                {"role": "user", "content": f"Conversation:\n{transcript}\n\nDid the assistant succeed?"},
            ],
            temperature=0, max_tokens=5,
        )
        verdict = str(response.choices[0].message.content or "").strip().upper()
        if verdict.startswith("SUCCESS"):
            return True
        if verdict.startswith("FAILURE"):
            return False
        return None
    except Exception as exc:
        logger.debug("session outcome classification failed: %s", exc)
        return None
