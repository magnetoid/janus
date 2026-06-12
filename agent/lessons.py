"""Reflexion write-back — turn failures into retrievable lessons.

Where ``outcome_tracker`` records *that* a session failed and ``memory_miner``
distills durable *facts*, this distills the actionable LESSON from a failure:
a short natural-language note ("next time, do X instead of Y") keyed to the
task type, so the agent can pull it back the next time a similar task comes up.

This is the Reflexion pattern (Shinn et al., 2023) applied across sessions:
verbalized self-critique stored in episodic memory and retrieved on demand.
It compounds — every failure makes the next similar attempt a little better —
and unlike memory facts, a lesson is explicitly tied to a *kind of task*.

Store: ``~/.janus/learning/lessons.json`` — append-only, capped to the most
recent ``_MAX_LESSONS`` so it can't grow without bound. Pure helpers with an
injectable ``llm_caller`` so reflection is testable without a live model; every
function is best-effort and never raises.
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

_MAX_LESSONS = 300  # keep the most recent; oldest are dropped on write

_STOP = {
    "the", "a", "an", "is", "are", "was", "were", "be", "to", "of", "and", "or",
    "in", "on", "for", "with", "my", "your", "it", "its", "that", "this", "i",
    "you", "we", "they", "as", "at", "by", "from", "but", "not", "do", "does",
    "next", "time", "when", "use", "using", "instead",
}


def get_lessons_path() -> Path:
    from janus_constants import get_janus_home
    return get_janus_home() / "learning" / "lessons.json"


def _now_iso() -> str:
    try:
        from janus_time import now as _now
        return _now().isoformat()
    except Exception:
        return ""


def load() -> List[Dict[str, Any]]:
    path = get_lessons_path()
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def _save(records: List[Dict[str, Any]]) -> None:
    path = get_lessons_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _tokens(s: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]+", str(s).lower()) if len(w) > 2 and w not in _STOP}


def _slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(name).strip().lower()).strip("-")
    return s or "general"


def record_lesson(
    lesson: str, *, task_type: str = "", session_id: str = "", source: str = "reflexion",
) -> Optional[Dict[str, Any]]:
    """Append a lesson, de-duplicating exact repeats. Returns the record (or None)."""
    lesson = str(lesson).strip()
    if not lesson:
        return None
    records = load()
    norm = lesson.lower()
    if any(str(r.get("lesson", "")).lower() == norm for r in records):
        return None  # already learned this
    rec = {
        "lesson": lesson,
        "task_type": _slug(task_type) if task_type else "general",
        "session_id": session_id or "",
        "source": source,
        "ts": _now_iso(),
    }
    records.append(rec)
    if len(records) > _MAX_LESSONS:
        records = records[-_MAX_LESSONS:]
    _save(records)
    return rec


# --- reflection (failure -> lesson) -----------------------------------------

_REFLECT_SYSTEM = (
    "You are doing a blameless post-mortem on an AI assistant's FAILED attempt at a "
    "task. Identify the single most useful, transferable lesson that would make the "
    "next similar attempt succeed. Be concrete and actionable — name what to do "
    "differently, not just what went wrong. Ignore one-off causes (a flaky network, "
    "a typo the user fixed). If there is no generalizable lesson, say so."
)


def _build_reflect_prompt(transcript: str) -> str:
    return (
        "From this failed session, extract ONE transferable lesson as JSON:\n"
        '  {"task_type": "<short kebab-case kind, e.g. \\"deploy-staging\\" or '
        '\\"sql-migration\\">",\n'
        '   "lesson": "<one or two sentences: what to do differently next time>"}\n'
        "Return {\"task_type\": \"\", \"lesson\": \"\"} if nothing generalizable applies. "
        "Return ONLY the JSON object.\n\n"
        f"SESSION:\n{transcript}"
    )


def _parse_reflection(raw: Optional[str]) -> Optional[Dict[str, str]]:
    if not raw or not raw.strip():
        return None
    m = re.search(r"\{.*\}", str(raw), re.DOTALL)
    if not m:
        return None
    try:
        data = json.loads(m.group(0))
    except (ValueError, TypeError):
        return None
    if not isinstance(data, dict):
        return None
    lesson = str(data.get("lesson", "")).strip()
    if not lesson:
        return None
    return {"task_type": str(data.get("task_type", "")).strip(), "lesson": lesson}


def reflect_on_failure(
    messages: List[Dict[str, Any]], *,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Optional[Dict[str, str]]:
    """Distill one transferable lesson from a failed session. None if none applies.

    Best-effort; never raises. Injectable ``llm_caller`` for tests.
    """
    try:
        from agent.memory_miner import _render_transcript
        transcript = _render_transcript(messages, max_chars=8000)
        if not transcript.strip():
            return None
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        response = llm_caller(
            task="reflexion_lesson",
            provider=provider, model=model,
            messages=[
                {"role": "system", "content": _REFLECT_SYSTEM},
                {"role": "user", "content": _build_reflect_prompt(transcript)},
            ],
            temperature=0, max_tokens=200,
        )
        return _parse_reflection(response.choices[0].message.content)
    except Exception as exc:
        logger.debug("failure reflection failed: %s", exc)
        return None


# --- recall (lesson retrieval) ----------------------------------------------


def recall_lessons(query: str, *, n: int = 3) -> List[Dict[str, Any]]:
    """Return up to ``n`` past lessons most relevant to ``query``, ranked.

    Lexical token overlap over the lesson text and its task type, with an
    optional semantic re-rank when an embedding backend is installed.
    """
    qt = _tokens(query)
    if not qt:
        return []
    scored: List[Dict[str, Any]] = []
    for rec in load():
        text = str(rec.get("lesson", ""))
        et = _tokens(text) | _tokens(str(rec.get("task_type", "")))
        if not et:
            continue
        overlap = len(qt & et)
        if overlap == 0:
            continue
        score = round(overlap / (len(et) ** 0.5), 4)
        scored.append({
            "lesson": text,
            "task_type": rec.get("task_type", "general"),
            "ts": rec.get("ts", ""),
            "score": score,
        })
    scored.sort(key=lambda x: x["score"], reverse=True)
    try:
        from agent.embeddings import hybrid_rerank
        return hybrid_rerank(query, scored, n, text_of=lambda h: h["lesson"])
    except Exception:
        return scored[:n]


def format_lessons_for_prompt(lessons: List[Dict[str, Any]]) -> str:
    """Render recalled lessons as a compact block for prompt injection."""
    if not lessons:
        return ""
    lines = ["Lessons from past mistakes on similar tasks:"]
    for h in lessons:
        tt = h.get("task_type") or "general"
        lines.append(f"- ({tt}) {h.get('lesson', '').strip()}")
    return "\n".join(lines)


def stats() -> Dict[str, Any]:
    """Aggregate counts for the dashboard: total + per task-type."""
    records = load()
    by_type: Dict[str, int] = {}
    for r in records:
        tt = str(r.get("task_type", "general")) or "general"
        by_type[tt] = by_type.get(tt, 0) + 1
    return {"total": len(records), "by_task_type": by_type}
