---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/ddgs/provider.py

Symbols in `plugins/web/ddgs/provider.py`.

- L23 `DDGSWebSearchProvider` (class) — DuckDuckGo HTML-scrape search provider.
- L32 `name(self)` (method)
- L36 `display_name(self)` (method)
- L39 `is_available(self)` (method) — Return True when the ``ddgs`` package is importable.
- L53 `supports_search(self)` (method)
- L56 `supports_extract(self)` (method)
- L59 `search(self, query: str, limit: int=5)` (method) — Execute a DuckDuckGo search and return normalized results.
- L95 `get_setup_schema(self)` (method)
