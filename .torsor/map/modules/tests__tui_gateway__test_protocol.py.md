---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tui_gateway/test_protocol.py

Symbols in `tests/tui_gateway/test_protocol.py`.

- L17 `_restore_stdout()` (function)
- L23 `server()` (function)
- L47 `capture(server)` (function) — Redirect server's real stdout to a StringIO and return (server, buf).
- L57 `test_unknown_method(server)` (function)
- L62 `test_ok_envelope(server)` (function)
- L68 `test_err_envelope(server)` (function)
- L77 `test_write_json(capture)` (function)
- L83 `test_write_json_broken_pipe(server)` (function)
- L92 `test_write_json_closed_stream_returns_false(server)` (function) — ValueError ('I/O on closed file') used to bubble up; treat as gone.
- L103 `test_write_json_unicode_encode_error_re_raises(server)` (function) — A non-UTF-8 stdout encoding raises UnicodeEncodeError (a ValueError
- L119 `test_write_json_unrelated_value_error_re_raises(server)` (function) — Only ValueError('...closed file...') means peer gone.  Other
- L132 `test_write_json_non_serializable_payload_re_raises(server)` (function) — Non-JSON-safe payloads are programming errors — they must NOT be
- L143 `test_write_json_peer_gone_oserror_on_flush_returns_false(server)` (function) — A flush that raises a peer-gone OSError (EPIPE) must not strand
- L159 `test_write_json_non_peer_gone_oserror_re_raises(server)` (function) — Host I/O failures (ENOSPC, EACCES, EIO …) are NOT peer-gone — they
- L174 `test_write_json_skips_flush_when_disable_flush_true(monkeypatch)` (function) — `StdioTransport` skips flush when `_DISABLE_FLUSH` is true.
- L201 `test_disable_flush_env_var_actually_wires_to_module_constant(monkeypatch)` (function) — End-to-end: setting `HERMES_TUI_GATEWAY_NO_FLUSH=1` and importing
- L223 `test_emit_with_payload(capture)` (function)
- L234 `test_emit_without_payload(capture)` (function)
- L244 `test_block_and_respond(capture)` (function)
- L267 `test_clear_pending(server)` (function)
- L280 `test_sess_missing(server)` (function)
- L285 `test_sess_found(server)` (function)
- L296 `test_session_resume_returns_hydrated_messages(server, monkeypatch)` (function)
- L339 `test_session_resume_handles_multimodal_list_content(server, monkeypatch)` (function) — A user message persisted with list-shaped multimodal content used to
- L397 `test_session_resume_reuses_existing_live_session(server, monkeypatch)` (function) — Repeated resume must not allocate duplicate live agents.
- L517 `test_session_resume_live_payload_uses_current_history_with_ancestors(server, monkeypatch)` (function) — Live resume should not reuse a stale ancestor-inclusive snapshot.
- L616 `test_session_branch_persists_branched_from_marker(server, monkeypatch)` (function) — TUI /branch must persist a _branched_from marker so the branch stays
- L681 `test_make_agent_accepts_list_system_prompt(server, monkeypatch)` (function)
- L714 `test_config_load_missing(server, tmp_path)` (function)
- L719 `test_config_roundtrip(server, tmp_path)` (function)
- L735 `test_cli_exec_blocked(server, argv)` (function)
- L743 `test_cli_exec_allowed(server, argv)` (function)
- L750 `test_slash_exec_rejects_skill_commands(server)` (function) — slash.exec must reject skill commands so the TUI falls through to command.dispatch.
- L772 `test_slash_exec_handles_plugin_commands_in_live_gateway(server)` (function) — Plugin slash commands return normal slash.exec output without using the worker.
- L802 `test_slash_exec_plugin_lookup_failure_falls_back_to_worker(server)` (function) — Plugin discovery failures must not break ordinary slash-worker commands.
- L832 `test_slash_exec_plugin_handler_error_returns_output(server)` (function) — Plugin handler failures return slash output so the TUI does not redispatch.
- L866 `test_slash_exec_rejects_pending_input_commands(server, cmd)` (function) — slash.exec must reject commands that use _pending_input in the CLI.
- L882 `test_command_dispatch_queue_sends_message(server)` (function) — command.dispatch /queue returns {type: 'send', message: ...} for the TUI.
- L899 `test_command_dispatch_queue_requires_arg(server)` (function) — command.dispatch /queue without an argument returns an error.
- L914 `test_skills_manage_search_uses_tools_hub_sources(server)` (function)
- L944 `test_command_dispatch_steer_fallback_sends_message(server)` (function) — command.dispatch /steer with no active agent falls back to send.
- L961 `test_command_dispatch_retry_finds_last_user_message(server)` (function) — command.dispatch /retry walks session['history'] to find the last user message.
- L994 `test_command_dispatch_retry_empty_history(server)` (function) — command.dispatch /retry with empty history returns error.
- L1015 `test_command_dispatch_retry_handles_multipart_content(server)` (function) — command.dispatch /retry extracts text from multipart content lists.
- L1045 `test_command_dispatch_returns_skill_payload(server)` (function) — command.dispatch returns structured skill payload for the TUI to send().
- L1068 `test_command_dispatch_awaits_async_plugin_handler(server)` (function)
- L1089 `test_dispatch_runs_short_handlers_inline(server)` (function) — Non-long handlers return their response synchronously from dispatch().
- L1098 `test_dispatch_offloads_long_handlers_and_emits_via_stdout(capture)` (function) — Long handlers run on the pool and write their response via write_json.
- L1115 `test_dispatch_long_handler_does_not_block_fast_handler(server)` (function) — A slow long handler must not prevent a concurrent fast handler from completing.
- L1133 `test_dispatch_session_compress_does_not_block_fast_handler(server)` (function) — Manual TUI compaction can take minutes, so it must not block the RPC loop.
- L1156 `test_dispatch_long_handler_exception_produces_error_response(capture)` (function) — An exception inside a pool-dispatched handler still yields a JSON-RPC error.
- L1178 `test_dispatch_unknown_long_method_still_goes_inline(server)` (function) — Method name not in _LONG_HANDLERS takes the sync path even if handler is slow.
