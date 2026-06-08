---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/codex_runtime_plugin_migration.py

Symbols in `hermes_cli/codex_runtime_plugin_migration.py`.

- L59 `MigrationReport` (class) — Outcome of a migration pass.
- L72 `summary(self)` (method)
- L127 `_translate_one_server(name: str, hermes_cfg: dict)` (function) — Translate one Hermes MCP server config to the codex inline-table dict
- L199 `_format_toml_value(value: Any)` (function) — Minimal TOML value formatter for the value types we emit.
- L239 `_quote_key(key: str)` (function) — Return key bare-or-quoted depending on whether it's a valid bare key.
- L246 `render_codex_toml_section(servers: dict[str, dict], plugins: Optional[list[dict]]=None, default_permission_profile: Optional[str]=None)` (function) — Render the managed [mcp_servers.<n>] / [plugins.<id>] / [permissions]
- L307 `_insert_managed_block_at_top_level(user_text: str, managed_block: str)` (function) — Insert Hermes' managed Codex TOML block while keeping root keys root-scoped.
- L338 `_strip_unmanaged_plugin_tables(toml_text: str)` (function) — Remove ``[plugins."<name>@<marketplace>"]`` tables that live OUTSIDE the
- L384 `_looks_like_table_header(stripped_line: str)` (function) — Return True if ``stripped_line`` is a TOML table header.
- L404 `_strip_existing_managed_block(toml_text: str)` (function) — Remove any prior managed section so re-runs idempotently replace it.
- L450 `_query_codex_plugins(codex_home: Optional[Path]=None, timeout: float=8.0)` (function) — Query codex's `plugin/list` for installed curated plugins.
- L531 `_looks_like_test_tempdir(path: str)` (function) — Heuristic: does ``path`` look like a pytest/transient tempdir?
- L557 `_build_hermes_tools_mcp_entry()` (function) — Build the codex stdio-transport entry that launches Hermes' own
- L609 `migrate(hermes_config: dict, *, codex_home: Optional[Path]=None, dry_run: bool=False, discover_plugins: bool=True, default_permission_profile: Optional[str]=':workspace', expose_hermes_tools: bool=True)` (function) — Translate Hermes mcp_servers config + Codex curated plugins into
