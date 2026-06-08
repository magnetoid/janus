---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_summary_prefix_semantics.py

Symbols in `tests/agent/test_summary_prefix_semantics.py`.

- L24 `test_no_resume_exactly_directive()` (function) — The prefix must not tell the model to resume Active Task verbatim.
- L29 `test_latest_message_wins_on_conflict()` (function) — The prefix must explicitly say latest user message wins on conflict.
- L37 `test_reverse_signals_called_out()` (function) — Reverse signals (stop/undo/never mind/topic change) must be named so
- L51 `test_summary_marked_reference_only()` (function) — The REFERENCE ONLY framing must remain — it's the entire point.
- L58 `test_memory_authority_preserved()` (function) — The fix must not weaken the MEMORY.md / USER.md authority clause.
