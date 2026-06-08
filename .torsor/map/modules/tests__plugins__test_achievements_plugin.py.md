---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_achievements_plugin.py

Symbols in `tests/plugins/test_achievements_plugin.py`.

- L39 `plugin_api(tmp_path, monkeypatch)` (function) — Load plugin_api with isolated ~/.hermes so state/snapshot files don't collide.
- L62 `_FakeSessionDB` (class) — Stand-in for hermes_state.SessionDB that records scan calls.
- L65 `__init__(self, session_count: int, scan_delay: float=0)` (method)
- L73 `list_sessions_rich(self, source: Optional[str]=None, exclude_sources: Optional[List[str]]=None, limit: int=20, offset: int=0, include_children: bool=False, project_compression_tips: bool=True)` (method)
- L103 `get_messages(self, session_id: str)` (method)
- L114 `close(self)` (method)
- L118 `_install_fake_session_db(plugin_api, fake_db)` (function) — Inject a fake SessionDB so ``scan_sessions`` finds it via its local import.
- L130 `test_scan_sessions_default_scans_all_history_not_first_200(plugin_api)` (function) — Bug regression: ``scan_sessions()`` used to cap at limit=200.
- L154 `test_scan_sessions_explicit_positive_limit_is_honored(plugin_api)` (function) — Callers can still pass a small limit for smoke tests.
- L165 `test_scan_sessions_zero_or_negative_limit_means_unlimited(plugin_api)` (function) — ``limit=0`` and ``limit=-1`` both map to the unlimited path.
- L177 `test_evaluate_all_first_run_returns_pending_and_starts_background_scan(plugin_api)` (function) — First-ever evaluate_all with no cache returns a pending placeholder
- L226 `test_evaluate_all_stale_cache_serves_stale_and_refreshes_in_background(plugin_api)` (function) — When the snapshot is on-disk but older than TTL, evaluate_all returns
- L264 `test_evaluate_all_force_runs_synchronously(plugin_api)` (function) — Manual /rescan (force=True) blocks the caller — users clicking
- L278 `test_start_background_scan_is_idempotent_while_running(plugin_api)` (function) — Multiple concurrent dashboard requests must not spawn duplicate scans.
- L305 `test_background_scan_publishes_partial_snapshots(plugin_api)` (function) — The background scanner publishes intermediate snapshots to the cache
- L353 `test_partial_snapshots_do_not_persist_unlock_timestamps(plugin_api)` (function) — Intermediate snapshots must not write to state.json — an unlock
