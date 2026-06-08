---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_api_server_toolset.py

Symbols in `tests/gateway/test_api_server_toolset.py`.

- L8 `TestHermesApiServerToolset` (class) — Tests for the hermes-api-server toolset definition.
- L11 `test_toolset_exists(self)` (method)
- L15 `test_toolset_validates(self)` (method)
- L18 `test_toolset_includes_web_tools(self)` (method)
- L23 `test_toolset_includes_core_tools(self)` (method)
- L35 `test_toolset_includes_browser_tools(self)` (method)
- L42 `test_toolset_includes_homeassistant_tools(self)` (method)
- L47 `test_toolset_excludes_clarify(self)` (method)
- L51 `test_toolset_excludes_send_message(self)` (method)
- L55 `test_toolset_excludes_text_to_speech(self)` (method)
- L60 `TestApiServerPlatformConfig` (class)
- L61 `test_platforms_dict_includes_api_server(self)` (method)
- L67 `TestApiServerAdapterToolset` (class)
- L69 `test_create_agent_reads_config_toolsets(self)` (method) — API server resolves toolsets from config like all other platforms.
- L99 `test_create_agent_respects_config_override(self)` (method) — User can override API server toolsets via platform_toolsets in config.yaml.
