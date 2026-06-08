---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/observability/nemo_relay/__init__.py

Symbols in `plugins/observability/nemo_relay/__init__.py`.

- L24 `_SessionState` (class)
- L36 `_SubagentParent` (class)
- L43 `_Settings` (class)
- L61 `_Runtime` (class)
- L62 `__init__(self, nemo_relay: Any, settings: _Settings)` (method)
- L72 `_configure_plugins_toml(self)` (method)
- L92 `_ensure_plugin_config_output_dirs(self, config: dict[str, Any])` (method)
- L111 `_configure_atof(self)` (method)
- L126 `ensure_session(self, kwargs: dict[str, Any])` (method)
- L163 `export_atif(self, state: _SessionState)` (method)
- L175 `close_session(self, kwargs: dict[str, Any])` (method)
- L193 `mark(self, name: str, kwargs: dict[str, Any])` (method)
- L202 `mark_subagent_start(self, kwargs: dict[str, Any])` (method)
- L219 `mark_subagent_stop(self, kwargs: dict[str, Any])` (method)
- L225 `managed_llm_enabled(self)` (method)
- L232 `managed_tool_enabled(self)` (method)
- L238 `execute_llm(self, kwargs: dict[str, Any])` (method)
- L279 `execute_tool(self, kwargs: dict[str, Any])` (method)
- L320 `register(ctx)` (function)
- L340 `on_session_start(**kwargs: Any)` (function)
- L346 `on_session_end(**kwargs: Any)` (function)
- L352 `on_session_finalize(**kwargs: Any)` (function)
- L358 `on_session_reset(**kwargs: Any)` (function)
- L364 `on_pre_llm_call(**kwargs: Any)` (function)
- L370 `on_post_llm_call(**kwargs: Any)` (function)
- L376 `on_pre_api_request(**kwargs: Any)` (function)
- L401 `on_post_api_request(**kwargs: Any)` (function)
- L424 `on_api_request_error(**kwargs: Any)` (function)
- L447 `on_pre_tool_call(**kwargs: Any)` (function)
- L469 `on_post_tool_call(**kwargs: Any)` (function)
- L492 `on_pre_approval_request(**kwargs: Any)` (function)
- L498 `on_post_approval_response(**kwargs: Any)` (function)
- L504 `on_subagent_start(**kwargs: Any)` (function)
- L510 `on_subagent_stop(**kwargs: Any)` (function)
- L516 `on_llm_execution_middleware(**kwargs: Any)` (function)
- L527 `on_tool_execution_middleware(**kwargs: Any)` (function)
- L538 `_get_runtime()` (function)
- L560 `_load_settings()` (function)
- L583 `_load_plugins_config(path: str)` (function)
- L593 `_enabled_component_config(plugins_config: dict[str, Any] | None, kind: str)` (function)
- L612 `_adaptive_mode(config: dict[str, Any] | None)` (function)
- L621 `_env(name: str)` (function)
- L625 `_atif_subagent_export_mode()` (function)
- L630 `_env_bool(name: str)` (function)
- L634 `_session_id(kwargs: dict[str, Any])` (function)
- L638 `_child_session_id(kwargs: dict[str, Any])` (function)
- L642 `_subagent_child_metadata(kwargs: dict[str, Any], parent_metadata: dict[str, Any])` (function)
- L666 `_api_key(kwargs: dict[str, Any])` (function)
- L670 `_tool_key(kwargs: dict[str, Any])` (function)
- L677 `_metadata(kwargs: dict[str, Any])` (function)
- L713 `_jsonable(value: Any)` (function)
- L736 `_value(obj: Any, key: str, default: Any=None)` (function)
- L742 `_llm_response_payload(response: Any)` (function) — Return the LLM response shape NeMo Relay's ATIF conversion expects.
- L778 `_tool_calls_payload(tool_calls: Any)` (function)
- L797 `_safe(fn)` (function)
- L804 `_resolve_awaitable(value: Any)` (function)
- L833 `reset_for_tests()` (function)
