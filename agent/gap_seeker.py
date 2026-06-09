"""Knowledge-gap seeking — turn repeated failures into learning targets.

Closes the loop between the outcome signal and the proactive learning engines.
It reads failed sessions (from the outcome tracker), clusters what they were
about, and surfaces the recurring themes where Janus struggles — so "I keep
failing at X" becomes "research/learn X". Proposed gaps can be turned into
tracked interests (which the discovery cron then researches).

Pure + injectable ``llm_caller``; best-effort.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

_SYSTEM = (
    "You analyze a list of tasks an AI assistant FAILED at. Identify the "
    "recurring themes or topics where it struggles — the knowledge gaps worth "
    "studying. Group similar failures; ignore one-off flukes."
)


def _failure_topics(records: List[Dict[str, Any]], lookback: int) -> List[str]:
    fails = [r for r in records if not r.get("success")][-lookback:]
    return [str(r.get("note", "")).strip() for r in fails if str(r.get("note", "")).strip()]


def _parse_gaps(raw: Optional[str]) -> List[Dict[str, str]]:
    if not raw or not raw.strip():
        return []
    txt = raw.strip()
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\n?", "", txt)
        txt = re.sub(r"\n?```$", "", txt).strip()
    m = re.search(r"\[.*\]", txt, re.DOTALL)
    if m:
        txt = m.group(0)
    try:
        data = json.loads(txt)
    except (ValueError, TypeError):
        return []
    if not isinstance(data, list):
        return []
    out = []
    for item in data:
        if isinstance(item, str) and item.strip():
            out.append({"topic": item.strip(), "why": ""})
        elif isinstance(item, dict) and str(item.get("topic", "")).strip():
            out.append({"topic": str(item["topic"]).strip(), "why": str(item.get("why", "")).strip()})
    return out[:5]


def identify_gaps(
    *, llm_caller: Optional[Callable[..., Any]] = None,
    lookback: int = 30, min_failures: int = 2,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Cluster recent failures into knowledge gaps. Returns {gaps, considered, error}."""
    result: Dict[str, Any] = {"gaps": [], "considered": 0, "error": None}
    try:
        from agent.outcome_tracker import load
        topics = _failure_topics(load(), lookback)
        result["considered"] = len(topics)
        if len(topics) < min_failures:
            return result
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        listing = "\n".join(f"- {t}" for t in topics)
        prompt = (
            f"Failed tasks:\n{listing}\n\n"
            "Return a JSON array of the recurring knowledge gaps worth studying, "
            'e.g. [{"topic":"short title","why":"why it keeps failing"}]. Only '
            "themes that appear more than once. If none, return []. Return ONLY the JSON array."
        )
        response = llm_caller(
            task="gap_seeking",
            provider=provider, model=model,
            messages=[
                {"role": "system", "content": _SYSTEM},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2, max_tokens=500,
        )
        result["gaps"] = _parse_gaps(response.choices[0].message.content)
    except Exception as exc:
        logger.debug("gap seeking failed: %s", exc)
        result["error"] = str(exc)
    return result


def adopt_gap_as_interest(topic: str) -> Dict[str, Any]:
    """Turn a gap into a tracked interest (the discovery cron will research it)."""
    from agent import interests as it
    return it.add(topic, note="auto-identified knowledge gap", source="gap-seeker")
