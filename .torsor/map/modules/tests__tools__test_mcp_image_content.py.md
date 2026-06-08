---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_image_content.py

Symbols in `tests/tools/test_mcp_image_content.py`.

- L24 `_png_bytes()` (function) — Return a minimal valid PNG byte sequence.
- L37 `TestMimeExtension` (class)
- L38 `test_maps_jpeg_variants_to_jpg(self)` (method)
- L45 `test_png_falls_through_to_mimetypes(self)` (method)
- L49 `test_unknown_defaults_to_png(self)` (method)
- L55 `TestCacheMcpImageBlock` (class)
- L56 `test_returns_media_tag_for_valid_image_block(self, tmp_path, monkeypatch)` (method) — A well-formed ImageContent block with valid PNG bytes caches
- L80 `test_returns_empty_when_block_is_not_an_image(self, tmp_path, monkeypatch)` (method) — Non-image MIME types shouldn't trigger caching.
- L91 `test_returns_empty_when_block_has_no_data(self, tmp_path, monkeypatch)` (method)
- L98 `test_returns_empty_on_malformed_base64(self, tmp_path, monkeypatch)` (method) — A server that sends garbage base64 shouldn't crash the handler —
- L110 `test_returns_empty_when_bytes_dont_look_like_an_image(self, tmp_path, monkeypatch)` (method) — ``cache_image_from_bytes`` has a format sniff; if the claimed
- L123 `test_handles_jpeg(self, tmp_path, monkeypatch)` (method) — JPEG signature should also be accepted.
