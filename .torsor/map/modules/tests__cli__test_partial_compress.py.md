---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_partial_compress.py

Symbols in `tests/cli/test_partial_compress.py`.

- L16 `_history(n_pairs: int)` (function) — Build n_pairs of (user, assistant) exchanges.
- L28 `test_empty_args_is_full_compress()` (function)
- L35 `test_here_defaults_keep_last()` (function)
- L42 `test_here_with_count()` (function)
- L49 `test_up_to_here_alias()` (function)
- L56 `test_keep_flag_forms()` (function)
- L64 `test_focus_topic_when_not_boundary_form()` (function)
- L70 `test_here_count_clamped_low_and_high()` (function)
- L77 `test_here_garbage_count_falls_back_to_default()` (function)
- L86 `test_split_keeps_last_n_exchanges()` (function)
- L96 `test_split_default_keep()` (function)
- L104 `test_split_tail_always_starts_on_user()` (function)
- L122 `test_split_degenerate_returns_no_tail()` (function)
- L131 `test_split_empty_history()` (function)
- L137 `test_split_rejoin_preserves_all_messages()` (function)
- L146 `_roles(msgs)` (function)
- L150 `_no_consecutive_dupes(msgs)` (function)
- L155 `test_rejoin_valid_seam_assistant_then_user()` (function)
- L166 `test_rejoin_user_user_seam_merges()` (function)
- L178 `test_rejoin_assistant_assistant_seam_merges()` (function)
- L188 `test_rejoin_empty_tail_returns_head()` (function)
- L193 `test_rejoin_tool_seam_left_alone()` (function)
