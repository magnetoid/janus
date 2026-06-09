"""recall_memory tool — surface the memory most relevant to a query.

Lets the agent pull specific durable facts (and dated-journal history) on
demand, instead of relying only on the always-injected memory snapshot. Backed
by agent/memory_recall.py (dependency-free lexical relevance).
"""
import json

from tools.registry import registry


def recall_memory(query: str, n: int = 5, task_id: str = None) -> str:
    try:
        from agent.memory_recall import recall

        try:
            n = int(n)
        except (TypeError, ValueError):
            n = 5
        hits = recall(query, n=max(1, min(n, 20)))
        return json.dumps({"success": True, "query": query, "results": hits}, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="recall_memory",
    toolset="memory",
    schema={
        "name": "recall_memory",
        "description": (
            "Surface the memory entries (and dated-journal history) most relevant to a "
            "query. Use this to pull specific durable facts on demand instead of relying "
            "only on the always-injected memory snapshot — e.g. recall how something was "
            "done before, or a preference the user stated weeks ago."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "What you're trying to recall (e.g. 'how do we deploy staging').",
                },
                "n": {"type": "integer", "description": "Max results to return (default 5)."},
            },
            "required": ["query"],
        },
    },
    handler=lambda args, **kw: recall_memory(
        query=args.get("query", ""), n=args.get("n", 5), task_id=kw.get("task_id")
    ),
)
