---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_web_tools_tavily.py

Symbols in `tests/tools/test_web_tools_tavily.py`.

- L21 `TestTavilyRequest` (class) — Test suite for the _tavily_request helper.
- L24 `test_raises_without_api_key(self)` (method) — No TAVILY_API_KEY → ValueError with guidance.
- L32 `test_posts_with_api_key_in_body(self)` (method) — api_key is injected into the JSON payload.
- L50 `test_raises_on_http_error(self)` (method) — Non-2xx responses propagate as httpx.HTTPStatusError.
- L67 `TestNormalizeTavilySearchResults` (class) — Test search result normalization.
- L70 `test_basic_normalization(self)` (method)
- L88 `test_empty_results(self)` (method)
- L94 `test_missing_fields(self)` (method)
- L105 `TestNormalizeTavilyDocuments` (class) — Test extract/crawl document normalization.
- L108 `test_basic_document(self)` (method)
- L125 `test_falls_back_to_content_when_no_raw_content(self)` (method)
- L131 `test_failed_results_included(self)` (method)
- L145 `test_failed_urls_included(self)` (method)
- L156 `test_fallback_url(self)` (method)
- L165 `TestWebSearchTavily` (class) — Test web_search_tool dispatch to Tavily.
- L171 `_populate_web_registry(self)` (method)
- L177 `test_search_dispatches_to_tavily(self)` (method)
- L197 `TestWebExtractTavily` (class) — Test web_extract_tool dispatch to Tavily.
- L203 `_populate_web_registry(self)` (method)
- L209 `test_extract_dispatches_to_tavily(self)` (method)
