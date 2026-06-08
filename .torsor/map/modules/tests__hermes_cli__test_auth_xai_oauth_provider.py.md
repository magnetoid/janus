---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_xai_oauth_provider.py

Symbols in `tests/hermes_cli/test_auth_xai_oauth_provider.py`.

- L41 `_setup_hermes_auth(hermes_home: Path, *, access_token: str='access', refresh_token: str='refresh', discovery: dict | None=None)` (function) — Write xAI OAuth tokens into the Hermes auth store at the given root.
- L73 `_jwt_with_exp(exp_epoch: int)` (function) — Build a minimal JWT-shaped string with the given exp claim.
- L84 `_StubHTTPResponse` (class)
- L85 `__init__(self, status_code: int, payload)` (method)
- L90 `json(self)` (method)
- L96 `_StubHTTPClient` (class)
- L97 `__init__(self, response)` (method)
- L101 `__enter__(self)` (method)
- L104 `__exit__(self, *args)` (method)
- L107 `post(self, *args, **kwargs)` (method)
- L112 `_patch_httpx_client(monkeypatch, response)` (function)
- L129 `test_xai_oauth_provider_registered()` (function)
- L137 `test_resolve_provider_normalizes_xai_oauth_aliases()` (function)
- L149 `test_xai_access_token_is_expiring_returns_true_for_expired_jwt()` (function)
- L154 `test_xai_access_token_is_expiring_returns_false_for_fresh_jwt()` (function)
- L159 `test_xai_access_token_is_expiring_honors_skew_window()` (function)
- L165 `test_xai_access_token_is_expiring_returns_false_for_non_jwt()` (function)
- L172 `test_xai_access_token_is_expiring_returns_false_for_jwt_without_exp()` (function)
- L184 `test_xai_validate_loopback_redirect_uri_accepts_localhost_with_port()` (function)
- L193 `test_xai_validate_loopback_redirect_uri_rejects_https()` (function)
- L199 `test_xai_validate_loopback_redirect_uri_rejects_non_loopback()` (function)
- L205 `test_xai_validate_loopback_redirect_uri_rejects_missing_port()` (function)
- L216 `_parse_authorize_url(url: str)` (function)
- L223 `test_xai_oauth_authorize_url_includes_plan_generic()` (function) — Regression: accounts.x.ai requires `plan=generic` for loopback OAuth on
- L237 `test_xai_oauth_authorize_url_includes_referrer_hermes_agent()` (function) — Attribution: xAI's OAuth server can identify Hermes-originated logins
- L251 `test_xai_oauth_authorize_url_includes_pkce_and_oidc_params()` (function)
- L275 `test_xai_callback_cors_origin_allowlist()` (function)
- L280 `test_xai_callback_cors_origin_rejects_unknown_origin()` (function)
- L286 `test_xai_callback_server_accepts_fallback_code_while_browser_connection_is_stuck()` (function) — Regression: Chrome/xAI can leave a loopback connection open after
- L309 `test_xai_callback_server_latches_first_terminal_callback_result()` (function)
- L336 `_get_callback(redirect_uri: str, query: str='')` (function) — GET the loopback callback URL with an optional query string.
- L350 `test_xai_callback_handler_returns_400_when_callback_url_lacks_code_and_error()` (function) — Bare loopback URL (no code, no error) must not claim authorization received.
- L374 `test_xai_callback_handler_accepts_callback_with_code()` (function) — A real OAuth redirect (code + state) still records both and shows success.
- L390 `test_xai_callback_handler_records_error_callback()` (function) — A redirect carrying an `error` param must surface the failure page and capture detail.
- L414 `test_save_and_read_xai_oauth_tokens_roundtrip(tmp_path, monkeypatch)` (function)
- L438 `test_read_xai_oauth_tokens_missing(tmp_path, monkeypatch)` (function)
- L450 `test_read_xai_oauth_tokens_missing_access_token(tmp_path, monkeypatch)` (function)
- L461 `test_read_xai_oauth_tokens_missing_refresh_token(tmp_path, monkeypatch)` (function)
- L477 `test_resolve_xai_runtime_credentials_returns_singleton_state(tmp_path, monkeypatch)` (function)
- L493 `test_resolve_xai_runtime_credentials_refreshes_expiring_token(tmp_path, monkeypatch)` (function)
- L521 `test_resolve_xai_runtime_credentials_force_refresh(tmp_path, monkeypatch)` (function)
- L547 `test_resolve_xai_runtime_credentials_honours_env_base_url(tmp_path, monkeypatch)` (function)
- L570 `test_xai_inference_base_url_accepts_default()` (function)
- L579 `test_xai_inference_base_url_accepts_bare_apex()` (function)
- L588 `test_xai_inference_base_url_accepts_subdomain()` (function)
- L597 `test_xai_inference_base_url_strips_trailing_slash()` (function)
- L606 `test_xai_inference_base_url_empty_returns_fallback()` (function)
- L617 `test_xai_inference_base_url_rejects_off_origin_host()` (function)
- L625 `test_xai_inference_base_url_rejects_suffix_lookalike()` (function)
- L643 `test_xai_inference_base_url_rejects_http()` (function)
- L653 `test_xai_inference_base_url_rejects_other_schemes()` (function)
- L667 `test_resolve_xai_runtime_credentials_rejects_off_origin_env_base_url(tmp_path, monkeypatch, caplog)` (function)
- L705 `_seed_xai_oauth_state(hermes_home: Path, state: dict, *, active_provider: str='xai-oauth')` (function)
- L717 `test_resolve_credentials_quarantines_dead_tokens_on_terminal_refresh_failure(tmp_path, monkeypatch: pytest.MonkeyPatch)` (function) — Terminal refresh failure (relogin_required=True, code=xai_refresh_failed)
- L769 `test_resolve_credentials_does_not_quarantine_on_transient_refresh_failure(tmp_path, monkeypatch: pytest.MonkeyPatch)` (function) — Transient refresh failure (relogin_required=False, e.g. 429 / 5xx) must
- L808 `test_get_xai_oauth_auth_status_logged_in_via_singleton(tmp_path, monkeypatch)` (function)
- L820 `test_get_xai_oauth_auth_status_logged_out(tmp_path, monkeypatch)` (function)
- L836 `test_refresh_xai_oauth_pure_requires_refresh_token()` (function)
- L843 `test_refresh_xai_oauth_pure_relogin_on_400(monkeypatch)` (function)
- L854 `test_refresh_xai_oauth_pure_no_relogin_on_500(monkeypatch)` (function)
- L865 `test_refresh_xai_oauth_pure_403_marked_tier_denied_not_relogin(monkeypatch)` (function) — 403 from xAI's token endpoint is tier/entitlement, not stale tokens.
- L889 `test_format_auth_error_tier_denied_does_not_suggest_relogin()` (function) — ``xai_oauth_tier_denied`` must not append the re-authenticate hint.
- L912 `test_refresh_xai_oauth_pure_returns_updated_tokens(monkeypatch)` (function)
- L942 `test_refresh_xai_oauth_pure_keeps_refresh_token_when_response_omits_it(monkeypatch)` (function) — Some OAuth providers don't rotate refresh tokens — preserve the old one.
- L962 `test_refresh_xai_oauth_pure_rejects_response_without_access_token(monkeypatch)` (function)
- L976 `test_refresh_xai_oauth_pure_raises_typed_error_on_malformed_json(monkeypatch)` (function) — xAI returning HTTP 200 with a non-JSON body (captive portal, proxy
- L991 `test_xai_oauth_discovery_raises_typed_error_on_malformed_json(monkeypatch)` (function) — Discovery is a cold-start, one-time fetch.  If the response is HTTP
- L1014 `test_xai_oauth_discovery_raises_typed_error_on_non_object_payload(monkeypatch)` (function) — A discovery body that decodes as JSON but isn't an object (e.g. a
- L1041 `test_refresh_xai_oauth_pure_rejects_non_https_token_endpoint(monkeypatch)` (function) — A poisoned auth.json (from MITM during initial discovery, or an older
- L1054 `test_refresh_xai_oauth_pure_rejects_off_origin_token_endpoint(monkeypatch)` (function) — Pin the cached token_endpoint host to the xAI origin. A one-time MITM
- L1067 `test_refresh_xai_oauth_pure_rejects_lookalike_suffix(monkeypatch)` (function) — Substring confusion: ``evil-x.ai`` ends in ``x.ai`` but is NOT a
- L1078 `test_refresh_xai_oauth_pure_accepts_apex_and_subdomain_endpoints(monkeypatch)` (function) — The validator must accept BOTH the bare xAI apex (``x.ai``) and any
- L1102 `test_xai_oauth_discovery_validates_endpoints(monkeypatch)` (function) — The discovery response itself goes through endpoint validation, so a
- L1131 `test_xai_oauth_discovery_validates_authorization_endpoint(monkeypatch)` (function) — A poisoned ``authorization_endpoint`` is just as dangerous as a
- L1168 `test_credential_pool_seeds_xai_oauth_from_singleton(tmp_path, monkeypatch)` (function) — After `hermes model` -> xai-oauth, the singleton holds tokens.  load_pool
- L1190 `test_credential_pool_does_not_seed_when_singleton_missing_access_token(tmp_path, monkeypatch)` (function)
- L1211 `test_credential_pool_seed_respects_suppression(tmp_path, monkeypatch)` (function) — `hermes auth remove xai-oauth <N>` for the seeded entry suppresses
- L1230 `test_auth_remove_xai_oauth_clears_singleton_and_sticks(tmp_path, monkeypatch)` (function) — End-to-end regression: ``hermes auth remove xai-oauth 1`` for a
- L1285 `test_pool_sync_back_writes_to_singleton(tmp_path, monkeypatch)` (function) — When the pool refreshes a singleton-seeded xAI entry, the new tokens
- L1333 `test_runtime_provider_uses_pool_entry_for_xai_oauth(tmp_path, monkeypatch)` (function)
- L1350 `test_runtime_provider_default_base_url_when_pool_entry_missing_url(tmp_path, monkeypatch)` (function) — Edge case: a pool entry that somehow has an empty base_url should still
- L1393 `test_pool_entry_needs_refresh_when_jwt_within_skew(tmp_path, monkeypatch)` (function) — The pool's proactive-refresh gate must trigger when the JWT exp claim
- L1426 `test_pool_entry_no_refresh_for_fresh_jwt(tmp_path, monkeypatch)` (function) — A fresh JWT beyond the skew window must NOT trigger proactive refresh.
- L1453 `test_pool_select_proactively_refreshes_expiring_token(tmp_path, monkeypatch)` (function) — End-to-end: pool.select() with refresh=True on an expiring entry must
- L1506 `test_pool_try_refresh_current_handles_xai_oauth(tmp_path, monkeypatch)` (function) — The reactive 401-recovery path uses pool.try_refresh_current().  This
- L1559 `test_pool_refresh_marks_entry_exhausted_on_failure(tmp_path, monkeypatch)` (function) — When the xAI refresh endpoint rejects the refresh_token (e.g. consumed
- L1601 `test_pool_seeded_entry_sync_back_after_refresh(tmp_path, monkeypatch)` (function) — When an entry seeded from the singleton (source='loopback_pkce')
- L1638 `test_pool_refresh_adopts_singleton_tokens_when_consumed_elsewhere(tmp_path, monkeypatch)` (function) — Multi-process race: another Hermes process refreshed the singleton
- L1696 `test_pool_refresh_recovers_when_other_process_already_refreshed(tmp_path, monkeypatch)` (function) — Variant of the multi-process race where the other process refreshes
- L1743 `test_pool_exhausted_xai_entry_recovers_after_singleton_refresh(tmp_path, monkeypatch)` (function) — When a singleton-seeded entry is parked as STATUS_EXHAUSTED and the
- L1797 `test_pool_manual_xai_entry_not_synced_from_singleton(tmp_path, monkeypatch)` (function) — Sync from the singleton must apply ONLY to the singleton-seeded
- L1835 `test_pool_manual_entry_does_not_sync_back_to_singleton(tmp_path, monkeypatch)` (function) — `hermes auth add xai-oauth` entries (source='manual:xai_pkce') are
- L1896 `test_auxiliary_client_routes_xai_oauth_through_responses_api(tmp_path, monkeypatch)` (function) — Without explicit xai-oauth handling in ``resolve_provider_client``, an
- L1934 `test_auxiliary_client_xai_oauth_returns_none_when_unauthenticated(tmp_path, monkeypatch)` (function) — No xAI OAuth tokens in the auth store → ``resolve_provider_client``
- L1951 `test_auxiliary_client_xai_oauth_requires_explicit_model(tmp_path, monkeypatch)` (function) — xAI's Responses API has no safe "cheap aux model" default —
- L1972 `test_pool_sync_back_preserves_active_provider(tmp_path, monkeypatch)` (function) — A token-rotation sync-back is a side effect of refresh, not the user
