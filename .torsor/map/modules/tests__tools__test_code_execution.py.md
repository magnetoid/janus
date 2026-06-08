---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_code_execution.py

Symbols in `tests/tools/test_code_execution.py`.

- L25 `_force_local_terminal(monkeypatch)` (function) — Re-set TERMINAL_ENV=local before every test.
- L50 `_mock_handle_function_call(function_name, function_args, task_id=None, user_task=None)` (function) — Mock dispatcher that returns canned responses for each tool.
- L70 `TestSandboxRequirements` (class)
- L71 `test_available_on_posix(self)` (method)
- L75 `test_schema_is_valid(self)` (method)
- L81 `TestHermesToolsGeneration` (class)
- L82 `test_generates_all_allowed_tools(self)` (method)
- L87 `test_generates_subset(self)` (method)
- L93 `test_empty_list_generates_nothing(self)` (method)
- L98 `test_non_allowed_tools_ignored(self)` (method)
- L103 `test_rpc_infrastructure_present(self)` (method)
- L110 `test_convenience_helpers_present(self)` (method) — Verify json_parse, shell_quote, and retry helpers are generated.
- L118 `test_file_transport_uses_tempfile_fallback_for_rpc_dir(self)` (method)
- L124 `test_uds_transport_serializes_concurrent_calls(self)` (method) — Regression: UDS _call() must hold a lock across send+recv so that
- L132 `test_file_transport_serializes_seq_allocation(self)` (method) — Regression: file transport _call() must allocate `_seq` under a
- L141 `TestExecuteCodeRemoteTempDir` (class)
- L142 `test_execute_remote_uses_backend_temp_dir_for_sandbox(self)` (method)
- L178 `TestExecuteCode` (class) — Integration tests using the mock dispatcher.
- L181 `_run(self, code, enabled_tools=None)` (method) — Helper: run code with mocked handle_function_call.
- L195 `test_basic_print(self)` (method) — Script that just prints -- no tool calls.
- L202 `test_repo_root_modules_are_importable(self)` (method) — Sandboxed scripts can import modules that live at the repo root.
- L208 `test_single_tool_call(self)` (method) — Script calls terminal and prints the result.
- L220 `test_multi_tool_chain(self)` (method) — Script calls multiple tools sequentially.
- L233 `test_syntax_error(self)` (method) — Script with a syntax error returns error status.
- L239 `test_runtime_exception(self)` (method) — Script with a runtime error returns error status.
- L244 `test_concurrent_tool_calls_match_responses(self)` (method) — Regression for the UDS RPC race: multiple threads inside the
- L302 `test_excluded_tool_returns_error(self)` (method) — Script calling a tool not in the allow-list gets an error from RPC.
- L314 `test_empty_code(self)` (method) — Empty code string returns an error.
- L319 `test_output_captured(self)` (method) — Multiple print statements are captured in order.
- L330 `test_stderr_on_error(self)` (method) — Traceback from stderr is included in the response.
- L342 `test_timeout_enforcement(self)` (method) — Script that sleeps too long is killed.
- L360 `test_web_search_tool(self)` (method) — Script calls web_search and processes results.
- L371 `test_json_parse_helper(self)` (method) — json_parse handles control characters that json.loads(strict=True) rejects.
- L384 `test_shell_quote_helper(self)` (method) — shell_quote properly escapes dangerous characters.
- L399 `test_retry_helper_success(self)` (method) — retry returns on first success.
- L414 `test_retry_helper_eventual_success(self)` (method) — retry retries on failure and succeeds eventually.
- L431 `test_retry_helper_all_fail(self)` (method) — retry raises the last error when all attempts fail.
- L448 `TestStubSchemaDrift` (class) — Verify that _TOOL_STUBS in code_execution_tool.py stay in sync with
- L462 `test_stubs_cover_all_schema_params(self)` (method) — Every user-facing parameter in the real schema must appear in the
- L497 `test_stubs_pass_all_params_to_rpc(self)` (method) — The args_dict_expr in each stub must include every parameter from
- L514 `test_search_files_target_uses_current_values(self)` (method) — search_files stub should use 'content'/'files', not old 'grep'/'find'.
- L525 `test_generated_module_accepts_all_params(self)` (method) — The generated hermes_tools.py module should accept all current params
- L547 `TestBuildExecuteCodeSchema` (class) — Tests for build_execute_code_schema — the dynamic schema generator.
- L550 `test_default_includes_all_tools(self)` (method)
- L556 `test_schema_structure(self)` (method)
- L563 `test_subset_only_lists_enabled_tools(self)` (method)
- L573 `test_single_tool(self)` (method)
- L579 `test_import_examples_prefer_web_search_and_terminal(self)` (method)
- L586 `test_import_examples_fallback_when_no_preferred(self)` (method) — When neither web_search nor terminal are enabled, falls back to
- L596 `test_empty_set_produces_valid_description(self)` (method) — build_execute_code_schema(set()) must not produce 'import , ...'
- L604 `test_real_scenario_all_sandbox_tools_disabled(self)` (method) — Reproduce the exact code path from model_tools.py:231-234.
- L631 `test_real_scenario_only_vision_enabled(self)` (method) — Another real path: user runs `hermes tools code_execution,vision`.
- L646 `test_description_mentions_limits(self)` (method)
- L653 `test_description_mentions_helpers(self)` (method)
- L660 `test_none_defaults_to_all_tools(self)` (method)
- L671 `TestEnvVarFiltering` (class) — Verify that execute_code filters environment variables correctly.
- L678 `_get_child_env(self, extra_env=None)` (method) — Run a script that dumps its environment and return the env dict.
- L701 `test_api_keys_excluded(self)` (method)
- L711 `test_tokens_excluded(self)` (method)
- L721 `test_password_vars_excluded(self)` (method)
- L731 `test_path_included(self)` (method)
- L735 `test_home_included(self)` (method)
- L739 `test_hermes_rpc_socket_injected(self)` (method)
- L743 `test_pythondontwritebytecode_set(self)` (method)
- L747 `test_timezone_injected_when_set(self)` (method)
- L757 `test_timezone_not_set_when_empty(self)` (method)
- L773 `TestExecuteCodeEdgeCases` (class)
- L775 `test_windows_returns_error(self)` (method) — When SANDBOX_AVAILABLE is False (e.g. when the backend deems
- L788 `test_whitespace_only_code(self)` (method)
- L794 `test_none_enabled_tools_uses_all(self)` (method) — When enabled_tools is None, all sandbox tools should be available.
- L808 `test_empty_enabled_tools_uses_all(self)` (method) — When enabled_tools is [] (empty), all sandbox tools should be available.
- L822 `test_nonoverlapping_tools_fallback(self)` (method) — When enabled_tools has no overlap with SANDBOX_ALLOWED_TOOLS,
- L843 `TestLoadConfig` (class)
- L844 `test_returns_empty_dict_when_cli_config_unavailable(self)` (method)
- L850 `test_returns_code_execution_section(self)` (method)
- L857 `test_does_not_import_interactive_cli(self)` (method)
- L872 `TestInterruptHandling` (class)
- L873 `test_interrupt_event_stops_execution(self)` (method) — When interrupt is set for the execution thread, execute_code should stop.
- L906 `TestHeadTailTruncation` (class) — Tests for head+tail truncation of large stdout in execute_code.
- L909 `_run(self, code)` (method)
- L918 `test_short_output_not_truncated(self)` (method) — Output under MAX_STDOUT_BYTES should not be truncated.
- L925 `test_large_output_preserves_head_and_tail(self)` (method) — Output exceeding MAX_STDOUT_BYTES keeps both head and tail.
- L944 `test_truncation_notice_format(self)` (method) — Truncation notice includes character counts.
