---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_approval_ui.py

Symbols in `tests/cli/test_cli_approval_ui.py`.

- L11 `_FakeBuffer` (class)
- L12 `__init__(self, text='', cursor_position=None)` (method)
- L16 `reset(self, append_to_history=False)` (method)
- L21 `_make_cli_stub()` (function)
- L34 `_make_background_cli_stub()` (function)
- L69 `TestCliApprovalUi` (class)
- L70 `test_sudo_prompt_restores_existing_draft_after_response(self)` (method)
- L99 `test_approval_callback_includes_view_for_long_commands(self)` (method)
- L121 `test_handle_approval_selection_view_expands_in_place(self)` (method)
- L139 `test_approval_display_places_title_inside_box_not_border(self)` (method)
- L159 `test_approval_display_shows_full_command_after_view(self)` (method)
- L180 `test_approval_display_preserves_command_and_choices_with_long_description(self)` (method) — Regression: long tirith descriptions used to push approve/deny off-screen.
- L229 `test_approval_display_skips_description_on_very_short_terminal(self)` (method) — On a 12-row terminal, only the command and choices have room.
- L259 `test_approval_display_truncates_giant_command_in_view_mode(self)` (method) — If the user hits /view on a massive command, choices still render.
- L293 `test_background_task_registers_thread_local_approval_callbacks(self)` (method) — Background /btw tasks must use the prompt_toolkit approval UI.
- L342 `TestApprovalCallbackThreadLocalWiring` (class) — Regression guard for the thread-local callback freeze (#13617 / #13618).
- L353 `test_main_thread_registration_is_invisible_to_child_thread(self)` (method) — Confirms the underlying threading.local semantics that drove the bug.
- L381 `test_child_thread_registration_is_visible_and_cleared_in_finally(self)` (method) — The fix pattern: register INSIDE the worker thread, clear in finally.
