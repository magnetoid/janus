---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/computer_use/cua_backend.py

Symbols in `tools/computer_use/cua_backend.py`.

- L77 `_is_macos()` (function)
- L81 `cua_driver_binary_available()` (function) — True if `cua-driver` is on $PATH or HERMES_CUA_DRIVER_CMD resolves.
- L86 `cua_driver_install_hint()` (function)
- L97 `_parse_windows_from_text(text: str)` (function) — Parse window records from list_windows text output.
- L110 `_parse_elements_from_tree(markdown: str)` (function) — Parse UIElement list from get_window_state AX tree markdown.
- L129 `_image_dimensions_from_bytes(raw: bytes)` (function) — Best-effort PNG/JPEG dimension sniffing without extra dependencies.
- L168 `_split_tree_text(full_text: str)` (function) — Split get_window_state text into (summary_line, tree_markdown).
- L176 `_parse_key_combo(keys: str)` (function) — Parse a key string like 'cmd+s' into (key, modifiers).
- L201 `_AsyncBridge` (class) — Runs one asyncio loop on a daemon thread; marshals coroutines from the caller.
- L204 `__init__(self)` (method)
- L209 `start(self)` (method)
- L231 `run(self, coro, timeout: Optional[float]=30.0)` (method)
- L242 `stop(self)` (method)
- L255 `_CuaDriverSession` (class) — Holds the mcp ClientSession. Spawned lazily; re-entered on drop.
- L258 `__init__(self, bridge: _AsyncBridge)` (method)
- L265 `_require_started(self)` (method)
- L269 `_aenter(self)` (method)
- L289 `_aexit(self)` (method)
- L298 `start(self)` (method)
- L306 `stop(self)` (method)
- L315 `_call_tool_async(self, name: str, args: Dict[str, Any])` (method)
- L320 `_is_closed_session_error(exc: Exception)` (method) — Return True for MCP/stdio failures that are recoverable by reconnecting.
- L330 `_restart_session_locked(self)` (method) — Recreate the MCP session after the daemon/stdin transport was closed.
- L341 `call_tool(self, name: str, args: Dict[str, Any], timeout: float=30.0)` (method)
- L357 `_extract_tool_result(mcp_result: Any)` (function) — Convert an mcp CallToolResult into a plain dict.
- L398 `CuaDriverBackend` (class) — Default computer-use backend. macOS-only via cua-driver MCP.
- L401 `__init__(self)` (method)
- L410 `start(self)` (method)
- L413 `stop(self)` (method)
- L419 `is_available(self)` (method)
- L425 `capture(self, mode: str='som', app: Optional[str]=None)` (method) — Capture the frontmost on-screen window (optionally filtered by app name).
- L554 `click(self, *, element: Optional[int]=None, x: Optional[int]=None, y: Optional[int]=None, button: str='left', click_count: int=1, modifiers: Optional[List[str]]=None)` (method)
- L595 `drag(self, *, from_element: Optional[int]=None, to_element: Optional[int]=None, from_xy: Optional[Tuple[int, int]]=None, to_xy: Optional[Tuple[int, int]]=None, button: str='left', modifiers: Optional[List[str]]=None)` (method)
- L625 `scroll(self, *, direction: str, amount: int=3, element: Optional[int]=None, x: Optional[int]=None, y: Optional[int]=None, modifiers: Optional[List[str]]=None)` (method)
- L653 `type_text(self, text: str)` (method)
- L660 `key(self, keys: str)` (method)
- L678 `set_value(self, value: str, element: Optional[int]=None)` (method) — Set a value on an element. Handles AXPopUpButton selects natively.
- L697 `list_apps(self)` (method)
- L714 `focus_app(self, app: str, raise_window: bool=False)` (method) — Target an app for subsequent actions without stealing system focus.
- L765 `_action(self, name: str, args: Dict[str, Any])` (method)
