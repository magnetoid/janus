---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_copilot_token_exchange.py

Symbols in `tests/hermes_cli/test_copilot_token_exchange.py`.

- L13 `_clear_jwt_cache()` (function) — Reset the module-level JWT cache before each test.
- L21 `TestExchangeCopilotToken` (class) — Tests for exchange_copilot_token().
- L24 `_mock_urlopen(self, token='tid=abc;exp=123;sku=copilot_individual', expires_at=None)` (method) — Create a mock urlopen context manager returning a token response.
- L36 `test_exchanges_token_successfully(self, mock_urlopen)` (method)
- L52 `test_caches_result(self, mock_urlopen)` (method)
- L64 `test_refreshes_expired_cache(self, mock_urlopen)` (method)
- L80 `test_raises_on_empty_token(self, mock_urlopen)` (method)
- L94 `test_raises_on_network_error(self, mock_urlopen)` (method)
- L101 `TestGetCopilotApiToken` (class) — Tests for get_copilot_api_token() — the fallback wrapper.
- L105 `test_returns_exchanged_token(self, mock_exchange)` (method)
- L112 `test_falls_back_to_raw_token(self, mock_exchange)` (method)
- L117 `test_empty_token_passthrough(self)` (method)
- L123 `TestTokenFingerprint` (class) — Tests for _token_fingerprint().
- L126 `test_consistent(self)` (method)
- L133 `test_different_tokens_different_fingerprints(self)` (method)
- L140 `test_length(self)` (method)
- L146 `TestCallerIntegration` (class) — Test that callers correctly use token exchange.
- L151 `test_auth_resolve_uses_exchange(self, mock_exchange, mock_resolve)` (method)
