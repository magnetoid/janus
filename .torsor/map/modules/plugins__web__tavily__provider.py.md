---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/tavily/provider.py

Symbols in `plugins/web/tavily/provider.py`.

- L35 `_tavily_request(endpoint: str, payload: Dict[str, Any])` (function) — POST to the Tavily API and return the parsed JSON response.
- L62 `_normalize_tavily_search_results(response: Dict[str, Any])` (function) — Map Tavily ``/search`` response to ``{success, data: {web: [...]}}``.
- L77 `_normalize_tavily_documents(response: Dict[str, Any], fallback_url: str='')` (function) — Map Tavily ``/extract`` response to standard documents.
- L128 `TavilyWebSearchProvider` (class) — Tavily search + extract provider.
- L132 `name(self)` (method)
- L136 `display_name(self)` (method)
- L139 `is_available(self)` (method) — Return True when ``TAVILY_API_KEY`` is set to a non-empty value.
- L143 `supports_search(self)` (method)
- L146 `supports_extract(self)` (method)
- L149 `search(self, query: str, limit: int=5)` (method) — Execute a Tavily search.
- L174 `extract(self, urls: List[str], **kwargs: Any)` (method) — Extract content from one or more URLs via Tavily.
- L208 `get_setup_schema(self)` (method)
