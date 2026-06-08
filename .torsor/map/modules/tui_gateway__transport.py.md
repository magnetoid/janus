---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tui_gateway/transport.py

Symbols in `tui_gateway/transport.py`.

- L67 `Transport` (class) — Minimal interface every transport implements.
- L70 `write(self, obj: dict)` (method) — Emit one JSON frame. Return ``False`` when the peer is gone.
- L73 `close(self)` (method) — Release any resources owned by this transport.
- L85 `current_transport()` (function) — Return the transport bound for the current request, if any.
- L90 `bind_transport(transport: Optional[Transport])` (function) — Bind *transport* for the current context. Returns a token for :func:`reset_transport`.
- L95 `reset_transport(token)` (function) — Restore the transport binding captured by :func:`bind_transport`.
- L100 `StdioTransport` (class) — Writes JSON frames to a stream (usually ``sys.stdout``).
- L110 `__init__(self, stream_getter: Callable[[], Any], lock: threading.Lock)` (method)
- L114 `write(self, obj: dict)` (method) — Return ``True`` on success, ``False`` ONLY when the peer is gone.
- L182 `close(self)` (method)
- L186 `TeeTransport` (class) — Mirrors writes to one primary plus N best-effort secondaries.
- L197 `__init__(self, primary: 'Transport', *secondaries: 'Transport')` (method)
- L201 `write(self, obj: dict)` (method)
- L211 `close(self)` (method)
