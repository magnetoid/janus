---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/mcp_tool.py

Symbols in `tools/mcp_tool.py`.

- L120 `_get_mcp_stderr_log()` (function) — Return a shared append-mode file handle for MCP subprocess stderr.
- L155 `_write_stderr_log_header(server_name: str)` (function) — Write a human-readable session marker before launching a server.
- L238 `_check_message_handler_support()` (function) — Check if ClientSession accepts ``message_handler`` kwarg.
- L296 `_build_safe_env(user_env: Optional[dict])` (function) — Build a filtered environment dict for stdio subprocesses.
- L315 `_sanitize_error(text: str)` (function) — Strip credential-like patterns from error text before returning to LLM.
- L324 `_exc_str(exc: BaseException)` (function) — Return a non-empty human-readable string for *exc*.
- L367 `_scan_mcp_description(server_name: str, tool_name: str, description: str)` (function) — Scan an MCP tool description for prompt injection patterns.
- L388 `_prepend_path(env: dict, directory: str)` (function) — Prepend *directory* to env PATH if it is not already present.
- L402 `_resolve_stdio_command(command: str, env: dict)` (function) — Resolve a stdio MCP command against the exact subprocess environment.
- L454 `_mcp_image_extension_for_mime_type(mime_type: str)` (function) — Return a reasonable file extension for an MCP image MIME type.
- L463 `_cache_mcp_image_block(block)` (function) — Cache an MCP ``ImageContent`` block to the shared image cache and
- L512 `InvalidMcpUrlError` (class) — Raised when a remote MCP server's ``url`` cannot be parsed as http(s)://.
- L521 `NonMcpEndpointError` (class) — Raised when an HTTP MCP URL serves a non-MCP response.
- L536 `_validate_remote_mcp_url(server_name: str, url: Any)` (function) — Return the URL as a string if it's a valid http(s) remote MCP URL.
- L588 `_resolve_client_cert(server_name: str, config: dict)` (function) — Resolve the ``client_cert`` / ``client_key`` config for mTLS.
- L661 `_format_connect_error(exc: BaseException)` (function) — Render nested MCP connection errors into an actionable short message.
- L725 `_safe_numeric(value, default, coerce=int, minimum=1)` (function) — Coerce a config value to a numeric type, returning *default* on failure.
- L740 `SamplingHandler` (class) — Handles sampling/createMessage requests for a single MCP server.
- L755 `__init__(self, server_name: str, config: dict)` (method)
- L778 `_check_rate_limit(self)` (method) — Sliding-window rate limiter.  Returns True if request is allowed.
- L790 `_resolve_model(self, preferences)` (method) — Config override > server hint > None (use default).
- L803 `_extract_tool_result_text(block)` (method) — Extract text from a ToolResultContent block.
- L810 `_convert_messages(self, params)` (method) — Convert MCP SamplingMessages to OpenAI format.
- L882 `_error(message: str, code: int=-1)` (method) — Return ErrorData (MCP spec) or raise as fallback.
- L890 `_build_tool_use_result(self, choice, response)` (method) — Build a CreateMessageResultWithTools from an LLM tool_calls response.
- L947 `_build_text_result(self, choice, response)` (method) — Build a CreateMessageResult from a normal text response.
- L968 `session_kwargs(self)` (method) — Return kwargs to pass to ClientSession for sampling support.
- L979 `__call__(self, context, params)` (method) — Sampling callback invoked by the MCP SDK.
- L1111 `MCPServerTask` (class) — Manages a single MCP server connection in a dedicated asyncio Task.
- L1130 `__init__(self, name: str)` (method)
- L1165 `_is_http(self)` (method) — Check if this server uses HTTP transport.
- L1171 `_refresh_tools_task(self)` (method) — Run a dynamic tool refresh and log failures from background tasks.
- L1180 `_schedule_tools_refresh(self)` (method) — Schedule a background tool refresh and keep it strongly referenced.
- L1187 `_make_message_handler(self)` (method) — Build a ``message_handler`` callback for ``ClientSession``.
- L1230 `_refresh_tools(self)` (method) — Re-fetch tools from the server and update the registry.
- L1292 `_wait_for_lifecycle_event(self)` (method) — Block until either _shutdown_event or _reconnect_event fires.
- L1355 `_run_stdio(self, config: dict)` (method) — Run the server using stdio transport.
- L1480 `_preflight_content_type(self, url: str, *, headers: Optional[dict]=None, ssl_verify: bool=True, client_cert=None, timeout: float=5.0)` (method) — Probe *url* for an MCP-shaped response before the SDK connects.
- L1555 `_run_http(self, config: dict)` (method) — Run the server using HTTP/StreamableHTTP transport.
- L1744 `_discover_tools(self)` (method) — Discover tools from the connected session.
- L1756 `run(self, config: dict)` (method) — Long-lived coroutine: connect, discover tools, wait, disconnect.
- L1941 `start(self, config: dict)` (method) — Create the background Task and wait until ready (or failed).
- L1948 `shutdown(self)` (method) — Signal the Task to exit and wait for clean resource teardown.
- L2013 `_bump_server_error(server_name: str)` (function) — Increment the consecutive-failure count for ``server_name``.
- L2026 `_reset_server_error(server_name: str)` (function) — Fully close the breaker for ``server_name``.
- L2045 `_get_auth_error_types()` (function) — Return a tuple of exception types that indicate MCP OAuth failure.
- L2087 `_is_auth_error(exc: BaseException)` (function) — Return True if ``exc`` indicates an MCP OAuth failure.
- L2106 `_handle_auth_error_and_retry(server_name: str, exc: BaseException, retry_call, op_description: str)` (function) — Attempt auth recovery and one retry; return None to fall through.
- L2249 `_is_session_expired_error(exc: BaseException)` (function) — Return True if ``exc`` looks like an MCP transport session expiry.
- L2275 `_handle_session_expired_and_retry(server_name: str, exc: BaseException, retry_call, op_description: str)` (function) — Trigger a transport reconnect and retry once on session expiry.
- L2406 `_snapshot_child_pids()` (function) — Return a set of current child process PIDs.
- L2432 `_mcp_loop_exception_handler(loop, context)` (function) — Suppress benign 'Event loop is closed' noise during shutdown.
- L2447 `_ensure_mcp_loop()` (function) — Start the background event loop thread if not already running.
- L2463 `_run_on_mcp_loop(coro_or_factory, timeout: float=30)` (function) — Schedule a coroutine on the MCP event loop and block until done.
- L2518 `_interrupted_call_result()` (function) — Standardized JSON error for a user-interrupted MCP tool call.
- L2529 `_interpolate_env_vars(value)` (function) — Recursively resolve ``${VAR}`` placeholders from ``os.environ``.
- L2542 `_load_mcp_config()` (function) — Read ``mcp_servers`` from the Hermes config file.
- L2575 `_connect_server(name: str, config: dict)` (function) — Create an MCPServerTask, start it, and return when ready.
- L2595 `_make_tool_handler(server_name: str, tool_name: str, tool_timeout: float)` (function) — Return a sync handler that calls an MCP tool via the background loop.
- L2739 `_make_list_resources_handler(server_name: str, tool_timeout: float)` (function) — Return a sync handler that lists resources from an MCP server.
- L2797 `_make_read_resource_handler(server_name: str, tool_timeout: float)` (function) — Return a sync handler that reads a resource by URI from an MCP server.
- L2857 `_make_list_prompts_handler(server_name: str, tool_timeout: float)` (function) — Return a sync handler that lists prompts from an MCP server.
- L2920 `_make_get_prompt_handler(server_name: str, tool_timeout: float)` (function) — Return a sync handler that gets a prompt by name from an MCP server.
- L2991 `_make_check_fn(server_name: str)` (function) — Return a check function that verifies the MCP connection is alive.
- L3006 `_normalize_mcp_input_schema(schema: dict | None)` (function) — Normalize MCP input schemas for LLM tool-calling compatibility.
- L3114 `sanitize_mcp_name_component(value: str)` (function) — Return an MCP name component safe for tool and prefix generation.
- L3125 `_convert_mcp_schema(server_name: str, mcp_tool)` (function) — Convert an MCP tool listing to the Hermes registry schema format.
- L3146 `_build_utility_schemas(server_name: str)` (function) — Build schemas for the MCP utility tools (resources & prompts).
- L3219 `_normalize_name_filter(value: Any, label: str)` (function) — Normalize include/exclude config to a set of tool names.
- L3231 `_parse_boolish(value: Any, default: bool=True)` (function) — Parse a bool-like config value with safe fallback.
- L3272 `_track_mcp_tool_server(tool_name: str, server_name: str)` (function) — Remember the exact MCP server that registered *tool_name*.
- L3279 `_forget_mcp_tool_server(tool_name: str)` (function) — Forget MCP server provenance for a deregistered tool.
- L3285 `_select_utility_schemas(server_name: str, server: MCPServerTask, config: dict)` (function) — Select utility schemas based on config and server capabilities.
- L3342 `_existing_tool_names()` (function) — Return tool names for all currently connected servers.
- L3355 `_register_server_tools(name: str, server: MCPServerTask, config: dict)` (function) — Register tools from an already-connected server into the registry.
- L3465 `_discover_and_register_server(name: str, config: dict)` (function) — Connect to a single MCP server, discover tools, and register them.
- L3494 `register_mcp_servers(servers: Dict[str, dict])` (function) — Connect to explicit MCP servers and register their tools.
- L3589 `discover_mcp_tools()` (function) — Entry point: load config, connect to MCP servers, register tools.
- L3638 `is_mcp_tool_parallel_safe(tool_name: str)` (function) — Check if an MCP tool belongs to a server that supports parallel tool calls.
- L3656 `get_mcp_status()` (function) — Return status of all configured MCP servers for banner display.
- L3702 `probe_mcp_server_tools()` (function) — Temporarily connect to configured MCP servers and list their tools.
- L3768 `shutdown_mcp_servers()` (function) — Close all MCP server connections and stop the background loop.
- L3814 `_kill_orphaned_mcp_children(include_active: bool=False)` (function) — Best-effort graceful shutdown of stdio MCP subprocesses to reap orphans.
- L3901 `_stop_mcp_loop()` (function) — Stop the background event loop and join its thread.
