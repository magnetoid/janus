"""recall_lessons tool — surface lessons learned from past failures.

Backed by agent/lessons.py (the Reflexion write-back loop). When the agent is
about to tackle a task that resembles one it has failed before, this pulls the
distilled "do X instead" lesson so the mistake isn't repeated.
"""
import json

from tools.registry import registry


def recall_lessons(query: str, n: int = 3, task_id: str = None) -> str:
    try:
        from agent.lessons import recall_lessons as _recall

        try:
            n = int(n)
        except (TypeError, ValueError):
            n = 3
        hits = _recall(query, n=max(1, min(n, 10)))
        return json.dumps({"success": True, "query": query, "results": hits}, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="recall_lessons",
    toolset="memory",
    schema={
        "name": "recall_lessons",
        "description": (
            "Recall lessons distilled from PAST FAILURES on similar tasks — concrete "
            "'do X instead of Y' guidance the agent wrote to itself after a session that "
            "didn't succeed. Call this before a non-trivial task (a deploy, a migration, a "
            "tricky debugging session) to avoid repeating an earlier mistake."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The task you're about to do (e.g. 'deploy to staging').",
                },
                "n": {"type": "integer", "description": "Max lessons to return (default 3)."},
            },
            "required": ["query"],
        },
    },
    handler=lambda args, **kw: recall_lessons(
        query=args.get("query", ""), n=args.get("n", 3), task_id=kw.get("task_id")
    ),
)
