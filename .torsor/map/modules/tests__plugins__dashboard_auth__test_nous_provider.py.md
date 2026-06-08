---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/dashboard_auth/test_nous_provider.py

Symbols in `tests/plugins/dashboard_auth/test_nous_provider.py`.

- L50 `rsa_keypair()` (function) — Generate an RS256 keypair + matching JWK for verify_session tests.
- L82 `_mint_token(rsa_keypair: Dict[str, Any], *, iss: str='https://portal.example.com', aud: str='agent:inst123', sub: str='usr_abc', agent_instance_id: str | None='inst123', oauth_contract_version: Any=1, org_id: str | None='org_xyz', scope: str='agent_dashboard:access', ttl_seconds: int=900, extra_claims: Dict[str, Any] | None=None)` (function)
- L120 `_patched_jwks(provider: nous_plugin.NousDashboardAuthProvider, rsa_keypair)` (function) — Patch the provider's JWKS client to return our fixture key.
- L136 `TestConstruction` (class)
- L137 `test_protocol_compliance(self)` (method)
- L140 `test_name_and_display(self)` (method)
- L147 `test_extracts_agent_instance_id(self)` (method)
- L153 `test_strips_trailing_slash_from_portal_url(self)` (method)
- L159 `test_rejects_malformed_client_id(self)` (method)
- L171 `TestPluginRegister` (class)
- L172 `test_skips_when_client_id_missing(self, monkeypatch)` (method)
- L181 `test_registers_with_default_portal_url_when_only_client_id_set(self, monkeypatch)` (method) — Phase 7 follow-up: HERMES_DASHBOARD_PORTAL_URL is optional —
- L198 `test_skips_when_client_id_malformed(self, monkeypatch)` (method)
- L208 `test_registers_with_explicit_portal_url(self, monkeypatch)` (method)
- L218 `test_strips_whitespace_from_env_vars(self, monkeypatch)` (method)
- L225 `test_empty_portal_url_env_uses_default(self, monkeypatch)` (method) — Explicit empty string still falls back to the production
- L242 `TestConfigYamlSource` (class) — ``dashboard.oauth.{client_id,portal_url}`` in ``config.yaml`` is the
- L257 `patch_config(self, monkeypatch)` (method) — Yield a callable that replaces ``hermes_cli.config.load_config``
- L272 `test_config_yaml_only_client_id_registers(self, patch_config, monkeypatch)` (method) — No env var, only config.yaml — plugin reads from config and
- L288 `test_config_yaml_client_id_and_portal_url(self, patch_config, monkeypatch)` (method)
- L301 `test_env_overrides_config_client_id(self, patch_config, monkeypatch)` (method) — Env wins. Critical for Fly.io: the Portal injects
- L315 `test_env_overrides_config_portal_url(self, patch_config, monkeypatch)` (method)
- L329 `test_empty_env_string_does_not_shadow_config(self, patch_config, monkeypatch)` (method) — ``HERMES_DASHBOARD_OAUTH_CLIENT_ID=`` (set but empty) is
- L344 `test_neither_source_skips_with_helpful_reason(self, patch_config, monkeypatch)` (method) — Neither env nor config.yaml set — skip with a reason that
- L364 `test_config_yaml_load_failure_falls_through_cleanly(self, monkeypatch)` (method) — If load_config() raises (e.g. malformed YAML, IOError), the
- L384 `test_config_yaml_with_non_dict_oauth_section(self, monkeypatch)` (method) — cfg_get handles 'config has a string where a section was
- L406 `TestStartLogin` (class)
- L408 `provider(self)` (method)
- L413 `test_returns_login_start(self, provider)` (method)
- L419 `test_redirect_url_targets_portal_authorize(self, provider)` (method)
- L427 `test_authorize_url_has_required_params(self, provider)` (method)
- L441 `test_code_verifier_in_cookie_payload_43_to_128_chars(self, provider)` (method)
- L454 `test_state_in_cookie_payload_matches_url_param(self, provider)` (method)
- L464 `test_code_challenge_is_s256_of_verifier(self, provider)` (method)
- L482 `test_two_calls_produce_different_state_and_verifier(self, provider)` (method)
- L493 `test_rejects_non_http_scheme(self, provider)` (method)
- L497 `test_allows_http_with_arbitrary_host(self, provider)` (method)
- L507 `test_allows_http_localhost(self, provider)` (method)
- L512 `test_rejects_wrong_callback_path(self, provider)` (method)
- L522 `TestCompleteLogin` (class)
- L524 `provider(self, rsa_keypair)` (method)
- L531 `_mock_post(self, status_code: int, body: Any, *, ctype: str='application/json')` (method)
- L546 `test_happy_path_returns_session(self, provider, rsa_keypair)` (method)
- L574 `test_happy_path_tolerates_missing_refresh_token(self, provider, rsa_keypair)` (method)
- L590 `test_400_raises_invalid_code(self, provider)` (method)
- L599 `test_500_raises_provider_error(self, provider)` (method)
- L609 `test_missing_access_token_raises(self, provider)` (method)
- L618 `test_unexpected_token_type_raises(self, provider, rsa_keypair)` (method)
- L630 `test_network_error_raises_provider_error(self, provider)` (method)
- L641 `test_captures_refresh_token_if_present_forward_compat(self, provider, rsa_keypair)` (method) — Forward-compat: contract V1 doesn't issue, but if a future Portal
- L668 `TestVerifySession` (class)
- L670 `provider(self, rsa_keypair)` (method)
- L677 `test_happy_path_returns_session(self, provider, rsa_keypair)` (method)
- L684 `test_expired_token_returns_none(self, provider, rsa_keypair)` (method)
- L688 `test_wrong_audience_raises_provider_error(self, provider, rsa_keypair)` (method)
- L693 `test_wrong_issuer_raises_provider_error(self, provider, rsa_keypair)` (method)
- L698 `test_verification_failure_message_surfaces_token_claims(self, provider, rsa_keypair)` (method) — Operators need to see the actual iss/aud the token carries to debug
- L711 `test_missing_sub_raises(self, provider, rsa_keypair)` (method)
- L720 `test_agent_instance_id_mismatch_rejected(self, provider, rsa_keypair)` (method)
- L725 `test_agent_instance_id_missing_is_tolerated(self, provider, rsa_keypair)` (method)
- L730 `test_contract_version_missing_warns_but_succeeds(self, provider, rsa_keypair, caplog)` (method)
- L742 `test_contract_version_mismatch_rejected(self, provider, rsa_keypair)` (method)
- L747 `test_jwks_unreachable_raises_provider_error(self, provider, rsa_keypair)` (method)
- L764 `TestRefreshAndRevoke` (class)
- L766 `provider(self, rsa_keypair)` (method)
- L773 `_mock_post(self, status_code, body, *, ctype='application/json')` (method)
- L785 `test_refresh_happy_path_returns_rotated_session(self, provider, rsa_keypair)` (method)
- L817 `test_refresh_400_raises_refresh_expired(self, provider)` (method)
- L824 `test_refresh_empty_token_raises_refresh_expired_without_network(self, provider)` (method)
- L831 `test_refresh_network_error_raises_provider_error(self, provider)` (method)
- L839 `test_refresh_500_raises_provider_error(self, provider)` (method)
- L845 `test_revoke_is_noop(self, provider)` (method)
