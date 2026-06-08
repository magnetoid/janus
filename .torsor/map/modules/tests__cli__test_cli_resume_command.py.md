---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_resume_command.py

Symbols in `tests/cli/test_cli_resume_command.py`.

- L6 `_make_cli()` (function)
- L22 `TestCliResumeCommand` (class)
- L23 `test_show_recent_sessions_includes_indexes_and_resume_hint(self, capsys)` (method)
- L41 `test_handle_resume_by_index_switches_to_numbered_session(self)` (method)
- L66 `test_handle_resume_by_index_out_of_range(self)` (method)
- L80 `test_handle_resume_strips_outer_brackets(self)` (method) — Users copy `<session_id>` from the usage hint literally.
- L102 `test_handle_resume_does_not_strip_partial_brackets(self)` (method) — Mismatched or single brackets must pass through unmodified.
- L122 `TestPendingResumeNumberedSelection` (class) — Bare `/resume` arms a one-shot prompt so the next bare number resumes.
- L131 `test_bare_resume_arms_pending_selection(self)` (method)
- L145 `test_bare_resume_no_sessions_does_not_arm(self)` (method)
- L155 `test_pending_number_resumes_selected_session(self)` (method)
- L182 `test_pending_out_of_range_consumed_with_message(self)` (method)
- L197 `test_pending_non_numeric_falls_through_and_disarms(self)` (method)
- L209 `test_no_pending_returns_false(self)` (method)
- L214 `test_pending_disarmed_by_other_command(self)` (method)
- L226 `TestRestoreSessionCwdMarkup` (class) — Regression: _restore_session_cwd must not crash with Rich MarkupError.
- L236 `test_missing_dir_does_not_raise_markup_error(self)` (method) — Session cwd gone → dim warning, no MarkupError.
- L250 `test_chdir_failure_does_not_raise_markup_error(self, tmp_path)` (method) — os.chdir fails → dim warning, no MarkupError.
- L275 `test_success_path_does_not_raise_markup_error(self, tmp_path)` (method) — Successful cwd switch → dim info, no MarkupError.
