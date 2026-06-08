---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# mcp_serve.py

Symbols in `mcp_serve.py`.

- L62 `_get_sessions_dir()` (function) — Return the sessions directory using HERMES_HOME.
- L71 `_get_session_db()` (function) — Get a SessionDB instance for reading message transcripts.
- L81 `_load_sessions_index()` (function) — Load the gateway sessions.json index directly.
- L98 `_load_channel_directory()` (function) — Load the cached channel directory for available targets.
- L118 `_coerce_int(value, *, default: int, minimum: int, maximum: int)` (function) — Coerce value to int with fallback and clamping.
- L137 `_extract_message_content(msg: dict)` (function) — Extract text content from a message, handling multi-part content.
- L149 `_extract_attachments(msg: dict)` (function) — Extract non-text attachments from a message.
- L196 `QueueEvent` (class) — An event in the bridge's in-memory queue.
- L204 `EventBridge` (class) — Background poller that watches SessionDB for new messages and
- L212 `__init__(self)` (method)
- L227 `start(self)` (method) — Start the background polling thread.
- L236 `stop(self)` (method) — Stop the background polling thread.
- L244 `poll_events(self, after_cursor: int=0, session_key: Optional[str]=None, limit: int=20)` (method) — Return events since after_cursor, optionally filtered by session_key.
- L268 `wait_for_event(self, after_cursor: int=0, session_key: Optional[str]=None, timeout_ms: int=30000)` (method) — Block until a matching event arrives or timeout expires.
- L296 `list_pending_approvals(self)` (method) — List approval requests observed during this bridge session.
- L304 `respond_to_approval(self, approval_id: str, decision: str)` (method) — Resolve a pending approval (best-effort without gateway IPC).
- L321 `_enqueue(self, event: QueueEvent)` (method) — Add an event to the queue and wake any waiters.
- L332 `_poll_loop(self)` (method) — Background loop: poll SessionDB for new messages.
- L346 `_poll_once(self, db)` (method) — Check for new messages across all sessions.
- L450 `create_mcp_server(event_bridge: Optional[EventBridge]=None)` (function) — Create and return the Hermes MCP server with all tools registered.
- L866 `run_mcp_server(verbose: bool=False)` (function) — Start the Hermes MCP server on stdio.
