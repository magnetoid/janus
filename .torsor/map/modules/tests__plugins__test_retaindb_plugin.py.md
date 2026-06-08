---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_retaindb_plugin.py

Symbols in `tests/plugins/test_retaindb_plugin.py`.

- L21 `_isolate_env(tmp_path, monkeypatch)` (function) — Ensure HERMES_HOME and RETAINDB vars are isolated.
- L32 `_cap_retaindb_sleeps(monkeypatch)` (function) — Cap production-code sleeps so background-thread tests run fast.
- L74 `TestClient` (class) — Test the HTTP client with mocked requests.
- L77 `_make_client(self, api_key='rdb-test-key', base_url='https://api.retaindb.com', project='test')` (method)
- L80 `test_base_url_trailing_slash_stripped(self)` (method)
- L84 `test_headers_include_auth(self)` (method)
- L90 `test_headers_include_api_key_for_memory_path(self)` (method)
- L95 `test_headers_include_api_key_for_context_path(self)` (method)
- L100 `test_headers_strip_bearer_prefix(self)` (method)
- L106 `test_add_memory_tries_fallback(self)` (method)
- L121 `test_delete_memory_tries_fallback(self)` (method)
- L140 `TestWriteQueue` (class) — Test the SQLite-backed write queue with real SQLite.
- L143 `_make_queue(self, tmp_path, client=None)` (method)
- L150 `test_enqueue_creates_row(self, tmp_path)` (method)
- L160 `test_enqueue_persists_to_sqlite(self, tmp_path)` (method)
- L176 `test_flush_deletes_row_on_success(self, tmp_path)` (method)
- L186 `test_flush_records_error_on_failure(self, tmp_path)` (method)
- L207 `test_thread_local_connection_reuse(self, tmp_path)` (method)
- L215 `test_crash_recovery_replays_pending(self, tmp_path)` (method) — Simulate crash: create rows, then new queue should replay them.
- L256 `TestBuildOverlay` (class) — Test the overlay formatter (pure function).
- L259 `test_empty_inputs_returns_empty(self)` (method)
- L262 `test_empty_memories_returns_empty(self)` (method)
- L265 `test_profile_items_included(self)` (method)
- L271 `test_query_results_included(self)` (method)
- L276 `test_deduplication_removes_duplicates(self)` (method)
- L282 `test_local_entries_filter(self)` (method)
- L288 `test_max_five_items_per_section(self)` (method)
- L296 `test_none_content_handled(self)` (method)
- L301 `test_truncation_at_320_chars(self)` (method)
- L315 `TestRetainDBMemoryProvider` (class) — Test the main plugin class.
- L318 `_make_provider(self, tmp_path, monkeypatch, api_key='rdb-test-key')` (method)
- L325 `test_name(self)` (method)
- L329 `test_is_available_without_key(self)` (method)
- L333 `test_is_available_with_key(self, monkeypatch)` (method)
- L338 `test_config_schema(self)` (method)
- L347 `test_initialize_creates_client_and_queue(self, tmp_path, monkeypatch)` (method)
- L355 `test_initialize_default_project(self, tmp_path, monkeypatch)` (method)
- L361 `test_initialize_explicit_project(self, tmp_path, monkeypatch)` (method)
- L368 `test_initialize_profile_project(self, tmp_path, monkeypatch)` (method)
- L375 `test_initialize_seeds_soul_md(self, tmp_path, monkeypatch)` (method)
- L386 `test_system_prompt_block(self, tmp_path, monkeypatch)` (method)
- L394 `test_handle_tool_call_not_initialized(self)` (method)
- L400 `test_handle_tool_call_unknown_tool(self, tmp_path, monkeypatch)` (method)
- L407 `test_dispatch_profile(self, tmp_path, monkeypatch)` (method)
- L415 `test_dispatch_search_requires_query(self, tmp_path, monkeypatch)` (method)
- L422 `test_dispatch_search(self, tmp_path, monkeypatch)` (method)
- L430 `test_dispatch_search_top_k_capped(self, tmp_path, monkeypatch)` (method)
- L440 `test_dispatch_remember(self, tmp_path, monkeypatch)` (method)
- L448 `test_dispatch_remember_requires_content(self, tmp_path, monkeypatch)` (method)
- L455 `test_dispatch_forget(self, tmp_path, monkeypatch)` (method)
- L463 `test_dispatch_forget_requires_id(self, tmp_path, monkeypatch)` (method)
- L470 `test_dispatch_context(self, tmp_path, monkeypatch)` (method)
- L480 `test_dispatch_file_list(self, tmp_path, monkeypatch)` (method)
- L488 `test_dispatch_file_upload_missing_path(self, tmp_path, monkeypatch)` (method)
- L494 `test_dispatch_file_upload_not_found(self, tmp_path, monkeypatch)` (method)
- L501 `test_dispatch_file_read_requires_id(self, tmp_path, monkeypatch)` (method)
- L508 `test_dispatch_file_ingest_requires_id(self, tmp_path, monkeypatch)` (method)
- L515 `test_dispatch_file_delete_requires_id(self, tmp_path, monkeypatch)` (method)
- L522 `test_handle_tool_call_wraps_exception(self, tmp_path, monkeypatch)` (method)
- L535 `TestPrefetch` (class) — Test background prefetch and thread accumulation prevention.
- L538 `_make_initialized_provider(self, tmp_path, monkeypatch)` (method)
- L547 `test_queue_prefetch_skips_without_client(self)` (method)
- L551 `test_prefetch_returns_empty_when_nothing_cached(self, tmp_path, monkeypatch)` (method)
- L557 `test_prefetch_consumes_context_result(self, tmp_path, monkeypatch)` (method)
- L568 `test_prefetch_consumes_dialectic_result(self, tmp_path, monkeypatch)` (method)
- L577 `test_prefetch_consumes_agent_model(self, tmp_path, monkeypatch)` (method)
- L593 `test_prefetch_skips_empty_agent_model(self, tmp_path, monkeypatch)` (method)
- L601 `test_thread_accumulation_guard(self, tmp_path, monkeypatch)` (method) — Verify old prefetch threads are joined before new ones spawn.
- L621 `test_reasoning_level_short(self)` (method)
- L624 `test_reasoning_level_medium(self)` (method)
- L627 `test_reasoning_level_long(self)` (method)
- L635 `TestSyncTurn` (class) — Test turn synchronization via the write queue.
- L638 `test_sync_turn_enqueues(self, tmp_path, monkeypatch)` (method)
- L657 `test_sync_turn_skips_empty_user_content(self, tmp_path, monkeypatch)` (method)
- L674 `TestOnMemoryWrite` (class) — Test the built-in memory mirror hook.
- L677 `test_mirrors_add_action(self, tmp_path, monkeypatch)` (method)
- L690 `test_skips_non_add_action(self, tmp_path, monkeypatch)` (method)
- L702 `test_skips_empty_content(self, tmp_path, monkeypatch)` (method)
- L714 `test_memory_target_maps_to_type(self, tmp_path, monkeypatch)` (method)
- L731 `TestRegister` (class)
- L732 `test_register_calls_register_memory_provider(self)` (method)
