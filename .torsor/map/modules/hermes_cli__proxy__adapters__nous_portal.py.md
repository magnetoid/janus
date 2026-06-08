---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/proxy/adapters/nous_portal.py

Symbols in `hermes_cli/proxy/adapters/nous_portal.py`.

- L44 `NousPortalAdapter` (class) — Proxy upstream for the Nous Portal inference API.
- L47 `__init__(self)` (method)
- L53 `name(self)` (method)
- L57 `display_name(self)` (method)
- L61 `allowed_paths(self)` (method)
- L64 `is_authenticated(self)` (method)
- L75 `get_credential(self)` (method)
- L78 `get_retry_credential(self, *, failed_credential: UpstreamCredential, status_code: int)` (method)
- L92 `_get_credential(self, *, force_refresh: bool=False)` (method)
- L152 `_read_state(self)` (method)
- L165 `_save_state(self, state: Dict[str, Any], *, quarantine_error: Optional[AuthError]=None, quarantine_reason: Optional[str]=None)` (method)
