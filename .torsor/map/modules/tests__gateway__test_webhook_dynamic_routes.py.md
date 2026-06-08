---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_webhook_dynamic_routes.py

Symbols in `tests/gateway/test_webhook_dynamic_routes.py`.

- L14 `_make_adapter(routes=None, extra=None)` (function)
- L24 `_isolate(tmp_path, monkeypatch)` (function)
- L28 `TestDynamicRouteLoading` (class)
- L29 `test_no_dynamic_file(self)` (method)
- L35 `test_loads_dynamic_routes(self, tmp_path)` (method)
- L44 `test_static_takes_precedence(self, tmp_path)` (method)
- L52 `test_mtime_gated(self, tmp_path)` (method)
- L73 `test_file_removal_clears(self, tmp_path)` (method)
- L84 `test_corrupted_file(self, tmp_path)` (method)
- L92 `TestDynamicRouteSecretValidation` (class) — Empty/missing secrets must be rejected during hot-reload.
- L103 `test_empty_secret_rejected(self, tmp_path)` (method)
- L114 `test_missing_secret_no_global_rejected(self, tmp_path)` (method)
- L124 `test_missing_secret_inherits_global(self, tmp_path)` (method)
- L134 `test_insecure_no_auth_preserved(self, tmp_path)` (method)
- L143 `test_insecure_no_auth_rejected_on_non_loopback_bind(self, tmp_path)` (method)
- L153 `test_warning_logged_on_skip(self, tmp_path, caplog)` (method)
- L163 `test_partial_skip(self, tmp_path)` (method)
