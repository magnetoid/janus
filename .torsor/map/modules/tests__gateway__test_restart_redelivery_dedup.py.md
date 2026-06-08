---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_restart_redelivery_dedup.py

Symbols in `tests/gateway/test_restart_redelivery_dedup.py`.

- L19 `_make_restart_event(update_id: int | None=100)` (function)
- L30 `test_restart_handler_writes_dedup_marker_with_update_id(tmp_path, monkeypatch)` (function) — First /restart writes .restart_last_processed.json with the triggering update_id.
- L51 `test_redelivered_restart_with_same_update_id_is_ignored(tmp_path, monkeypatch)` (function) — A /restart with update_id <= recorded marker is silently ignored as a redelivery.
- L75 `test_redelivered_restart_with_older_update_id_is_ignored(tmp_path, monkeypatch)` (function) — update_id strictly LESS than the recorded one is also a redelivery.
- L100 `test_fresh_restart_with_higher_update_id_is_processed(tmp_path, monkeypatch)` (function) — A NEW /restart from the user (higher update_id) bypasses the dedup guard.
- L128 `test_stale_marker_older_than_5min_does_not_block(tmp_path, monkeypatch)` (function) — A marker older than the 5-minute window is ignored — fresh /restart proceeds.
- L152 `test_no_marker_file_allows_restart(tmp_path, monkeypatch)` (function) — Clean gateway start (no prior marker) processes /restart normally.
- L168 `test_corrupt_marker_file_is_treated_as_absent(tmp_path, monkeypatch)` (function) — Malformed JSON in the marker file doesn't crash — /restart proceeds.
- L187 `test_event_without_update_id_bypasses_dedup(tmp_path, monkeypatch)` (function) — Events with no platform_update_id (non-Telegram, CLI fallback) aren't gated.
- L211 `test_different_platform_bypasses_dedup(tmp_path, monkeypatch)` (function) — Marker from Telegram doesn't block a /restart from another platform.
