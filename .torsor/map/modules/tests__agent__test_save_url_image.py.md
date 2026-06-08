---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_save_url_image.py

Symbols in `tests/agent/test_save_url_image.py`.

- L29 `_TinyImageHandler` (class) — Tiny HTTP server that mimics the shapes save_url_image must handle.
- L32 `do_GET(self)` (method)
- L72 `log_message(self, *args, **kw)` (method)
- L77 `http_server(tmp_path, monkeypatch)` (function) — Spin up a localhost HTTP server and isolate HERMES_HOME under tmp_path.
- L96 `TestSaveUrlImage` (class)
- L97 `test_writes_real_bytes_to_hermes_home_cache(self, http_server)` (method)
- L110 `test_extension_inferred_from_content_type(self, http_server)` (method)
- L117 `test_extension_falls_back_to_url_suffix(self, http_server)` (method) — Some CDNs send ``application/octet-stream`` — the URL suffix wins then.
- L125 `test_extension_defaults_to_png_when_unknowable(self, http_server)` (method)
- L132 `test_404_raises(self, http_server)` (method) — HTTP errors must propagate — caller decides whether to fall back.
- L141 `test_empty_body_raises_without_writing_file(self, http_server)` (method) — 0-byte responses are not images — refuse to cache.
- L149 `test_oversize_raises_and_cleans_up(self, http_server, tmp_path)` (method) — Oversize downloads must NOT leak a partial file into the cache.
- L161 `test_unique_filenames_avoid_collision(self, http_server)` (method) — Two back-to-back saves of the same URL must produce different paths.
