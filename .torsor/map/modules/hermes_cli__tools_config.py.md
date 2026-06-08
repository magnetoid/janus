---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/tools_config.py

Symbols in `hermes_cli/tools_config.py`.

- L86 `gui_toolset_label(label: str)` (function) — Strip leading emoji/icons from toolset titles for GUI surfaces.
- L118 `_xai_credentials_present()` (function) — Cheap, side-effect-free check for usable xAI credentials.
- L156 `_toolset_allowed_for_platform(ts_key: str, platform: str)` (function) — Return True if ``ts_key`` is configurable on ``platform``.
- L165 `_get_effective_configurable_toolsets()` (function) — Return CONFIGURABLE_TOOLSETS + any plugin-provided toolsets.
- L191 `_get_plugin_toolset_keys()` (function) — Return the set of toolset keys provided by plugins.
- L201 `_checklist_toolset_keys(platform: str)` (function) — Return the toolset keys the ``hermes tools`` checklist actually offers
- L578 `_cua_driver_cmd()` (function) — Return the cua-driver executable name/path, honoring non-empty overrides.
- L583 `_pip_install(args: List[str], *, timeout: int=300, capture_output: bool=True)` (function) — Install Python packages from a post-setup hook.
- L652 `_check_cua_driver_asset_for_arch()` (function) — Check whether the latest CUA release ships an asset for this architecture.
- L700 `install_cua_driver(upgrade: bool=False)` (function) — Install or refresh the cua-driver binary used by Computer Use.
- L793 `_run_cua_driver_installer(label: str='Installing', verbose: bool=True)` (function) — Run the upstream cua-driver install.sh. Returns True on success.
- L833 `_run_post_setup(post_setup_key: str)` (function) — Run post-setup hooks for tools that need extra installation steps.
- L1175 `valid_post_setup_keys()` (function) — Return the set of post-setup keys declared by any visible provider.
- L1207 `run_post_setup_command(args)` (function) — ``hermes tools post-setup <key>`` — non-interactive post-setup runner.
- L1239 `_get_enabled_platforms()` (function) — Return platform keys that are configured (have tokens or are CLI).
- L1255 `_platform_toolset_summary(config: dict, platforms: Optional[List[str]]=None)` (function) — Return a summary of enabled toolsets per platform.
- L1271 `_parse_enabled_flag(value, default: bool=True)` (function) — Parse bool-like config values used by tool/platform settings.
- L1288 `_get_platform_tools(config: dict, platform: str, *, include_default_mcp_servers: bool=True)` (function) — Resolve which individual toolset names are enabled for a platform.
- L1538 `_save_platform_tools(config: dict, platform: str, enabled_toolset_keys: Set[str])` (function) — Save the selected toolset keys for a platform to config.
- L1594 `_toolset_has_keys(ts_key: str, config: dict=None, *, force_fresh: bool=False)` (function) — Check if a toolset's required API keys are configured.
- L1639 `_prompt_choice(question: str, choices: list, default: int=0)` (function) — Single-select menu (arrow keys). Delegates to curses_radiolist.
- L1651 `_estimate_tool_tokens()` (function) — Return estimated token counts per individual tool name.
- L1693 `_prompt_toolset_checklist(platform_label: str, enabled: Set[str], platform: str='cli', *, force_fresh: bool=True)` (function) — Multi-select checklist of toolsets. Returns set of selected toolset keys.
- L1756 `_configure_toolset(ts_key: str, config: dict, *, force_fresh: bool=True)` (function) — Configure a toolset - provider selection + API keys.
- L1776 `_plugin_image_gen_providers()` (function) — Build picker-row dicts from plugin-registered image gen providers.
- L1816 `_plugin_video_gen_providers()` (function) — Build picker-row dicts from plugin-registered video gen providers.
- L1864 `_plugin_web_search_providers()` (function) — Build picker-row dicts from plugin-registered web search providers.
- L1920 `_plugin_browser_providers()` (function) — Build picker-row dicts from plugin-registered cloud browser providers.
- L1967 `_plugin_tts_providers()` (function) — Build picker-row dicts from plugin-registered TTS providers.
- L2023 `_visible_providers(cat: dict, config: dict, *, force_fresh: bool=False)` (function) — Return provider entries visible for the current auth/config state.
- L2107 `_hidden_nous_gateway_message(cat: dict, config: dict, capability: str, *, force_fresh: bool=False)` (function) — Deprecated: Nous Tool Gateway rows are no longer hidden.
- L2144 `_post_setup_already_installed(post_setup_key: str)` (function) — Return True when the post_setup install side-effect is satisfied.
- L2157 `_toolset_needs_configuration_prompt(ts_key: str, config: dict, *, force_fresh: bool=False)` (function) — Return True when enabling this toolset should open provider setup.
- L2226 `_configure_tool_category(ts_key: str, cat: dict, config: dict, *, force_fresh: bool=True)` (function) — Configure a tool category with provider selection.
- L2340 `_is_provider_active(provider: dict, config: dict, *, force_fresh: bool=False)` (function) — Check if a provider entry matches the currently active config.
- L2415 `_detect_active_provider_index(providers: list, config: dict, *, force_fresh: bool=False)` (function) — Return the index of the currently active provider, or 0.
- L2445 `_fal_model_catalog()` (function) — Lazy-load the FAL model catalog from the tool module.
- L2460 `_format_imagegen_model_row(model_id: str, meta: dict, widths: dict)` (function) — Format a single picker row with column-aligned speed / strengths / price.
- L2470 `_configure_imagegen_model(backend_name: str, config: dict)` (function) — Prompt the user to pick a model for the given imagegen backend.
- L2532 `_plugin_image_gen_catalog(plugin_name: str)` (function) — Return ``(catalog_dict, default_model_id)`` for a plugin provider.
- L2559 `_configure_imagegen_model_for_plugin(plugin_name: str, config: dict)` (function) — Prompt the user to pick a model for a plugin-registered backend.
- L2614 `_select_plugin_image_gen_provider(plugin_name: str, config: dict)` (function) — Persist a plugin-backed image generation provider selection.
- L2629 `_plugin_video_gen_catalog(plugin_name: str)` (function) — Return ``(catalog_dict, default_model_id)`` for a video gen plugin.
- L2654 `_configure_videogen_model_for_plugin(plugin_name: str, config: dict)` (function) — Prompt for a video gen model from a plugin's catalog.
- L2714 `_select_plugin_video_gen_provider(plugin_name: str, config: dict, *, use_gateway: bool=False)` (function) — Persist a plugin-backed video generation provider selection.
- L2726 `_write_provider_config(provider: dict, config: dict, *, managed_feature)` (function) — Persist the provider/backend config keys for a selected provider.
- L2771 `apply_provider_selection(ts_key: str, provider_name: str, config: dict)` (function) — Non-interactively persist a provider selection for a toolset.
- L2827 `_configure_provider(provider: dict, config: dict, *, force_fresh: bool=True)` (function) — Configure a single provider - prompt for API keys and set config.
- L3004 `_configure_simple_requirements(ts_key: str)` (function) — Simple fallback for toolsets that just need env vars (no provider selection).
- L3067 `_reconfigure_tool(config: dict, *, force_fresh: bool=True)` (function) — Let user reconfigure an existing tool's provider or API key.
- L3113 `_toolset_enabled_for_reconfigure(ts_key: str, config: dict)` (function) — Return True if a configurable toolset is enabled anywhere.
- L3135 `_configure_tool_category_for_reconfig(ts_key: str, cat: dict, config: dict, *, force_fresh: bool=True)` (function) — Reconfigure a tool category - provider selection + API key update.
- L3198 `_reconfigure_provider(provider: dict, config: dict, *, force_fresh: bool=True)` (function) — Reconfigure a provider - update API keys.
- L3346 `_reconfigure_simple_requirements(ts_key: str)` (function) — Reconfigure simple env var requirements.
- L3372 `tools_command(args=None, first_install: bool=False, config: dict=None)` (function) — Entry point for `hermes tools` and `hermes setup tools`.
- L3643 `_configure_mcp_tools_interactive(config: dict)` (function) — Probe MCP servers for available tools and let user toggle them on/off.
- L3779 `_apply_toolset_change(config: dict, platform: str, toolset_names: List[str], action: str)` (function) — Add or remove built-in toolsets for a platform.
- L3789 `_apply_mcp_change(config: dict, targets: List[str], action: str)` (function) — Add or remove specific MCP tools from a server's exclude list.
- L3814 `_print_tools_list(enabled_toolsets: set, mcp_servers: dict, platform: str='cli')` (function) — Print a summary of enabled/disabled toolsets and MCP tool filters.
- L3856 `tools_disable_enable_command(args)` (function) — Enable, disable, or list tools for a platform.
