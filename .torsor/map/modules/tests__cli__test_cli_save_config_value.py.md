---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_save_config_value.py

Symbols in `tests/cli/test_cli_save_config_value.py`.

- L9 `TestSaveConfigValueAtomic` (class) — save_config_value() must use atomic round-trip YAML updates.
- L13 `config_env(self, tmp_path, monkeypatch)` (method) — Isolated config environment with a writable config.yaml.
- L25 `test_calls_roundtrip_yaml_update(self, config_env, monkeypatch)` (method) — save_config_value must preserve user-edited YAML structure.
- L35 `test_preserves_existing_keys(self, config_env)` (method) — Writing a new key must not clobber existing config entries.
- L46 `test_creates_nested_keys(self, config_env)` (method) — Dot-separated paths create intermediate dicts as needed.
- L54 `test_overwrites_existing_value(self, config_env)` (method) — Updating an existing key replaces the value.
- L62 `test_preserves_env_ref_templates_in_unrelated_fields(self, config_env)` (method) — The /model --global persistence path must not inline env-backed secrets.
- L80 `test_preserves_comments_after_config_mutation(self, config_env)` (method) — CLI config writes should not strip existing user comments.
- L102 `test_preserves_readable_unicode_after_config_mutation(self, config_env)` (method) — Non-ASCII prompts should remain readable instead of \u-escaped.
- L121 `test_file_not_truncated_on_error(self, config_env, monkeypatch)` (method) — If atomic_yaml_write raises, the original file is untouched.
