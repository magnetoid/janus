---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tts_plugin_dispatch.py

Symbols in `tests/tools/test_tts_plugin_dispatch.py`.

- L40 `_FakeTTSProvider` (class)
- L41 `__init__(self, name: str, voice_compat: bool=False, raise_exc: Optional[BaseException]=None, return_path: Optional[str]=None)` (method)
- L56 `name(self)` (method)
- L60 `voice_compatible(self)` (method)
- L63 `synthesize(self, text, output_path, **kw)` (method)
- L75 `_reset_registry()` (function)
- L86 `TestBuiltinAlwaysWins` (class) — Built-in TTS provider names short-circuit the dispatcher.
- L99 `test_dispatcher_short_circuits_builtin(self, builtin)` (method)
- L113 `test_dispatcher_short_circuits_builtin_case_insensitive(self)` (method)
- L123 `TestCommandProviderWins` (class) — A same-name ``tts.providers.<name>: type: command`` config beats a plugin.
- L130 `test_command_config_beats_plugin(self)` (method)
- L152 `TestPluginDispatch` (class) — Happy path: configured name matches a registered plugin, dispatcher fires.
- L155 `test_registered_plugin_called(self)` (method)
- L170 `test_unregistered_name_returns_none(self)` (method)
- L179 `test_voice_model_speed_format_forwarded(self)` (method)
- L201 `test_empty_string_voice_passed_as_none(self)` (method) — Empty-string config values are normalized to None so providers can
- L217 `test_provider_returning_different_path_honored(self)` (method) — If a provider rewrites the output path (e.g. format-driven extension
- L231 `test_provider_returning_none_falls_back_to_output_path(self)` (method) — Defensive: a provider returning None means the dispatcher should
- L254 `test_provider_exception_bubbles_up(self)` (method) — Plugin exceptions are NOT swallowed by the dispatcher — they bubble
- L279 `TestVoiceCompatibleHelper` (class)
- L280 `test_voice_compatible_true(self)` (method)
- L286 `test_voice_compatible_false_by_default(self)` (method)
- L290 `test_unregistered_provider_returns_false(self)` (method)
- L293 `test_empty_provider_name_returns_false(self)` (method)
- L301 `test_builtin_names_return_false(self, builtin)` (method) — voice_compatible helper short-circuits built-ins so they go
- L306 `test_voice_compatible_case_insensitive(self)` (method)
- L313 `test_provider_property_exception_returns_false(self)` (method) — A buggy ``voice_compatible`` property raising must not crash the
