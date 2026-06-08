---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_debug_helpers.py

Symbols in `tests/tools/test_debug_helpers.py`.

- L10 `TestDebugSessionDisabled` (class) — When the env var is not set, DebugSession should be a cheap no-op.
- L13 `test_not_active_by_default(self)` (method)
- L18 `test_session_id_empty_when_disabled(self)` (method)
- L22 `test_log_call_noop(self)` (method)
- L27 `test_save_noop(self, tmp_path)` (method)
- L35 `test_get_session_info_disabled(self)` (method)
- L44 `TestDebugSessionEnabled` (class) — When the env var is set to 'true', DebugSession records and saves.
- L47 `_make_enabled(self, tmp_path)` (method)
- L53 `test_active_when_env_set(self, tmp_path)` (method)
- L58 `test_session_id_generated(self, tmp_path)` (method)
- L62 `test_log_call_appends(self, tmp_path)` (method)
- L71 `test_save_creates_json_file(self, tmp_path)` (method)
- L86 `test_get_session_info_enabled(self, tmp_path)` (method)
- L96 `test_env_var_case_insensitive(self, tmp_path)` (method)
- L105 `test_env_var_false_disables(self)` (method)
- L110 `test_save_empty_log(self, tmp_path)` (method)
