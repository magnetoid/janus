---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_goal_interrupt.py

Symbols in `tests/cli/test_cli_goal_interrupt.py`.

- L28 `hermes_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME so SessionDB.state_meta writes stay hermetic.
- L42 `_make_cli_with_goal(session_id: str, goal_text: str='build a thing')` (function) — Build a minimal HermesCLI stub with an active goal wired in.
- L69 `TestInterruptAutoPause` (class)
- L70 `test_interrupted_turn_pauses_goal_and_skips_continuation(self, hermes_home)` (method) — Ctrl+C mid-turn must auto-pause the goal, not queue another round.
- L100 `test_interrupted_turn_is_resumable(self, hermes_home)` (method) — After auto-pause from Ctrl+C, /goal resume puts it back to active.
- L116 `TestEmptyResponseSkip` (class)
- L117 `test_empty_response_does_not_invoke_judge(self, hermes_home)` (method) — Whitespace-only replies skip judging (transient failure guard).
- L137 `test_no_assistant_message_skipped(self, hermes_home)` (method) — Conversation with zero assistant replies must not trip the judge.
- L156 `TestHealthyTurnStillRuns` (class)
- L157 `test_clean_response_enqueues_continuation_when_judge_says_continue(self, hermes_home)` (method) — Sanity check: the hook still works in the happy path.
- L182 `test_clean_response_marks_done_when_judge_says_done(self, hermes_home)` (method)
- L200 `TestInterruptFlagLifecycle` (class)
- L201 `test_chat_resets_flag_at_entry(self, hermes_home)` (method) — chat() must reset _last_turn_interrupted at the top of each turn.
