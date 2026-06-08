---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/web/parallel/provider.py

Symbols in `plugins/web/parallel/provider.py`.

- L46 `_ensure_parallel_sdk_installed()` (function) — Trigger lazy install of the parallel SDK if it isn't present.
- L64 `_get_sync_client()` (function) — Lazy-load + cache the sync Parallel client.
- L91 `_get_async_client()` (function) — Lazy-load + cache the async Parallel client.
- L117 `_reset_clients_for_tests()` (function) — Drop both cached clients so tests can re-instantiate cleanly.
- L135 `_resolve_search_mode()` (function) — Return the validated PARALLEL_SEARCH_MODE value (default "agentic").
- L143 `ParallelWebSearchProvider` (class) — Parallel.ai search + async extract provider.
- L147 `name(self)` (method)
- L151 `display_name(self)` (method)
- L154 `is_available(self)` (method) — Return True when ``PARALLEL_API_KEY`` is set to a non-empty value.
- L158 `supports_search(self)` (method)
- L161 `supports_extract(self)` (method)
- L164 `search(self, query: str, limit: int=5)` (method) — Execute a Parallel search (sync).
- L212 `extract(self, urls: List[str], **kwargs: Any)` (method) — Extract content from one or more URLs via the async SDK.
- L279 `get_setup_schema(self)` (method)
