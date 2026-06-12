"""Relevance recall over memory — surface what matters for a query.

Today MEMORY.md is injected wholesale (char-capped), and the long tail in the
daily journal isn't reachable mid-task. This scores every memory entry AND the
dated-journal history against a query and returns the most relevant few — so
the agent can pull the *right* facts on demand instead of carrying everything.

Ranking follows the Generative Agents retrieval signal — a weighted blend of
**relevance** (lexical token overlap, length-normalized), **recency** (journal
entries decay with age; durable memory stays current), and **importance** (a
substance proxy) — rather than relevance alone. Recency and importance only
re-order entries that already match the query lexically, so precision is
unchanged: an irrelevant-but-fresh entry never surfaces. Dependency-free and
deterministic; an optional embedding backend adds a semantic re-rank on top.
"""
from __future__ import annotations

import re
from typing import Any, Dict, List

# Generative-Agents-style retrieval weights (relevance dominant). Recency and
# importance act as boosters/tie-breakers among lexically-matched candidates.
_W_RELEVANCE = 0.60
_W_RECENCY = 0.25
_W_IMPORTANCE = 0.15
_RECENCY_HALF_LIFE_DAYS = 30.0  # a journal entry's recency halves every 30 days
_IMPORTANCE_FULL_CHARS = 240.0  # length at which the importance proxy saturates

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


def _today():
    try:
        from janus_time import now as _now
        return _now()
    except Exception:
        return None


def _recency(source: str, today) -> float:
    """1.0 for durable memory/user entries; journal entries decay with age."""
    if today is None or not source.startswith("journal:"):
        return 1.0
    from datetime import datetime
    try:
        day = datetime.strptime(source.split(":", 1)[1], "%Y-%m-%d").date()
        age_days = max(0, (today.date() - day).days)
        return 0.5 ** (age_days / _RECENCY_HALF_LIFE_DAYS)
    except (ValueError, AttributeError):
        return 1.0


def _importance(text: str) -> float:
    """A cheap substance proxy: longer, more specific entries score higher (capped)."""
    return min(1.0, len(text) / _IMPORTANCE_FULL_CHARS)


def recall(query: str, *, n: int = 5, include_journal: bool = True, journal_days: int = 30) -> List[Dict[str, Any]]:
    """Return up to ``n`` memory entries most relevant to ``query``, ranked."""
    qt = _tokens(query)
    if not qt:
        return []
    today = _today()
    matched: List[Dict[str, Any]] = []
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
        # raw relevance: length-normalized overlap (favors concise, on-topic)
        matched.append({
            "text": text, "source": c["source"],
            "_rel": overlap / (len(et) ** 0.5),
            "_rec": _recency(c["source"], today),
            "_imp": _importance(text),
        })
    if not matched:
        return []
    # normalize relevance across the matched set so the blend is comparable
    max_rel = max(m["_rel"] for m in matched) or 1.0
    scored: List[Dict[str, Any]] = []
    for m in matched:
        rel = m["_rel"] / max_rel
        score = _W_RELEVANCE * rel + _W_RECENCY * m["_rec"] + _W_IMPORTANCE * m["_imp"]
        scored.append({"text": m["text"], "source": m["source"], "score": round(score, 4)})
    scored.sort(key=lambda x: x["score"], reverse=True)
    # Hybrid: semantically re-rank the lexical top candidates when an embedding
    # backend is installed; otherwise this returns the lexical top-n unchanged.
    try:
        from agent.embeddings import hybrid_rerank
        return hybrid_rerank(query, scored, n, text_of=lambda h: h["text"])
    except Exception:
        return scored[:n]
