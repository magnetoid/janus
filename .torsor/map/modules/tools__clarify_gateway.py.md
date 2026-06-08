---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/clarify_gateway.py

Symbols in `tools/clarify_gateway.py`.

- L48 `_ClarifyEntry` (class) — One pending clarify request inside a gateway session.
- L58 `signature(self)` (method)
- L78 `register(clarify_id: str, session_key: str, question: str, choices: Optional[List[str]])` (function) — Register a pending clarify request and return the entry.
- L103 `wait_for_response(clarify_id: str, timeout: float)` (function) — Block on the entry's event until resolved or timeout fires.
- L150 `resolve_gateway_clarify(clarify_id: str, response: str)` (function) — Unblock the agent thread waiting on ``clarify_id``.
- L165 `get_pending_for_session(session_key: str)` (function) — Return the OLDEST pending clarify entry for a session, or None.
- L183 `mark_awaiting_text(clarify_id: str)` (function) — Flip an entry into text-capture mode (user picked the 'Other' button).
- L196 `has_pending(session_key: str)` (function) — Return True when this session has at least one pending clarify entry.
- L203 `clear_session(session_key: str)` (function) — Resolve and drop every pending clarify for a session.
- L231 `get_clarify_timeout()` (function) — Read the clarify response timeout (seconds) from config.
- L261 `register_notify(session_key: str, cb: Callable[[_ClarifyEntry], None])` (function) — Register a per-session notify callback used by ``clarify_callback``.
- L267 `unregister_notify(session_key: str)` (function) — Drop the per-session notify callback and cancel any pending clarify entries.
- L276 `get_notify(session_key: str)` (function)
