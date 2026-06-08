---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_hangup_protection.py

Symbols in `tests/hermes_cli/test_update_hangup_protection.py`.

- L29 `TestUpdateOutputStream` (class)
- L30 `test_write_mirrors_to_both_original_and_log(self)` (method)
- L40 `test_write_continues_after_broken_original(self)` (method) — When the terminal disconnects, original.write raises BrokenPipeError.
- L65 `test_write_tolerates_oserror_and_valueerror(self)` (method) — OSError (EIO) and ValueError (closed file) should also be absorbed.
- L84 `test_log_failure_does_not_abort_write(self)` (method) — Even if the log file write raises, the original write must still happen.
- L100 `test_flush_tolerates_broken_original(self)` (method)
- L113 `test_isatty_delegates_to_original(self)` (method)
- L127 `test_isatty_returns_false_after_broken(self)` (method)
- L142 `test_getattr_delegates_unknown_attrs(self)` (method)
- L161 `TestInstallHangupProtection` (class)
- L162 `test_gateway_mode_is_noop(self)` (method) — In gateway mode the process is already detached — don't touch stdio or signals.
- L182 `test_installs_sighup_ignore(self, tmp_path, monkeypatch)` (method) — SIGHUP should be set to SIG_IGN so SSH disconnect doesn't kill the update.
- L200 `test_wraps_stdout_and_stderr_with_mirror(self, tmp_path, monkeypatch)` (method)
- L231 `test_logs_dir_created_if_missing(self, tmp_path, monkeypatch)` (method)
- L247 `test_non_fatal_if_log_setup_fails(self, monkeypatch)` (method) — If get_hermes_home() raises, stdio must be left untouched but SIGHUP still handled.
- L283 `TestFinalizeUpdateOutput` (class)
- L284 `test_none_state_is_noop(self)` (method)
- L287 `test_restores_streams_and_closes_log(self, tmp_path, monkeypatch)` (method)
- L306 `test_skipped_install_leaves_stdio_alone(self)` (method) — When install failed (state['installed']=False) finalize should not
