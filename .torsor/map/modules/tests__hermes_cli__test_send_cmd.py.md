---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_send_cmd.py

Symbols in `tests/hermes_cli/test_send_cmd.py`.

- L23 `_parse(argv)` (function) — Build the top-level parser and return the parsed args for ``argv``.
- L33 `_FakeTool` (class) — Replacement for ``tools.send_message_tool.send_message_tool``.
- L36 `__init__(self, payload)` (method)
- L40 `__call__(self, args, **_kw)` (method)
- L46 `fake_tool(monkeypatch)` (function) — Install a fake send_message_tool and return the stub for inspection.
- L67 `test_positional_message_success(fake_tool, capsys)` (function)
- L79 `test_stdin_message(fake_tool, monkeypatch, capsys)` (function)
- L92 `test_file_message(fake_tool, tmp_path)` (function)
- L102 `test_file_dash_means_stdin(fake_tool, monkeypatch)` (function)
- L111 `test_subject_prepends_header(fake_tool)` (function)
- L119 `test_json_mode_emits_payload(fake_tool, capsys)` (function)
- L130 `test_quiet_suppresses_stdout(fake_tool, capsys)` (function)
- L144 `test_missing_target(fake_tool, capsys, monkeypatch)` (function)
- L155 `test_missing_message(fake_tool, capsys, monkeypatch)` (function)
- L165 `test_file_not_found_is_usage_error(fake_tool, capsys, monkeypatch)` (function)
- L175 `test_file_decode_error_is_usage_error(fake_tool, capsys, monkeypatch, tmp_path)` (function)
- L188 `test_tool_error_returns_failure_exit(monkeypatch, capsys)` (function)
- L208 `test_skipped_result_is_success(monkeypatch)` (function)
- L229 `test_list_human_output(monkeypatch, capsys)` (function)
- L248 `test_list_json(monkeypatch, capsys)` (function)
- L268 `test_list_filter_platform(monkeypatch, capsys)` (function)
- L293 `test_list_unknown_platform_fails(monkeypatch, capsys)` (function)
- L315 `test_register_send_subparser_is_reusable()` (function) — Sanity check: the registrar returns a parser and wires ``cmd_send``.
- L334 `test_load_hermes_env_bridges_config_yaml_scalars(tmp_path, monkeypatch)` (function) — Top-level config.yaml scalars should be bridged into os.environ.
- L368 `test_load_hermes_env_does_not_override_existing(tmp_path, monkeypatch)` (function) — Existing env vars must not be clobbered by config.yaml values.
- L388 `test_load_hermes_env_handles_missing_files(tmp_path, monkeypatch)` (function) — No .env or config.yaml should be a silent no-op, not an exception.
