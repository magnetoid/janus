---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/prompt_caching.py

Symbols in `agent/prompt_caching.py`.

- L15 `_apply_cache_marker(msg: dict, cache_marker: dict, native_anthropic: bool=False)` (function) — Add cache_control to a single message, handling all format variations.
- L41 `_build_marker(ttl: str)` (function) — Build a cache_control marker dict for the given TTL ('5m' or '1h').
- L49 `apply_anthropic_cache_control(api_messages: List[Dict[str, Any]], cache_ttl: str='5m', native_anthropic: bool=False)` (function) — Apply system_and_3 caching strategy to messages for Anthropic models.
