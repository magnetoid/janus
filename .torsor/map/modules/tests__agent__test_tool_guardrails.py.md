---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_tool_guardrails.py

Symbols in `tests/agent/test_tool_guardrails.py`.

- L14 `test_tool_call_signature_hashes_canonical_nested_unicode_args_without_exposing_raw_args()` (function)
- L36 `test_default_config_is_soft_warning_only_with_hard_stop_disabled()` (function)
- L49 `test_config_parses_nested_warn_and_hard_stop_thresholds()` (function)
- L77 `test_default_repeated_identical_failed_call_warns_without_blocking()` (function)
- L95 `test_hard_stop_enabled_blocks_repeated_exact_failure_before_next_execution()` (function)
- L121 `test_success_resets_exact_signature_failure_streak()` (function)
- L135 `test_file_mutation_lint_error_result_is_not_a_tool_failure()` (function)
- L150 `test_same_tool_varying_args_warns_by_default_without_halting()` (function)
- L170 `test_hard_stop_enabled_halts_same_tool_varying_args_failure_streak()` (function)
- L191 `test_idempotent_no_progress_repeated_result_warns_without_blocking_by_default()` (function)
- L208 `test_hard_stop_enabled_blocks_idempotent_no_progress_future_repeat()` (function)
- L231 `test_mutating_or_unknown_tools_are_not_blocked_for_repeated_identical_success_output_by_default()` (function)
- L243 `test_reset_for_turn_clears_bounded_guardrail_state()` (function)
