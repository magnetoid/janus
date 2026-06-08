---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_manual_compress.py

Symbols in `tests/cli/test_manual_compress.py`.

- L8 `_make_history()` (function)
- L17 `test_manual_compress_reports_noop_without_success_banner(capsys)` (function)
- L41 `test_manual_compress_explains_when_token_estimate_rises(capsys)` (function)
- L73 `test_manual_compress_syncs_session_id_after_split()` (function) — Regression for cli.session_id desync after /compress.
- L114 `test_manual_compress_flushes_compressed_history_to_child_session_db()` (function) — Manual /compress must persist the handoff in the continuation DB.
- L149 `test_manual_compress_does_not_flush_full_history_when_session_id_unchanged()` (function)
- L165 `test_manual_compress_no_sync_when_session_id_unchanged()` (function) — If compression is a no-op (agent.session_id didn't change), the CLI
