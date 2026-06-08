---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_dm_thread_seeding.py

Symbols in `tests/gateway/test_session_dm_thread_seeding.py`.

- L24 `store(tmp_path, monkeypatch)` (function) — SessionStore with SQLite — load_transcript reads from DB only.
- L39 `_dm_source(platform=Platform.SLACK, chat_id='D123', thread_id=None, user_id='U1')` (function)
- L49 `_group_source(platform=Platform.SLACK, chat_id='C456', thread_id=None, user_id='U1')` (function)
- L65 `TestDMThreadIsolation` (class) — Thread sessions must start empty — no parent transcript seeding.
- L68 `test_thread_session_starts_empty(self, store)` (method) — New DM thread session should NOT inherit parent's transcript.
- L81 `test_parent_transcript_unaffected_by_thread(self, store)` (method) — Creating a thread session should not alter parent's transcript.
- L98 `test_multiple_threads_are_independent(self, store)` (method) — Each thread from the same parent starts empty and stays independent.
- L125 `test_existing_thread_session_preserved(self, store)` (method) — Returning to an existing thread session should not reset it.
- L148 `TestDMThreadIsolationEdgeCases` (class) — Edge cases — threads always start empty regardless of context.
- L151 `test_group_thread_starts_empty(self, store)` (method) — Group/channel threads should also start empty.
- L164 `test_thread_without_parent_session_starts_empty(self, store)` (method) — Thread session without a parent DM session should start empty.
- L172 `test_dm_without_thread_starts_empty(self, store)` (method) — Top-level DMs (no thread_id) should start empty as always.
- L181 `TestDMThreadIsolationCrossPlatform` (class) — Verify thread isolation is consistent across all platforms.
- L185 `test_thread_starts_empty_across_platforms(self, store, platform)` (method) — DM thread sessions start empty regardless of platform.
