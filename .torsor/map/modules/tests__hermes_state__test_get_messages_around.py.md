---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_state/test_get_messages_around.py

Symbols in `tests/hermes_state/test_get_messages_around.py`.

- L14 `db(tmp_path)` (function)
- L18 `_seed(db, sid='s1', n=10)` (function) — Create session with n alternating user/assistant messages, return ids ascending.
- L30 `TestBasicWindow` (class)
- L31 `test_returns_window_around_anchor(self, db)` (method)
- L42 `test_window_zero_returns_only_anchor(self, db)` (method)
- L50 `test_negative_window_clamps_to_zero(self, db)` (method)
- L58 `TestBoundaryDetection` (class) — messages_before / messages_after tell the agent it's at start/end.
- L61 `test_at_session_start_messages_before_is_short(self, db)` (method)
- L70 `test_at_session_end_messages_after_is_short(self, db)` (method)
- L77 `test_window_larger_than_session(self, db)` (method)
- L86 `TestAnchorValidation` (class)
- L87 `test_missing_anchor_returns_empty(self, db)` (method)
- L94 `test_anchor_in_different_session_returns_empty(self, db)` (method)
- L102 `TestScrollPattern` (class) — The forward/backward scroll loop the agent will run.
- L105 `test_scroll_forward_re_anchored_on_last_id(self, db)` (method)
- L117 `test_scroll_backward_re_anchored_on_first_id(self, db)` (method)
- L128 `TestContentHydration` (class)
- L129 `test_content_is_decoded(self, db)` (method)
- L136 `test_tool_calls_deserialized(self, db)` (method)
