---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_state/test_get_anchored_view.py

Symbols in `tests/hermes_state/test_get_anchored_view.py`.

- L13 `db(tmp_path)` (function)
- L17 `_seed_long_session(db, sid='s1', n=30)` (function) — Create a long session with alternating user/assistant prose. Returns ids ascending.
- L28 `TestWindowAndBookendShape` (class)
- L29 `test_returns_window_with_bookend_start_and_end(self, db)` (method)
- L42 `test_window_anchor_marked_correctly(self, db)` (method)
- L51 `TestBookendOverlap` (class) — Bookends shouldn't duplicate messages that are already in the window.
- L54 `test_bookend_start_empty_when_window_covers_session_head(self, db)` (method)
- L64 `test_bookend_end_empty_when_window_covers_session_tail(self, db)` (method)
- L72 `test_short_session_both_bookends_empty(self, db)` (method)
- L82 `TestRoleFiltering` (class)
- L83 `test_tool_role_filtered_from_window(self, db)` (method)
- L95 `test_anchor_preserved_even_when_tool_role(self, db)` (method)
- L105 `test_keep_roles_none_disables_filter(self, db)` (method)
- L114 `TestEmptyContentFilter` (class) — Tool-call-only assistant turns (empty content) should be skipped in bookends.
- L117 `test_empty_content_messages_excluded_from_bookends(self, db)` (method)
- L141 `TestAnchorValidation` (class)
- L142 `test_missing_anchor_returns_empty_view(self, db)` (method)
- L152 `TestSessionIsolation` (class) — Bookends must not cross session boundaries.
- L155 `test_bookends_only_from_anchor_session(self, db)` (method)
