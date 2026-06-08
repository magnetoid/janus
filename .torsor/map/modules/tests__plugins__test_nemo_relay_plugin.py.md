---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_nemo_relay_plugin.py

Symbols in `tests/plugins/test_nemo_relay_plugin.py`.

- L21 `_FakeNemoRelay` (class)
- L22 `__init__(self)` (method)
- L47 `_scope_push(self, name, scope_type, **kwargs)` (method)
- L52 `_scope_pop(self, handle, **kwargs)` (method)
- L55 `_scope_event(self, name, **kwargs)` (method)
- L58 `_llm_call(self, name, request, **kwargs)` (method)
- L63 `_llm_call_end(self, handle, response, **kwargs)` (method)
- L66 `_llm_execute(self, name, request, func, **kwargs)` (method)
- L72 `_tool_call(self, name, args, **kwargs)` (method)
- L77 `_tool_call_end(self, handle, result, **kwargs)` (method)
- L80 `_tool_execute(self, name, args, func, **kwargs)` (method)
- L86 `_make_atof_exporter(self, config)` (method)
- L89 `_make_atif_exporter(self, session_id, agent_name, agent_version, **kwargs)` (method)
- L92 `_plugin_initialize(self, config)` (method)
- L97 `_FakeLLMRequest` (class)
- L98 `__init__(self, headers, content)` (method)
- L103 `_FakeAtofExporterConfig` (class)
- L104 `__init__(self)` (method)
- L110 `_FakeAtofExporter` (class)
- L111 `__init__(self, events, config)` (method)
- L115 `register(self, name)` (method)
- L119 `_FakeAtifExporter` (class)
- L120 `__init__(self, events, session_id, agent_name, agent_version, kwargs)` (method)
- L127 `register(self, name)` (method)
- L130 `deregister(self, name)` (method)
- L134 `export_json(self)` (method)
- L138 `_fresh_plugin(monkeypatch, fake)` (function)
- L146 `test_manifest_fields()` (function)
- L168 `test_nemo_relay_plugin_is_discoverable_as_bundled_plugin(tmp_path, monkeypatch)` (function)
- L180 `test_nemo_relay_plugin_uses_nemo_relay_runtime(monkeypatch)` (function)
- L189 `test_nemo_relay_plugin_emits_llm_tool_and_exports_atif(tmp_path, monkeypatch)` (function)
- L232 `test_nemo_relay_plugin_closes_api_span_on_error(monkeypatch)` (function)
- L264 `test_nemo_relay_plugin_emits_approval_marks(monkeypatch)` (function)
- L276 `test_nemo_relay_plugin_emits_unmatched_fallback_marks(monkeypatch)` (function)
- L294 `test_nemo_relay_plugin_metadata_promotes_trajectory_and_subagent_ids(monkeypatch)` (function)
- L340 `test_nemo_relay_plugin_reparents_child_session_scope_for_embedded_atif(monkeypatch)` (function)
- L369 `test_nemo_relay_plugin_skips_embedded_child_atif_file_by_default(tmp_path, monkeypatch)` (function)
- L391 `test_nemo_relay_plugin_can_write_embedded_child_atif_file_in_all_mode(tmp_path, monkeypatch)` (function)
- L414 `test_nemo_relay_plugin_can_initialize_plugins_toml(tmp_path, monkeypatch)` (function)
- L448 `test_nemo_relay_adaptive_llm_execution_middleware_preserves_raw_response(tmp_path, monkeypatch)` (function)
- L530 `test_nemo_relay_llm_execution_middleware_calls_through_without_adaptive(monkeypatch)` (function)
- L546 `test_nemo_relay_adaptive_tool_execution_middleware_preserves_raw_response(tmp_path, monkeypatch)` (function)
- L589 `test_nemo_relay_tool_execution_middleware_calls_through_without_adaptive(monkeypatch)` (function)
- L604 `test_nemo_relay_adaptive_execution_skips_duplicate_observer_spans(tmp_path, monkeypatch)` (function)
- L663 `test_nemo_relay_plugin_noops_without_dependency(monkeypatch)` (function)
