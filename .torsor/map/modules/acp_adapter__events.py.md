---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# acp_adapter/events.py

Symbols in `acp_adapter/events.py`.

- L28 `_json_loads_maybe_prefix(value: str)` (function) — Parse a JSON object even when Hermes appended a human hint after it.
- L39 `_build_plan_update_from_todo_result(result: Any)` (function) — Translate Hermes' todo tool result into ACP's native plan update.
- L87 `_send_update(conn: acp.Client, session_id: str, loop: asyncio.AbstractEventLoop, update: Any)` (function) — Fire-and-forget an ACP session update from a worker thread.
- L114 `make_tool_progress_cb(conn: acp.Client, session_id: str, loop: asyncio.AbstractEventLoop, tool_call_ids: Dict[str, Deque[str]], tool_call_meta: Dict[str, Dict[str, Any]], edit_approval_policy_getter: Callable[[], tuple[str, str | None]] | None=None)` (function) — Create a ``tool_progress_callback`` for AIAgent.
- L189 `make_thinking_cb(conn: acp.Client, session_id: str, loop: asyncio.AbstractEventLoop)` (function) — Create a ``thinking_callback`` for AIAgent.
- L209 `make_step_cb(conn: acp.Client, session_id: str, loop: asyncio.AbstractEventLoop, tool_call_ids: Dict[str, Deque[str]], tool_call_meta: Dict[str, Dict[str, Any]])` (function) — Create a ``step_callback`` for AIAgent.
- L266 `make_message_cb(conn: acp.Client, session_id: str, loop: asyncio.AbstractEventLoop)` (function) — Create a callback that streams agent response text to the editor.
