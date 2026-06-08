---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tool_backend_helpers.py

Symbols in `tests/tools/test_tool_backend_helpers.py`.

- L33 `_raise_import()` (function)
- L40 `TestManagedNousToolsEnabled` (class) — Subscription-based gate: True for paid Nous subscribers.
- L43 `test_disabled_when_not_logged_in(self, monkeypatch)` (method)
- L50 `test_disabled_for_free_tier(self, monkeypatch)` (method)
- L62 `test_enabled_for_paid_subscriber(self, monkeypatch)` (method)
- L74 `test_force_fresh_is_forwarded(self, monkeypatch)` (method)
- L94 `test_returns_false_on_exception(self, monkeypatch)` (method) — Should never crash — returns False on any exception.
- L103 `TestNousToolGatewayUnavailableMessage` (class)
- L104 `test_uses_entitlement_reason_for_logged_in_user(self, monkeypatch)` (method)
- L135 `TestNormalizeBrowserCloudProvider` (class) — Coerce arbitrary input to a lowercase browser provider key.
- L138 `test_none_returns_default(self)` (method)
- L141 `test_empty_string_returns_default(self)` (method)
- L144 `test_whitespace_only_returns_default(self)` (method)
- L147 `test_known_provider_normalized(self)` (method)
- L150 `test_strips_whitespace(self)` (method)
- L153 `test_integer_coerced(self)` (method)
- L162 `TestCoerceModalMode` (class) — Validate and coerce the requested modal execution mode.
- L166 `test_valid_modes_passthrough(self, value)` (method)
- L169 `test_none_returns_auto(self)` (method)
- L172 `test_empty_string_returns_auto(self)` (method)
- L175 `test_whitespace_only_returns_auto(self)` (method)
- L178 `test_uppercase_normalized(self)` (method)
- L181 `test_mixed_case_normalized(self)` (method)
- L184 `test_invalid_mode_falls_back_to_auto(self)` (method)
- L188 `test_strips_whitespace(self)` (method)
- L192 `TestNormalizeModalMode` (class) — normalize_modal_mode is an alias for coerce_modal_mode.
- L195 `test_delegates_to_coerce(self)` (method)
- L204 `TestHasDirectModalCredentials` (class) — Detect Modal credentials via env vars or config file.
- L207 `test_no_env_no_file(self, monkeypatch, tmp_path)` (method)
- L213 `test_both_env_vars_set(self, monkeypatch, tmp_path)` (method)
- L219 `test_only_token_id_not_enough(self, monkeypatch, tmp_path)` (method)
- L225 `test_only_token_secret_not_enough(self, monkeypatch, tmp_path)` (method)
- L231 `test_config_file_present(self, monkeypatch, tmp_path)` (method)
- L238 `test_env_vars_take_priority_over_file(self, monkeypatch, tmp_path)` (method)
- L245 `test_home_dir_permission_denied(self, monkeypatch)` (method) — PermissionError on Path.home() should not crash (issue #33525).
- L252 `test_home_dir_permission_denied_with_env_vars(self, monkeypatch)` (method) — PermissionError on Path.home() should not prevent env var detection.
- L263 `TestPrefersGateway` (class) — Honor bool-ish config values for tool gateway routing.
- L266 `test_returns_false_for_quoted_false(self, monkeypatch)` (method)
- L273 `test_returns_true_for_quoted_true(self, monkeypatch)` (method)
- L284 `TestResolveModalBackendState` (class) — Full matrix of direct vs managed Modal backend selection.
- L288 `_resolve(monkeypatch, mode, *, has_direct, managed_ready, nous_enabled=False)` (method) — Helper to call resolve_modal_backend_state with feature flag control.
- L300 `test_auto_prefers_managed_when_available(self, monkeypatch)` (method)
- L304 `test_auto_falls_back_to_direct(self, monkeypatch)` (method)
- L308 `test_auto_no_backends_available(self, monkeypatch)` (method)
- L312 `test_auto_managed_ready_but_nous_disabled(self, monkeypatch)` (method)
- L316 `test_auto_nothing_when_only_managed_and_nous_disabled(self, monkeypatch)` (method)
- L322 `test_direct_selects_direct_when_available(self, monkeypatch)` (method)
- L326 `test_direct_none_when_no_credentials(self, monkeypatch)` (method)
- L332 `test_managed_selects_managed_when_ready_and_enabled(self, monkeypatch)` (method)
- L336 `test_managed_none_when_not_ready(self, monkeypatch)` (method)
- L340 `test_managed_blocked_when_nous_disabled(self, monkeypatch)` (method)
- L347 `test_return_dict_keys(self, monkeypatch)` (method)
- L359 `test_passthrough_flags(self, monkeypatch)` (method)
- L368 `test_invalid_mode_treated_as_auto(self, monkeypatch)` (method)
- L377 `TestResolveOpenaiAudioApiKey` (class) — Priority: VOICE_TOOLS_OPENAI_KEY > OPENAI_API_KEY.
- L380 `test_voice_key_preferred(self, monkeypatch)` (method)
- L385 `test_falls_back_to_openai_key(self, monkeypatch)` (method)
- L390 `test_empty_voice_key_falls_back(self, monkeypatch)` (method)
- L395 `test_no_keys_returns_empty(self, monkeypatch)` (method)
- L400 `test_strips_whitespace(self, monkeypatch)` (method)
