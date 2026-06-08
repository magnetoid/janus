---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_registry.py

Symbols in `tests/tools/test_registry.py`.

- L11 `_dummy_handler(args, **kwargs)` (function)
- L15 `_make_schema(name='test_tool')` (function)
- L23 `TestRegisterAndDispatch` (class)
- L24 `test_register_and_dispatch(self)` (method)
- L35 `test_dispatch_passes_args(self)` (method)
- L51 `TestGetDefinitions` (class)
- L52 `test_returns_openai_format(self)` (method)
- L67 `test_skips_unavailable_tools(self)` (method)
- L87 `test_reuses_shared_check_fn_once_per_call(self)` (method)
- L115 `TestUnknownToolDispatch` (class)
- L116 `test_returns_error_json(self)` (method)
- L123 `TestToolsetAvailability` (class)
- L124 `test_no_check_fn_is_available(self)` (method)
- L131 `test_check_fn_controls_availability(self)` (method)
- L142 `test_check_toolset_requirements(self)` (method)
- L163 `test_get_all_tool_names(self)` (method)
- L173 `test_get_registered_toolset_names(self)` (method)
- L186 `test_get_tool_names_for_toolset(self)` (method)
- L199 `test_handler_exception_returns_error(self)` (method)
- L213 `TestCheckFnExceptionHandling` (class) — Verify that a raising check_fn is caught rather than crashing.
- L216 `test_is_toolset_available_catches_exception(self)` (method)
- L228 `test_check_toolset_requirements_survives_raising_check(self)` (method)
- L249 `test_get_definitions_skips_raising_check(self)` (method)
- L269 `test_check_tool_availability_survives_raising_check(self)` (method)
- L291 `TestBuiltinDiscovery` (class)
- L292 `test_discovers_all_real_self_registering_builtin_tool_modules(self)` (method)
- L306 `test_imports_only_self_registering_modules(self, tmp_path)` (method)
- L323 `test_skips_mcp_tool_even_if_it_registers(self, tmp_path)` (method)
- L343 `TestEmojiMetadata` (class) — Verify per-tool emoji registration and lookup.
- L346 `test_emoji_stored_on_entry(self)` (method)
- L354 `test_get_emoji_returns_registered(self)` (method)
- L362 `test_get_emoji_returns_default_when_unset(self)` (method)
- L371 `test_get_emoji_returns_default_for_unknown_tool(self)` (method)
- L376 `test_emoji_empty_string_treated_as_unset(self)` (method)
- L385 `TestEntryLookup` (class)
- L386 `test_get_entry_returns_registered_entry(self)` (method)
- L396 `test_get_entry_returns_none_for_unknown_tool(self)` (method)
- L401 `TestSecretCaptureResultContract` (class)
- L402 `test_secret_request_result_does_not_include_secret_value(self)` (method)
- L411 `TestThreadSafety` (class)
- L412 `test_get_available_toolsets_uses_coherent_snapshot(self, monkeypatch)` (method)
- L434 `test_check_tool_availability_tolerates_concurrent_register(self)` (method)
- L494 `test_get_available_toolsets_tolerates_concurrent_deregister(self)` (method)
