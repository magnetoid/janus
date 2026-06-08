---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tui_gateway/ws.py

Symbols in `tui_gateway/ws.py`.

- L50 `WSTransport` (class) — Per-connection WS transport.
- L66 `__init__(self, ws: Any, loop: asyncio.AbstractEventLoop, *, peer: str='unknown')` (method)
- L78 `write(self, obj: dict)` (method)
- L110 `write_async(self, obj: dict)` (method) — Send from the owning event loop. Awaits until the frame is on the wire.
- L117 `_safe_send(self, line: str)` (method)
- L127 `close(self)` (method)
- L131 `_ws_peer_label(ws: Any)` (function) — Return ``host:port`` when available, else a stable placeholder.
- L141 `_disable_nagle(ws: Any)` (function) — Disable Nagle so streamed JSON-RPC frames go out individually.
- L159 `handle_ws(ws: Any)` (function) — Run one WebSocket session. Wire-compatible with ``tui_gateway.entry``.
