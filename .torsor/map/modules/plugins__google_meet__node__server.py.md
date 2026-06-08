---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/node/server.py

Symbols in `plugins/google_meet/node/server.py`.

- L37 `_default_token_path()` (function)
- L41 `NodeServer` (class) — WebSocket server that executes meet bot RPCs locally.
- L44 `__init__(self, host: str='127.0.0.1', port: int=18789, token_path: Optional[Path]=None, display_name: str='hermes-meet-node')` (method)
- L59 `ensure_token(self)` (method) — Return the persisted shared secret, generating one on first use.
- L90 `get_token(self)` (method) — Alias for :meth:`ensure_token`; does not mutate on subsequent calls.
- L96 `_handle_request(self, msg: Dict[str, Any])` (method) — Validate + dispatch a single decoded request envelope.
- L172 `serve(self)` (method) — Run the WebSocket server until cancelled.
