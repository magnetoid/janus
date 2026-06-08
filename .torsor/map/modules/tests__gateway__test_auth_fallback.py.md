---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_auth_fallback.py

Symbols in `tests/gateway/test_auth_fallback.py`.

- L8 `TestResolveRuntimeAgentKwargsAuthFallback` (class) — _resolve_runtime_agent_kwargs should try fallback on AuthError.
- L11 `test_auth_error_tries_fallback(self, tmp_path, monkeypatch)` (method) — When primary provider raises AuthError, fallback is attempted.
- L57 `test_auth_error_no_fallback_raises(self, tmp_path, monkeypatch)` (method) — When primary fails and no fallback configured, RuntimeError is raised.
- L74 `test_legacy_fallback_is_appended_after_fallback_providers(self, tmp_path, monkeypatch)` (method) — When both keys exist, the legacy entry still participates in resolution.
