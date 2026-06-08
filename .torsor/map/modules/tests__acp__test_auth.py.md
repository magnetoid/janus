---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_auth.py

Symbols in `tests/acp/test_auth.py`.

- L11 `TestHasProvider` (class)
- L12 `test_has_provider_with_resolved_runtime(self, monkeypatch)` (method)
- L19 `test_has_no_provider_when_runtime_has_no_key(self, monkeypatch)` (method)
- L26 `test_has_no_provider_when_runtime_resolution_fails(self, monkeypatch)` (method)
- L34 `TestDetectProvider` (class)
- L35 `test_detect_openrouter(self, monkeypatch)` (method)
- L42 `test_detect_anthropic(self, monkeypatch)` (method)
- L49 `test_detect_none_when_no_key(self, monkeypatch)` (method)
- L56 `test_detect_none_on_resolution_error(self, monkeypatch)` (method)
- L63 `test_detect_provider_strips_and_lowercases_provider(self, monkeypatch)` (method)
- L71 `TestBuildAuthMethods` (class)
- L72 `test_build_auth_methods_returns_provider_and_terminal_when_configured(self, monkeypatch)` (method)
- L85 `test_build_auth_methods_returns_terminal_setup_when_unconfigured(self, monkeypatch)` (method)
