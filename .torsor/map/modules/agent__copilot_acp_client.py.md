---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/copilot_acp_client.py

Symbols in `agent/copilot_acp_client.py`.

- L47 `_is_gh_copilot_deprecation_message(stderr_text: str)` (function) — True iff stderr looks like the deprecated gh-copilot extension's banner.
- L56 `_resolve_command()` (function)
- L64 `_resolve_args()` (function)
- L71 `_resolve_home_dir()` (function) — Return a stable HOME for child ACP processes.
- L106 `_build_subprocess_env()` (function)
- L112 `_jsonrpc_error(message_id: Any, code: int, message: str)` (function)
- L123 `_permission_denied(message_id: Any)` (function)
- L135 `_format_messages_as_prompt(messages: list[dict[str, Any]], model: str | None=None, tools: list[dict[str, Any]] | None=None, tool_choice: Any=None)` (function)
- L210 `_render_message_content(content: Any)` (function)
- L234 `_extract_tool_calls_from_text(text: str)` (function)
- L308 `_ensure_path_within_cwd(path_text: str, cwd: str)` (function)
- L321 `_ACPChatCompletions` (class)
- L322 `__init__(self, client: 'CopilotACPClient')` (method)
- L325 `create(self, **kwargs: Any)` (method)
- L329 `_ACPChatNamespace` (class)
- L330 `__init__(self, client: 'CopilotACPClient')` (method)
- L334 `CopilotACPClient` (class) — Minimal OpenAI-client-compatible facade for Copilot ACP.
- L337 `__init__(self, *, api_key: str | None=None, base_url: str | None=None, default_headers: dict[str, str] | None=None, acp_command: str | None=None, acp_args: list[str] | None=None, acp_cwd: str | None=None, command: str | None=None, args: list[str] | None=None, **_: Any)` (method)
- L361 `close(self)` (method)
- L378 `_create_chat_completion(self, *, model: str | None=None, messages: list[dict[str, Any]] | None=None, timeout: float | None=None, tools: list[dict[str, Any]] | None=None, tool_choice: Any=None, **_: Any)` (method)
- L438 `_run_prompt(self, prompt_text: str, *, timeout_seconds: float)` (method)
- L598 `_handle_server_message(self, msg: dict[str, Any], *, process: subprocess.Popen[str], cwd: str, text_parts: list[str] | None, reasoning_parts: list[str] | None)` (method)
