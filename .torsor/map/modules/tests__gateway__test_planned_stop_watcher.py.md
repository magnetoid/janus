---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_planned_stop_watcher.py

Symbols in `tests/gateway/test_planned_stop_watcher.py`.

- L26 `_write_self_marker(marker, *, stale: bool=False)` (function) — Write a planned-stop marker that targets the CURRENT process.
- L44 `_FakeRunner` (class) — Stand-in for GatewayRunner — only exposes the two flags the watcher reads.
- L47 `__init__(self, *, running: bool=True, draining: bool=False)` (method)
- L52 `_make_loop_capturing_calls()` (function) — Build a fake asyncio loop whose call_soon_threadsafe records its args.
- L64 `test_watcher_fires_shutdown_when_marker_appears(tmp_path, monkeypatch)` (function) — When a marker targeting THIS process exists, fire the shutdown handler.
- L98 `test_watcher_does_not_fire_when_marker_absent(tmp_path, monkeypatch)` (function) — No marker = no shutdown call. Watcher just spins until stop_event.
- L129 `test_watcher_skips_when_runner_already_draining(tmp_path, monkeypatch)` (function) — If shutdown is already in progress, don't re-fire the handler.
- L161 `test_watcher_skips_when_runner_not_started(tmp_path, monkeypatch)` (function) — If the runner hasn't started, the marker is for a previous instance —
- L190 `test_watcher_responds_to_stop_event_promptly(tmp_path, monkeypatch)` (function) — Setting stop_event must exit the watcher within ~poll_interval seconds.
- L217 `test_watcher_fires_only_once_when_marker_persists(tmp_path, monkeypatch)` (function) — Marker file existing for multiple polls must NOT spam the handler.
- L251 `test_watcher_tolerates_marker_path_resolution_errors(tmp_path, monkeypatch, caplog)` (function) — If _get_planned_stop_marker_path() raises, the watcher logs and continues.
- L295 `test_watcher_does_not_fire_for_foreign_pid_marker(tmp_path, monkeypatch)` (function) — A marker naming a DIFFERENT process must not trigger our shutdown.
- L341 `test_watcher_cleans_up_stale_marker_and_keeps_running(tmp_path, monkeypatch)` (function) — A marker older than the TTL is unlinked and never fires shutdown.
- L371 `test_planned_stop_marker_targets_self_probe_is_non_destructive(tmp_path, monkeypatch)` (function) — The probe returns True for a self-marker WITHOUT unlinking it.
- L387 `test_planned_stop_marker_targets_self_drops_malformed(tmp_path, monkeypatch)` (function) — A malformed marker reports False and is cleaned up.
