"""pagemem_remember tool — PageMem.

Backed by agent/page_memory.py. After the agent SUCCEEDS at a task on a website, it
calls this to persist the winning action sequence (a 'playbook') for that site, so a
future visit recalls what worked instead of re-deriving page structure. Targets use
the stable ``role "name"`` identity (e.g. ``button "Search"``), not ephemeral @e
refs. Typed secrets (passwords/tokens) are scrubbed before storage.
"""
import json

from tools.registry import registry


def pagemem_remember(url, task, steps, task_id: str = None) -> str:
    try:
        from agent.page_memory import enabled, record_playbook
        if not enabled():
            return json.dumps({"success": False, "error": "page_memory is disabled"})
        if isinstance(steps, str):
            # some models stringify the whole array — parse it back to a list
            try:
                parsed = json.loads(steps)
                steps = parsed if isinstance(parsed, list) else []
            except (ValueError, TypeError):
                steps = []
        pid = record_playbook(url, task, list(steps or []))
        if not pid:
            return json.dumps({"success": False,
                               "error": "could not record (need a url, a task, and steps)"})
        n = len(steps or [])
        return (f"📍 Saved a PageMem playbook for {url}: '{task}' ({n} step"
                f"{'s' if n != 1 else ''}). I'll recall it on the next visit.")
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="pagemem_remember",
    toolset="browser",
    schema={
        "name": "pagemem_remember",
        "description": (
            "Remember HOW to do a task on a website for next time. Call this AFTER you "
            "successfully complete a web task, to save the action sequence that worked. "
            "Use STABLE element identities (role + accessible-name, e.g. 'button "
            "\"Search\"'), never the @e refs. PageMem recalls this automatically when "
            "you navigate back to the site. Don't include passwords — they're scrubbed."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The page/site URL the task was done on."},
                "task": {"type": "string", "description": "Short description of the task accomplished."},
                "steps": {
                    "type": "array",
                    "description": "Ordered actions that worked.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "action": {"type": "string", "description": "e.g. click, type, scroll, press."},
                            "target": {"type": "string", "description": 'Stable target, e.g. button "Search".'},
                            "value": {"type": "string", "description": "Typed value, if any (secrets scrubbed)."},
                        },
                        "required": ["action", "target"],
                    },
                },
            },
            "required": ["url", "task", "steps"],
        },
    },
    handler=lambda args, **kw: pagemem_remember(
        url=args.get("url"), task=args.get("task"),
        steps=args.get("steps", []), task_id=kw.get("task_id")),
)
