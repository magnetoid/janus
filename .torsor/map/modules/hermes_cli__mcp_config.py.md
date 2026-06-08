---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/mcp_config.py

Symbols in `hermes_cli/mcp_config.py`.

- L45 `_info(text: str)` (function)
- L48 `_success(text: str)` (function)
- L51 `_warning(text: str)` (function)
- L54 `_error(text: str)` (function)
- L58 `_confirm(question: str, default: bool=True)` (function)
- L70 `_prompt(question: str, *, password: bool=False, default: str='')` (function)
- L77 `_get_mcp_servers(config: Optional[dict]=None)` (function) — Return the ``mcp_servers`` dict from config, or empty dict.
- L87 `_save_mcp_server(name: str, server_config: dict)` (function) — Add or update a server entry in config.yaml.
- L94 `_remove_mcp_server(name: str)` (function) — Remove a server from config.yaml.  Returns True if it existed.
- L107 `_env_key_for_server(name: str)` (function) — Convert server name to an env-var key like ``MCP_MYSERVER_API_KEY``.
- L112 `_strip_bearer_prefix(token: str)` (function) — Strip a leading ``Bearer `` from a pasted token.
- L127 `_parse_env_assignments(raw_env: Optional[List[str]])` (function) — Parse ``KEY=VALUE`` strings from CLI args into an env dict.
- L146 `_apply_mcp_preset(name: str, *, preset_name: Optional[str], url: Optional[str], command: Optional[str], cmd_args: List[str], server_config: Dict[str, Any])` (function) — Apply a known MCP preset when transport details were omitted.
- L182 `_resolve_mcp_server_config(config: dict)` (function) — Resolve ``${ENV}`` placeholders in a server config before connecting.
- L203 `_probe_single_server(name: str, config: dict, connect_timeout: float=30)` (function) — Temporarily connect to one MCP server, list its tools, disconnect.
- L248 `_oauth_tokens_present(name: str)` (function) — Return True if an OAuth token file exists on disk for ``name``.
- L264 `_unwrap_exception_group(exc: BaseException)` (function) — Extract the root-cause exception from anyio TaskGroup wrappers.
- L282 `cmd_mcp_add(args)` (function) — Add a new MCP server with discovery-first tool selection.
- L479 `cmd_mcp_remove(args)` (function) — Remove an MCP server from config.
- L511 `cmd_mcp_list(args=None)` (function) — List all configured MCP servers.
- L580 `cmd_mcp_test(args)` (function) — Test connection to an MCP server.
- L644 `cmd_mcp_login(args)` (function) — Force re-authentication for an OAuth-based MCP server.
- L731 `cmd_mcp_configure(args)` (function) — Reconfigure which tools are enabled for an existing MCP server.
- L830 `mcp_command(args)` (function) — Main dispatcher for ``hermes mcp`` subcommands.
