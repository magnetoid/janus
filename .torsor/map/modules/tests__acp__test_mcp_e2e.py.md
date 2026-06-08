---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_mcp_e2e.py

Symbols in `tests/acp/test_mcp_e2e.py`.

- L38 `mock_manager()` (function)
- L43 `acp_agent(mock_manager)` (function)
- L52 `TestMcpRegistrationE2E` (class) — Full flow: session with MCP servers → prompt with tool calls → ACP events.
- L56 `test_session_with_mcp_servers_registers_tools(self, acp_agent, mock_manager)` (method) — new_session with mcpServers converts them to Hermes config and registers.
- L112 `test_prompt_with_tool_calls_emits_acp_events(self, acp_agent, mock_manager)` (method) — Prompt → agent fires callbacks → ACP ToolCallStart + ToolCallUpdate events.
- L183 `test_patch_mode_tool_start_defers_diff_to_edit_approval_prompt(self)` (method)
- L198 `test_prompt_tool_results_paired_by_call_id(self, acp_agent, mock_manager)` (method) — The ToolCallUpdate's toolCallId must match the ToolCallStart's.
- L248 `TestMcpSanitizationE2E` (class) — Verify server names with special chars work end-to-end.
- L252 `test_slashed_server_name_registers_cleanly(self, acp_agent, mock_manager)` (method) — Server name 'ai.exa/exa' should not crash — tools get sanitized names.
- L281 `TestSessionLifecycleMcpE2E` (class) — Verify MCP servers are registered on all session lifecycle methods.
- L285 `test_load_session_registers_mcp(self, acp_agent, mock_manager)` (method) — load_session re-registers MCP servers (spec says agents may not retain them).
- L313 `test_resume_session_registers_mcp(self, acp_agent, mock_manager)` (method) — resume_session re-registers MCP servers.
- L340 `test_fork_session_registers_mcp(self, acp_agent, mock_manager)` (method) — fork_session registers MCP servers on the new forked session.
