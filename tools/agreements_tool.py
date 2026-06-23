"""pin_agreement / recall_agreements tools — Standing Agreements.

Backed by agent/agreements.py. ``pin_agreement`` records a binding commitment
made during the conversation; its return value is a marker-prefixed message that
stays in the transcript (a cache-safe append) AND is mirrored to a persistent
per-session store, so it survives context compression. ``recall_agreements``
re-fetches the session's agreements from that store — so even after a long session
compresses the original message away, the agent can re-ground on what was agreed
instead of forgetting it or rushing past it.
"""
import json

from tools.registry import registry


def pin_agreement(text: str, task_id: str = None) -> str:
    try:
        from agent.agreements import format_agreement, record
        text = str(text).strip()
        if not text:
            return json.dumps({"success": False, "error": "empty agreement"})
        record(task_id or "default", text, source="agent")
        return format_agreement(text)
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


def recall_agreements(task_id: str = None) -> str:
    try:
        from agent.agreements import render_for_prompt
        block = render_for_prompt(task_id or "default")
        return block or "No standing agreements recorded for this session yet."
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


registry.register(
    name="pin_agreement",
    toolset="memory",
    schema={
        "name": "pin_agreement",
        "description": (
            "Pin a STANDING AGREEMENT — a binding decision or constraint agreed "
            "during this conversation (e.g. 'deploy only to staging', 'never "
            "force-push main', 'use the shared fixture, not per-test patches'). "
            "Call this the moment you and the user settle on how something will be "
            "done, so it survives a long session and you don't drift or rush past "
            "it. The agreement is recorded and echoed back marked 📌."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The agreement, as one concrete sentence.",
                },
            },
            "required": ["text"],
        },
    },
    handler=lambda args, **kw: pin_agreement(text=args.get("text", ""), task_id=kw.get("task_id")),
)

registry.register(
    name="recall_agreements",
    toolset="memory",
    schema={
        "name": "recall_agreements",
        "description": (
            "Recall the STANDING AGREEMENTS pinned earlier in this conversation. "
            "Call this before starting a new or similar task — especially deep into "
            "a long session — to re-ground on prior commitments before acting, even "
            "if they have scrolled out of the visible context."
        ),
        "parameters": {"type": "object", "properties": {}},
    },
    handler=lambda args, **kw: recall_agreements(task_id=kw.get("task_id")),
)
