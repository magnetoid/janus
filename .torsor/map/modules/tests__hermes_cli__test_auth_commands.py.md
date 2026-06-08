---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_commands.py

Symbols in `tests/hermes_cli/test_auth_commands.py`.

- L14 `_write_auth_store(tmp_path, payload: dict)` (function)
- L20 `_jwt_with_email(email: str)` (function)
- L29 `_clear_provider_env(monkeypatch)` (function)
- L40 `test_auth_add_api_key_persists_manual_entry(tmp_path, monkeypatch)` (function)
- L65 `test_auth_add_anthropic_oauth_persists_pool_entry(tmp_path, monkeypatch)` (function)
- L100 `test_auth_add_google_gemini_cli_sets_active_provider(tmp_path, monkeypatch)` (function) — hermes auth add google-gemini-cli must set active_provider in auth.json.
- L145 `test_auth_add_qwen_oauth_sets_active_provider(tmp_path, monkeypatch)` (function) — hermes auth add qwen-oauth must set active_provider in auth.json.
- L194 `test_auth_add_nous_oauth_persists_pool_entry(tmp_path, monkeypatch)` (function)
- L267 `test_auth_add_minimax_oauth_starts_login_and_persists_pool_entry(tmp_path, monkeypatch)` (function)
- L311 `test_auth_add_nous_oauth_honors_custom_label(tmp_path, monkeypatch)` (function) — `hermes auth add nous --type oauth --label <name>` must preserve the
- L372 `test_auth_add_codex_oauth_persists_pool_entry(tmp_path, monkeypatch)` (function)
- L409 `test_auth_add_xai_oauth_sets_active_provider(tmp_path, monkeypatch)` (function) — hermes auth add xai-oauth must write providers singleton and set active_provider.
- L461 `test_auth_remove_reindexes_priorities(tmp_path, monkeypatch)` (function)
- L513 `test_auth_remove_accepts_label_target(tmp_path, monkeypatch)` (function)
- L560 `test_auth_remove_prefers_exact_numeric_label_over_index(tmp_path, monkeypatch)` (function)
- L614 `test_auth_reset_clears_provider_statuses(tmp_path, monkeypatch, capsys)` (function)
- L655 `test_clear_provider_auth_removes_provider_pool_entries(tmp_path, monkeypatch)` (function)
- L701 `test_logout_resets_codex_config_when_auth_state_already_cleared(tmp_path, monkeypatch, capsys)` (function) — `hermes logout --provider openai-codex` must still clear model.provider.
- L730 `test_logout_defaults_to_configured_codex_when_no_active_provider(tmp_path, monkeypatch, capsys)` (function) — Bare `hermes logout` should target configured Codex if auth has no active provider.
- L753 `test_logout_clears_stale_active_codex_without_provider_credentials(tmp_path, monkeypatch, capsys)` (function) — Logout must clear active_provider even when provider credential payloads are gone.
- L786 `test_reset_config_provider_uses_atomic_yaml_write(tmp_path, monkeypatch)` (function) — Logout config reset should delegate the YAML write atomically.
- L819 `test_auth_list_does_not_call_mutating_select(monkeypatch, capsys)` (function)
- L856 `test_auth_list_shows_exhausted_cooldown(monkeypatch, capsys)` (function)
- L888 `test_auth_list_shows_auth_failure_when_exhausted_entry_is_unauthorized(monkeypatch, capsys)` (function)
- L923 `test_auth_list_prefers_explicit_reset_time(monkeypatch, capsys)` (function)
- L961 `test_auth_remove_env_seeded_clears_env_var(tmp_path, monkeypatch)` (function) — Removing an env-seeded credential should also clear the env var from .env
- L1012 `test_auth_remove_env_seeded_does_not_resurrect(tmp_path, monkeypatch)` (function) — After removing an env-seeded credential, load_pool should NOT re-create it.
- L1056 `test_auth_remove_manual_entry_does_not_touch_env(tmp_path, monkeypatch)` (function) — Removing a manually-added credential should NOT touch .env.
- L1097 `test_auth_remove_claude_code_suppresses_reseed(tmp_path, monkeypatch)` (function) — Removing a claude_code credential must prevent it from being re-seeded.
- L1135 `test_unsuppress_credential_source_clears_marker(tmp_path, monkeypatch)` (function) — unsuppress_credential_source() removes a previously-set marker.
- L1154 `test_unsuppress_credential_source_returns_false_when_absent(tmp_path, monkeypatch)` (function) — unsuppress_credential_source() returns False if no marker exists.
- L1165 `test_unsuppress_credential_source_preserves_other_markers(tmp_path, monkeypatch)` (function) — Clearing one marker must not affect unrelated markers.
- L1183 `test_auth_remove_codex_device_code_suppresses_reseed(tmp_path, monkeypatch)` (function) — Removing an auto-seeded openai-codex credential must mark the source as suppressed.
- L1230 `test_auth_remove_codex_manual_source_suppresses_reseed(tmp_path, monkeypatch)` (function) — Removing a manually-added (`manual:device_code`) openai-codex credential must also suppress.
- L1277 `test_auth_add_codex_clears_suppression_marker(tmp_path, monkeypatch)` (function) — Re-linking codex via `hermes auth add openai-codex` must clear any suppression marker.
- L1322 `test_seed_from_singletons_respects_codex_suppression(tmp_path, monkeypatch)` (function) — _seed_from_singletons() for openai-codex must skip auto-import when suppressed.
- L1360 `test_auth_remove_env_seeded_suppresses_shell_exported_var(tmp_path, monkeypatch, capsys)` (function) — `hermes auth remove xai 1` must stick even when the env var is exported
- L1412 `test_auth_remove_env_seeded_dotenv_only_no_shell_hint(tmp_path, monkeypatch, capsys)` (function) — When the env var lives only in ~/.hermes/.env (not the shell), the
- L1454 `test_auth_add_clears_env_suppression_for_provider(tmp_path, monkeypatch)` (function) — Re-adding a credential via `hermes auth add <provider>` clears any
- L1485 `test_seed_from_env_respects_env_suppression(tmp_path, monkeypatch)` (function) — _seed_from_env() must skip env:<VAR> sources that the user suppressed
- L1510 `test_seed_from_env_respects_openrouter_suppression(tmp_path, monkeypatch)` (function) — OpenRouter is the special-case branch in _seed_from_env; verify it
- L1542 `test_seed_from_singletons_respects_nous_suppression(tmp_path, monkeypatch)` (function) — nous device_code must not re-seed from auth.json when suppressed.
- L1562 `test_seed_from_singletons_respects_copilot_suppression(tmp_path, monkeypatch)` (function) — copilot gh_cli must not re-seed when suppressed.
- L1586 `test_seed_from_singletons_respects_qwen_suppression(tmp_path, monkeypatch)` (function) — qwen-oauth qwen-cli must not re-seed from ~/.qwen/oauth_creds.json when suppressed.
- L1611 `test_seed_from_singletons_respects_hermes_pkce_suppression(tmp_path, monkeypatch)` (function) — anthropic hermes_pkce must not re-seed from ~/.hermes/.anthropic_oauth.json when suppressed.
- L1640 `test_seed_custom_pool_respects_config_suppression(tmp_path, monkeypatch)` (function) — Custom provider config:<name> source must not re-seed when suppressed.
- L1670 `test_credential_sources_registry_has_expected_steps()` (function) — Sanity check — the registry contains the expected RemovalSteps.
- L1705 `test_credential_sources_find_step_returns_none_for_manual()` (function) — Manual entries have nothing external to clean up — no step registered.
- L1712 `test_credential_sources_find_step_copilot_before_generic_env(tmp_path, monkeypatch)` (function) — copilot env:GH_TOKEN must dispatch to the copilot step, not the
- L1730 `test_auth_remove_copilot_suppresses_all_variants(tmp_path, monkeypatch)` (function) — Removing any copilot source must suppress gh_cli + all env:* variants
- L1770 `test_auth_add_clears_all_suppressions_including_non_env(tmp_path, monkeypatch)` (function) — Re-adding a credential via `hermes auth add <provider>` clears ALL
- L1804 `test_auth_remove_codex_manual_device_code_suppresses_canonical(tmp_path, monkeypatch)` (function) — Removing a manual:device_code entry (from `hermes auth add openai-codex`)
