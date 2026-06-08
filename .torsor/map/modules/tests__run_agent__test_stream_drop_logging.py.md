---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_stream_drop_logging.py

Symbols in `tests/run_agent/test_stream_drop_logging.py`.

- L28 `_make_agent()` (function)
- L38 `test_stream_diag_init_returns_well_formed_dict()` (function)
- L48 `_FakeHeaders` (class)
- L49 `__init__(self, d)` (method)
- L50 `get(self, k, default=None)` (method)
- L53 `_FakeResponse` (class)
- L54 `__init__(self, headers, status=200)` (method)
- L59 `test_stream_diag_capture_response_collects_known_headers()` (function)
- L80 `test_stream_diag_capture_response_safe_with_none()` (function)
- L88 `test_flatten_exception_chain_walks_cause()` (function)
- L101 `test_flatten_exception_chain_caps_depth()` (function) — Chain renders no more than 4 deep so log lines stay bounded.
- L114 `test_log_stream_retry_includes_diagnostic_fields(caplog)` (function)
- L173 `test_log_stream_retry_works_without_diag(caplog)` (function) — diag is optional — older callers / unit tests still work.
- L197 `test_emit_stream_drop_ui_includes_elapsed_when_available()` (function)
- L219 `test_emit_stream_drop_ui_omits_suffix_without_diag()` (function) — When there's no diag, no suffix — line stays compact.
- L240 `test_quiet_mode_does_not_clobber_runagent_logger_level()` (function) — Regression guard for the parent fix — must persist across this PR.
