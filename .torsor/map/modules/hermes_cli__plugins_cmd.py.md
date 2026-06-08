---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/plugins_cmd.py

Symbols in `hermes_cli/plugins_cmd.py`.

- L30 `_resolve_git_executable()` (function) — Resolve a git binary for subprocess use when ``PATH`` may be minimal.
- L64 `PluginOperationError` (class) — Recoverable plugin install/update failure (CLI exits; HTTP maps to 4xx).
- L74 `_plugins_dir()` (function) — Return the user plugins directory, creating it if needed.
- L81 `_sanitize_plugin_name(name: str, plugins_dir: Path, *, allow_subdir: bool=False)` (function) — Validate a plugin name and return the safe target path inside *plugins_dir*.
- L138 `_resolve_git_url(identifier: str)` (function) — Turn an identifier into a cloneable Git URL.
- L166 `_repo_name_from_url(url: str)` (function) — Extract the repo name from a Git URL for the plugin directory name.
- L180 `_read_manifest(plugin_dir: Path)` (function) — Read plugin.yaml and return the parsed dict, or empty dict.
- L195 `_copy_example_files(plugin_dir: Path, console)` (function) — Copy any .example files to their real names if they don't already exist.
- L216 `_missing_requires_env_names(manifest: dict)` (function) — Return declared ``requires_env`` names that are unset in ``~/.hermes/.env``.
- L234 `_prompt_plugin_env_vars(manifest: dict, console)` (function) — Prompt for required environment variables declared in plugin.yaml.
- L309 `_display_after_install(plugin_dir: Path, identifier: str)` (function) — Show after-install.md if it exists, otherwise a default message.
- L338 `_display_removed(name: str, plugins_dir: Path)` (function) — Show confirmation after removing a plugin.
- L348 `_require_installed_plugin(name: str, plugins_dir: Path, console)` (function) — Return the plugin path if it exists, or exit with an error listing installed plugins.
- L366 `_install_plugin_core(identifier: str, *, force: bool)` (function) — Clone Git plugin into ``~/.hermes/plugins``.
- L459 `cmd_install(identifier: str, force: bool=False, enable: Optional[bool]=None)` (function) — Install a plugin from a Git URL or owner/repo shorthand.
- L542 `cmd_update(name: str)` (function) — Update an installed plugin by pulling latest from its git remote.
- L582 `cmd_remove(name: str)` (function) — Remove an installed plugin by name.
- L599 `_get_disabled_set()` (function) — Read the disabled plugins set from config.yaml.
- L614 `_save_disabled_set(disabled: set)` (function) — Write the disabled plugins list to config.yaml.
- L624 `_get_enabled_set()` (function) — Read the enabled plugins allow-list from config.yaml.
- L642 `_save_enabled_set(enabled: set)` (function) — Write the enabled plugins list to config.yaml.
- L652 `cmd_enable(name: str)` (function) — Add a plugin to the enabled allow-list (and remove it from disabled).
- L679 `cmd_disable(name: str)` (function) — Remove a plugin from the enabled allow-list (and add to disabled).
- L705 `_plugin_exists(name: str)` (function) — Return True if a plugin with *name* is installed (user) or bundled.
- L731 `_discover_all_plugins()` (function) — Return a list of (name, version, description, source, dir_path) for
- L784 `_plugin_status(name: str, enabled: set, disabled: set)` (function) — Return the user-facing activation state for a plugin name.
- L793 `_filter_plugin_entries(entries: list, args: Any, enabled: set, disabled: set)` (function) — Apply ``hermes plugins list`` CLI filters.
- L806 `cmd_list(args: Any | None=None)` (function) — List all plugins (bundled + user) with enabled/disabled state.
- L877 `_discover_memory_providers()` (function) — Return [(name, description), ...] for available memory providers.
- L886 `_discover_context_engines()` (function) — Return [(name, description), ...] for available context engines.
- L918 `_get_current_memory_provider()` (function) — Return the current memory.provider from config (empty = built-in).
- L928 `_get_current_context_engine()` (function) — Return the current context.engine from config.
- L938 `_save_memory_provider(name: str)` (function) — Persist memory.provider to config.yaml.
- L948 `_save_context_engine(name: str)` (function) — Persist context.engine to config.yaml.
- L958 `_configure_memory_provider()` (function) — Launch a radio picker for memory providers. Returns True if changed.
- L996 `_configure_context_engine()` (function) — Launch a radio picker for context engines. Returns True if changed.
- L1039 `cmd_toggle()` (function) — Interactive composite UI — general plugins + provider plugin categories.
- L1095 `_run_composite_ui(curses, plugin_names, plugin_labels, plugin_selected, disabled, categories, console)` (function) — Custom curses screen with checkboxes + category action rows.
- L1356 `_run_composite_fallback(plugin_names, plugin_labels, plugin_selected, disabled, categories, console)` (function) — Text-based fallback for the composite plugins UI.
- L1416 `dashboard_install_plugin(identifier: str, *, force: bool, enable: bool)` (function) — Non-interactive install for the web dashboard. Returns a JSON-serializable dict.
- L1465 `_get_plugin_toolset_key(name: str)` (function) — Return the toolset key a plugin registers its tools under, or None.
- L1511 `_toggle_plugin_toolset(name: str, *, enable: bool)` (function) — Add or remove a plugin's toolset from platform_toolsets for all platforms.
- L1549 `dashboard_set_agent_plugin_enabled(name: str, *, enabled: bool)` (function) — Enable or disable a plugin in ``config.yaml`` (runtime allow/deny lists).
- L1582 `_user_installed_plugin_dir(name: str)` (function) — Resolved path under ``~/.hermes/plugins/<name>`` if it exists.
- L1592 `dashboard_update_user_plugin(name: str)` (function) — ``git pull`` inside ``~/.hermes/plugins/<name>``.
- L1618 `_git_pull_plugin_dir(target: Path)` (function)
- L1641 `dashboard_remove_user_plugin(name: str)` (function) — Delete a plugin tree under ``~/.hermes/plugins/`` only.
- L1659 `plugins_command(args)` (function) — Dispatch hermes plugins subcommands.
