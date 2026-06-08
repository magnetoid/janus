---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_document_cache.py

Symbols in `tests/gateway/test_document_cache.py`.

- L26 `_redirect_cache(tmp_path, monkeypatch)` (function) — Point the module-level DOCUMENT_CACHE_DIR to a fresh tmp_path.
- L37 `TestGetDocumentCacheDir` (class)
- L38 `test_creates_directory(self, tmp_path)` (method)
- L43 `test_returns_existing_directory(self)` (method)
- L54 `TestCacheDocumentFromBytes` (class)
- L55 `test_basic_caching(self)` (method)
- L61 `test_filename_preserved_in_path(self)` (method)
- L65 `test_empty_filename_uses_fallback(self)` (method)
- L69 `test_unique_filenames(self)` (method)
- L74 `test_path_traversal_blocked(self)` (method) — Malicious directory components are stripped — only the leaf name survives.
- L85 `test_null_bytes_stripped(self)` (method)
- L91 `test_dot_dot_filename_handled(self)` (method) — A filename that is literally '..' falls back to 'document'.
- L97 `test_none_filename_uses_fallback(self)` (method)
- L106 `TestCleanupDocumentCache` (class)
- L107 `test_removes_old_files(self, tmp_path)` (method)
- L119 `test_keeps_recent_files(self)` (method)
- L128 `test_returns_removed_count(self)` (method)
- L138 `test_empty_cache_dir(self)` (method)
- L146 `TestSupportedDocumentTypes` (class)
- L147 `test_all_extensions_have_mime_types(self)` (method)
- L156 `test_expected_extensions_present(self, ext)` (method)
- L171 `TestCacheMediaBytes` (class)
- L172 `test_pdf_routes_to_document(self)` (method)
- L182 `test_png_routes_to_image(self)` (method)
- L190 `test_native_photo_without_filename_uses_default_kind(self)` (method)
- L196 `test_mp4_routes_to_video(self)` (method)
- L203 `test_mime_only_resolves_extension(self)` (method)
- L210 `test_unsupported_document_returns_none(self)` (method)
- L215 `test_invalid_image_returns_none(self)` (method)
