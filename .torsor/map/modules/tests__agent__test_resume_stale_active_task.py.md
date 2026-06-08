---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_resume_stale_active_task.py

Symbols in `tests/agent/test_resume_stale_active_task.py`.

- L49 `test_latest_message_wins_over_inherited_active_task()` (function) — The handoff must explicitly privilege the latest user message over a
- L60 `test_no_resume_exactly_directive_can_hijack()` (function) — The directive that caused the hijack ("resume exactly from Active
- L66 `test_resumed_stale_handoff_gets_renormalized_to_current_prefix()` (function) — A handoff persisted under the OLD conflicting prefix (e.g. saved before
- L92 `test_legacy_prefix_handoff_also_renormalized()` (function) — The same upgrade applies to the oldest ``[CONTEXT SUMMARY]:`` handoff
- L102 `test_inherited_handoff_detected_in_resumed_protected_head()` (function) — On a resumed lineage the handoff commonly sits right after the system
- L125 `test_historical_prefixed_handoff_detected_and_stripped()` (function) — A pre-fix handoff (old conflicting prefix) inherited into a resumed
