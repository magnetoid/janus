---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_lazy_session_regressions.py

Symbols in `tests/test_lazy_session_regressions.py`.

- L22 `_make_session_db(tmp_path)` (function) — Create a real SessionDB for integration-style tests.
- L29 `_tui_session(agent=None, session_key='session-key-old', **extra)` (function) — Minimal TUI gateway session dict matching server._sessions values.
- L53 `TestFinalizeSessionUsesAgentSessionId` (class) — After compression rotates agent.session_id, _finalize_session()
- L58 `test_finalize_targets_agent_session_id_not_stale_key(self, tmp_path)` (method) — Reproduction: agent.session_id rotated by compression, but
- L104 `test_finalize_fallback_to_session_key_when_agent_is_none(self, tmp_path)` (method) — When agent is None (e.g. session never fully initialized),
- L127 `TestSyncSessionKeyAfterAutoCompress` (class) — When auto-compression fires inside run_conversation(), the post-turn
- L132 `test_session_key_synced_after_run_conversation_with_compression(self, monkeypatch)` (method) — Simulate: run_conversation() internally compresses and rotates
- L208 `TestPendingTitleValueError` (class) — When set_session_title raises ValueError (duplicate/invalid title),
- L212 `test_valueerror_clears_pending_title(self, monkeypatch)` (method) — ValueError from set_session_title should drop pending_title.
- L266 `test_other_exception_keeps_pending_title_for_retry(self, monkeypatch)` (method) — Non-ValueError exceptions should keep pending_title for retry.
- L325 `TestGatewaySurfacesNullResponse` (class) — When the agent does work (api_calls > 0) but returns no final_response,
- L330 `test_partial_response_surfaces_error(self)` (method) — Agent returns partial=True with no response → user sees error.
- L350 `test_interrupted_response_stays_empty(self)` (method) — Interrupted agent → response stays empty (platform handles UX).
- L368 `test_failed_context_overflow(self)` (method) — Agent failed with context overflow → specific guidance message.
- L387 `test_failed_generic_error(self)` (method) — Agent failed with non-context error → generic error message.
- L406 `test_nonempty_response_passes_through(self)` (method) — Non-empty response is returned unchanged.
- L423 `TestFinalizeOrphanedCompressionSessions` (class) — The prune migration marks ghost compression continuations as ended.
- L426 `test_marks_ghost_continuation_with_compression_parent(self, tmp_path)` (method) — Ghost session with compression-ended parent + messages → finalized.
- L459 `test_skips_session_without_parent(self, tmp_path)` (method) — Ghost session without parent_session_id is NOT a compression
- L477 `test_skips_recent_sessions(self, tmp_path)` (method) — Sessions younger than 7 days are not touched.
- L495 `test_skips_sessions_with_end_reason(self, tmp_path)` (method) — Properly finalized sessions (even without api_call_count) are skipped.
- L522 `test_skips_session_with_non_compression_parent(self, tmp_path)` (method) — Child session whose parent was NOT ended by compression should
- L549 `test_skips_sessions_without_messages(self, tmp_path)` (method) — Empty sessions (no messages) are NOT targeted by this prune —
- L576 `test_titled_ghost_with_parent_is_caught(self, tmp_path)` (method) — Ghost continuation that HAS a title (propagated from parent by
