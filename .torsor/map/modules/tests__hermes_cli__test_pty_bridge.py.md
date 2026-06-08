---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_pty_bridge.py

Symbols in `tests/hermes_cli/test_pty_bridge.py`.

- L26 `_read_until(bridge: PtyBridge, needle: bytes, timeout: float=5.0)` (function) — Accumulate PTY output until we see `needle` or time out.
- L41 `TestPtyBridgeSpawn` (class)
- L42 `test_is_available_on_posix(self)` (method)
- L45 `test_spawn_returns_bridge_with_pid(self)` (method)
- L52 `test_spawn_raises_on_missing_argv0(self, tmp_path)` (method)
- L58 `TestPtyBridgeIO` (class)
- L59 `test_reads_child_stdout(self)` (method)
- L67 `test_write_sends_to_child_stdin(self)` (method)
- L78 `test_read_returns_none_after_child_exits(self)` (method)
- L98 `TestPtyBridgeResize` (class)
- L99 `test_resize_updates_child_winsize(self)` (method)
- L123 `test_resize_clamps_wsl_garbage_dimensions(self)` (method)
- L152 `TestClampDimension` (class)
- L153 `test_clamps_above_max(self)` (method)
- L159 `test_floors_at_one(self)` (method)
- L165 `test_passes_through_sane_values(self)` (method)
- L171 `test_non_numeric_falls_back_to_min(self)` (method)
- L178 `test_clamped_values_pack_as_unsigned_short(self)` (method)
- L191 `TestPtyBridgeClose` (class)
- L192 `test_close_is_idempotent(self)` (method)
- L198 `test_close_terminates_long_running_child(self)` (method)
- L216 `TestPtyBridgeEnv` (class)
- L217 `test_cwd_is_respected(self, tmp_path)` (method)
- L228 `test_env_is_forwarded(self)` (method)
- L240 `TestPtyBridgeUnavailable` (class) — Platform fallback semantics — PtyUnavailableError is importable and
- L244 `test_error_carries_user_message(self)` (method)
