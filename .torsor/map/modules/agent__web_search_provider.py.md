---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/web_search_provider.py

Symbols in `agent/web_search_provider.py`.

- L63 `WebSearchProvider` (class) — Abstract base class for a web search/extract backend.
- L76 `name(self)` (method) — Stable short identifier used in ``web.search_backend`` /
- L86 `display_name(self)` (method) — Human-readable label shown in ``hermes tools``. Defaults to ``name``.
- L91 `is_available(self)` (method) — Return True when this provider can service calls.
- L99 `supports_search(self)` (method) — Return True if this provider implements :meth:`search`.
- L103 `supports_extract(self)` (method) — Return True if this provider implements :meth:`extract`.
- L116 `search(self, query: str, limit: int=5)` (method) — Execute a web search.
- L127 `extract(self, urls: List[str], **kwargs: Any)` (method) — Extract content from one or more URLs.
- L160 `get_setup_schema(self)` (method) — Return provider metadata for the ``hermes tools`` picker.
