---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/honcho_plugin/test_async_memory.py

Symbols in `tests/honcho_plugin/test_async_memory.py`.

- L28 `_make_session(**kwargs)` (function)
- L38 `_make_manager(write_frequency='turn')` (function)
- L53 `TestWriteFrequencyParsing` (class)
- L54 `test_string_async(self, tmp_path)` (method)
- L60 `test_string_turn(self, tmp_path)` (method)
- L66 `test_string_session(self, tmp_path)` (method)
- L72 `test_integer_frequency(self, tmp_path)` (method)
- L78 `test_integer_string_coerced(self, tmp_path)` (method)
- L84 `test_host_block_overrides_root(self, tmp_path)` (method)
- L94 `test_defaults_to_async(self, tmp_path)` (method)
- L105 `TestResolveSessionNameTitle` (class)
- L106 `test_manual_override_beats_title(self)` (method)
- L111 `test_title_beats_dirname(self)` (method)
- L116 `test_title_with_peer_prefix(self)` (method)
- L121 `test_title_sanitized(self)` (method)
- L127 `test_title_all_invalid_chars_falls_back_to_dirname(self)` (method)
- L133 `test_none_title_falls_back_to_dirname(self)` (method)
- L138 `test_empty_title_falls_back_to_dirname(self)` (method)
- L143 `test_per_session_uses_session_id(self)` (method)
- L148 `test_per_session_with_peer_prefix(self)` (method)
- L153 `test_per_session_no_id_falls_back_to_dirname(self)` (method)
- L158 `test_title_beats_session_id(self)` (method)
- L163 `test_manual_beats_session_id(self)` (method)
- L168 `test_global_strategy_returns_workspace(self)` (method)
- L178 `TestSaveRouting` (class)
- L179 `_make_session_with_message(self, mgr=None)` (method)
- L187 `test_turn_flushes_immediately(self)` (method)
- L194 `test_session_mode_does_not_flush(self)` (method)
- L201 `test_async_mode_enqueues(self)` (method)
- L210 `test_int_frequency_flushes_on_nth_turn(self)` (method)
- L220 `test_int_frequency_skips_other_turns(self)` (method)
- L235 `TestFlushAll` (class)
- L236 `test_flushes_all_cached_sessions(self)` (method)
- L248 `test_flush_all_drains_async_queue(self)` (method)
- L262 `test_flush_all_tolerates_errors(self)` (method)
- L275 `TestAsyncWriterThread` (class)
- L276 `test_thread_started_on_async_mode(self)` (method)
- L282 `test_no_thread_for_turn_mode(self)` (method)
- L287 `test_shutdown_joins_thread(self)` (method)
- L293 `test_async_writer_calls_flush(self)` (method)
- L315 `test_shutdown_sentinel_stops_loop(self)` (method)
- L327 `TestAsyncWriterRetry` (class)
- L328 `test_retries_once_on_failure(self)` (method)
- L352 `test_drops_after_two_failures(self)` (method)
- L376 `test_retries_when_flush_reports_failure(self)` (method)
- L399 `TestMemoryFileMigrationTargets` (class)
- L400 `test_soul_upload_targets_ai_peer(self, tmp_path)` (method)
- L441 `TestNewConfigFieldDefaults` (class)
- L442 `test_write_frequency_default(self)` (method)
- L446 `test_write_frequency_set(self)` (method)
- L451 `TestPrefetchCacheAccessors` (class)
- L452 `test_set_and_pop_context_result(self)` (method)
