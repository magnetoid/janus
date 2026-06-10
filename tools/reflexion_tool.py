"""deep_reason — solve a hard problem with deliberate self-critique + retry.

Reflexion-style depth to complement mixture_of_agents' breadth: one model
attempts, critiques its own answer, and retries with the critique until a
verifier approves or an iteration cap is hit. Use for genuinely hard problems
where a first pass is likely flawed (tricky math/logic, careful analysis,
multi-constraint reasoning) — like MoA, it spends extra calls, so reach for it
deliberately.
"""
import json

from tools.registry import registry


def deep_reason(task: str, max_iterations: int = 3, **_kw) -> str:
    try:
        from agent.reflexion import deep_reason as _run
        res = _run(task, max_iterations=int(max_iterations))
        return json.dumps({
            "success": res.get("error") is None,
            "answer": res.get("answer", ""),
            "converged": res.get("converged"),
            "iterations": res.get("iterations"),
            "error": res.get("error"),
        }, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="deep_reason",
    toolset="moa",
    schema={
        "name": "deep_reason",
        "description": (
            "Solve a hard problem with deliberate plan->attempt->self-critique->retry "
            "(Reflexion). The answer is iteratively refined until an internal critic "
            "approves it or the iteration cap is reached. Best for tricky reasoning "
            "where a first attempt is likely flawed. Spends multiple model calls — use "
            "deliberately, like mixture_of_agents."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "task": {"type": "string", "description": "The problem to solve carefully."},
                "max_iterations": {"type": "integer", "description": "Max refine cycles (1-6, default 3)."},
            },
            "required": ["task"],
        },
    },
    handler=lambda args, **kw: deep_reason(
        task=args.get("task", ""), max_iterations=args.get("max_iterations", 3)
    ),
)
