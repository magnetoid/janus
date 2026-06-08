---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_foreground_timeout_cap.py

Symbols in `tests/tools/test_terminal_foreground_timeout_cap.py`.

- L13 `_make_env_config(**overrides)` (function) — Return a minimal _get_env_config()-shaped dict with optional overrides.
- L30 `TestForegroundTimeoutCap` (class) — FOREGROUND_MAX_TIMEOUT rejects foreground commands that exceed it.
- L33 `test_foreground_timeout_rejected_above_max(self)` (method) — When model requests timeout > FOREGROUND_MAX_TIMEOUT, return error.
- L50 `test_foreground_rejects_shell_level_background_wrappers(self)` (method) — Foreground nohup/disown/setsid commands should be redirected to background mode.
- L65 `test_foreground_rejects_long_lived_server_command(self)` (method) — Foreground dev server commands should be redirected to background mode.
- L78 `test_foreground_allows_help_variant_for_server_command(self)` (method) — Informational variants like '--help' should not be blocked.
- L97 `test_foreground_timeout_within_max_executes(self)` (method) — When model requests timeout <= FOREGROUND_MAX_TIMEOUT, execute normally.
- L119 `test_config_default_above_cap_not_rejected(self)` (method) — When config default timeout > cap but model passes no timeout, execute normally.
- L145 `test_background_not_rejected(self)` (method) — Background commands should NOT be subject to foreground timeout cap.
- L175 `test_default_timeout_not_rejected(self)` (method) — Default timeout (180s) should not trigger rejection.
- L197 `test_exactly_at_max_not_rejected(self)` (method) — Timeout exactly at FOREGROUND_MAX_TIMEOUT should execute normally.
- L220 `TestForegroundMaxTimeoutConstant` (class) — Verify the FOREGROUND_MAX_TIMEOUT constant and schema.
- L223 `test_default_value_is_600(self)` (method) — Default FOREGROUND_MAX_TIMEOUT is 600 when env var is not set.
- L228 `test_schema_mentions_max(self)` (method) — Tool schema description should mention the max timeout.
