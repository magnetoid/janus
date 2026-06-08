---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/slash_confirm.py

Symbols in `tools/slash_confirm.py`.

- L51 `register(session_key: str, confirm_id: str, command: str, handler: Callable[[str], Awaitable[Optional[str]]])` (function) — Register a pending slash-command confirmation.
- L71 `get_pending(session_key: str)` (function) — Return the pending confirm dict for a session, or None.
- L78 `clear(session_key: str)` (function) — Drop the pending confirm for ``session_key`` without running it.
- L84 `clear_if_stale(session_key: str, timeout: float=DEFAULT_TIMEOUT_SECONDS)` (function) — Drop the pending confirm if older than ``timeout`` seconds.
- L99 `resolve(session_key: str, confirm_id: str, choice: str, timeout: float=DEFAULT_TIMEOUT_SECONDS)` (function) — Resolve a pending confirm.
- L143 `resolve_sync_compat(loop: asyncio.AbstractEventLoop, session_key: str, confirm_id: str, choice: str)` (function) — Synchronous helper: schedule resolve() on a loop and wait for the result.
