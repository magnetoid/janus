---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/sticker_cache.py

Symbols in `gateway/sticker_cache.py`.

- L29 `_load_cache()` (function) — Load the sticker cache from disk.
- L39 `_save_cache(cache: dict)` (function) — Save the sticker cache to disk atomically.
- L59 `get_cached_description(file_unique_id: str)` (function) — Look up a cached sticker description.
- L70 `cache_sticker_description(file_unique_id: str, description: str, emoji: str='', set_name: str='')` (function) — Store a sticker description in the cache.
- L95 `build_sticker_injection(description: str, emoji: str='', set_name: str='')` (function) — Build the warm-style injection text for a sticker description.
- L115 `build_animated_sticker_injection(emoji: str='')` (function) — Build injection text for animated/video stickers we can't analyze.
