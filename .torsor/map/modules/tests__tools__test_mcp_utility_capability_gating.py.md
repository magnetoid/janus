---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_utility_capability_gating.py

Symbols in `tests/tools/test_mcp_utility_capability_gating.py`.

- L34 `_make_init_result(*, resources: bool, prompts: bool)` (function) — Build a fake ``InitializeResult`` whose ``capabilities`` sub-object
- L50 `_make_fake_server(*, initialize_result)` (function) — Build a stand-in ``MCPServerTask`` that exposes just the fields
- L68 `_handler_keys(selected)` (function)
- L72 `TestCapabilityGatedRegistration` (class)
- L73 `test_tools_only_server_gets_no_utility_schemas(self)` (method) — Context7-shaped server (tools only, no prompts / resources) should
- L88 `test_resources_only_server_gets_resource_stubs_only(self)` (method)
- L97 `test_prompts_only_server_gets_prompt_stubs_only(self)` (method)
- L106 `test_fully_capable_server_gets_all_four_stubs(self)` (method)
- L118 `TestConfigFilterStillApplies` (class) — Per-server config flags ``tools.resources: false`` / ``tools.prompts: false``
- L122 `test_config_disables_resources_even_when_advertised(self)` (method)
- L135 `test_config_disables_prompts_even_when_advertised(self)` (method)
- L149 `TestLegacyFallback` (class) — When ``initialize_result`` is missing (older test fixtures or code
- L154 `test_no_initialize_result_falls_back_to_hasattr_check(self)` (method)
- L165 `test_no_initialize_result_respects_session_spec(self)` (method) — Legacy fallback still filters by ``hasattr(session, method)``, so
