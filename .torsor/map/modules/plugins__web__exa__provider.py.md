---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/exa/provider.py

Symbols in `plugins/web/exa/provider.py`.

- L41 `_get_exa_client()` (function) — Lazy-import and cache an Exa SDK client.
- L78 `_reset_client_for_tests()` (function) — Drop the cached Exa client so tests can re-instantiate cleanly.
- L85 `ExaWebSearchProvider` (class) — Exa search + extract provider.
- L94 `name(self)` (method)
- L98 `display_name(self)` (method)
- L101 `is_available(self)` (method) — Return True when ``EXA_API_KEY`` is set to a non-empty value.
- L105 `supports_search(self)` (method)
- L108 `supports_extract(self)` (method)
- L111 `search(self, query: str, limit: int=5)` (method) — Execute an Exa search.
- L153 `extract(self, urls: List[str], **kwargs: Any)` (method) — Extract content from one or more URLs via Exa.
- L200 `get_setup_schema(self)` (method)
