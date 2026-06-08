---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_notify_on_complete.py

Symbols in `tests/tools/test_notify_on_complete.py`.

- L24 `registry()` (function) — Create a fresh ProcessRegistry.
- L29 `_make_session(sid='proc_test_notify', command='echo hello', task_id='t1', exited=False, exit_code=None, output='', notify_on_complete=False)` (function)
- L55 `TestProcessSessionField` (class)
- L56 `test_default_false(self)` (method)
- L60 `test_set_true(self)` (method)
- L69 `TestCompletionQueue` (class)
- L70 `test_queue_exists(self, registry)` (method)
- L74 `test_move_to_finished_no_notify(self, registry)` (method) — Processes without notify_on_complete don't enqueue.
- L84 `test_move_to_finished_with_notify(self, registry)` (method) — Processes with notify_on_complete push to queue.
- L104 `test_move_to_finished_nonzero_exit(self, registry)` (method) — Nonzero exit codes are captured correctly.
- L121 `test_move_to_finished_idempotent_no_duplicate(self, registry)` (method) — Calling _move_to_finished twice must NOT enqueue two notifications.
- L141 `test_output_truncated_to_2000(self, registry)` (method) — Long output is truncated to last 2000 chars.
- L157 `test_multiple_completions_queued(self, registry)` (method) — Multiple notify processes all push to the same queue.
- L183 `TestCheckpointNotify` (class)
- L184 `test_checkpoint_includes_notify(self, registry, tmp_path)` (method)
- L194 `test_checkpoint_without_notify(self, registry, tmp_path)` (method)
- L203 `test_recover_preserves_notify(self, registry, tmp_path)` (method)
- L218 `test_recover_requeues_notify_watchers(self, registry, tmp_path)` (method)
- L242 `test_recover_defaults_false(self, registry, tmp_path)` (method) — Old checkpoint entries without the field default to False.
- L262 `TestTerminalSchema` (class)
- L263 `test_schema_has_notify_on_complete(self)` (method)
- L270 `test_handler_passes_notify(self)` (method) — _handle_terminal passes notify_on_complete to terminal_tool.
- L286 `TestCodeExecutionBlocked` (class)
- L287 `test_notify_on_complete_blocked_in_sandbox(self)` (method)
- L296 `TestCompletionConsumed` (class) — Test that wait/poll/log suppress redundant completion notifications.
- L299 `test_wait_marks_completion_consumed(self, registry)` (method) — wait() returning exited status marks session as consumed.
- L319 `test_poll_marks_completion_consumed(self, registry)` (method) — poll() returning exited status marks session as consumed.
- L330 `test_log_marks_completion_consumed(self, registry)` (method) — read_log() on exited session marks as consumed.
- L341 `test_running_process_not_consumed(self, registry)` (method) — poll() on a still-running process does not mark as consumed.
- L363 `_silent_bg_base_config(tmp_path)` (function)
- L375 `_silent_bg_harness(monkeypatch, tmp_path)` (function) — Common test fixture: patch enough of terminal_tool to spawn a fake
- L408 `test_background_without_notify_emits_silent_process_hint(monkeypatch, tmp_path)` (function) — The footgun case (May 2026 PR #31231): bg=True alone runs silently
- L434 `test_background_with_notify_does_not_emit_hint(monkeypatch, tmp_path)` (function) — The correct shape — bg+notify together — must not nag.
- L455 `test_background_with_watch_patterns_does_not_emit_hint(monkeypatch, tmp_path)` (function) — watch_patterns is the other legitimate non-silent shape — also no hint.
- L475 `test_foreground_command_does_not_emit_hint(monkeypatch, tmp_path)` (function) — Hint only applies to background processes — foreground returns its
- L520 `test_homebrew_ci_poller_via_statusCheckRollup_emits_hint(monkeypatch, tmp_path)` (function) — The canonical anti-pattern: jq pipeline parsing statusCheckRollup
- L553 `test_homebrew_ci_poller_via_gh_pr_checks_piped_to_jq_emits_hint(monkeypatch, tmp_path)` (function) — `gh pr checks` doesn't emit JSON, so piping it to jq is a confused-
- L579 `test_canonical_column2_awk_poller_does_not_emit_homebrew_hint(monkeypatch, tmp_path)` (function) — The blessed column-2 awk-on-tabs poller from green-ci-policy is the
- L611 `test_canonical_gh_pr_checks_exit_code_loop_does_not_emit_hint(monkeypatch, tmp_path)` (function) — The blessed exit-code-driven snippet from green-ci-policy is exactly
- L640 `test_non_ci_background_command_does_not_emit_homebrew_hint(monkeypatch, tmp_path)` (function) — A long-running task that happens to use awk for unrelated reasons
