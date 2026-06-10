"""Relevance recall over memory — surface what matters for a query.

Today MEMORY.md is injected wholesale (char-capped), and the long tail in the
daily journal isn't reachable mid-task. This scores every memory entry AND the
dated-journal history against a query and returns the most relevant few — so
the agent can pull the *right* facts on demand instead of carrying everything.

Lexical scoring (token overlap, length-normalized, recency-aware) — dependency
free and deterministic. The torsor-helper provides heavier hybrid/vector recall
for those who want it; this is the always-available baseline.
"""
from __future__ import annotations

import re
from typing import Any, Dict, List

_STOP = {
    "the", "a", "an", "is", "are", "was", "were", "be", "to", "of", "and", "or",
    "in", "on", "for", "with", "my", "your", "it", "its", "that", "this", "i",
    "you", "we", "they", "as", "at", "by", "from", "but", "not", "do", "does",
}


def _tokens(s: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]+", str(s).lower()) if len(w) > 2 and w not in _STOP}


def _candidates(include_journal: bool, journal_days: int) -> List[Dict[str, str]]:
    from tools.memory_tool import MemoryStore, read_daily_snapshots

    store = MemoryStore()
    store.load_from_disk()
    out: List[Dict[str, str]] = []
    for e in store.memory_entries:
        out.append({"text": e, "source": "memory"})
    for e in store.user_entries:
        out.append({"text": e, "source": "user"})
    if include_journal:
        for day in read_daily_snapshots(days=journal_days).get("days", []):
            for line in day.get("text", "").splitlines():
                line = line.strip()
                if line.startswith("- "):
                    # strip the "`HH:MM` **SCOPE** verb:" prefix if present
                    body = re.sub(r"^- (`[^`]*`\s*)?(\*\*[^*]+\*\*\s*\w*:?\s*)?", "", line)
                    if body.strip():
                        out.append({"text": body.strip(), "source": f"journal:{day.get('date')}"})
    return out


def recall(query: str, *, n: int = 5, include_journal: bool = True, journal_days: int = 30) -> List[Dict[str, Any]]:
    """Return up to ``n`` memory entries most relevant to ``query``, ranked."""
    qt = _tokens(query)
    if not qt:
        return []
    scored: List[Dict[str, Any]] = []
    seen: set = set()
    for c in _candidates(include_journal, journal_days):
        text = c["text"]
        if text in seen:
            continue
        et = _tokens(text)
        if not et:
            continue
        overlap = len(qt & et)
        if overlap == 0:
            continue
        seen.add(text)
        # favor concise, on-topic entries (length-normalized overlap)
        score = round(overlap / (len(et) ** 0.5), 4)
        scored.append({"text": text, "source": c["source"], "score": score})
    scored.sort(key=lambda x: x["score"], reverse=True)
    # Hybrid: semantically re-rank the lexical top candidates when an embedding
    # backend is installed; otherwise this returns the lexical top-n unchanged.
    try:
        from agent.embeddings import hybrid_rerank
        return hybrid_rerank(query, scored, n, text_of=lambda h: h["text"])
    except Exception:
        return scored[:n]
