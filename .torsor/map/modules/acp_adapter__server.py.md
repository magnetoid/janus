---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# acp_adapter/server.py

Symbols in `acp_adapter/server.py`.

- L105 `_resource_display_name(uri: str, name: str | None=None, title: str | None=None)` (function) — Human-readable attachment name for prompt context.
- L120 `_is_text_resource(mime_type: str | None)` (function)
- L127 `_is_image_resource(mime_type: str | None)` (function)
- L132 `_guess_image_mime_from_path(path: Path)` (function)
- L145 `_image_data_url(data: bytes, mime_type: str)` (function)
- L149 `_path_from_file_uri(uri: str)` (function) — Convert local file URIs/paths from ACP clients into a readable Path.
- L184 `_decode_text_bytes(data: bytes, mime_type: str | None)` (function) — Decode resource bytes if they are probably text; return None for binary.
- L196 `_format_resource_text(*, uri: str, body: str, name: str | None=None, title: str | None=None, note: str | None=None)` (function)
- L211 `_resource_link_to_parts(block: ResourceContentBlock)` (function) — Convert an ACP resource_link block to OpenAI content parts.
- L310 `_embedded_resource_to_parts(block: EmbeddedResourceContentBlock)` (function)
- L359 `_extract_text(prompt: list[TextContentBlock | ImageContentBlock | AudioContentBlock | ResourceContentBlock | EmbeddedResourceContentBlock])` (function) — Extract plain text from ACP content blocks for display/commands.
- L378 `_image_block_to_openai_part(block: ImageContentBlock)` (function) — Convert an ACP image content block to OpenAI-style multimodal content.
- L394 `_content_blocks_to_openai_user_content(prompt: list[TextContentBlock | ImageContentBlock | AudioContentBlock | ResourceContentBlock | EmbeddedResourceContentBlock])` (function) — Convert ACP prompt blocks into a Hermes/OpenAI-compatible user content payload.
- L445 `HermesACPAgent` (class) — ACP Agent implementation wrapping Hermes AIAgent.
- L516 `__init__(self, session_manager: SessionManager | None=None)` (method)
- L523 `on_connect(self, conn: acp.Client)` (method) — Store the client connection for sending session updates.
- L529 `_session_modes(self, state: SessionState)` (method) — Return ACP session modes while preserving Zed's separate model picker.
- L562 `_edit_approval_policy_for_state(self, state: SessionState)` (method)
- L568 `_encode_model_choice(provider: str | None, model: str | None)` (method) — Encode a model selection so ACP clients can keep provider context.
- L578 `_build_model_state(self, state: SessionState)` (method) — Return the ACP model selector payload for editors like Zed.
- L641 `_resolve_model_selection(raw_model: str, current_provider: str)` (method) — Resolve ``provider:model`` input into the provider and normalized model id.
- L660 `_build_usage_update(state: SessionState)` (method) — Build ACP native context-usage data for clients like Zed.
- L693 `_send_usage_update(self, state: SessionState)` (method) — Send ACP native context usage to the connected client.
- L712 `_send_session_info_update(self, session_id: str)` (method) — Send ACP native session metadata after Hermes changes it.
- L743 `_schedule_usage_update(self, state: SessionState)` (method) — Schedule native context indicator refresh after ACP responses.
- L750 `_register_session_mcp_servers(self, state: SessionState, mcp_servers: list[McpServerStdio | McpServerHttp | McpServerSse] | None)` (method) — Register ACP-provided MCP servers and refresh the agent tool surface.
- L821 `initialize(self, protocol_version: int | None=None, client_capabilities: ClientCapabilities | None=None, client_info: Implementation | None=None, **kwargs: Any)` (method)
- L855 `authenticate(self, method_id: str, **kwargs: Any)` (method)
- L880 `_flatten_history_text(value: Any)` (method) — Normalize a persisted text-or-text-parts value into a single string.
- L906 `_history_message_text(cls, message: dict[str, Any])` (method) — Extract displayable text from a persisted OpenAI-style message.
- L911 `_history_reasoning_text(cls, message: dict[str, Any])` (method) — Extract displayable reasoning/thought text from a persisted assistant message.
- L929 `_history_message_update(*, role: str, text: str)` (method) — Build an ACP history replay update for a user/assistant message.
- L949 `_history_thought_update(text: str)` (method) — Build an ACP history replay update for an assistant thought.
- L954 `_history_tool_call_name_args(tool_call: dict[str, Any])` (method) — Extract function name/arguments from an OpenAI-style tool_call.
- L970 `_history_tool_call_id(tool_call: dict[str, Any])` (method) — Return the stable provider tool call id for ACP history replay.
- L979 `_replay_session_history(self, state: SessionState)` (method) — Replay persisted user/assistant history during session/load or session/resume.
- L1069 `new_session(self, cwd: str, mcp_servers: list | None=None, **kwargs: Any)` (method)
- L1086 `load_session(self, cwd: str, session_id: str, mcp_servers: list | None=None, **kwargs: Any)` (method)
- L1130 `resume_session(self, cwd: str, session_id: str, mcp_servers: list | None=None, **kwargs: Any)` (method)
- L1162 `cancel(self, session_id: str, **kwargs: Any)` (method)
- L1176 `fork_session(self, cwd: str, session_id: str, mcp_servers: list | None=None, **kwargs: Any)` (method)
- L1196 `list_sessions(self, cursor: str | None=None, cwd: str | None=None, **kwargs: Any)` (method) — List ACP sessions with optional ``cwd`` filtering and cursor pagination.
- L1243 `prompt(self, prompt: list[TextContentBlock | ImageContentBlock | AudioContentBlock | ResourceContentBlock | EmbeddedResourceContentBlock], session_id: str, **kwargs: Any)` (method) — Run Hermes on the user's prompt and stream events back to the editor.
- L1585 `_available_commands(cls)` (method)
- L1600 `_send_available_commands_update(self, session_id: str)` (method) — Advertise supported slash commands to the connected ACP client.
- L1620 `_schedule_available_commands_update(self, session_id: str)` (method) — Send the command advertisement after the session response is queued.
- L1629 `_handle_slash_command(self, text: str, state: SessionState)` (method) — Dispatch a slash command and return the response text.
- L1660 `_cmd_help(self, args: str, state: SessionState)` (method)
- L1668 `_cmd_model(self, args: str, state: SessionState)` (method)
- L1689 `_cmd_tools(self, args: str, state: SessionState)` (method)
- L1710 `_cmd_context(self, args: str, state: SessionState)` (method) — Show ACP session context pressure and compression guidance.
- L1791 `_cmd_reset(self, args: str, state: SessionState)` (method)
- L1796 `_cmd_compact(self, args: str, state: SessionState)` (method)
- L1849 `_cmd_steer(self, args: str, state: SessionState)` (method)
- L1868 `_cmd_queue(self, args: str, state: SessionState)` (method)
- L1877 `_cmd_version(self, args: str, state: SessionState)` (method)
- L1882 `set_session_model(self, model_id: str, session_id: str, **kwargs: Any)` (method) — Switch the model for a session (called by ACP protocol).
- L1916 `set_session_mode(self, mode_id: str, session_id: str, **kwargs: Any)` (method) — Persist the editor-requested mode so ACP clients do not fail on mode switches.
- L1932 `set_config_option(self, config_id: str, session_id: str, value: str, **kwargs: Any)` (method) — Accept ACP config option updates even when Hermes has no typed ACP config surface yet.
