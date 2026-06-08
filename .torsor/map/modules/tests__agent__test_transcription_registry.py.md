---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_transcription_registry.py

Symbols in `tests/agent/test_transcription_registry.py`.

- L26 `_FakeProvider` (class)
- L27 `__init__(self, name: str='fake', display: Optional[str]=None, available: bool=True, transcribe_impl: Optional[Any]=None)` (method)
- L40 `name(self)` (method)
- L44 `display_name(self)` (method)
- L47 `is_available(self)` (method)
- L50 `transcribe(self, file_path: str, **kw)` (method)
- L57 `_reset_registry()` (function)
- L68 `TestRegistration` (class)
- L69 `test_happy_path(self)` (method)
- L75 `test_rejects_non_provider_type(self)` (method)
- L80 `test_rejects_empty_name(self)` (method)
- L86 `test_rejects_whitespace_name(self)` (method)
- L96 `test_rejects_builtin_shadow_with_warning(self, builtin, caplog)` (method)
- L105 `test_builtin_shadow_case_insensitive(self, caplog)` (method)
- L114 `test_reregistration_overwrites(self, caplog)` (method)
- L129 `TestLookup` (class)
- L130 `test_get_provider_missing_returns_none(self)` (method)
- L133 `test_get_provider_non_string_returns_none(self)` (method)
- L137 `test_get_provider_case_insensitive(self)` (method)
- L143 `test_get_provider_whitespace_tolerant(self)` (method)
- L148 `test_list_providers_sorted(self)` (method)
- L161 `TestABCContract` (class)
- L162 `test_must_implement_transcribe(self)` (method)
- L172 `test_must_implement_name(self)` (method)
- L181 `test_display_name_defaults_to_title(self)` (method)
- L185 `test_display_name_override_respected(self)` (method)
- L189 `test_is_available_default_true(self)` (method)
- L193 `test_list_models_default_empty(self)` (method)
- L197 `test_default_model_none_when_no_models(self)` (method)
- L201 `test_default_model_first_listed(self)` (method)
- L209 `test_get_setup_schema_default_minimal(self)` (method)
- L221 `TestBuiltinSync` (class) — ``_BUILTIN_NAMES`` in agent/transcription_registry.py is duplicated
- L232 `test_registry_builtins_match_dispatcher_builtins(self)` (method)
