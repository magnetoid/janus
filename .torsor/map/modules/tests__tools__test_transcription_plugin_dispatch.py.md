---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_transcription_plugin_dispatch.py

Symbols in `tests/tools/test_transcription_plugin_dispatch.py`.

- L28 `_FakeProvider` (class)
- L29 `__init__(self, name: str, result: dict | None=None, raise_exc: BaseException | None=None, available: bool=True, available_raises: BaseException | None=None)` (method)
- L45 `name(self)` (method)
- L48 `is_available(self)` (method)
- L53 `transcribe(self, file_path: str, **kw)` (method)
- L63 `_reset_registry()` (function)
- L74 `TestBuiltinAlwaysWins` (class) — Built-in STT provider names short-circuit the dispatcher.
- L86 `test_dispatcher_short_circuits_builtin(self, builtin)` (method)
- L94 `test_dispatcher_short_circuits_none(self)` (method) — The ``none`` sentinel from _get_provider() means no provider
- L102 `test_dispatcher_short_circuits_empty(self)` (method)
- L107 `test_dispatcher_short_circuits_builtin_case_insensitive(self)` (method)
- L121 `TestPluginDispatch` (class)
- L122 `test_registered_plugin_called(self)` (method)
- L136 `test_unregistered_name_returns_none(self)` (method) — Unknown name + no plugin → return None so the caller surfaces
- L144 `test_model_kwarg_forwarded(self)` (method)
- L153 `test_language_kwarg_forwarded(self)` (method)
- L162 `test_provider_exception_converted_to_error_envelope(self)` (method)
- L175 `test_provider_non_dict_result_converted_to_error(self)` (method)
- L187 `test_provider_field_stamped_if_missing(self)` (method) — If a plugin forgets to set ``provider`` in its result, the
- L208 `TestTranscribeAudioE2E` (class) — transcribe_audio() routes plugin dispatch correctly when the
- L217 `test_unknown_name_with_plugin_dispatches(self)` (method)
- L232 `test_unknown_name_without_plugin_falls_to_legacy_error(self)` (method) — When no plugin is registered for the unknown name, the
- L247 `test_builtin_name_does_not_consult_plugin_registry(self)` (method) — Even if a plugin's name collides with a built-in (which the
- L277 `TestAvailabilityGate` (class) — When the configured plugin reports ``is_available() == False``,
- L287 `test_unavailable_plugin_returns_envelope_not_none(self)` (method)
- L305 `test_available_plugin_dispatches_normally(self)` (method)
- L315 `test_is_available_raising_treated_as_unavailable(self)` (method) — Per the ABC contract ``is_available()`` MUST NOT raise; we
- L333 `test_unavailable_plugin_at_transcribe_audio_level(self)` (method) — End-to-end: ``stt.provider: openrouter`` + plugin reports
- L361 `TestLanguageForwardingFromConfig` (class) — ``transcribe_audio`` must forward ``stt.<provider>.language``
- L367 `test_language_read_from_provider_namespaced_config(self)` (method) — ``stt.openrouter.language: ja`` reaches the plugin's
- L387 `test_model_from_provider_namespaced_config(self)` (method) — ``stt.openrouter.model: whisper-large-v3`` reaches the
- L407 `test_caller_model_overrides_config_model(self)` (method) — An explicit ``model`` arg to transcribe_audio wins over
- L428 `test_missing_provider_namespace_passes_none(self)` (method) — No ``stt.<provider>`` subsection → language is None,
- L444 `test_non_dict_provider_namespace_does_not_crash(self)` (method) — If someone accidentally writes ``stt.openrouter: "foo"`` (a
