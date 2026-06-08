---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/mcp_catalog.py

Symbols in `hermes_cli/mcp_catalog.py`.

- L55 `EnvVarSpec` (class)
- L64 `AuthSpec` (class)
- L74 `TransportSpec` (class)
- L83 `InstallSpec` (class) — Optional bootstrap step (git clone + dep install).
- L95 `ToolsSpec` (class) — Manifest-side tool-selection hints.
- L109 `CatalogEntry` (class)
- L124 `CatalogError` (class) — Manifest parse/validation failure or install error.
- L128 `_catalog_root()` (function) — Return the optional-mcps/ directory shipped with this Hermes install.
- L135 `_parse_env_spec(raw: Any)` (function)
- L150 `_parse_manifest(path: Path)` (function) — Read and validate a manifest.yaml. Raise CatalogError on any problem.
- L265 `list_catalog()` (function) — Return all valid catalog entries, sorted by name.
- L301 `catalog_diagnostics()` (function) — Diagnostics from the most recent :func:`list_catalog` call.
- L314 `get_entry(name: str)` (function) — Look up a single entry by name. ``official/<name>`` prefix accepted.
- L327 `installed_servers()` (function) — Return current ``mcp_servers`` block from config.yaml.
- L334 `is_installed(name: str)` (function)
- L338 `is_enabled(name: str)` (function)
- L352 `_install_root()` (function) — Where git-bootstrapped MCPs are cloned. Per-user, profile-aware.
- L359 `_run_bootstrap(cwd: Path, commands: List[str])` (function) — Execute bootstrap commands in *cwd*. Raise CatalogError on first failure.
- L374 `_do_git_install(entry: CatalogEntry)` (function) — Clone the entry's repo into ``~/.hermes/mcp-installs/<name>`` and run
- L426 `_expand_install_dir(value: str, install_dir: Optional[Path])` (function)
- L436 `_prompt_env_vars(specs: List[EnvVarSpec])` (function) — Walk the env spec list, prompting the user for each. Writes secrets and
- L460 `_build_server_config(entry: CatalogEntry, install_dir: Optional[Path])` (function) — Translate a manifest into the ``mcp_servers.<name>`` block format used
- L478 `_read_prior_tool_selection(name: str)` (function) — Return the user's prior `tools.include` for *name*, if any.
- L496 `_probe_tools(name: str)` (function) — Connect to a freshly-configured MCP and list its tools.
- L520 `_write_tools_include(name: str, include: Optional[List[str]])` (function) — Persist or clear ``mcp_servers.<name>.tools.include``.
- L540 `_apply_tool_selection(entry: CatalogEntry, *, prior_selection: Optional[List[str]])` (function) — Probe the server and let the user pick which tools to enable.
- L669 `install_entry(entry: CatalogEntry, *, enable: bool=True)` (function) — Install a catalog entry end-to-end.
- L754 `uninstall_entry(name: str, *, purge_install_dir: bool=True)` (function) — Remove a catalog-installed MCP from config and (optionally) wipe its
