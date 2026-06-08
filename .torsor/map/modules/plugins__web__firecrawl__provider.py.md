---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/firecrawl/provider.py

Symbols in `plugins/web/firecrawl/provider.py`.

- L76 `_load_firecrawl_cls()` (function) — Import and cache ``firecrawl.Firecrawl``.
- L94 `_FirecrawlProxy` (class) — Callable proxy that looks like ``firecrawl.Firecrawl`` but imports lazily.
- L99 `__call__(self, *args: Any, **kwargs: Any)` (method)
- L102 `__instancecheck__(self, obj: Any)` (method)
- L105 `__repr__(self)` (method)
- L122 `_get_direct_firecrawl_config()` (function) — Return explicit direct Firecrawl kwargs + cache key, or None when unset.
- L139 `_get_firecrawl_gateway_url()` (function) — Return the configured Firecrawl gateway URL.
- L146 `_is_tool_gateway_ready()` (function) — Return True when gateway URL + Nous Subscriber token are available.
- L162 `_has_direct_firecrawl_config()` (function) — Return True when direct Firecrawl config is explicitly configured.
- L167 `check_firecrawl_api_key()` (function) — Return True when Firecrawl backend (direct or gateway) is usable.
- L176 `_firecrawl_backend_help_suffix()` (function) — Return optional managed-gateway guidance for Firecrawl help text.
- L188 `_raise_web_backend_configuration_error()` (function) — Raise a clear error for unsupported web backend configuration.
- L209 `_get_firecrawl_client()` (function) — Get or create the cached Firecrawl client.
- L265 `_reset_client_for_tests()` (function) — Drop the cached Firecrawl client so tests can re-instantiate cleanly.
- L282 `_to_plain_object(value: Any)` (function) — Convert SDK objects to plain python data structures when possible.
- L305 `_normalize_result_list(values: Any)` (function) — Normalize mixed SDK/list payloads into a list of dicts.
- L318 `_extract_web_search_results(response: Any)` (function) — Extract Firecrawl search results across SDK/direct/gateway response shapes.
- L349 `_extract_scrape_payload(scrape_result: Any)` (function) — Normalize Firecrawl scrape payload shape across SDK and gateway variants.
- L367 `FirecrawlWebSearchProvider` (class) — Firecrawl search + extract provider with dual auth paths.
- L371 `name(self)` (method)
- L375 `display_name(self)` (method)
- L378 `is_available(self)` (method) — Return True when direct Firecrawl OR managed-gateway path is configured.
- L382 `supports_search(self)` (method)
- L385 `supports_extract(self)` (method)
- L388 `search(self, query: str, limit: int=5)` (method) — Execute a Firecrawl search.
- L420 `extract(self, urls: List[str], **kwargs: Any)` (method) — Extract content from one or more URLs via Firecrawl.
- L579 `get_setup_schema(self)` (method)
