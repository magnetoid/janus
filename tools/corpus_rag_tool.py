"""search_corpus — agentic retrieval over a user-registered corpus.

Only exposed when at least one corpus is registered (``janus corpus add``). The
agent drives multi-hop retrieval: issue a query, read the ranked file:line
chunks, then issue follow-up queries based on what it found.
"""
import json

from tools.registry import registry


def _has_corpus() -> bool:
    try:
        from agent.corpus_rag import load_corpora
        return bool(load_corpora())
    except Exception:
        return False


def search_corpus(query: str, corpus: str = None, n: int = 5, **_kw) -> str:
    try:
        from agent.corpus_rag import search_corpus as _search, load_corpora

        hits = _search(query, corpus=corpus, n=int(n))
        return json.dumps({
            "success": True,
            "query": query,
            "corpus": corpus or (next(iter(load_corpora()), None)),
            "results": hits,
        }, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="search_corpus",
    toolset="rag",
    schema={
        "name": "search_corpus",
        "description": (
            "Retrieve the most relevant chunks (with file:line citations) from a "
            "registered corpus — a code repo, docs folder, or knowledge base. Issue "
            "follow-up queries based on what you find to dig deeper (multi-hop). "
            "Available only when the user has registered a corpus with 'janus corpus add'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "What you're looking for."},
                "corpus": {"type": "string", "description": "Corpus name (optional if only one is registered)."},
                "n": {"type": "integer", "description": "Max results (default 5)."},
            },
            "required": ["query"],
        },
    },
    handler=lambda args, **kw: search_corpus(
        query=args.get("query", ""), corpus=args.get("corpus"), n=args.get("n", 5)
    ),
    check_fn=_has_corpus,
)
