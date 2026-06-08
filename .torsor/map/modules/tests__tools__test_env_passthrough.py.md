---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_env_passthrough.py

Symbols in `tests/tools/test_env_passthrough.py`.

- L17 `_clean_passthrough()` (function) — Ensure a clean passthrough state for every test.
- L26 `TestSkillScopedPassthrough` (class)
- L27 `test_register_and_check(self)` (method)
- L32 `test_register_multiple(self)` (method)
- L38 `test_clear(self)` (method)
- L44 `test_get_all(self)` (method)
- L50 `test_strips_whitespace(self)` (method)
- L54 `test_skips_empty(self)` (method)
- L60 `TestConfigPassthrough` (class)
- L61 `test_reads_from_config(self, tmp_path, monkeypatch)` (method)
- L72 `test_empty_config(self, tmp_path, monkeypatch)` (method)
- L81 `test_missing_config_key(self, tmp_path, monkeypatch)` (method)
- L90 `test_no_config_file(self, tmp_path, monkeypatch)` (method)
- L96 `test_union_of_skill_and_config(self, tmp_path, monkeypatch)` (method)
- L109 `TestExecuteCodeIntegration` (class) — Verify that the passthrough is checked in execute_code's env filtering.
- L112 `test_secret_substring_blocked_by_default(self)` (method) — TENOR_API_KEY should be blocked without passthrough.
- L135 `test_passthrough_allows_secret_through(self)` (method) — TENOR_API_KEY should pass through when registered.
- L162 `TestTerminalIntegration` (class) — Verify that the passthrough is checked in terminal's env sanitizers.
- L165 `test_blocklisted_var_blocked_by_default(self)` (method)
- L175 `test_passthrough_cannot_override_provider_blocklist(self)` (method) — GHSA-rhgp-j443-p4rf: register_env_passthrough must NOT accept
- L198 `test_make_run_env_blocklist_override_rejected(self)` (method) — _make_run_env must NOT expose a blocklisted var to subprocess env
- L220 `test_non_hermes_api_key_still_registerable(self)` (method) — Third-party API keys (TENOR_API_KEY, NOTION_TOKEN, etc.) are NOT
