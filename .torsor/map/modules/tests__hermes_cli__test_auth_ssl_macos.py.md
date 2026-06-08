---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_ssl_macos.py

Symbols in `tests/hermes_cli/test_auth_ssl_macos.py`.

- L28 `real_bundle_file(tmp_path: Path)` (function) — Return a path to a real openssl-generated self-signed cert.
- L53 `TestDefaultVerify` (class)
- L54 `test_returns_ssl_context_on_darwin(self, monkeypatch)` (method)
- L59 `test_returns_true_on_linux(self, monkeypatch)` (method)
- L63 `test_returns_true_on_windows(self, monkeypatch)` (method)
- L67 `test_darwin_falls_back_to_true_when_certifi_missing(self, monkeypatch)` (method)
- L81 `TestResolveVerifyIntegration` (class) — _resolve_verify should defer to _default_verify in the no-CA path.
- L84 `test_no_ca_uses_default_verify_on_darwin(self, monkeypatch)` (method)
- L91 `test_no_ca_uses_default_verify_on_linux(self, monkeypatch)` (method)
- L97 `test_requests_ca_bundle_respected(self, monkeypatch, real_bundle_file)` (method)
- L104 `test_missing_ca_path_falls_back_to_default_verify(self, monkeypatch, tmp_path)` (method)
- L111 `test_insecure_wins_over_everything(self, monkeypatch, tmp_path)` (method)
