---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_credential_pool.py

Symbols in `tests/agent/test_credential_pool.py`.

- L13 `_write_auth_store(tmp_path, payload: dict)` (function)
- L19 `_jwt_with_claims(claims: dict)` (function)
- L27 `test_fill_first_selection_skips_recently_exhausted_entry(tmp_path, monkeypatch)` (function)
- L72 `test_select_clears_expired_exhaustion(tmp_path, monkeypatch)` (function)
- L105 `test_round_robin_strategy_rotates_priorities(tmp_path, monkeypatch)` (function)
- L149 `test_random_strategy_uses_random_choice(tmp_path, monkeypatch)` (function)
- L192 `test_exhausted_entry_resets_after_ttl(tmp_path, monkeypatch)` (function)
- L227 `test_exhausted_402_entry_resets_after_one_hour(tmp_path, monkeypatch)` (function) — 402-exhausted credentials recover after 1 hour, not 24.
- L263 `test_exhausted_401_entry_resets_after_five_minutes(tmp_path, monkeypatch)` (function) — Transient auth failures should not strand single-key setups for an hour.
- L299 `test_explicit_reset_timestamp_overrides_default_429_ttl(tmp_path, monkeypatch)` (function)
- L337 `test_mark_exhausted_and_rotate_persists_status(tmp_path, monkeypatch)` (function)
- L382 `test_token_invalidated_marks_credential_dead(tmp_path, monkeypatch)` (function) — OpenAI Codex token_invalidated must mark the credential DEAD, not exhausted.
- L447 `test_dead_credential_never_re_enters_rotation_after_ttl(tmp_path, monkeypatch)` (function) — A DEAD credential must stay excluded regardless of how much time passes.
- L510 `test_429_rate_limit_still_uses_exhausted_not_dead(tmp_path, monkeypatch)` (function) — 429 rate limits must NOT be treated as terminal.
- L565 `test_generic_401_without_terminal_reason_still_uses_exhausted(tmp_path, monkeypatch)` (function) — A 401 with no specific code/reason should keep TTL semantics.
- L619 `test_dead_manual_entry_pruned_after_24h(tmp_path, monkeypatch)` (function) — A DEAD manual entry is removed from the pool after the prune TTL.
- L678 `test_dead_manual_entry_kept_within_24h(tmp_path, monkeypatch)` (function) — A DEAD manual entry stays in the pool until the prune TTL elapses.
- L736 `test_dead_singleton_seeded_entry_not_pruned(tmp_path, monkeypatch)` (function) — A DEAD ``device_code`` entry must NOT be pruned even after 24h.
- L791 `test_load_pool_seeds_env_api_key(tmp_path, monkeypatch)` (function)
- L807 `test_load_pool_does_not_persist_env_seeded_secret_value(tmp_path, monkeypatch)` (function) — Runtime env keys may be used in memory but must not land in auth.json.
- L835 `test_load_pool_persists_bitwarden_origin_metadata_without_secret(tmp_path, monkeypatch)` (function) — Bitwarden-injected env vars retain source metadata but not raw values.
- L864 `test_load_pool_sanitizes_legacy_raw_borrowed_entry_when_value_unchanged(tmp_path, monkeypatch)` (function) — Existing raw env-seeded pool entries are rewritten even if the env value matches.
- L905 `test_pooled_credential_to_dict_strips_borrowed_secret_fields()` (function)
- L966 `test_borrowed_source_variants_strip_secret_fields(source)` (function)
- L992 `test_load_pool_prunes_stale_borrowed_custom_config_entry(tmp_path, monkeypatch)` (function)
- L1026 `test_write_credential_pool_sanitizes_borrowed_payload_at_disk_boundary(tmp_path, monkeypatch)` (function) — Direct dictionary callers cannot bypass the borrowed-secret guard.
- L1071 `test_write_credential_pool_treats_unowned_oauth_source_as_borrowed(tmp_path, monkeypatch)` (function)
- L1099 `test_write_credential_pool_preserves_known_provider_owned_oauth_state(tmp_path, monkeypatch)` (function)
- L1125 `test_load_pool_prefers_dotenv_over_stale_os_environ(tmp_path, monkeypatch)` (function) — Regression for #18254: stale OPENROUTER_API_KEY in os.environ (inherited
- L1158 `test_load_pool_falls_back_to_os_environ_when_dotenv_empty(tmp_path, monkeypatch)` (function) — When ~/.hermes/.env does not define OPENROUTER_API_KEY (typical Docker /
- L1182 `test_load_pool_removes_stale_seeded_env_entry(tmp_path, monkeypatch)` (function)
- L1215 `test_load_pool_migrates_nous_provider_state(tmp_path, monkeypatch)` (function)
- L1250 `test_load_pool_mirrors_nous_invoke_jwt_agent_key_runtime_api_key(tmp_path, monkeypatch)` (function)
- L1296 `test_nous_runtime_api_key_rejects_opaque_agent_key()` (function)
- L1319 `test_nous_pool_terminal_refresh_removes_device_code_entry(tmp_path, monkeypatch)` (function)
- L1396 `test_load_pool_removes_nous_device_code_when_singleton_quarantined(tmp_path, monkeypatch)` (function)
- L1447 `test_load_pool_removes_stale_file_backed_singleton_entry(tmp_path, monkeypatch)` (function)
- L1492 `test_load_pool_migrates_nous_provider_state_preserves_tls(tmp_path, monkeypatch)` (function)
- L1538 `test_singleton_seed_does_not_clobber_manual_oauth_entry(tmp_path, monkeypatch)` (function)
- L1587 `test_load_pool_prefers_anthropic_env_token_over_file_backed_oauth(tmp_path, monkeypatch)` (function)
- L1617 `test_load_pool_api_key_path_skips_oauth_autodiscovery(tmp_path, monkeypatch)` (function) — API-key auth path: autodiscovered OAuth creds must NOT be seeded.
- L1671 `test_load_pool_api_key_path_prunes_stale_oauth_entries(tmp_path, monkeypatch)` (function) — Switching OAuth -> API key must prune stale OAuth entries from auth.json.
- L1723 `test_load_pool_oauth_path_still_autodiscovers(tmp_path, monkeypatch)` (function) — OAuth path: ANTHROPIC_TOKEN set, autodiscovery still fires.
- L1761 `test_least_used_strategy_selects_lowest_count(tmp_path, monkeypatch)` (function) — least_used strategy should select the credential with the lowest request_count.
- L1823 `test_thread_safety_concurrent_select(tmp_path, monkeypatch)` (function) — Concurrent select() calls should not corrupt pool state.
- L1885 `test_custom_endpoint_pool_keyed_by_name(tmp_path, monkeypatch)` (function) — Verify load_pool('custom:together.ai') works and returns entries from auth.json.
- L1937 `test_custom_endpoint_pool_seeds_from_config(tmp_path, monkeypatch)` (function) — Verify seeding from custom_providers api_key in config.yaml.
- L1965 `test_custom_endpoint_pool_seeds_from_model_config(tmp_path, monkeypatch)` (function) — Verify seeding from model.api_key when model.provider=='custom' and base_url matches.
- L1997 `test_custom_pool_does_not_break_existing_providers(tmp_path, monkeypatch)` (function) — Existing registry providers work exactly as before with custom pool support.
- L2012 `test_get_custom_provider_pool_key(tmp_path, monkeypatch)` (function) — get_custom_provider_pool_key maps base_url to custom:<name> pool key.
- L2041 `test_get_custom_provider_pool_key_prefers_name_over_base_url(tmp_path, monkeypatch)` (function) — When two custom providers share the same base_url, provider_name resolves to the correct one.
- L2078 `test_list_custom_pool_providers(tmp_path, monkeypatch)` (function) — list_custom_pool_providers returns custom: pool keys from auth.json.
- L2129 `test_acquire_lease_prefers_unleased_entry(tmp_path, monkeypatch)` (function)
- L2171 `test_release_lease_decrements_counter(tmp_path, monkeypatch)` (function)
- L2203 `test_load_pool_does_not_seed_claude_code_when_anthropic_not_configured(tmp_path, monkeypatch)` (function) — Claude Code credentials must not be auto-seeded when the user never selected anthropic.
- L2230 `test_load_pool_seeds_copilot_via_gh_auth_token(tmp_path, monkeypatch)` (function) — Copilot credentials from `gh auth token` should be seeded into the pool.
- L2251 `test_load_pool_does_not_seed_copilot_when_no_token(tmp_path, monkeypatch)` (function) — Copilot pool should be empty when resolve_copilot_token() returns nothing.
- L2268 `test_load_pool_seeds_qwen_oauth_via_cli_tokens(tmp_path, monkeypatch)` (function) — Qwen OAuth credentials from ~/.qwen/oauth_creds.json should be seeded into the pool.
- L2295 `test_load_pool_does_not_seed_qwen_oauth_when_no_token(tmp_path, monkeypatch)` (function) — Qwen OAuth pool should be empty when no CLI credentials exist.
- L2316 `test_nous_seed_from_singletons_preserves_obtained_at_timestamps(tmp_path, monkeypatch)` (function) — Regression test for #15099 secondary issue.
- L2384 `TestLeastUsedStrategy` (class) — Regression: least_used strategy must increment request_count on select.
- L2387 `test_request_count_increments(self)` (method) — Each select() call should increment the chosen entry's request_count.
- L2417 `test_sync_nous_entry_from_auth_store_adopts_newer_tokens(tmp_path, monkeypatch)` (function) — When auth.json has a newer refresh token, the pool entry should adopt it.
- L2479 `test_sync_nous_entry_noop_when_tokens_match(tmp_path, monkeypatch)` (function) — When auth.json has the same refresh token, sync should be a no-op.
- L2513 `test_nous_exhausted_entry_recovers_via_auth_store_sync(tmp_path, monkeypatch)` (function) — An exhausted Nous entry should recover when auth.json has newer tokens.
- L2586 `_codex_auth_store(access: str, refresh: str)` (function)
- L2604 `test_sync_codex_entry_from_auth_store_adopts_newer_tokens(tmp_path, monkeypatch)` (function) — When auth.json has newer Codex tokens, the pool entry should adopt them.
- L2629 `test_sync_codex_entry_noop_when_tokens_match(tmp_path, monkeypatch)` (function) — When auth.json has the same tokens, sync should be a no-op.
- L2644 `test_codex_exhausted_entry_recovers_via_auth_store_sync(tmp_path, monkeypatch)` (function) — An exhausted Codex entry should recover when auth.json has newer tokens.
- L2693 `test_codex_exhausted_entry_stays_stuck_without_auth_store_update(tmp_path, monkeypatch)` (function) — Regression guard: if auth.json tokens haven't changed, the exhausted
- L2729 `_xai_auth_store(access_token: str, refresh_token: str)` (function)
- L2746 `test_is_terminal_xai_oauth_refresh_error()` (function)
- L2767 `test_xai_oauth_terminal_refresh_clears_auth_json_and_removes_pool_entries(tmp_path, monkeypatch)` (function)
- L2829 `test_xai_oauth_nonterminal_refresh_does_not_quarantine(tmp_path, monkeypatch)` (function)
- L2867 `_codex_auth_store(access_token: str, refresh_token: str)` (function)
- L2882 `test_is_terminal_codex_oauth_refresh_error()` (function)
- L2909 `test_codex_oauth_terminal_refresh_clears_auth_json_and_removes_pool_entries(tmp_path, monkeypatch)` (function)
- L2970 `test_codex_oauth_nonterminal_refresh_does_not_quarantine(tmp_path, monkeypatch)` (function)
