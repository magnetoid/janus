---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/openviking/__init__.py

Symbols in `plugins/memory/openviking/__init__.py`.

- L78 `_atexit_commit_sessions()` (function) — Fire on_session_end for the last active provider on process exit.
- L98 `_get_httpx()` (function) — Lazy import httpx.
- L107 `_VikingClient` (class) — Thin HTTP client for the OpenViking REST API.
- L110 `__init__(self, endpoint: str, api_key: str='', account: str='', user: str='', agent: str='')` (method)
- L121 `_headers(self)` (method)
- L141 `_url(self, path: str)` (method)
- L144 `_multipart_headers(self)` (method)
- L149 `_parse_response(self, resp)` (method)
- L178 `get(self, path: str, **kwargs)` (method)
- L184 `post(self, path: str, payload: dict=None, **kwargs)` (method)
- L191 `upload_temp_file(self, file_path: Path)` (method)
- L207 `health(self)` (method)
- L356 `_zip_directory(dir_path: Path)` (function) — Create a temporary zip file containing a directory tree.
- L374 `_is_windows_absolute_path(value: str)` (function)
- L383 `_is_remote_resource_source(value: str)` (function)
- L387 `_is_local_path_reference(value: str)` (function)
- L401 `_path_from_file_uri(uri: str)` (function)
- L412 `OpenVikingMemoryProvider` (class) — Full bidirectional memory via OpenViking context database.
- L415 `__init__(self)` (method)
- L427 `name(self)` (method)
- L430 `is_available(self)` (method) — Check if OpenViking endpoint is configured. No network calls.
- L434 `get_config_schema(self)` (method)
- L469 `initialize(self, session_id: str, **kwargs)` (method)
- L494 `system_prompt_block(self)` (method)
- L521 `prefetch(self, query: str, *, session_id: str='')` (method) — Return prefetched results from the background thread.
- L532 `queue_prefetch(self, query: str, *, session_id: str='')` (method) — Fire a background search to pre-load relevant context.
- L568 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method) — Record the conversation turn in OpenViking's session (non-blocking).
- L605 `on_session_end(self, messages: List[Dict[str, Any]])` (method) — Commit the session to trigger memory extraction.
- L629 `_build_memory_uri(self, subdir: str)` (method) — Build a viking:// memory URI under the configured user/agent/subdir.
- L634 `on_memory_write(self, action: str, target: str, content: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Mirror built-in memory writes to OpenViking via content/write.
- L665 `get_tool_schemas(self)` (method)
- L668 `handle_tool_call(self, tool_name: str, args: dict, **kwargs)` (method)
- L687 `shutdown(self)` (method)
- L700 `_unwrap_result(resp: Any)` (method) — Return OpenViking payload body regardless of wrapped/unwrapped shape.
- L707 `_normalize_summary_uri(uri: str)` (method) — Map pseudo summary files to their parent directory URI for L0/L1 reads.
- L716 `_is_directory_uri(self, uri: str)` (method) — Probe fs/stat to decide if a URI is a directory.
- L739 `_tool_search(self, args: dict)` (method)
- L781 `_tool_read(self, args: dict)` (method)
- L854 `_tool_browse(self, args: dict)` (method)
- L886 `_tool_remember(self, args: dict)` (method)
- L913 `_tool_add_resource(self, args: dict)` (method)
- L976 `register(ctx)` (function) — Register OpenViking as a memory provider plugin.
