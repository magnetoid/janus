---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_store_prune.py

Symbols in `tests/gateway/test_session_store_prune.py`.

- L27 `_make_store(tmp_path, max_age_days: int=90, has_active_processes_fn=None)` (function) — Build a SessionStore bypassing SQLite/disk-load side effects.
- L44 `_entry(key: str, age_days: float, *, suspended: bool=False, session_id: str | None=None)` (function)
- L58 `TestPruneBasics` (class)
- L59 `test_prune_removes_entries_past_max_age(self, tmp_path)` (method)
- L70 `test_prune_uses_updated_at_not_created_at(self, tmp_path)` (method) — A session created long ago but updated recently must be kept.
- L89 `test_prune_disabled_when_max_age_is_zero(self, tmp_path)` (method)
- L97 `test_prune_disabled_when_max_age_is_negative(self, tmp_path)` (method)
- L104 `test_prune_skips_suspended_entries(self, tmp_path)` (method) — /stop-suspended sessions must be kept for later resume.
- L118 `test_prune_skips_entries_with_active_processes(self, tmp_path)` (method) — Sessions with active bg processes aren't pruned even if old.
- L148 `test_prune_active_check_uses_session_key_not_session_id(self, tmp_path)` (method) — Regression guard: a callback that only recognises session_ids must
- L168 `test_prune_does_not_write_disk_when_no_removals(self, tmp_path)` (method) — If nothing is evictable, _save() should NOT be called.
- L180 `test_prune_writes_disk_after_removal(self, tmp_path)` (method)
- L191 `test_prune_is_thread_safe(self, tmp_path)` (method) — Prune acquires _lock internally; concurrent update_session is safe.
- L224 `TestPrunePersistsToDisk` (class)
- L225 `test_prune_rewrites_sessions_json(self, tmp_path)` (method) — After prune, sessions.json on disk reflects the new dict.
- L249 `TestGatewayConfigSerialization` (class)
- L250 `test_session_store_max_age_days_defaults_to_90(self)` (method)
- L254 `test_session_store_max_age_days_roundtrips(self)` (method)
- L259 `test_session_store_max_age_days_missing_defaults_90(self)` (method) — Loading an old config (pre-this-field) falls back to default.
- L264 `test_session_store_max_age_days_negative_coerced_to_zero(self)` (method) — A negative value (accidental or hostile) becomes 0 (disabled).
- L269 `test_session_store_max_age_days_bad_type_falls_back(self)` (method) — Non-int values fall back to the default, not a crash.
- L275 `TestGatewayWatcherCallsPrune` (class) — The session_expiry_watcher should call prune_old_entries once per hour.
- L278 `test_prune_gate_fires_on_first_tick(self)` (method) — First watcher tick has _last_prune_ts=0, so the gate opens.
- L290 `test_prune_gate_suppresses_within_interval(self)` (method)
