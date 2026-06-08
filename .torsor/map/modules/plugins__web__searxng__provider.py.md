---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/searxng/provider.py

Symbols in `plugins/web/searxng/provider.py`.

- L34 `_searxng_url()` (function) — Return SEARXNG_URL from Hermes config-aware env, falling back to process env.
- L47 `SearXNGWebSearchProvider` (class) — Search via a user-hosted SearXNG instance.
- L51 `name(self)` (method)
- L55 `display_name(self)` (method)
- L58 `is_available(self)` (method) — Return True when ``SEARXNG_URL`` is set.
- L62 `supports_search(self)` (method)
- L65 `supports_extract(self)` (method)
- L68 `search(self, query: str, limit: int=5)` (method) — Execute a search against the configured SearXNG instance.
- L141 `get_setup_schema(self)` (method)
