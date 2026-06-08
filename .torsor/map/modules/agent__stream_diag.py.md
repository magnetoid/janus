---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/stream_diag.py

Symbols in `agent/stream_diag.py`.

- L41 `stream_diag_init()` (function) — Return a fresh per-attempt diagnostic dict.
- L58 `stream_diag_capture_response(agent: Any, diag: Dict[str, Any], http_response: Any)` (function) — Snapshot interesting headers + HTTP status from the live stream.
- L89 `flatten_exception_chain(error: BaseException)` (function) — Return a compact ``Outer(msg) <- Inner(msg) <- ...`` rendering.
- L120 `log_stream_retry(agent: Any, *, kind: str, error: BaseException, attempt: int, max_attempts: int, mid_tool_call: bool, diag: Optional[Dict[str, Any]]=None)` (function) — Record a transient stream-drop and retry to ``agent.log``.
- L214 `emit_stream_drop(agent: Any, *, error: BaseException, attempt: int, max_attempts: int, mid_tool_call: bool, diag: Optional[Dict[str, Any]]=None)` (function) — Emit a single user-visible line for a stream drop+retry.
