---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_accretion_caps.py

Symbols in `tests/tools/test_accretion_caps.py`.

- L23 `TestReadTrackerCaps` (class)
- L24 `setup_method(self)` (method)
- L31 `test_read_history_capped(self, monkeypatch)` (method) — read_history set is bounded by _READ_HISTORY_CAP.
- L46 `test_dedup_capped_oldest_first(self, monkeypatch)` (method) — dedup dict is bounded; oldest entries evicted first.
- L65 `test_read_timestamps_capped_oldest_first(self, monkeypatch)` (method) — read_timestamps dict is bounded; oldest entries evicted first.
- L81 `test_cap_is_idempotent_under_cap(self, monkeypatch)` (method) — When containers are under cap, _cap_read_tracker_data is a no-op.
- L103 `test_cap_handles_missing_containers(self)` (method) — Missing sub-keys don't cause AttributeError.
- L111 `test_live_cap_applied_after_read_add(self, tmp_path, monkeypatch)` (method) — Live read_file path enforces caps.
- L136 `TestCompletionConsumedPrune` (class)
- L137 `test_prune_drops_completion_entry_with_expired_session(self)` (method) — When a finished session is pruned, _completion_consumed is
- L160 `test_prune_drops_completion_entry_for_lru_evicted(self)` (method) — Same contract for the LRU path (over MAX_PROCESSES).
- L190 `test_prune_clears_dangling_completion_entries(self)` (method) — Stale entries in _completion_consumed without a backing session
