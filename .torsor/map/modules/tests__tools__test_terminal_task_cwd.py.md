---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_terminal_task_cwd.py

Symbols in `tests/tools/test_terminal_task_cwd.py`.

- L9 `_minimal_terminal_config(cwd='/default')` (function)
- L18 `test_foreground_command_uses_registered_task_cwd_for_existing_environment(monkeypatch)` (function) — ACP can update task cwd after the local env exists; foreground must honor it.
- L46 `test_explicit_workdir_still_wins_over_registered_task_cwd(monkeypatch)` (function)
- L79 `test_foreground_command_prefers_live_env_cwd_over_init_time_cwd(monkeypatch)` (function) — A prior `cd` updates env.cwd; terminal_tool must honor that live cwd.
- L110 `test_background_command_prefers_live_env_cwd_over_init_time_cwd(monkeypatch)` (function) — Background process launches must also use the live session cwd.
- L162 `test_registering_cwd_override_updates_live_env_cwd(monkeypatch)` (function) — An ACP ``update_cwd`` (re-)registered mid-session must win over a
- L193 `test_registering_cwd_override_noop_when_no_live_env(monkeypatch)` (function) — Registering an override before the env exists must not crash; the cwd
- L205 `test_registering_non_cwd_override_leaves_live_env_cwd_untouched(monkeypatch)` (function) — A non-cwd override (e.g. a per-task Modal image) must not disturb the
- L223 `test_safe_getcwd_returns_real_cwd(monkeypatch)` (function)
- L228 `test_safe_getcwd_falls_back_to_terminal_cwd_when_cwd_deleted(monkeypatch)` (function)
- L237 `test_safe_getcwd_falls_back_to_home_when_no_terminal_cwd(monkeypatch)` (function)
