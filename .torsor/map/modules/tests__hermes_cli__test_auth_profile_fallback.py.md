---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_profile_fallback.py

Symbols in `tests/hermes_cli/test_auth_profile_fallback.py`.

- L20 `_make_auth_store(pool: dict | None=None, providers: dict | None=None)` (function)
- L30 `profile_env(tmp_path, monkeypatch)` (function) — Set up a global root + an active profile under Path.home()/.hermes/profiles/coder.
- L49 `_write(path: Path, payload: dict)` (function)
- L58 `test_profile_with_zero_entries_falls_back_to_global(profile_env)` (function) — Empty profile pool inherits the global-root entries for that provider.
- L81 `test_profile_with_entries_fully_shadows_global(profile_env)` (function) — Once the profile has any entries for a provider, global is ignored.
- L112 `test_per_provider_shadowing_is_independent(profile_env)` (function) — Profile can override one provider while inheriting another from global.
- L152 `test_missing_global_auth_file_is_safe(profile_env)` (function) — Profile processes that never had a global auth.json still work.
- L172 `test_malformed_global_auth_file_does_not_break_profile_read(profile_env)` (function)
- L198 `test_whole_pool_merges_global_providers_when_missing_locally(profile_env)` (function)
- L241 `test_provider_auth_state_falls_back_to_global_when_profile_has_none(profile_env)` (function)
- L254 `test_provider_auth_state_profile_wins_when_present(profile_env)` (function)
- L269 `test_provider_auth_state_returns_none_when_neither_has_it(profile_env)` (function)
- L291 `test_load_provider_state_falls_back_to_global(profile_env)` (function) — When the loaded profile store has no provider entry, fall back to global.
- L306 `test_load_provider_state_profile_wins_over_global(profile_env)` (function)
- L322 `test_load_provider_state_returns_none_when_neither_has_it(profile_env)` (function)
- L332 `test_load_provider_state_classic_mode_no_fallback(tmp_path, monkeypatch)` (function) — In classic mode there is no global to fall back to; behavior is unchanged.
- L355 `test_load_provider_state_malformed_global_does_not_break_profile(profile_env)` (function) — A corrupt global auth.json must not break profile reads.
- L375 `test_classic_mode_does_not_double_read_same_file(tmp_path, monkeypatch)` (function) — In classic mode (HERMES_HOME == global root), no fallback path runs.
- L420 `test_write_credential_pool_targets_profile_not_global(profile_env)` (function)
