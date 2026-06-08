---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/node/protocol.py

Symbols in `plugins/google_meet/node/protocol.py`.

- L31 `make_request(type: str, token: str, payload: Dict[str, Any], req_id: str | None=None)` (function) — Construct a request envelope.
- L58 `make_response(req_id: str, payload: Dict[str, Any])` (function) — Build a success response. The caller supplies the *request* type;
- L71 `make_error(req_id: str, error: str)` (function)
- L75 `encode(msg: Dict[str, Any])` (function) — Serialize a message envelope to a JSON string.
- L80 `decode(raw: str)` (function) — Parse a JSON envelope, raising ValueError on anything malformed.
- L100 `validate_request(msg: Dict[str, Any], expected_token: str)` (function) — Check a decoded request against the server's shared token.
