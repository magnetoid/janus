---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_tts_registry.py

Symbols in `tests/agent/test_tts_registry.py`.

- L32 `_FakeProvider` (class)
- L33 `__init__(self, name: str='fake', display: Optional[str]=None, voice_compat: bool=False, synthesize_impl: Optional[Any]=None)` (method)
- L46 `name(self)` (method)
- L50 `display_name(self)` (method)
- L54 `voice_compatible(self)` (method)
- L57 `synthesize(self, text: str, output_path: str, **kw)` (method)
- L64 `_reset_registry()` (function)
- L75 `TestRegistration` (class)
- L76 `test_happy_path(self)` (method)
- L82 `test_rejects_non_provider_type(self)` (method)
- L87 `test_rejects_empty_name(self)` (method)
- L93 `test_rejects_whitespace_name(self)` (method)
- L104 `test_rejects_builtin_shadow_with_warning(self, builtin, caplog)` (method) — Built-in names always win — plugin registration is silently ignored
- L116 `test_builtin_shadow_case_insensitive(self, caplog)` (method) — ``EDGE``/``Edge``/``  edge  `` all collide with the ``edge`` built-in.
- L126 `test_reregistration_overwrites(self, caplog)` (method)
- L141 `TestLookup` (class)
- L142 `test_get_provider_missing_returns_none(self)` (method)
- L145 `test_get_provider_non_string_returns_none(self)` (method)
- L149 `test_get_provider_case_insensitive(self)` (method)
- L155 `test_get_provider_whitespace_tolerant(self)` (method)
- L160 `test_list_providers_sorted(self)` (method)
- L173 `TestABCContract` (class)
- L174 `test_must_implement_synthesize(self)` (method)
- L184 `test_must_implement_name(self)` (method)
- L193 `test_display_name_defaults_to_title(self)` (method)
- L197 `test_display_name_override_respected(self)` (method)
- L201 `test_is_available_default_true(self)` (method)
- L205 `test_list_voices_default_empty(self)` (method)
- L209 `test_list_models_default_empty(self)` (method)
- L213 `test_default_model_none_when_no_models(self)` (method)
- L217 `test_default_voice_none_when_no_voices(self)` (method)
- L221 `test_default_model_first_listed(self)` (method)
- L229 `test_default_voice_first_listed(self)` (method)
- L237 `test_get_setup_schema_default_minimal(self)` (method)
- L243 `test_stream_raises_not_implemented_by_default(self)` (method)
- L248 `test_voice_compatible_default_false(self)` (method)
- L252 `test_voice_compatible_override(self)` (method)
- L262 `TestResolveOutputFormat` (class)
- L264 `test_valid_passes_through(self, valid)` (method)
- L267 `test_uppercase_normalized(self)` (method)
- L271 `test_whitespace_stripped(self)` (method)
- L274 `test_invalid_returns_default(self)` (method)
- L278 `test_none_returns_default(self)` (method)
- L281 `test_non_string_returns_default(self)` (method)
- L291 `TestBuiltinSync` (class) — ``_BUILTIN_NAMES`` in agent/tts_registry.py is duplicated from
- L301 `test_registry_builtins_match_dispatcher_builtins(self)` (method)
