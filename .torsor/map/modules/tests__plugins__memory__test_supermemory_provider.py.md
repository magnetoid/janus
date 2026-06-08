---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/memory/test_supermemory_provider.py

Symbols in `tests/plugins/memory/test_supermemory_provider.py`.

- L17 `FakeClient` (class)
- L18 `__init__(self, api_key: str, timeout: float, container_tag: str, search_mode: str='hybrid')` (method)
- L30 `add_memory(self, content, metadata=None, *, entity_context='', container_tag=None, custom_id=None)` (method)
- L41 `search_memories(self, query, *, limit=5, container_tag=None, search_mode=None)` (method)
- L44 `get_profile(self, query=None, *, container_tag=None)` (method)
- L47 `forget_memory(self, memory_id, *, container_tag=None)` (method)
- L50 `forget_by_query(self, query, *, container_tag=None)` (method)
- L53 `ingest_conversation(self, session_id, messages, metadata=None)` (method)
- L58 `provider(monkeypatch, tmp_path)` (function)
- L66 `test_is_available_false_without_api_key(monkeypatch)` (function)
- L72 `test_is_available_false_when_import_missing(monkeypatch)` (function)
- L88 `test_load_and_save_config_round_trip(tmp_path)` (function)
- L97 `test_clean_text_for_capture_strips_injected_context()` (function)
- L102 `test_format_prefetch_context_deduplicates_overlap()` (function)
- L114 `test_prefetch_includes_profile_on_first_turn(provider)` (function)
- L127 `test_prefetch_skips_profile_between_frequency(provider)` (function)
- L139 `test_sync_turn_buffers_short_messages(provider)` (function)
- L147 `test_sync_turn_buffers_cleaned_exchange(provider)` (function)
- L163 `test_on_session_end_ingests_clean_messages(provider)` (function)
- L184 `test_merge_metadata_stamps_sm_source()` (function)
- L201 `test_on_memory_write_tracks_thread(provider)` (function)
- L209 `test_shutdown_joins_threads_and_flushes_buffer(provider, monkeypatch)` (function)
- L257 `test_store_tool_returns_saved_payload(provider)` (function)
- L263 `test_search_tool_formats_results(provider)` (function)
- L272 `test_forget_tool_by_id(provider)` (function)
- L278 `test_forget_tool_by_query(provider)` (function)
- L285 `test_profile_tool_formats_sections(provider)` (function)
- L297 `test_handle_tool_call_returns_error_when_unconfigured(monkeypatch)` (function)
- L307 `test_identity_template_resolved_in_container_tag(monkeypatch, tmp_path)` (function) — container_tag with {identity} resolves to profile-scoped tag.
- L317 `test_identity_template_default_profile(monkeypatch, tmp_path)` (function) — Without agent_identity kwarg, {identity} resolves to 'default'.
- L327 `test_container_tag_env_var_override(monkeypatch, tmp_path)` (function) — SUPERMEMORY_CONTAINER_TAG env var overrides config.
- L340 `test_search_mode_config_passed_to_client(monkeypatch, tmp_path)` (function) — search_mode from config is passed to _SupermemoryClient.
- L351 `test_invalid_search_mode_falls_back_to_default(monkeypatch, tmp_path)` (function) — Invalid search_mode falls back to 'hybrid'.
- L364 `test_multi_container_disabled_by_default(provider)` (function) — Multi-container is off by default; schemas have no container_tag param.
- L372 `test_multi_container_enabled_adds_schema_param(monkeypatch, tmp_path)` (function) — When enabled, tool schemas include container_tag parameter.
- L389 `test_multi_container_tool_store_with_custom_tag(monkeypatch, tmp_path)` (function) — supermemory_store uses the resolved container_tag when multi-container is enabled.
- L408 `test_multi_container_rejects_unlisted_tag(monkeypatch, tmp_path)` (function) — Tool calls with a non-whitelisted container_tag return an error.
- L426 `test_multi_container_system_prompt_includes_instructions(monkeypatch, tmp_path)` (function) — system_prompt_block includes container list and instructions when multi-container is enabled.
- L443 `test_get_config_schema_minimal()` (function) — get_config_schema only returns the API key field.
- L453 `test_save_config_sets_owner_only_permissions(tmp_path)` (function) — supermemory.json must be written with 0o600 so API key is not world-readable.
