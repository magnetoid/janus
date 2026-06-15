"""Memory reconciliation — keep the injected memory crisp, not just big.

Memory accumulates. Without reconciliation, an old fact ("uses Python 3.11")
and a newer one ("now on 3.12") both live in MEMORY.md and contradict each
other — dedup only catches near-repeats, not supersession. This gardener
reviews the entries, detects which are outdated/contradicted via a cheap aux
model, and drops the stale ones (the dated daily journal still keeps the full
history, so nothing is truly lost).

Pure + injectable ``llm_caller`` so reconciliation logic is testable without a
live model; best-effort.
"""
from __future__ import annotations

import json
import logging
import re
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)

_SYSTEM = (
    "You reconcile a list of memory entries. Identify entries that are OUTDATED "
    "or CONTRADICTED by another, more current entry — not merely similar. Be "
    "conservative: only flag genuine supersession or contradiction."
)


def _build_prompt(entries: List[str]) -> str:
    numbered = "\n".join(f"[{i}] {e}" for i, e in enumerate(entries))
    return (
        "Memory entries:\n" + numbered + "\n\n"
        "Return a JSON array of the entries to DROP because another entry "
        'supersedes or contradicts them: [{"drop": <index>, "kept": <index>, '
        '"reason": "<short>"}]. Only genuine supersession/contradiction. If '
        "nothing should be dropped, return []. Return ONLY the JSON array."
    )


def _parse(raw: Optional[str], n: int) -> List[Dict[str, Any]]:
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
        if not isinstance(item, dict):
            continue
        try:
            drop = int(item.get("drop"))
        except (TypeError, ValueError):
            continue
        if 0 <= drop < n:
            out.append({"drop": drop, "kept": item.get("kept"), "reason": str(item.get("reason", ""))})
    return out


def find_stale(
    entries: List[str], *,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Return [{drop, kept, reason}] for entries superseded/contradicted by others."""
    if len(entries) < 2:
        return []
    if llm_caller is None:
        from agent.auxiliary_client import call_llm as llm_caller
    response = llm_caller(
        task="memory_reconcile",
        provider=provider, model=model,
        messages=[
            {"role": "system", "content": _SYSTEM},
            {"role": "user", "content": _build_prompt(entries)},
        ],
        temperature=0, max_tokens=600,
    )
    return _parse(response.choices[0].message.content, len(entries))


_RECONCILE_SYSTEM = (
    "You decide how a NEW candidate memory fact relates to EXISTING memory. "
    "Choose exactly one action: ADD (genuinely new), UPDATE (supersedes a "
    "specific existing fact — give its index), DELETE (directly contradicts a "
    "specific existing fact, which should be removed — give its index), or NOOP "
    "(already covered by existing memory). Be conservative."
)


def _reconcile_prompt(candidate: str, existing: List[str]) -> str:
    numbered = "\n".join(f"[{i}] {e}" for i, e in enumerate(existing)) or "(none)"
    return (
        f"EXISTING:\n{numbered}\n\nCANDIDATE:\n{candidate}\n\n"
        'Return ONLY JSON: {"action": "ADD|UPDATE|DELETE|NOOP", "target_index": '
        '<int, required for UPDATE/DELETE>}.'
    )


def reconcile_candidate(
    candidate: str, existing: List[str], *,
    llm_caller: Optional[Callable[..., Any]] = None,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Classify a candidate fact vs existing memory. Always returns a safe dict.

    ``{"action": "ADD"|"UPDATE"|"DELETE"|"NOOP", "target_index": int|None}``.
    Any error or out-of-range index degrades to ``ADD`` (never destructive on
    bad input). Best-effort; never raises.
    """
    safe = {"action": "ADD", "target_index": None}
    try:
        if not existing:
            return safe
        if llm_caller is None:
            from agent.auxiliary_client import call_llm as llm_caller
        resp = llm_caller(
            task="memory_reconcile_candidate", provider=provider, model=model,
            messages=[{"role": "system", "content": _RECONCILE_SYSTEM},
                      {"role": "user", "content": _reconcile_prompt(candidate, existing)}],
            temperature=0, max_tokens=60,
        )
        raw = resp.choices[0].message.content or ""
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if not m:
            return safe
        data = json.loads(m.group(0))
        action = str(data.get("action", "")).strip().upper()
        if action not in {"ADD", "UPDATE", "DELETE", "NOOP"}:
            return safe
        if action in {"UPDATE", "DELETE"}:
            try:
                idx = int(data.get("target_index"))
            except (TypeError, ValueError):
                return safe
            if not (0 <= idx < len(existing)):
                return safe
            return {"action": action, "target_index": idx}
        return {"action": action, "target_index": None}
    except Exception as exc:
        logger.debug("reconcile_candidate failed: %s", exc)
        return safe


def reconcile(
    store: Any, target: str = "memory", *,
    llm_caller: Optional[Callable[..., Any]] = None,
    apply: bool = True,
    provider: Optional[str] = None, model: Optional[str] = None,
) -> Dict[str, Any]:
    """Detect + (optionally) remove stale/contradicted entries from ``store``.

    Returns ``{"removed": [text...], "stale": [{drop,kept,reason}...], "error"}``.
    Best-effort; never raises. With ``apply=False`` it reports without changing
    anything (dry run).
    """
    result: Dict[str, Any] = {"removed": [], "stale": [], "error": None}
    try:
        entries = list(getattr(store, f"{'user' if target == 'user' else 'memory'}_entries", []))
        if len(entries) < 2:
            return result
        stale = find_stale(entries, llm_caller=llm_caller, provider=provider, model=model)
        result["stale"] = stale
        # Resolve drop indices to their text, drop duplicates, never drop everything.
        drop_texts = []
        seen = set()
        for s in stale:
            i = s["drop"]
            if i not in seen:
                seen.add(i)
                drop_texts.append(entries[i])
        if len(drop_texts) >= len(entries):  # safety: don't wipe memory
            drop_texts = drop_texts[: len(entries) - 1]
        if apply:
            for text in drop_texts:
                try:
                    store.remove(target, text)
                    result["removed"].append(text)
                except Exception as exc:
                    logger.debug("reconcile remove failed: %s", exc)
        else:
            result["removed"] = drop_texts
    except Exception as exc:
        logger.debug("memory reconcile failed: %s", exc)
        result["error"] = str(exc)
    return result
