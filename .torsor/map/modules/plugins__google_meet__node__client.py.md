---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/node/client.py

Symbols in `plugins/google_meet/node/client.py`.

- L19 `NodeClient` (class) — Thin synchronous WS client matching the server's request surface.
- L22 `__init__(self, url: str, token: str, timeout: float=10.0)` (method)
- L33 `_rpc(self, type: str, payload: Dict[str, Any])` (method) — Send one request, return the response payload dict.
- L73 `start_bot(self, url: str, guest_name: str='Hermes Agent', duration: Optional[str]=None, headed: bool=False, mode: str='transcribe')` (method)
- L91 `stop(self)` (method)
- L94 `status(self)` (method)
- L97 `transcript(self, last: Optional[int]=None)` (method)
- L103 `say(self, text: str)` (method)
- L106 `ping(self)` (method)
