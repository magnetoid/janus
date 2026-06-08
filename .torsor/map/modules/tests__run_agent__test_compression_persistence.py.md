---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_compression_persistence.py

Symbols in `tests/run_agent/test_compression_persistence.py`.

- L30 `TestFlushAfterCompression` (class) — Verify that compressed messages are flushed to the new session's SQLite
- L35 `_make_agent(self, session_db)` (method)
- L50 `test_flush_after_compression_with_long_history(self)` (method) — The actual bug: conversation_history longer than compressed messages.
- L103 `test_flush_with_stale_history_loses_messages(self)` (method) — Demonstrates the bug condition: stale conversation_history causes data loss.
- L140 `TestGatewayHistoryOffsetAfterSplit` (class) — Verify that when the agent creates a new session during compression,
- L145 `test_history_offset_zero_on_session_split(self)` (method) — When agent.session_id differs from the original, history_offset must be 0.
- L162 `test_history_offset_preserved_without_split(self)` (method) — When no compression happened, history_offset is the original length.
- L174 `test_new_messages_extraction_after_split(self)` (method) — After compression with offset=0, new_messages should be ALL agent messages.
- L191 `test_new_messages_empty_with_stale_offset(self)` (method) — Demonstrates the bug: stale offset produces empty new_messages.
