---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_base_environment.py

Symbols in `tests/tools/test_base_environment.py`.

- L12 `_TestableEnv` (class) — Concrete subclass for testing base class methods.
- L15 `__init__(self, cwd='/tmp', timeout=10)` (method)
- L18 `_run_bash(self, cmd_string, *, login=False, timeout=120, stdin_data=None)` (method)
- L21 `cleanup(self)` (method)
- L25 `TestWrapCommand` (class)
- L26 `test_basic_shape(self)` (method)
- L40 `test_no_snapshot_skips_source(self)` (method)
- L47 `test_single_quote_escaping(self)` (method)
- L54 `test_tilde_not_quoted(self)` (method)
- L62 `test_tilde_subpath_with_spaces_uses_home_and_quotes_suffix(self)` (method)
- L70 `test_tilde_slash_maps_to_home(self)` (method)
- L78 `test_hyphen_prefixed_workdir_is_passed_after_double_dash(self)` (method)
- L85 `test_cd_failure_exit_126(self)` (method)
- L93 `TestExtractCwdFromOutput` (class)
- L94 `test_happy_path(self)` (method)
- L105 `test_missing_marker(self)` (method)
- L112 `test_marker_in_command_output(self)` (method) — If the marker appears in command output AND as the real marker,
- L124 `test_output_cleaned(self)` (method)
- L136 `TestEmbedStdinHeredoc` (class)
- L137 `test_heredoc_format(self)` (method)
- L144 `test_unique_delimiter_each_call(self)` (method)
- L154 `TestInitSessionFailure` (class)
- L155 `test_snapshot_ready_false_on_failure(self)` (method)
- L166 `test_login_flag_when_snapshot_not_ready(self)` (method) — When _snapshot_ready=False, execute() should pass login=True to _run_bash.
- L188 `TestCwdMarker` (class)
- L189 `test_marker_contains_session_id(self)` (method)
- L193 `test_unique_per_instance(self)` (method)
