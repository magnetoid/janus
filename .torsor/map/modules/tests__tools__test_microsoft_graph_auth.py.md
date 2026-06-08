---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_microsoft_graph_auth.py

Symbols in `tests/tools/test_microsoft_graph_auth.py`.

- L20 `TestGraphCredentials` (class)
- L21 `test_from_env_raises_for_missing_required_values(self)` (method)
- L28 `test_from_env_optional_returns_none_when_not_configured(self)` (method)
- L31 `test_from_env_builds_normalized_credentials(self)` (method)
- L45 `TestMicrosoftGraphTokenProvider` (class)
- L46 `test_reuses_cached_token_until_expiry(self)` (method)
- L72 `test_concurrent_calls_share_one_token_fetch(self)` (method)
- L99 `test_refreshes_when_cached_token_is_expired(self)` (method)
- L127 `test_force_refresh_bypasses_cache(self)` (method)
- L152 `test_invalid_token_response_raises(self)` (method)
- L165 `test_http_error_includes_server_message(self)` (method)
