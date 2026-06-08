---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/xai_http.py

Symbols in `tools/xai_http.py`.

- L10 `has_xai_credentials()` (function) — Cheap probe — return True when xAI credentials are *likely* usable.
- L48 `get_env_value(name: str, default=None)` (function) — Read ``name`` from ``~/.hermes/.env`` first, then ``os.environ``.
- L66 `hermes_xai_user_agent()` (function) — Return a stable Hermes-specific User-Agent for xAI HTTP calls.
- L75 `resolve_xai_http_credentials(*, force_refresh: bool=False)` (function) — Resolve bearer credentials for direct xAI HTTP endpoints.
