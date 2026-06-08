---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_sticker_cache.py

Symbols in `tests/gateway/test_sticker_cache.py`.

- L15 `TestLoadSaveCache` (class)
- L16 `test_load_missing_file(self, tmp_path)` (method)
- L20 `test_load_corrupt_file(self, tmp_path)` (method)
- L26 `test_save_and_load_roundtrip(self, tmp_path)` (method)
- L34 `test_save_creates_parent_dirs(self, tmp_path)` (method)
- L41 `TestCacheSticker` (class)
- L42 `test_cache_and_retrieve(self, tmp_path)` (method)
- L54 `test_missing_sticker_returns_none(self, tmp_path)` (method)
- L60 `test_overwrite_existing(self, tmp_path)` (method)
- L69 `test_multiple_stickers(self, tmp_path)` (method)
- L81 `TestBuildStickerInjection` (class)
- L82 `test_exact_format_no_context(self)` (method)
- L86 `test_exact_format_emoji_only(self)` (method)
- L90 `test_exact_format_emoji_and_set_name(self)` (method)
- L94 `test_set_name_without_emoji_ignored(self)` (method) — set_name alone (no emoji) produces no context — only emoji+set_name triggers 'from' clause.
- L100 `test_description_with_quotes(self)` (method)
- L105 `test_empty_description(self)` (method)
- L110 `TestBuildAnimatedStickerInjection` (class)
- L111 `test_exact_format_with_emoji(self)` (method)
- L118 `test_exact_format_without_emoji(self)` (method)
- L122 `test_empty_emoji_same_as_no_emoji(self)` (method)
