---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_mcp_config.py

Symbols in `tests/hermes_cli/test_mcp_config.py`.

- L19 `_isolate_config(tmp_path, monkeypatch)` (function) — Redirect all config I/O to a temp directory.
- L36 `_make_args(**kwargs)` (function) — Build a minimal argparse.Namespace.
- L52 `_seed_config(tmp_path: Path, mcp_servers: dict)` (function) — Write a config.yaml with the given mcp_servers.
- L62 `FakeTool` (class) — Mimics an MCP tool object returned by the SDK.
- L65 `__init__(self, name: str, description: str='')` (method)
- L74 `TestMcpList` (class)
- L75 `test_list_empty_config(self, tmp_path, capsys)` (method)
- L82 `test_list_with_servers(self, tmp_path, capsys)` (method)
- L104 `test_list_enabled_default_true(self, tmp_path, capsys)` (method) — Server without explicit enabled key defaults to enabled.
- L121 `TestMcpRemove` (class)
- L122 `test_remove_existing_server(self, tmp_path, capsys, monkeypatch)` (method)
- L140 `test_remove_nonexistent(self, tmp_path, capsys)` (method)
- L148 `test_remove_cleans_oauth_tokens(self, tmp_path, capsys, monkeypatch)` (method)
- L174 `TestMcpAdd` (class)
- L175 `test_add_no_transport(self, capsys)` (method) — Must specify --url or --command.
- L183 `test_add_http_server_all_tools(self, tmp_path, capsys, monkeypatch)` (method) — Add an HTTP server, accept all tools.
- L214 `test_add_stdio_server(self, tmp_path, capsys, monkeypatch)` (method) — Add a stdio server.
- L244 `test_add_connection_failure_save_disabled(self, tmp_path, capsys, monkeypatch)` (method) — Failed connection → option to save as disabled.
- L269 `test_add_stdio_server_with_env(self, tmp_path, capsys, monkeypatch)` (method) — Stdio servers can persist explicit environment variables.
- L305 `test_add_stdio_server_rejects_invalid_env_name(self, capsys)` (method) — Invalid environment variable names are rejected up front.
- L318 `test_add_http_server_rejects_env_flag(self, capsys)` (method) — The --env flag is only valid for stdio transports.
- L330 `test_add_preset_fills_transport(self, tmp_path, capsys, monkeypatch)` (method) — A preset fills in command/args when no explicit transport given.
- L363 `test_preset_does_not_override_explicit_command(self, tmp_path, capsys, monkeypatch)` (method) — Explicit transports win over presets.
- L400 `test_unknown_preset_rejected(self, capsys)` (method) — An unknown preset name is rejected with a clear error.
- L413 `TestMcpTest` (class)
- L414 `test_test_not_found(self, tmp_path, capsys)` (method)
- L422 `test_test_success(self, tmp_path, capsys, monkeypatch)` (method)
- L445 `TestEnvVarInterpolation` (class)
- L446 `test_interpolate_simple(self, monkeypatch)` (method)
- L453 `test_interpolate_missing_var(self, monkeypatch)` (method)
- L460 `test_interpolate_nested_dict(self, monkeypatch)` (method)
- L471 `test_interpolate_list(self, monkeypatch)` (method)
- L478 `test_interpolate_non_string(self)` (method)
- L490 `TestProbeEnvResolution` (class) — The probe path must resolve ``${ENV}`` before connecting, so the
- L496 `test_resolve_interpolates_header(self, monkeypatch)` (method)
- L506 `test_resolve_leaves_unset_var_literal(self, monkeypatch)` (method)
- L517 `test_probe_resolves_before_connect(self, monkeypatch)` (method) — _probe_single_server must pass the RESOLVED config to _connect_server.
- L550 `TestStripBearerPrefix` (class) — Pasted tokens that already include ``Bearer `` would otherwise produce
- L554 `test_bare_token_unchanged(self)` (method)
- L559 `test_strips_bearer_prefix(self)` (method)
- L564 `test_strips_case_insensitive_and_whitespace(self)` (method)
- L570 `test_does_not_strip_without_space(self)` (method)
- L576 `test_non_string_passthrough(self)` (method)
- L586 `TestConfigHelpers` (class)
- L587 `test_save_and_load_mcp_server(self, tmp_path)` (method)
- L595 `test_remove_mcp_server(self, tmp_path)` (method)
- L609 `test_remove_nonexistent(self, tmp_path)` (method)
- L614 `test_env_key_for_server(self)` (method)
- L625 `TestDispatcher` (class)
- L626 `test_no_action_shows_list(self, tmp_path, capsys)` (method)
- L641 `TestMcpRemoveEvictsManager` (class)
- L642 `test_remove_evicts_in_memory_provider(self, tmp_path, capsys, monkeypatch)` (method) — After cmd_mcp_remove, the MCPOAuthManager no longer caches the provider.
- L668 `TestMcpLogin` (class)
- L669 `test_login_rejects_unknown_server(self, tmp_path, capsys)` (method)
- L676 `test_login_rejects_non_oauth_server(self, tmp_path, capsys)` (method)
- L685 `test_login_rejects_stdio_server(self, tmp_path, capsys)` (method)
- L694 `test_login_false_success_no_token(self, tmp_path, capsys, monkeypatch)` (method) — Probe lists tools without auth (Google Drive), but no token landed.
- L722 `test_login_genuine_success_with_token(self, tmp_path, capsys, monkeypatch)` (method) — Probe lists tools AND a token exists → report real success.
