---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/browser/browser_use/provider.py

Symbols in `plugins/browser/browser_use/provider.py`.

- L55 `_get_or_create_pending_create_key(task_id: str)` (function)
- L66 `_clear_pending_create_key(task_id: str)` (function)
- L71 `_should_preserve_pending_create_key(response: requests.Response)` (function) — Decide whether to keep the idempotency key after a failed create.
- L104 `BrowserUseBrowserProvider` (class) — Browser Use (https://browser-use.com) cloud browser backend.
- L114 `name(self)` (method)
- L118 `display_name(self)` (method)
- L121 `is_available(self)` (method)
- L128 `_get_config_or_none(self, *, refresh_token: bool=True)` (method)
- L162 `_get_config(self)` (method)
- L182 `_headers(self, config: Dict[str, Any])` (method)
- L188 `create_session(self, task_id: str)` (method)
- L253 `close_session(self, session_id: str)` (method)
- L284 `emergency_cleanup(self, session_id: str)` (method)
- L304 `get_setup_schema(self)` (method)
