---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_destructive_slash_confirm.py

Symbols in `tests/cli/test_destructive_slash_confirm.py`.

- L14 `_bound(fn, instance)` (function) — Bind an unbound method to a stand-in instance.
- L19 `_make_self(prompt_response)` (function) — Build a minimal stand-in 'self' for _confirm_destructive_slash.
- L34 `test_gate_off_returns_once_without_prompting()` (function) — When approvals.destructive_slash_confirm is False, return 'once'
- L52 `test_gate_on_choice_once_returns_once()` (function) — When the gate is on and the user picks '1', return 'once'.
- L69 `test_gate_on_choice_cancel_returns_none()` (function) — When the user picks '3' (cancel), return None — caller must abort.
- L86 `test_gate_on_no_input_returns_none()` (function) — No input (None / EOF / Ctrl-C) treated as cancel.
- L103 `test_gate_on_unknown_choice_returns_none()` (function) — Garbage input is treated as cancel — fail safe, don't destroy state.
- L120 `test_gate_on_choice_always_persists_and_returns_always()` (function) — User picks 'always' → returns 'always' AND
- L144 `test_gate_default_true_when_config_missing()` (function) — If load_cli_config raises or returns malformed data, treat as
- L162 `test_slash_confirm_modal_number_selection_submits_without_raw_input()` (function) — Pressing 2 in the TUI modal should resolve to Always Approve directly.
- L188 `test_slash_confirm_display_fragments_include_choice_mapping()` (function) — The modal itself must show what 1/2/3 mean, not only 'Choice [1/2/3]'.
- L224 `test_split_destructive_skip_recognized_tokens()` (function) — ``now``, ``--yes``, and ``-y`` are recognized as skip tokens.
- L233 `test_split_destructive_skip_strips_command_word()` (function) — Leading ``/cmd`` token is stripped; remaining args survive.
- L241 `test_split_destructive_skip_case_insensitive()` (function) — Token matching is case-insensitive but not a substring match.
- L250 `test_split_destructive_skip_handles_empty_and_none()` (function) — Defensive against missing/empty input.
- L259 `test_confirm_destructive_slash_now_skips_modal()` (function) — ``/reset now`` skips the modal even when the gate is on.
- L288 `test_confirm_destructive_slash_yes_flag_skips_modal()` (function) — ``--yes`` flag is equivalent to ``now``.
- L315 `test_confirm_destructive_slash_no_skip_token_still_prompts()` (function) — Without a skip token the gate-on path still consults the modal.
