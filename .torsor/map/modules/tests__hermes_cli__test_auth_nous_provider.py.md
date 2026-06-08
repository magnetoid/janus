---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_nous_provider.py

Symbols in `tests/hermes_cli/test_auth_nous_provider.py`.

- L21 `TestResolveVerifyFallback` (class) — Verify _resolve_verify falls back to True when CA bundle path doesn't exist.
- L25 `_pin_platform_to_linux(self, monkeypatch)` (method) — Pin sys.platform so the macOS certifi fallback doesn't alter the
- L30 `test_missing_ca_bundle_in_auth_state_falls_back(self)` (method)
- L38 `test_valid_ca_bundle_in_auth_state_is_returned(self, tmp_path, monkeypatch)` (method)
- L56 `test_missing_ssl_cert_file_env_falls_back(self, monkeypatch)` (method)
- L64 `test_missing_hermes_ca_bundle_env_falls_back(self, monkeypatch)` (method)
- L72 `test_insecure_takes_precedence_over_missing_ca(self)` (method)
- L81 `test_string_false_in_auth_state_does_not_disable_tls_verify(self)` (method)
- L89 `test_string_true_in_auth_state_disables_tls_verify(self)` (method)
- L95 `test_no_ca_bundle_returns_true(self, monkeypatch)` (method)
- L103 `test_explicit_ca_bundle_param_missing_falls_back(self)` (method)
- L109 `test_explicit_ca_bundle_param_valid_is_returned(self, tmp_path, monkeypatch)` (method)
- L126 `_setup_nous_auth(hermes_home: Path, *, access_token: str='', refresh_token: str='refresh-old', scope: str='inference:invoke', expires_at: str='2026-02-01T00:00:00+00:00', expires_in: int=0, agent_key: str | None=None, agent_key_expires_at: str | None=None)` (function)
- L166 `_jwt_with_claims(claims: dict)` (function)
- L174 `_future_iso(seconds: int=3600)` (function)
- L178 `_invoke_jwt(*, seconds: int=3600, scope: object='inference:invoke')` (function)
- L186 `test_resolve_nous_runtime_credentials_prefers_invoke_jwt_and_mirrors(tmp_path, monkeypatch)` (function)
- L220 `test_resolve_nous_runtime_credentials_invoke_jwt_is_idempotent(tmp_path, monkeypatch)` (function)
- L293 `test_resolve_nous_runtime_credentials_trusts_invoke_jwt_exp_over_stale_metadata(tmp_path, monkeypatch)` (function)
- L328 `test_resolve_nous_runtime_credentials_does_not_apply_agent_key_ttl_to_invoke_jwt(tmp_path, monkeypatch)` (function)
- L354 `test_resolve_nous_runtime_credentials_refreshes_legacy_agent_key_to_invoke_jwt(tmp_path, monkeypatch)` (function)
- L403 `test_resolve_nous_runtime_credentials_reauths_when_invoke_scope_missing(tmp_path, monkeypatch)` (function)
- L435 `test_nous_device_code_login_does_not_retry_legacy_scope_when_invoke_refused(monkeypatch)` (function)
- L467 `test_removed_legacy_session_env_var_does_not_change_jwt_auth(tmp_path, monkeypatch)` (function)
- L526 `test_nous_inference_auth_logs_do_not_include_secret_values(tmp_path, monkeypatch, caplog)` (function)
- L571 `test_get_nous_auth_status_checks_credential_pool(tmp_path, monkeypatch)` (function) — get_nous_auth_status() should find Nous credentials in the pool
- L612 `test_get_nous_auth_status_pool_opaque_key_is_not_inference_credential(tmp_path, monkeypatch)` (function)
- L648 `test_get_nous_auth_status_auth_store_fallback(tmp_path, monkeypatch)` (function) — get_nous_auth_status() falls back to auth store when credential
- L672 `test_get_nous_auth_status_prefers_runtime_auth_store_over_stale_pool(tmp_path, monkeypatch)` (function)
- L714 `test_get_nous_auth_status_reports_revoked_refresh_session(tmp_path, monkeypatch)` (function)
- L733 `test_get_nous_auth_status_empty_returns_not_logged_in(tmp_path, monkeypatch)` (function) — get_nous_auth_status() returns logged_in=False when both pool
- L750 `test_refresh_token_persisted_when_refreshed_jwt_lacks_invoke_scope(tmp_path, monkeypatch)` (function)
- L797 `test_refresh_token_persisted_when_refreshed_token_is_not_jwt(tmp_path, monkeypatch)` (function)
- L826 `test_terminal_refresh_failure_quarantines_tokens(tmp_path, monkeypatch, shared_store_env)` (function) — A revoked/invalid Nous refresh token must not be replayed forever.
- L881 `test_managed_access_token_refresh_failure_quarantines_tokens(tmp_path, monkeypatch, shared_store_env)` (function)
- L923 `test_unusable_access_token_refresh_uses_latest_rotated_refresh_token(tmp_path, monkeypatch)` (function)
- L961 `TestLoginNousSkipKeepsCurrent` (class) — When a user runs `hermes model` → Nous Portal → Skip (keep current) after
- L971 `_setup_home_with_openrouter(self, tmp_path, monkeypatch)` (method)
- L993 `_patch_login_internals(self, monkeypatch, *, prompt_returns)` (method) — Patch OAuth + model-list + prompt so _login_nous doesn't hit network.
- L1030 `test_skip_keep_current_preserves_provider_and_model(self, tmp_path, monkeypatch)` (method) — User picks Skip → config.yaml untouched, Nous creds still saved.
- L1061 `test_picking_model_switches_to_nous(self, tmp_path, monkeypatch)` (method) — User picks a Nous model → provider flips to nous with that model.
- L1088 `test_skip_with_no_prior_active_provider_clears_it(self, tmp_path, monkeypatch)` (method) — Fresh install (no prior active_provider) → Skip clears active_provider
- L1124 `_full_state_fixture()` (function) — Shape of the dict returned by _nous_device_code_login /
- L1150 `test_persist_nous_credentials_writes_both_pool_and_providers(tmp_path, monkeypatch)` (function) — Helper must populate BOTH credential_pool.nous AND providers.nous.
- L1194 `test_persist_nous_credentials_allows_recovery_from_401(tmp_path, monkeypatch)` (function) — End-to-end: after persisting via the helper, resolve_nous_runtime_credentials
- L1237 `test_persist_nous_credentials_idempotent_no_duplicate_pool_entries(tmp_path, monkeypatch)` (function) — Re-running persist must upsert — not accumulate duplicate device_code rows.
- L1283 `test_persist_nous_credentials_reloads_pool_after_singleton_write(tmp_path, monkeypatch)` (function) — The entry returned by the helper must come from a fresh ``load_pool`` so
- L1307 `test_persist_nous_credentials_embeds_custom_label(tmp_path, monkeypatch)` (function) — User-supplied ``--label`` round-trips through providers.nous and the pool.
- L1335 `test_persist_nous_credentials_custom_label_survives_reseed(tmp_path, monkeypatch)` (function) — Reopening the pool (which re-runs _seed_from_singletons) must keep the
- L1359 `test_persist_nous_credentials_no_label_uses_auto_derived(tmp_path, monkeypatch)` (function) — When the caller doesn't pass ``label``, the auto-derived fingerprint
- L1385 `test_refresh_token_reuse_detection_surfaces_actionable_message()` (function) — Regression for #15099.
- L1429 `test_refresh_token_reuse_error_code_is_terminal()` (function) — Nous may return refresh_token_reused as the OAuth error code itself.
- L1459 `test_refresh_token_exchange_sends_refresh_token_header()` (function) — Nous refresh tokens must be sent in a header so sandbox proxies can
- L1499 `test_refresh_non_reuse_error_keeps_original_description()` (function) — Non-reuse invalid_grant errors must keep their original description untouched.
- L1541 `shared_store_env(tmp_path, monkeypatch)` (function) — Redirect HERMES_SHARED_AUTH_DIR to a tmp_path.
- L1554 `test_shared_store_seat_belt_refuses_real_home_under_pytest(monkeypatch)` (function) — Without HERMES_SHARED_AUTH_DIR override, the seat belt must trip.
- L1569 `test_shared_store_honors_env_override(tmp_path, monkeypatch)` (function) — HERMES_SHARED_AUTH_DIR must redirect the path.
- L1580 `test_shared_store_read_missing_returns_none(shared_store_env)` (function) — Missing file → ``_read_shared_nous_state()`` returns None.
- L1587 `test_shared_store_read_malformed_returns_none(shared_store_env)` (function) — Unreadable / non-JSON file → None, not an exception.
- L1598 `test_shared_store_read_missing_required_fields_returns_none(shared_store_env)` (function) — Payload without refresh_token → None (nothing worth importing).
- L1609 `test_shared_store_write_and_read_roundtrip(shared_store_env)` (function) — Write → read must preserve refresh_token + OAuth URLs.
- L1639 `test_shared_store_write_skips_when_refresh_token_missing(shared_store_env)` (function) — Write is a no-op when refresh_token is absent (nothing to share).
- L1651 `test_persist_nous_credentials_mirrors_to_shared_store(tmp_path, monkeypatch, shared_store_env)` (function) — persist_nous_credentials must populate BOTH per-profile auth.json
- L1686 `test_try_import_shared_returns_none_when_store_missing(shared_store_env)` (function) — No shared store → no rehydrate (fall through to device-code).
- L1693 `test_try_import_shared_returns_none_on_refresh_failure(shared_store_env, monkeypatch)` (function) — If the portal rejects the stored refresh_token (revoked, expired,
- L1720 `test_try_import_shared_persists_rotated_token_when_jwt_validation_fails(shared_store_env, monkeypatch)` (function) — A forced shared import refresh rotates the single-use token before validation.
- L1755 `test_try_import_shared_rehydrates_on_success(shared_store_env, monkeypatch)` (function) — Happy path: stored refresh_token is accepted, forced refresh
- L1789 `test_shared_store_survives_across_profile_switch(tmp_path, monkeypatch, shared_store_env)` (function) — End-to-end: profile A logs in → shared store populated → profile B
- L1857 `test_runtime_refresh_uses_newer_shared_token_before_local_stale_token(tmp_path, monkeypatch, shared_store_env)` (function) — A sibling profile may rotate the single-use Nous refresh token.
- L1900 `test_managed_gateway_access_token_uses_newer_shared_token(tmp_path, monkeypatch, shared_store_env)` (function) — Managed-tool token reads share the same stale-refresh-token hazard.
