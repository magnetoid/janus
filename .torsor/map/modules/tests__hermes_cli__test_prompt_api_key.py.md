---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_prompt_api_key.py

Symbols in `tests/hermes_cli/test_prompt_api_key.py`.

- L16 `profile_env(tmp_path, monkeypatch)` (function)
- L25 `_pconfig(name='deepseek')` (function)
- L30 `_run_prompt(existing_key, choice, new_key='', provider_id='', pconfig_name='deepseek')` (function) — Invoke _prompt_api_key with mocked input()/getpass() responses.
- L42 `test_first_time_save_new_key(profile_env)` (function)
- L51 `test_first_time_cancelled(profile_env)` (function)
- L59 `test_keep_default_empty_input(profile_env)` (function)
- L68 `test_keep_letter_k(profile_env)` (function)
- L74 `test_keep_on_unrecognised_input(profile_env)` (function) — Garbage input falls through to keep — never destroys the user's key.
- L81 `test_replace_saves_new_key(profile_env)` (function)
- L93 `test_replace_cancelled_preserves_key(profile_env)` (function) — Empty entry to the Replace prompt means cancel — keeps the old key intact.
- L106 `test_clear_wipes_env_and_aborts(profile_env)` (function)
- L119 `test_ctrl_c_at_choice_prompt_keeps(profile_env)` (function)
- L131 `test_lmstudio_first_time_empty_uses_placeholder(profile_env)` (function)
- L144 `test_lmstudio_replace_empty_does_not_overwrite_with_placeholder(profile_env)` (function) — On REPLACE with empty input, preserve the user's existing key — do NOT
