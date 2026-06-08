---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_model_metadata_ssl.py

Symbols in `tests/agent/test_model_metadata_ssl.py`.

- L27 `clean_env(monkeypatch)` (function) — Clear all three SSL env vars so each test starts from a known state.
- L35 `bundle_file(tmp_path: Path)` (function) — Create a placeholder CA bundle file and return its absolute path.
- L42 `TestResolveRequestsVerify` (class)
- L43 `test_no_env_returns_true(self, clean_env)` (method)
- L46 `test_hermes_ca_bundle_returns_path(self, clean_env, bundle_file)` (method)
- L50 `test_requests_ca_bundle_returns_path(self, clean_env, bundle_file)` (method)
- L54 `test_ssl_cert_file_returns_path(self, clean_env, bundle_file)` (method)
- L58 `test_priority_hermes_over_requests(self, clean_env, tmp_path, bundle_file)` (method)
- L65 `test_priority_requests_over_ssl_cert_file(self, clean_env, tmp_path, bundle_file)` (method)
- L72 `test_nonexistent_path_falls_through(self, clean_env, tmp_path, bundle_file)` (method)
- L78 `test_all_nonexistent_returns_true(self, clean_env, tmp_path)` (method)
- L87 `test_empty_string_env_var_ignored(self, clean_env, bundle_file)` (method)
