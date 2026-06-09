"""Shared slash-command handlers for the proactive / self-learning features.

Each ``handle_*`` returns a plain string, so the same logic backs both the
interactive CLI (``process_command``) and the messaging gateway. They read/write
the durable stores (aspirations, interests, memory journal) and never touch the
live agent, so they're safe to run mid-conversation.
"""
from __future__ import annotations

from typing import List


def _args(rest: str) -> List[str]:
    return (rest or "").strip().split()


def handle_aspire(rest: str) -> str:
    """/aspire [set <goal> | list | show <id> | done <id> | clear <id>]"""
    from agent import aspirations as asp

    parts = _args(rest)
    sub = parts[0].lower() if parts else "list"

    if sub == "set":
        title = " ".join(parts[1:]).strip()
        if not title:
            return "Usage: /aspire set <your long-term goal>"
        roadmap = asp.draft_roadmap(title)
        rec = asp.add(title, roadmap=roadmap)
        lines = [f"✓ Aspiration set: {rec['title']}  [{rec['id']}]"]
        for i, m in enumerate(roadmap, 1):
            lines.append(f"  {i}. {m}")
        lines.append("I'll check in on this periodically.")
        return "\n".join(lines)
    if sub == "show" and len(parts) > 1:
        a = asp.get(parts[1])
        if not a:
            return f"No aspiration '{parts[1]}'."
        lines = [f"{a['title']}  [{a['id']}] ({a['status']})"]
        for i, m in enumerate(a.get("roadmap") or [], 1):
            lines.append(f"  {i}. {m}")
        return "\n".join(lines)
    if sub == "done" and len(parts) > 1:
        return "✓ Marked achieved." if asp.set_status(parts[1], "achieved") else f"No aspiration '{parts[1]}'."
    if sub == "clear" and len(parts) > 1:
        return "✓ Removed." if asp.remove(parts[1]) else f"No aspiration '{parts[1]}'."
    # list (default)
    items = asp.load()
    if not items:
        return "No aspirations yet. Set one: /aspire set <goal>"
    out = ["Your aspirations:"]
    for a in items:
        flag = {"achieved": "✓", "active": "•"}.get(a.get("status"), "·")
        out.append(f"{flag} [{a['id']}] {a['title']} ({a.get('status')})")
    return "\n".join(out)


def handle_interest(rest: str) -> str:
    """/interest [add <field> | list | remove <id>]"""
    from agent import interests as it

    parts = _args(rest)
    sub = parts[0].lower() if parts else "list"

    if sub == "add":
        field = " ".join(parts[1:]).strip()
        if not field:
            return "Usage: /interest add <field>"
        rec = it.add(field)
        return f"✓ Now tracking: {rec['field']}  [{rec['id']}]. I'll research the latest in it periodically."
    if sub == "remove" and len(parts) > 1:
        return "✓ Stopped tracking." if it.remove(parts[1]) else f"No interest '{parts[1]}'."
    # list (default)
    items = it.load()
    if not items:
        return 'No interests yet. Add one: /interest add "<field>"'
    out = ["Tracked interests:"]
    for a in items:
        flag = "•" if a.get("status") == "active" else "·"
        out.append(f"{flag} [{a['id']}] {a['field']} ({a.get('status')})")
    return "\n".join(out)


def handle_memory(rest: str) -> str:
    """/memory [log [N] | mine]  — browse the dated journal (mine handled by CLI/agent)."""
    from tools.memory_tool import read_daily_snapshots

    parts = _args(rest)
    sub = parts[0].lower() if parts else "log"
    if sub == "mine":
        # Mining the *live* session needs the running agent; the surfaces that
        # have it handle 'mine' directly. Here we just point the way.
        return "Mining runs against your session — use `janus memory mine` in the terminal."
    days = 7
    if len(parts) > 1 and parts[-1].isdigit():
        days = int(parts[-1])
    result = read_daily_snapshots(days=days)
    snaps = result.get("days", [])
    if not snaps:
        return "No daily memory snapshots yet — they fill in as memory is saved."
    return "\n\n".join(d["text"].rstrip() for d in snaps)
