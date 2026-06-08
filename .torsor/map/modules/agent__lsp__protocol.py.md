---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/protocol.py

Symbols in `agent/lsp/protocol.py`.

- L32 `LSPProtocolError` (class) — Raised when the wire protocol is violated.
- L41 `LSPRequestError` (class) — Raised when an LSP request returns an error response.
- L47 `__init__(self, code: int, message: str, data: Any=None)` (method)
- L54 `encode_message(obj: dict)` (function) — Encode a JSON-RPC envelope as a Content-Length framed byte string.
- L66 `read_message(reader: asyncio.StreamReader)` (function) — Read one Content-Length framed JSON-RPC message from the stream.
- L132 `make_request(req_id: int, method: str, params: Any)` (function) — Build a JSON-RPC 2.0 request envelope.
- L140 `make_notification(method: str, params: Any)` (function) — Build a JSON-RPC 2.0 notification envelope (no ``id``).
- L148 `make_response(req_id: Any, result: Any)` (function) — Build a JSON-RPC 2.0 success response envelope.
- L153 `make_error_response(req_id: Any, code: int, message: str, data: Any=None)` (function) — Build a JSON-RPC 2.0 error response envelope.
- L161 `classify_message(msg: dict)` (function) — Return ``(kind, key)`` where kind is one of ``request``,
