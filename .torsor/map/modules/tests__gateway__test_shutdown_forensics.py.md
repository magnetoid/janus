---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_shutdown_forensics.py

Symbols in `tests/gateway/test_shutdown_forensics.py`.

- L21 `TestSignalName` (class)
- L22 `test_known_signals_resolve_to_names(self)` (method)
- L26 `test_unknown_int_returns_signal_num_token(self)` (method)
- L30 `test_none_returns_unknown(self)` (method)
- L33 `test_non_integer_falls_back_to_str(self)` (method)
- L41 `TestSnapshotShutdownContext` (class)
- L42 `test_includes_self_pid_and_signal(self)` (method)
- L48 `test_handles_none_signal(self)` (method)
- L53 `test_includes_timestamps(self)` (method)
- L61 `test_includes_parent_summary_on_linux(self)` (method)
- L66 `test_under_systemd_flag_uses_invocation_id(self, monkeypatch)` (method)
- L72 `test_under_systemd_false_without_invocation_id_and_normal_ppid(self, monkeypatch)` (method)
- L83 `test_completes_quickly(self)` (method) — Snapshot must NOT block — it runs inside the asyncio signal handler.
- L91 `test_detects_takeover_marker_for_self(self, tmp_path, monkeypatch)` (method)
- L102 `test_detects_takeover_marker_for_other(self, tmp_path, monkeypatch)` (method)
- L111 `test_detects_planned_stop_marker(self, tmp_path, monkeypatch)` (method)
- L125 `TestFormatters` (class)
- L126 `test_format_context_for_log_includes_signal_and_parent(self)` (method)
- L133 `test_context_as_json_round_trips(self)` (method)
- L140 `test_context_as_json_handles_unserialisable_values(self)` (method)
- L153 `TestSpawnAsyncDiagnostic` (class)
- L155 `test_spawns_subprocess_and_writes_output(self, tmp_path)` (method)
- L180 `test_returns_none_on_windows(self, tmp_path, monkeypatch)` (method)
- L188 `test_handles_unwritable_log_path_gracefully(self, tmp_path)` (method)
- L195 `test_does_not_block_caller(self, tmp_path)` (method) — The spawn must return immediately even if ``ps`` takes seconds.
- L210 `TestParseSystemdDuration` (class)
- L211 `test_seconds(self)` (method)
- L214 `test_minutes(self)` (method)
- L217 `test_combined_min_sec(self)` (method)
- L220 `test_hours(self)` (method)
- L223 `test_milliseconds(self)` (method)
- L226 `test_empty_returns_none(self)` (method)
- L229 `test_unknown_unit_returns_none(self)` (method)
- L237 `TestCheckSystemdTimingAlignment` (class)
- L238 `test_returns_none_when_not_under_systemd(self, monkeypatch)` (method)
- L243 `test_returns_none_when_unit_undeterminable(self, monkeypatch)` (method)
