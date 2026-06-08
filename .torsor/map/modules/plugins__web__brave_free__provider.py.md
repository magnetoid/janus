---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/brave_free/provider.py

Symbols in `plugins/web/brave_free/provider.py`.

- L33 `BraveFreeWebSearchProvider` (class) — Search-only Brave provider using the free-tier Data-for-Search API.
- L41 `name(self)` (method)
- L47 `display_name(self)` (method)
- L50 `is_available(self)` (method) — Return True when ``BRAVE_SEARCH_API_KEY`` is set to a non-empty value.
- L54 `supports_search(self)` (method)
- L57 `supports_extract(self)` (method)
- L60 `search(self, query: str, limit: int=5)` (method) — Execute a search against the Brave Search API.
- L125 `get_setup_schema(self)` (method)
