---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_honcho_client_config.py

Symbols in `tests/test_honcho_client_config.py`.

- L14 `TestHonchoClientConfigAutoEnable` (class) — Test auto-enable behavior when API key is present.
- L17 `test_auto_enables_when_api_key_present_no_explicit_enabled(self, tmp_path)` (method) — When API key exists and enabled is not set, should auto-enable.
- L30 `test_respects_explicit_enabled_false(self, tmp_path)` (method) — When enabled is explicitly False, should stay disabled even with API key.
- L43 `test_respects_explicit_enabled_true(self, tmp_path)` (method) — When enabled is explicitly True, should be enabled.
- L56 `test_disabled_when_no_api_key_and_no_explicit_enabled(self, tmp_path)` (method) — When no API key and enabled not set, should be disabled.
- L74 `test_auto_enables_with_env_var_api_key(self, tmp_path, monkeypatch)` (method) — When API key is in env var (not config), should auto-enable.
- L89 `test_from_env_always_enabled(self, monkeypatch)` (method) — from_env() should always set enabled=True.
- L98 `test_falls_back_to_env_when_no_config_file(self, tmp_path, monkeypatch)` (method) — When config file doesn't exist, should fall back to from_env().
- L110 `test_save_config_sets_owner_only_permissions(tmp_path, monkeypatch)` (function) — honcho.json is created atomically with 0o600, not chmod-after-write.
