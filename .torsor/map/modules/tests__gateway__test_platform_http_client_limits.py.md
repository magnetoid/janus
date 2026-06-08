---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_platform_http_client_limits.py

Symbols in `tests/gateway/test_platform_http_client_limits.py`.

- L20 `_clear_env(monkeypatch)` (function)
- L25 `test_returns_none_when_httpx_unavailable(monkeypatch)` (function) — If httpx can't be imported, the helper returns None so callers
- L33 `test_default_limits_tighten_keepalive_below_httpx_default()` (function)
- L48 `test_env_override_keepalive_expiry(monkeypatch)` (function)
- L55 `test_env_override_max_keepalive(monkeypatch)` (function)
- L62 `test_env_override_rejects_garbage(monkeypatch)` (function) — Malformed env values fall back to defaults rather than raising.
- L74 `test_helper_is_importable_from_every_platform_that_uses_it()` (function) — Every persistent-httpx-client platform adapter imports this helper.
- L87 `TestWhatsappTypingLeakFix` (class) — #18451 — whatsapp.send_typing previously used a bare
- L99 `test_bare_await_removed(self)` (method)
