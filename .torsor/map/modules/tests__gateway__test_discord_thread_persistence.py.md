---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_thread_persistence.py

Symbols in `tests/gateway/test_discord_thread_persistence.py`.

- L13 `TestDiscordThreadPersistence` (class) — Thread IDs are saved to disk and reloaded on init.
- L16 `_make_adapter(self, tmp_path)` (method) — Build a minimal DiscordAdapter with HERMES_HOME pointed at tmp_path.
- L25 `test_starts_empty_when_no_state_file(self, tmp_path)` (method)
- L29 `test_track_thread_persists_to_disk(self, tmp_path)` (method)
- L40 `test_threads_survive_restart(self, tmp_path)` (method) — Threads tracked by one adapter instance are visible to the next.
- L51 `test_duplicate_track_does_not_double_save(self, tmp_path)` (method)
- L60 `test_caps_at_max_tracked_threads(self, tmp_path)` (method)
- L71 `test_capacity_keeps_newest_thread_when_existing_state_is_full(self, tmp_path)` (method) — A newly joined thread must not be evicted by unordered set iteration.
- L85 `test_corrupted_state_file_falls_back_to_empty(self, tmp_path)` (method)
- L91 `test_missing_hermes_home_does_not_crash(self, tmp_path)` (method) — Load/save tolerate missing directories.
