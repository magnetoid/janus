---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_set_config_value.py

Symbols in `tests/hermes_cli/test_set_config_value.py`.

- L13 `_isolated_hermes_home(tmp_path)` (function) — Point HERMES_HOME at a temp dir so tests never touch real config.
- L21 `_read_env(tmp_path)` (function)
- L25 `_read_config(tmp_path)` (function)
- L34 `TestExplicitAllowlist` (class) — Keys in the hardcoded allowlist should always go to .env.
- L52 `test_explicit_key_routes_to_env(self, key, _isolated_hermes_home)` (method)
- L64 `TestCatchAllPatterns` (class) — Any key ending in _API_KEY or _TOKEN should route to .env.
- L74 `test_api_key_suffix_routes_to_env(self, key, _isolated_hermes_home)` (method)
- L80 `test_case_insensitive(self, _isolated_hermes_home)` (method) — Keys should be uppercased regardless of input casing.
- L86 `test_terminal_ssh_prefix_routes_to_env(self, _isolated_hermes_home)` (method)
- L96 `TestConfigYamlRouting` (class) — Regular config keys should go to config.yaml, NOT .env.
- L99 `test_simple_key(self, _isolated_hermes_home)` (method)
- L105 `test_nested_key(self, _isolated_hermes_home)` (method)
- L111 `test_terminal_image_goes_to_config(self, _isolated_hermes_home)` (method) — TERMINAL_DOCKER_IMAGE doesn't match _API_KEY or _TOKEN, so config.yaml.
- L117 `test_terminal_docker_cwd_mount_flag_goes_to_config_and_env(self, _isolated_hermes_home)` (method)
- L132 `TestFalsyValues` (class) — config set should accept empty strings and falsy values like '0'.
- L135 `test_empty_string_routes_to_env(self, _isolated_hermes_home)` (method) — Blanking an API key should write an empty value to .env.
- L141 `test_empty_string_routes_to_config(self, _isolated_hermes_home)` (method) — Blanking a config key should write an empty string to config.yaml.
- L147 `test_zero_routes_to_config(self, _isolated_hermes_home)` (method) — Setting a config key to '0' should write 0 to config.yaml.
- L153 `test_config_command_rejects_missing_value(self)` (method) — config set with no value arg (None) should still exit.
- L159 `test_config_command_accepts_empty_string(self, _isolated_hermes_home)` (method) — config set KEY '' should not exit — it should set the value.
- L171 `TestListNavigation` (class) — hermes config set must preserve YAML list fields when using numeric
- L177 `_write_config(self, tmp_path, body)` (method)
- L180 `test_indexed_set_preserves_sibling_list_entries(self, _isolated_hermes_home)` (method) — Setting custom_providers.0.api_key must not destroy entry 1.
- L208 `test_indexed_set_preserves_non_targeted_fields(self, _isolated_hermes_home)` (method) — Setting one field in a list entry must not drop other fields.
- L230 `test_deeper_nesting_through_list(self, _isolated_hermes_home)` (method) — Navigation path mixing dict → list → dict → scalar.
