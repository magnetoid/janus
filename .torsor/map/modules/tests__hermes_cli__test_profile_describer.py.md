---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_profile_describer.py

Symbols in `tests/hermes_cli/test_profile_describer.py`.

- L18 `profile_env(tmp_path, monkeypatch)` (function) — Set up an isolated HERMES_HOME with a default profile dir.
- L27 `test_read_profile_meta_empty_when_missing(profile_env)` (function)
- L32 `test_write_and_read_profile_meta(profile_env)` (function)
- L43 `test_write_profile_meta_preserves_other_fields(profile_env)` (function)
- L57 `test_write_profile_meta_rejects_missing_dir(tmp_path)` (function)
- L63 `test_read_profile_meta_tolerates_corrupt_yaml(profile_env)` (function)
- L74 `_fake_aux_response(content: str)` (function)
- L81 `_patch_aux_client(content: str)` (function)
- L90 `test_describer_writes_description_with_auto_true(profile_env, monkeypatch)` (function)
- L115 `test_describer_refuses_to_overwrite_user_authored(profile_env, monkeypatch)` (function)
- L130 `test_describer_overwrite_flag_replaces_user_authored(profile_env, monkeypatch)` (function)
- L149 `test_describer_handles_malformed_llm_response(profile_env, monkeypatch)` (function)
- L163 `test_describer_returns_false_when_profile_missing(profile_env, monkeypatch)` (function)
