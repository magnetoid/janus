---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_title_command.py

Symbols in `tests/gateway/test_title_command.py`.

- L17 `_make_event(text='/title', platform=Platform.TELEGRAM, user_id='12345', chat_id='67890')` (function) — Build a MessageEvent for testing.
- L29 `_make_runner(session_db=None)` (function) — Create a bare GatewayRunner with a mock session_store and optional session_db.
- L53 `TestHandleTitleCommand` (class) — Tests for GatewayRunner._handle_title_command.
- L57 `test_set_title(self, tmp_path)` (method) — Setting a title returns confirmation.
- L74 `test_show_title_when_set(self, tmp_path)` (method) — Showing title when one is set returns the title.
- L89 `test_show_title_when_not_set(self, tmp_path)` (method) — Showing title when none is set returns usage hint.
- L103 `test_title_conflict(self, tmp_path)` (method) — Setting a title already used by another session returns error.
- L119 `test_no_session_db(self)` (method) — Returns error when session database is not available.
- L127 `test_title_too_long(self, tmp_path)` (method) — Setting a title that exceeds max length returns error.
- L142 `test_title_control_chars_sanitized(self, tmp_path)` (method) — Control characters are stripped and sanitized title is stored.
- L156 `test_title_only_control_chars(self, tmp_path)` (method) — Title with only control chars returns empty error.
- L169 `test_works_across_platforms(self, tmp_path)` (method) — The /title command works for Discord, Slack, and WhatsApp too.
- L189 `TestTitleInHelp` (class) — Verify /title appears in help text and known commands.
- L193 `test_title_in_help_output(self)` (method) — The /help output includes /title.
- L203 `test_title_is_known_command(self)` (method) — The /title command is in the _known_commands set.
- L216 `TestResetCommandWithTitle` (class) — Tests for GatewayRunner._handle_reset_command with a title argument.
- L220 `test_reset_command_with_title(self)` (method) — Sending /new <title> resets session and sets the title.
- L280 `test_reset_command_duplicate_title_surfaces_warning(self)` (method) — /new <title> with an already-in-use title returns a warning in the reply.
- L348 `TestNewInHelp` (class) — Verify /new appears in help text with the [name] args hint.
- L351 `test_new_command_in_help_output(self)` (method) — The gateway help output includes /new with the [name] hint.
