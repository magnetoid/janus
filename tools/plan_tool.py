"""propose_plan tool — Plan Mode.

Backed by agent/plan_mode.py. The agent calls this for hard, multi-step,
state-changing work BEFORE executing: it records the plan to a per-session store
and returns the formatted plan plus an approval prompt. The agent presents that and
yields the turn (same flow as the clarify gateway); on the user's "go" it executes,
seeding the todo list from the steps.
"""
import json

from tools.registry import registry


def propose_plan(steps, task_id: str = None) -> str:
    try:
        from agent.plan_mode import record_plan, format_plan
        if isinstance(steps, str):
            steps = [steps]
        cleaned = record_plan(task_id or "default", list(steps or []))
        if not cleaned:
            return json.dumps({"success": False, "error": "no plan steps provided"})
        return format_plan(cleaned)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="propose_plan",
    toolset="memory",
    schema={
        "name": "propose_plan",
        "description": (
            "Propose a step-by-step PLAN and wait for the user's approval BEFORE "
            "executing. Call this first for any hard, multi-step, state-changing "
            "task (editing files, running commands, deploying, migrating). After "
            "calling it, present the plan and STOP — do not start executing until "
            "the user replies 'go' or adjusts it. Keep simple one-step work immediate."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "steps": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Ordered, concrete steps you intend to take.",
                },
            },
            "required": ["steps"],
        },
    },
    handler=lambda args, **kw: propose_plan(steps=args.get("steps", []), task_id=kw.get("task_id")),
)
