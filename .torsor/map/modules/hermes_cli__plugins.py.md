---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/plugins.py

Symbols in `hermes_cli/plugins.py`.

- L55 `get_bundled_plugins_dir()` (function) — Locate the bundled ``plugins/`` directory.
- L95 `_install_plugin_debug_handler(force: bool=False)` (function) — When HERMES_PLUGINS_DEBUG is on, tee plugin logs to stderr at DEBUG.
- L177 `_env_enabled(name: str)` (function) — Return True when an env var is set to a truthy opt-in value.
- L182 `_get_disabled_plugins()` (function) — Read the disabled plugins list from config.yaml.
- L198 `_get_enabled_plugins()` (function) — Read the enabled-plugins allow-list from config.yaml.
- L236 `PluginManifest` (class) — Parsed representation of a plugin.yaml manifest.
- L273 `LoadedPlugin` (class) — Runtime state for a single loaded plugin.
- L290 `PluginContext` (class) — Facade given to plugins so they can register tools and hooks.
- L293 `__init__(self, manifest: PluginManifest, manager: 'PluginManager')` (method)
- L302 `llm(self)` (method) — Return the plugin's :class:`agent.plugin_llm.PluginLlm` facade.
- L320 `register_tool(self, name: str, toolset: str, schema: dict, handler: Callable, check_fn: Callable | None=None, requires_env: list | None=None, is_async: bool=False, description: str='', emoji: str='', override: bool=False)` (method) — Register a tool in the global registry **and** track it as plugin-provided.
- L362 `inject_message(self, content: str, role: str='user')` (method) — Inject a message into the active conversation.
- L390 `register_cli_command(self, name: str, help: str, setup_fn: Callable, handler_fn: Callable | None=None, description: str='')` (method) — Register a CLI subcommand (e.g. ``hermes honcho ...``).
- L415 `register_command(self, name: str, handler: Callable, description: str='', args_hint: str='')` (method) — Register a slash command (e.g. ``/lcm``) available in CLI and gateway sessions.
- L471 `dispatch_tool(self, tool_name: str, args: dict, **kwargs)` (method) — Dispatch a tool call through the registry, with parent agent context.
- L502 `register_context_engine(self, engine)` (method) — Register a context engine to replace the built-in ContextCompressor.
- L534 `register_image_gen_provider(self, provider)` (method) — Register an image generation backend.
- L561 `register_dashboard_auth_provider(self, provider)` (method) — Register a dashboard authentication provider.
- L601 `register_video_gen_provider(self, provider)` (method) — Register a video generation backend.
- L628 `register_web_search_provider(self, provider)` (method) — Register a web search/extract backend.
- L656 `register_browser_provider(self, provider)` (method) — Register a cloud browser backend.
- L688 `register_tts_provider(self, provider)` (method) — Register a text-to-speech backend.
- L726 `register_transcription_provider(self, provider)` (method) — Register a speech-to-text backend.
- L770 `register_platform(self, name: str, label: str, adapter_factory: Callable, check_fn: Callable, validate_config: Callable | None=None, required_env: list | None=None, install_hint: str='', **entry_kwargs: Any)` (method) — Register a gateway platform adapter.
- L828 `register_auxiliary_task(self, key: str, *, display_name: str, description: str, defaults: Optional[Dict[str, Any]]=None)` (method) — Register a plugin-defined auxiliary LLM task.
- L939 `register_hook(self, hook_name: str, callback: Callable)` (method) — Register a lifecycle hook callback.
- L958 `register_middleware(self, kind: str, callback: Callable)` (method) — Register a behavior-changing middleware callback.
- L979 `register_skill(self, name: str, path: Path, description: str='')` (method) — Register a read-only skill provided by this plugin.
- L1029 `PluginManager` (class) — Central manager that discovers, loads, and invokes plugins.
- L1032 `__init__(self)` (method)
- L1053 `discover_and_load(self, force: bool=False)` (method) — Scan all plugin sources and load each plugin found.
- L1226 `_scan_directory(self, path: Path, source: str, skip_names: Optional[Set[str]]=None)` (method) — Read ``plugin.yaml`` manifests from subdirectories of *path*.
- L1251 `_scan_directory_level(self, path: Path, source: str, *, skip_names: Optional[Set[str]], prefix: str, depth: int)` (method) — Recursive implementation of :meth:`_scan_directory`.
- L1307 `_parse_manifest(self, manifest_file: Path, plugin_dir: Path, source: str, prefix: str)` (method) — Parse a single ``plugin.yaml`` into a :class:`PluginManifest`.
- L1402 `_scan_entry_points(self)` (method) — Check ``importlib.metadata`` for pip-installed plugins.
- L1432 `_load_plugin(self, manifest: PluginManifest)` (method) — Import a plugin module and call its ``register(ctx)`` function.
- L1514 `_load_directory_module(self, manifest: PluginManifest)` (method) — Import a directory-based plugin as ``hermes_plugins.<slug>``.
- L1552 `_load_entrypoint_module(self, manifest: PluginManifest)` (method) — Load a pip-installed plugin via its entry-point reference.
- L1574 `invoke_hook(self, hook_name: str, **kwargs: Any)` (method) — Call all registered callbacks for *hook_name*.
- L1611 `has_hook(self, hook_name: str)` (method) — Return True when at least one callback is registered for a hook.
- L1615 `has_middleware(self, kind: str)` (method) — Return True when at least one callback is registered for middleware.
- L1619 `invoke_middleware(self, kind: str, **kwargs: Any)` (method) — Call registered middleware callbacks for *kind*.
- L1646 `list_plugins(self)` (method) — Return a list of info dicts for all discovered plugins.
- L1672 `find_plugin_skill(self, qualified_name: str)` (method) — Return the ``Path`` to a plugin skill's SKILL.md, or ``None``.
- L1677 `list_plugin_skills(self, plugin_name: str)` (method) — Return sorted bare names of all skills registered by *plugin_name*.
- L1686 `remove_plugin_skill(self, qualified_name: str)` (method) — Remove a stale registry entry (silently ignores missing keys).
- L1698 `get_plugin_manager()` (function) — Return (and lazily create) the global PluginManager singleton.
- L1706 `discover_plugins(force: bool=False)` (function) — Discover and load all plugins.
- L1715 `invoke_hook(hook_name: str, **kwargs: Any)` (function) — Invoke a lifecycle hook on all loaded plugins.
- L1723 `invoke_middleware(kind: str, **kwargs: Any)` (function) — Invoke registered middleware callbacks.
- L1731 `has_middleware(kind: str)` (function) — Return True when middleware callbacks are registered for ``kind``.
- L1740 `has_hook(hook_name: str)` (function) — Return True when a hook has registered callbacks.
- L1748 `set_thread_tool_whitelist(allowed: Optional[Set[str]], deny_msg_fmt: str="Tool '{tool_name}' denied: not in this thread's tool whitelist")` (function)
- L1756 `clear_thread_tool_whitelist()` (function)
- L1760 `get_pre_tool_call_block_message(tool_name: str, args: Optional[Dict[str, Any]], task_id: str='', session_id: str='', tool_call_id: str='', turn_id: str='', api_request_id: str='', middleware_trace: Optional[List[Dict[str, Any]]]=None)` (function) — Check ``pre_tool_call`` hooks for a blocking directive.
- L1810 `_ensure_plugins_discovered(force: bool=False)` (function) — Return the global manager after ensuring plugin discovery has run.
- L1820 `get_plugin_context_engine()` (function) — Return the plugin-registered context engine, or None.
- L1825 `get_plugin_command_handler(name: str)` (function) — Return the handler for a plugin-registered slash command, or ``None``.
- L1834 `resolve_plugin_command_result(result: Any)` (function) — Resolve a plugin command return value, awaiting async handlers when needed.
- L1880 `get_plugin_commands()` (function) — Return the full plugin commands dict (name → {handler, description, plugin}).
- L1889 `get_plugin_auxiliary_tasks()` (function) — Return all plugin-registered auxiliary tasks as a stable-ordered list.
- L1904 `get_plugin_toolsets()` (function) — Return plugin toolsets as ``(key, label, description)`` tuples.
