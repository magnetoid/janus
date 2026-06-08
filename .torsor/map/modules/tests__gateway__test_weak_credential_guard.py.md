---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_weak_credential_guard.py

Symbols in `tests/gateway/test_weak_credential_guard.py`.

- L20 `_make_gateway_config(platform, token, enabled=True, **extra_kwargs)` (function) — Create a minimal GatewayConfig-like object for validation testing.
- L30 `_validate_and_return(config)` (function) — Call _validate_gateway_config and return the config (mutated in place).
- L41 `TestPlatformTokenPlaceholderGuard` (class) — Verify that _validate_gateway_config disables platforms with placeholder tokens.
- L44 `test_rejects_triple_asterisk(self, caplog)` (method) — '***' is the .env.example placeholder — should be rejected.
- L52 `test_rejects_changeme(self, caplog)` (method)
- L58 `test_rejects_your_api_key(self, caplog)` (method)
- L64 `test_rejects_placeholder(self, caplog)` (method)
- L70 `test_accepts_real_token(self, caplog)` (method) — A real-looking bot token should pass validation.
- L80 `test_accepts_empty_token_without_error(self, caplog)` (method) — Empty tokens get a warning (existing behavior), not a placeholder error.
- L89 `test_disabled_platform_not_checked(self, caplog)` (method) — Disabled platforms should not be validated.
- L96 `test_rejects_whitespace_padded_placeholder(self, caplog)` (method) — Whitespace-padded placeholders should still be caught.
- L109 `TestAPIServerPlaceholderKeyGuard` (class) — Verify that the API server rejects placeholder keys on network hosts.
- L113 `test_refuses_wildcard_with_placeholder_key(self)` (method)
- L123 `test_refuses_wildcard_with_asterisk_key(self)` (method)
- L132 `test_allows_loopback_with_placeholder_key(self)` (method) — Loopback with a placeholder key is fine — not network-exposed.
