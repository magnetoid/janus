---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_memory_nudge_counter_hydration.py

Symbols in `tests/run_agent/test_memory_nudge_counter_hydration.py`.

- L19 `_make_minimal_agent()` (function) — Build the smallest object that can run the hydration block.
- L33 `_run_hydration(conversation_history, memory_nudge_interval=10, prior_turn_count=0, prior_turns_since_memory=0)` (function) — Replicate the hydration block from run_agent.py:11128-11150.
- L54 `test_no_history_leaves_counters_at_zero()` (function)
- L60 `test_seven_user_turns_history_hydrates_to_seven()` (function) — Mid-cycle history: 7 prior user turns, interval 10 → counter at 7.
- L73 `test_thirteen_turns_history_wraps_via_modulo()` (function) — 13 prior user turns, interval 10 → counter at 3 (post-wrap), preserving cadence.
- L83 `test_idempotent_when_counters_already_set()` (function) — A cached agent with existing counters must NOT have them clobbered.
- L99 `test_zero_nudge_interval_disables_hydration_of_review_counter()` (function) — When memory.nudge_interval=0 (review disabled), don't touch the counter.
- L107 `test_assistant_only_history_does_not_advance_user_turn_count()` (function) — Defensive: only role==user messages contribute. Other roles are noise.
- L119 `test_production_code_contains_hydration_block()` (function) — Smoke test: confirm the hydration code is actually wired into
