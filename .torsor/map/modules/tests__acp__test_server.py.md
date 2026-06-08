---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_server.py

Symbols in `tests/acp/test_server.py`.

- L45 `mock_manager()` (function) — SessionManager with a mock agent factory.
- L51 `agent(mock_manager)` (function) — HermesACPAgent backed by a mock session manager.
- L57 `test_new_session_exposes_edit_approvals_as_modes_not_config_options(agent)` (function)
- L71 `test_set_config_option_persists_edit_approval_policy_without_advertising_config(agent)` (function)
- L90 `TestInitialize` (class)
- L92 `test_initialize_returns_correct_protocol_version(self, agent)` (method)
- L98 `test_initialize_returns_agent_info(self, agent)` (method)
- L106 `test_initialize_returns_capabilities(self, agent)` (method)
- L117 `test_initialize_capabilities_wire_format(self, agent)` (method) — Verify the JSON wire format uses correct aliases so ACP clients see the right keys.
- L128 `test_initialize_advertises_provider_and_terminal_auth_methods(self, agent, monkeypatch)` (method)
- L142 `test_initialize_advertises_terminal_setup_auth_when_no_provider(self, agent, monkeypatch)` (method)
- L168 `TestAuthenticate` (class)
- L170 `test_authenticate_with_matching_method_id(self, agent, monkeypatch)` (method)
- L179 `test_authenticate_is_case_insensitive(self, agent, monkeypatch)` (method)
- L188 `test_authenticate_rejects_mismatched_method_id(self, agent, monkeypatch)` (method)
- L197 `test_authenticate_without_provider(self, agent, monkeypatch)` (method)
- L206 `test_authenticate_accepts_terminal_setup_after_provider_configured(self, agent, monkeypatch)` (method)
- L215 `test_authenticate_rejects_terminal_setup_without_provider(self, agent, monkeypatch)` (method)
- L229 `TestSessionOps` (class)
- L231 `test_new_session_creates_session(self, agent)` (method)
- L241 `test_new_session_returns_model_state(self)` (method)
- L260 `test_available_commands_include_help(self, agent)` (method)
- L271 `test_send_available_commands_update(self, agent)` (method)
- L301 `test_build_usage_update_for_zed_context_indicator(self, agent, mock_manager)` (method)
- L320 `test_send_usage_update_to_client(self, agent, mock_manager)` (method)
- L342 `test_cancel_sets_event(self, agent)` (method)
- L350 `test_cancel_nonexistent_session_is_noop(self, agent)` (method)
- L355 `test_load_session_not_found_returns_none(self, agent)` (method)
- L360 `test_load_session_replays_persisted_history_to_client(self, agent)` (method)
- L426 `test_load_session_replays_native_plan_for_persisted_todo_tool(self, agent)` (method) — Persisted todo tool results should rebuild Zed's native plan panel.
- L477 `test_resume_session_replays_persisted_history_to_client(self, agent)` (method)
- L500 `test_load_session_replays_reasoning_thought_before_message(self, agent)` (method) — Thinking-model thoughts must be replayed via ``agent_thought_chunk``.
- L564 `test_load_session_replays_reasoning_only_turn(self, agent)` (method) — Assistant turns with reasoning but no content should still emit a thought.
- L606 `test_load_session_skips_empty_reasoning_fields(self, agent)` (method) — Empty/whitespace reasoning fields must not produce notifications.
- L636 `test_load_session_replays_thought_then_tool_call_without_message(self, agent)` (method) — Canonical thinking-model shape: reasoning + tool_call + no body text.
- L705 `test_load_session_replays_history_before_returning_response(self, agent)` (method) — Per ACP spec, replay must complete BEFORE load_session returns.
- L733 `test_resume_session_replays_history_before_returning_response(self, agent)` (method) — Same spec rationale as ``load_session`` — replay before responding.
- L751 `test_load_session_survives_replay_helper_exception(self, agent, caplog)` (method) — A replay helper raising must not turn load_session into an error.
- L775 `test_resume_session_survives_replay_helper_exception(self, agent, caplog)` (method) — Same guarantee as ``load_session`` for the resume path.
- L792 `test_resume_session_creates_new_if_missing(self, agent)` (method)
- L802 `TestListAndFork` (class)
- L804 `test_fork_session(self, agent)` (method)
- L811 `test_list_sessions_includes_title_and_updated_at(self, agent)` (method)
- L831 `test_list_sessions_passes_cwd_filter(self, agent)` (method)
- L838 `test_list_sessions_pagination_first_page(self, agent)` (method)
- L852 `test_list_sessions_pagination_no_more(self, agent)` (method)
- L864 `test_list_sessions_cursor_resumes_after_match(self, agent)` (method)
- L877 `test_list_sessions_unknown_cursor_returns_empty(self, agent)` (method)
- L893 `TestSessionConfiguration` (class)
- L895 `test_set_session_mode_returns_response(self, agent)` (method)
- L904 `test_router_accepts_stable_session_config_methods(self, agent)` (method)
- L927 `test_router_accepts_unstable_model_switch_when_enabled(self, agent)` (method)
- L942 `test_set_session_model_accepts_provider_prefixed_choice(self, tmp_path, monkeypatch)` (method)
- L1006 `TestPrompt` (class)
- L1008 `test_prompt_returns_refusal_for_unknown_session(self, agent)` (method)
- L1015 `test_prompt_returns_end_turn_for_empty_message(self, agent)` (method)
- L1022 `test_prompt_runs_agent(self, agent)` (method) — The prompt method should call run_conversation on the agent.
- L1054 `test_prompt_updates_history(self, agent)` (method) — After a prompt, session history should be updated.
- L1078 `test_prompt_sends_final_message_update(self, agent)` (method) — The final response should be sent as an AgentMessageChunk.
- L1104 `test_prompt_propagates_hermes_session_id_env(self, agent, monkeypatch)` (method) — ACP must propagate the originating session id to the agent loop
- L1149 `test_prompt_restores_prior_hermes_session_id(self, agent, monkeypatch)` (method) — If the env already had HERMES_SESSION_ID set (e.g. nested
- L1178 `test_prompt_does_not_duplicate_streamed_final_message(self, agent)` (method) — If ACP already streamed response chunks, final_response should not be sent again.
- L1205 `test_prompt_delivers_transformed_response_after_streaming(self, agent)` (method) — If a transform_llm_output plugin hook modifies the response after
- L1247 `test_prompt_auto_titles_session(self, agent)` (method)
- L1273 `test_prompt_sends_session_info_update_after_auto_title(self, agent)` (method)
- L1314 `test_prompt_populates_usage_from_top_level_run_conversation_fields(self, agent)` (method) — ACP should map top-level token fields into PromptResponse.usage.
- L1345 `test_prompt_cancelled_returns_cancelled_stop_reason(self, agent)` (method) — If cancel is called during prompt, stop_reason should be 'cancelled'.
- L1372 `TestOnConnect` (class)
- L1373 `test_on_connect_stores_client(self, agent)` (method)
- L1384 `TestSlashCommands` (class) — Test slash command dispatch in the ACP adapter.
- L1387 `_make_state(self, mock_manager)` (method)
- L1394 `test_help_lists_commands(self, agent, mock_manager)` (method)
- L1403 `test_model_shows_current(self, agent, mock_manager)` (method)
- L1408 `test_context_empty(self, agent, mock_manager)` (method)
- L1414 `test_context_with_messages(self, agent, mock_manager)` (method)
- L1424 `test_context_shows_usage_and_compression_threshold(self, agent, mock_manager)` (method)
- L1444 `test_context_says_compression_due_when_past_threshold(self, agent, mock_manager)` (method)
- L1461 `test_reset_clears_history(self, agent, mock_manager)` (method)
- L1468 `test_version(self, agent, mock_manager)` (method)
- L1473 `test_compact_compresses_context(self, agent, mock_manager)` (method)
- L1523 `test_unknown_command_returns_none(self, agent, mock_manager)` (method)
- L1529 `test_slash_command_intercepted_in_prompt(self, agent, mock_manager)` (method) — Slash commands should be handled without calling the LLM.
- L1548 `test_unknown_slash_falls_through_to_llm(self, agent, mock_manager)` (method) — Unknown /commands should be sent to the LLM, not intercepted.
- L1567 `test_model_switch_uses_requested_provider(self, tmp_path, monkeypatch)` (method) — `/model provider:model` should rebuild the ACP agent on that provider.
- L1637 `TestRegisterSessionMcpServers` (class) — Tests for ACP MCP server registration in session lifecycle.
- L1641 `test_noop_when_no_servers(self, agent, mock_manager)` (method) — No-op when mcp_servers is None or empty.
- L1649 `test_registers_stdio_servers(self, agent, mock_manager)` (method) — McpServerStdio servers are converted and passed to register_mcp_servers.
- L1683 `test_registers_http_servers(self, agent, mock_manager)` (method) — McpServerHttp servers are converted correctly.
- L1714 `test_refreshes_agent_tool_surface(self, agent, mock_manager)` (method) — After MCP registration, agent.tools and valid_tool_names are refreshed.
- L1753 `test_register_failure_logs_warning(self, agent, mock_manager)` (method) — If register_mcp_servers raises, warning is logged but no crash.
