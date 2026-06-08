---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_minimax_oauth.py

Symbols in `tests/test_minimax_oauth.py`.

- L44 `_make_httpx_response(status_code: int, body: dict | None=None, text: str='')` (function) — Return a minimal mock that quacks like httpx.Response.
- L58 `_future_iso(seconds_from_now: int=3600)` (function)
- L63 `_past_iso(seconds_ago: int=3600)` (function)
- L72 `test_resolve_token_expiry_unix_ttl_seconds()` (function)
- L78 `test_resolve_token_expiry_unix_absolute_ms()` (function)
- L89 `test_pkce_pair_produces_valid_s256()` (function)
- L120 `test_request_user_code_happy_path()` (function)
- L155 `test_request_user_code_state_mismatch_raises()` (function)
- L183 `test_request_user_code_non_200_raises()` (function)
- L207 `test_poll_token_pending_then_success()` (function)
- L247 `test_poll_token_error_raises()` (function)
- L273 `test_poll_token_timeout_raises()` (function)
- L323 `test_refresh_skip_when_not_expired()` (function) — When token is far from expiry, refresh should return the same state.
- L343 `test_refresh_updates_access_token()` (function) — When token is close to expiry, refresh should update the state.
- L380 `test_refresh_updates_access_token_absolute_ms_expired_in()` (function) — Refresh payload may use unix-ms absolute ``expired_in`` (same as device-code).
- L424 `test_refresh_reuse_triggers_relogin_required()` (function) — On 400 + invalid_grant body, relogin_required should be set.
- L458 `test_resolve_credentials_requires_login()` (function) — When no state is stored, resolve_minimax_oauth_runtime_credentials raises.
- L472 `test_resolve_credentials_quarantines_dead_tokens_on_terminal_refresh_failure()` (function) — Terminal refresh failure (relogin_required + refresh_token present) must
- L540 `test_resolve_credentials_does_not_quarantine_on_transient_refresh_failure()` (function) — When refresh raises with relogin_required=False (e.g. 429 / 5xx), the
- L576 `test_provider_registry_contains_minimax_oauth()` (function)
- L591 `test_minimax_oauth_alias_resolves()` (function)
- L602 `test_get_minimax_oauth_auth_status_not_logged_in()` (function)
- L614 `test_get_minimax_oauth_auth_status_logged_in()` (function)
- L628 `test_generic_auth_status_dispatches_minimax_oauth()` (function)
- L651 `test_token_provider_returns_current_access_token_when_fresh()` (function) — When token is far from expiry, callable just returns the cached token.
- L675 `test_token_provider_refreshes_when_near_expiry()` (function) — When token is within the skew window, callable mints a fresh one.
- L712 `test_token_provider_rereads_state_each_call()` (function) — Each callable invocation re-reads auth.json so cross-process refreshes
- L745 `test_token_provider_raises_not_logged_in_when_state_missing()` (function) — No state in auth.json → AuthError(not_logged_in, relogin_required=True).
- L758 `test_token_provider_quarantines_state_on_terminal_refresh()` (function) — When refresh returns invalid_grant, callable raises AuthError AND
- L804 `test_resolve_returns_callable_when_as_token_provider_true()` (function) — Explicit opt-in path: resolve_minimax_oauth_runtime_credentials(as_token_provider=True)
- L824 `test_resolve_returns_string_by_default()` (function) — Backwards-compatible default: api_key is a string materialized once.
