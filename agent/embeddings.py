"""Optional semantic embeddings for HYBRID retrieval.

Retrieval (memory recall + corpus RAG) is lexical by default. When an embedding
backend is installed, this adds a hybrid re-rank: lexical prefilters the
candidates (fast, no embedding the whole corpus), then embeddings re-rank the
top pool by MEANING. Auto-detected — with no backend installed, callers keep
their lexical ranking unchanged, so nothing breaks.

No heavy dependency lives in core. Install one to enable semantic re-rank:
    uv pip install fastembed          # preferred (small, ONNX)
    # or: uv pip install sentence-transformers
"""
from __future__ import annotations

import logging
from functools import lru_cache
from typing import Any, Callable, List, Optional

logger = logging.getLogger(__name__)

_FASTEMBED_MODEL = "BAAI/bge-small-en-v1.5"
_ST_MODEL = "all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def _get_model():
    """Return ``(kind, model)`` for the first available backend, else ``(None, None)``."""
    try:
        from fastembed import TextEmbedding  # type: ignore
        return ("fastembed", TextEmbedding(model_name=_FASTEMBED_MODEL))
    except Exception:
        pass
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
        return ("st", SentenceTransformer(_ST_MODEL))
    except Exception:
        pass
    return (None, None)


def available() -> bool:
    return _get_model()[0] is not None


def embed(texts: List[str]):
    """Return an ``(n, d)`` numpy array of embeddings, or None if no backend."""
    kind, model = _get_model()
    if kind is None:
        return None
    try:
        import numpy as np
        if kind == "fastembed":
            return np.asarray(list(model.embed(list(texts))), dtype="float32")
        return np.asarray(model.encode(list(texts)), dtype="float32")
    except Exception as exc:
        logger.debug("embed failed: %s", exc)
        return None


def rerank(query: str, candidates: List[str], n: int) -> Optional[List[int]]:
    """Indices of ``candidates`` ranked by cosine similarity to ``query`` (best
    first), capped at ``n``. None when no embedding backend is available."""
    if not candidates:
        return []
    embs = embed([query] + list(candidates))
    if embs is None or len(embs) != len(candidates) + 1:
        return None
    try:
        import numpy as np
        q = embs[0]
        docs = embs[1:]
        qn = q / (np.linalg.norm(q) + 1e-9)
        dn = docs / (np.linalg.norm(docs, axis=1, keepdims=True) + 1e-9)
        sims = dn @ qn
        return [int(i) for i in np.argsort(-sims)[:n]]
    except Exception as exc:
        logger.debug("rerank failed: %s", exc)
        return None


def hybrid_rerank(
    query: str, ranked_items: List[Any], n: int, *,
    text_of: Callable[[Any], str], candidate_pool: int = 40,
) -> List[Any]:
    """Semantically re-rank the top ``candidate_pool`` of an ALREADY lexically
    ranked list (best first) and return the best ``n``. Falls back to
    ``ranked_items[:n]`` when no embedding backend is available."""
    if not ranked_items:
        return []
    pool = ranked_items[:candidate_pool]
    order = rerank(query, [text_of(x) for x in pool], n)
    if order is None:
        return ranked_items[:n]
    return [pool[i] for i in order]
