---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_client_xai_oauth_recovery.py

Symbols in `tests/agent/test_auxiliary_client_xai_oauth_recovery.py`.

- L16 `_import_is_auth_error()` (function)
- L21 `TestIsAuthErrorXaiOauth403` (class) — Verify _is_auth_error correctly identifies xAI's 403 bad-credentials.
- L25 `_import(self)` (method)
- L28 `test_xai_403_bad_credentials_is_auth_error(self)` (method) — The exact error xAI returns for expired OAuth tokens.
- L38 `test_xai_403_bad_credentials_without_status_code(self)` (method) — Fallback match when status_code attribute is missing.
- L46 `test_generic_403_is_not_auth_error(self)` (method) — A generic 403 (e.g. rate limit, forbidden) should NOT be treated as auth.
- L52 `test_401_status_code_is_auth_error(self)` (method) — Existing 401 detection still works.
- L58 `test_401_string_is_auth_error(self)` (method) — Existing string-based 401 detection still works.
- L63 `test_authentication_error_class_is_auth_error(self)` (method) — Existing AuthenticationError class detection still works.
- L69 `test_permission_denied_without_bad_credentials_is_not_auth_error(self)` (method) — 403 PermissionDenied without bad-credentials should not be auth.
- L75 `test_500_is_not_auth_error(self)` (method) — Server errors are not auth errors.
- L81 `test_unauthenticated_without_bad_credentials_is_not_auth_error(self)` (method) — 'unauthenticated' alone (without 'bad-credentials') should not match.
- L89 `_import_recoverable_pool_provider()` (function)
- L94 `TestRecoverablePoolProviderXaiOAuth` (class) — Verify _recoverable_pool_provider maps api.x.ai to xai-oauth.
- L98 `_import(self)` (method)
- L101 `test_explicit_xai_oauth_provider(self)` (method) — Explicit provider name passes through.
- L106 `test_api_x_ai_host_match(self)` (method) — api.x.ai base URL maps to xai-oauth pool.
- L114 `test_auto_with_unknown_host_returns_none(self)` (method) — auto provider with unknown host returns None.
- L125 `_import_refresh_provider_credentials()` (function)
- L130 `TestRefreshProviderCredentialsXaiOAuth` (class) — Verify _refresh_provider_credentials has xai-oauth branch.
- L138 `_import(self)` (method)
- L141 `test_xai_oauth_no_pool_returns_false(self)` (method) — When no xai-oauth pool exists, refresh returns False gracefully.
- L150 `test_unknown_provider_returns_false(self)` (method) — Unknown providers fall through to return False.
