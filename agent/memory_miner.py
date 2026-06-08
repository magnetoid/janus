"""Session-end memory mining.

Distill a conversation transcript into durable memory facts via a cheap
auxiliary model, then write them to MEMORY.md / USER.md (and, transitively,
the dated daily journal). Inspired by OpenClaw's session mining: where Janus's
built-in memory is *active-only* (the agent saves a fact when it decides to),
this recovers durable facts the agent never explicitly saved.

Design:
- Pure + injectable: ``mine_session_memory`` takes an ``llm_caller`` so it is
  fully testable without a live model.
- Best-effort: any failure is swallowed and reported in the result dict — a
  mining failure must never break a session.
- De-duplicated: new facts are normalized and skipped if they already exist
  (exact / substring either direction) so repeated sessions don't pile up.
- Writes go through ``MemoryStore.add`` so the daily-snapshot journal and the
  char-limit guards apply automatically.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

_MINING_SYSTEM = (
    "You extract DURABLE memory from a conversation transcript. Keep only "
    "facts worth remembering across future sessions: stable user preferences, "
    "identity, environment, project conventions, decisions, and tool quirks. "
    "EXCLUDE transient task details, one-off requests, and anything ephemeral."
)


def _build_prompt(transcript: str) -> str:
    return (
        "From the transcript below, extract durable memory as JSON with two "
        'string arrays: "user" (facts about the user — preferences, identity, '
        'environment, communication style) and "memory" (project facts, '
        "decisions, conventions, tool quirks). Each item is one concise "
        "sentence. Omit transient or one-off details. If nothing is worth "
        'saving, return {"user": [], "memory": []}. Return ONLY the JSON.\n\n'
        f"TRANSCRIPT:\n{transcript}"
    )


def _render_transcript(messages: List[Dict[str, Any]], max_chars: int = 12000) -> str:
    """Flatten user+assistant text turns; keep the most recent ``max_chars``."""
    parts: List[str] = []
    for m in messages:
        if m.get("role") not in ("user", "assistant"):
            continue
        content = m.get("content")
        if not isinstance(content, str) or not content.strip():
            continue
        parts.append(f"{m['role'].upper()}: {content.strip()}")
    text = "\n\n".join(parts)
    return text[-max_chars:]


def _normalize(s: str) -> str:
    return " ".join(s.lower().split())


def _is_duplicate(content: str, existing_norm: List[str]) -> bool:
    n = _normalize(content)
    if not n:
        return True
    for e in existing_norm:
        if n == e or n in e or e in n:
            return True
    return False


def _parse_facts(raw: Optional[str]) -> Dict[str, List[str]]:
    """Parse the model's JSON reply, tolerating code fences / surrounding prose."""
    empty = {"user": [], "memory": []}
    if not raw or not raw.strip():
        return empty
    txt = raw.strip()
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\n?", "", txt)
        txt = re.sub(r"\n?```$", "", txt).strip()
    match = re.search(r"\{.*\}", txt, re.DOTALL)
    if match:
        txt = match.group(0)
    try:
        data = json.loads(txt)
    except (ValueError, TypeError):
        return empty
    if not isinstance(data, dict):
        return empty
    out = {"user": [], "memory": []}
    for key in ("user", "memory"):
        v = data.get(key, [])
        if isinstance(v, list):
            out[key] = [str(x).strip() for x in v if str(x).strip()]
    return out


def mine_session_memory(
    messages: List[Dict[str, Any]],
    memory_store: Any,
    *,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    max_facts_per_target: int = 12,
) -> Dict[str, Any]:
    """Distill durable facts from ``messages`` into ``memory_store``.

    Returns a summary dict: ``{"added": {"user": N, "memory": M},
    "skipped_duplicates": K, "error": None|str}``. Never raises.
    """
    result: Dict[str, Any] = {
        "added": {"user": 0, "memory": 0},
        "skipped_duplicates": 0,
        "error": None,
    }
    try:
        transcript = _render_transcript(messages)
        if not transcript.strip():
            return result

        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller

        response = llm_caller(
            task="memory_mining",
            provider=provider,
            model=model,
            messages=[
                {"role": "system", "content": _MINING_SYSTEM},
                {"role": "user", "content": _build_prompt(transcript)},
            ],
            temperature=0,
            max_tokens=1000,
        )
        raw = response.choices[0].message.content
        facts = _parse_facts(raw)

        existing = {
            "user": [_normalize(e) for e in getattr(memory_store, "user_entries", [])],
            "memory": [_normalize(e) for e in getattr(memory_store, "memory_entries", [])],
        }
        for target in ("user", "memory"):
            for content in facts.get(target, [])[:max_facts_per_target]:
                content = content.strip()
                if not content:
                    continue
                if _is_duplicate(content, existing[target]):
                    result["skipped_duplicates"] += 1
                    continue
                add_result = memory_store.add(target, content)
                if isinstance(add_result, dict) and add_result.get("success"):
                    result["added"][target] += 1
                    existing[target].append(_normalize(content))
                else:
                    # char-limit hit or rejected — stop piling onto this target
                    result["skipped_duplicates"] += 1
    except Exception as exc:  # mining must never break a session
        logger.debug("session memory mining failed: %s", exc)
        result["error"] = str(exc)
    return result
