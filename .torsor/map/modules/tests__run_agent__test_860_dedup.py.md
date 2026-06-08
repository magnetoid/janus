---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_860_dedup.py

Symbols in `tests/run_agent/test_860_dedup.py`.

- L21 `TestFlushDeduplication` (class) — Verify _flush_messages_to_session_db tracks what it already wrote.
- L24 `_make_agent(self, session_db)` (method) — Create a minimal AIAgent with a real session DB.
- L42 `test_flush_writes_only_new_messages(self)` (method) — First flush writes all new messages, second flush writes none.
- L74 `test_flush_writes_incrementally(self)` (method) — Messages added between flushes are written exactly once.
- L105 `test_persist_session_multiple_calls_no_duplication(self)` (method) — Multiple _persist_session calls don't duplicate DB entries.
- L132 `test_flush_reset_after_compression(self)` (method) — After compression creates a new session, flush index resets.
- L177 `TestAppendToTranscriptSkipDb` (class) — Verify skip_db=True skips the SQLite write.
- L180 `test_skip_db_prevents_sqlite_write(self, tmp_path)` (method) — With skip_db=True and a real DB, message does NOT appear in SQLite.
- L205 `test_default_writes_to_sqlite(self, tmp_path)` (method) — Without skip_db, message appears in SQLite.
- L235 `TestFlushIdxInit` (class) — Verify _last_flushed_db_idx is properly initialized.
- L238 `test_init_zero(self)` (method) — Agent starts with _last_flushed_db_idx = 0.
- L252 `test_no_session_db_noop(self)` (method) — Without session_db, flush is a no-op and doesn't crash.
