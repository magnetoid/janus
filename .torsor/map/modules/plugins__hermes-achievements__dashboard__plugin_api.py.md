---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/hermes-achievements/dashboard/plugin_api.py

Symbols in `plugins/hermes-achievements/dashboard/plugin_api.py`.

- L56 `tiers(values: List[int])` (function)
- L60 `req(metric: str, gte: int)` (function)
- L145 `state_path()` (function)
- L149 `snapshot_path()` (function)
- L153 `checkpoint_path()` (function)
- L157 `load_state()` (function)
- L167 `save_state(state: Dict[str, Any])` (function)
- L173 `_json_safe(value: Any)` (function)
- L183 `load_snapshot()` (function)
- L196 `save_snapshot(data: Dict[str, Any])` (function)
- L202 `load_checkpoint()` (function)
- L219 `save_checkpoint(data: Dict[str, Any])` (function)
- L225 `session_fingerprint(meta: Dict[str, Any])` (function)
- L234 `_cache_is_fresh(now: int)` (function)
- L238 `_is_snapshot_stale(snapshot: Optional[Dict[str, Any]], now: Optional[int]=None)` (function)
- L248 `_scan_status_payload(now: Optional[int]=None)` (function)
- L266 `_tool_name_from_call(call: Any)` (function)
- L273 `_content(msg: Dict[str, Any])` (function)
- L285 `_count_tool(tool_names: List[str], *needles: str)` (function)
- L290 `model_provider(model_name: str)` (function)
- L302 `is_local_model_name(model_name: str)` (function)
- L310 `analyze_messages(session_id: str, title: str, messages: List[Dict[str, Any]])` (function)
- L422 `evaluate_tiered(definition: Dict[str, Any], aggregate: Dict[str, Any])` (function)
- L440 `evaluate_requirements(definition: Dict[str, Any], aggregate: Dict[str, Any])` (function)
- L458 `evaluate_boolean(definition: Dict[str, Any], aggregate: Dict[str, Any])` (function)
- L530 `metric_label(metric: str)` (function)
- L534 `criteria_for(definition: Dict[str, Any])` (function)
- L552 `display_achievement(item: Dict[str, Any])` (function)
- L560 `scan_sessions(limit: Optional[int]=None, progress_callback: Optional[Any]=None, progress_every: int=250)` (function) — Scan Hermes sessions and build per-session achievement stats.
- L674 `aggregate_stats(sessions: List[Dict[str, Any]])` (function)
- L758 `evaluate_definition(definition: Dict[str, Any], aggregate: Dict[str, Any])` (function)
- L766 `evidence_for(definition: Dict[str, Any], sessions: List[Dict[str, Any]])` (function)
- L787 `_compute_from_scan(scan: Dict[str, Any], *, is_partial: bool=False)` (function) — Evaluate every achievement definition against a scan result.
- L829 `compute_all(progress_callback: Optional[Any]=None, progress_every: int=250)` (function)
- L838 `_build_pending_snapshot(now: int)` (function) — Placeholder payload used while the first-ever scan is still running.
- L859 `_run_scan_and_update_cache(publish_partial_snapshots: bool=True)` (function) — Execute a scan + snapshot update. Called synchronously or from a thread.
- L920 `_start_background_scan()` (function) — Kick off a scan in a daemon thread if one isn't already running.
- L944 `evaluate_all(force: bool=False)` (function) — Return the current achievements payload.
- L1000 `achievements()` (function)
- L1012 `scan_status()` (function)
- L1017 `recent_unlocks()` (function)
- L1023 `session_badges(session_id: str)` (function)
- L1038 `rescan()` (function)
- L1043 `reset_state()` (function)
