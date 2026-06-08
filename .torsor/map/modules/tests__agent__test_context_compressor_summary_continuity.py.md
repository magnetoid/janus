---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_context_compressor_summary_continuity.py

Symbols in `tests/agent/test_context_compressor_summary_continuity.py`.

- L8 `_compressor()` (function)
- L19 `_response(content: str)` (function)
- L26 `_messages_with_handoff(summary_body: str)` (function)
- L39 `test_existing_previous_summary_is_not_serialized_again_as_new_turn()` (function) — Same-process iterative compression should not feed the old handoff twice.
- L55 `test_resume_rehydrates_previous_summary_from_handoff_message()` (function) — After restart/resume, the persisted handoff should regain summary identity.
- L72 `test_handoff_in_protected_head_populates_previous_summary_before_update()` (function) — A resumed protected-head handoff should restore iterative-summary state.
