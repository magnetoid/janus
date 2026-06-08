---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_hermes_bootstrap.py

Symbols in `tests/test_hermes_bootstrap.py`.

- L34 `_fresh_import()` (function) — Return a freshly-imported hermes_bootstrap module.
- L45 `TestWindowsBehavior` (class) — Windows: the bootstrap does its job.
- L52 `test_env_vars_set_on_windows(self, monkeypatch)` (method)
- L66 `test_stdout_reconfigured_to_utf8_on_windows(self)` (method)
- L89 `test_child_process_inherits_utf8_mode(self)` (method) — A subprocess spawned from this process should inherit
- L117 `TestUserOptOut` (class) — If the user has explicitly set PYTHONUTF8 / PYTHONIOENCODING in
- L125 `test_user_pythonutf8_zero_preserved(self, monkeypatch)` (method)
- L136 `test_user_pythonioencoding_preserved(self, monkeypatch)` (method)
- L142 `TestPosixNoOp` (class) — POSIX: zero behavior change.  We don't touch LANG, LC_*, or any
- L147 `test_noop_on_fake_posix(self, monkeypatch)` (method) — Even when imported, the bootstrap function must return False
- L168 `test_real_posix_bootstrap_is_noop(self, monkeypatch)` (method) — On actual Linux/macOS, importing the module must not set
- L179 `TestIdempotence` (class) — Calling apply_windows_utf8_bootstrap() multiple times must be safe.
- L182 `test_second_call_returns_false(self)` (method)
- L190 `test_no_exceptions_on_repeated_calls(self)` (method)
- L196 `TestStdioReconfigureErrorHandling` (class) — If sys.stdout/stderr/stdin have been replaced with streams that
- L201 `test_non_reconfigurable_stream_does_not_crash(self, monkeypatch)` (method) — Replace sys.stdout with a BytesIO (no reconfigure method),
- L216 `test_reconfigure_oserror_is_caught(self, monkeypatch)` (method) — If reconfigure() itself raises (closed stream, etc.), swallow
- L234 `TestEntryPointsImportBootstrap` (class) — Every Hermes entry point must import hermes_bootstrap as its
- L252 `test_entry_point_imports_bootstrap(self, path)` (method) — The file must contain 'import hermes_bootstrap' and that
