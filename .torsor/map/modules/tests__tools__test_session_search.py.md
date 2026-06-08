---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_session_search.py

Symbols in `tests/tools/test_session_search.py`.

- L25 `db(tmp_path)` (function)
- L29 `_seed_modpack_sessions(db)` (function) — Create three sessions about a modpack so FTS5 has hits to dedupe.
- L65 `TestSchema` (class)
- L66 `test_schema_has_required_params(self)` (method)
- L79 `test_no_mode_parameter(self)` (method)
- L84 `test_sort_enum(self)` (method)
- L88 `test_schema_description_teaches_scroll(self)` (method)
- L96 `test_no_llm_promise_in_description(self)` (method)
- L102 `TestHiddenSources` (class)
- L103 `test_tool_source_hidden(self)` (method)
- L107 `TestFormatTimestamp` (class)
- L108 `test_unix_timestamp(self)` (method)
- L112 `test_none(self)` (method)
- L115 `test_iso_string_passthrough(self)` (method)
- L124 `TestBrowseShape` (class)
- L125 `test_no_args_returns_recent_sessions(self, db)` (method)
- L132 `test_browse_excludes_current_session(self, db)` (method)
- L138 `test_browse_returns_titles(self, db)` (method)
- L149 `TestDiscoveryShape` (class)
- L150 `test_query_returns_anchored_windows(self, db)` (method)
- L157 `test_discovery_result_has_bookends_and_window(self, db)` (method)
- L169 `test_match_message_id_is_anchor_in_window(self, db)` (method)
- L177 `test_no_results_returns_empty_list(self, db)` (method)
- L184 `test_limit_clamped_to_max_10(self, db)` (method)
- L190 `test_limit_floor_to_1(self, db)` (method)
- L196 `test_non_int_limit_falls_back(self, db)` (method)
- L201 `test_current_session_filtered_out(self, db)` (method)
- L208 `TestDiscoverySort` (class)
- L209 `test_sort_newest_orders_by_recency(self, db)` (method)
- L216 `test_sort_oldest_orders_by_age(self, db)` (method)
- L222 `test_invalid_sort_silently_ignored(self, db)` (method)
- L229 `TestRoleFilter` (class)
- L230 `test_default_excludes_tool_role(self, db)` (method)
- L240 `test_explicit_tool_role_includes_tool(self, db)` (method)
- L253 `TestScrollShape` (class)
- L254 `test_scroll_returns_window_without_bookends(self, db)` (method)
- L272 `test_scroll_window_clamped_to_20(self, db)` (method)
- L282 `test_scroll_window_floor_to_1(self, db)` (method)
- L292 `test_scroll_returns_messages_before_after_counts(self, db)` (method)
- L303 `test_scroll_anchor_in_window(self, db)` (method)
- L315 `test_scroll_missing_anchor_errors(self, db)` (method)
- L323 `test_scroll_missing_session_errors(self, db)` (method)
- L329 `test_scroll_rejects_current_session_lineage(self, db)` (method)
- L343 `test_scroll_invalid_around_message_id_errors(self, db)` (method)
- L351 `TestScrollPattern` (class) — The forward/backward scroll loop using tool output.
- L354 `test_scroll_forward_from_last_id(self, db)` (method)
- L380 `TestShapePrecedence` (class)
- L381 `test_scroll_args_beat_query(self, db)` (method)
- L393 `test_empty_query_falls_back_to_browse(self, db)` (method)
- L398 `test_non_string_query_falls_back_to_browse(self, db)` (method)
- L403 `test_session_id_without_anchor_reads(self, db)` (method)
- L414 `TestReadShape` (class)
- L415 `test_read_returns_full_session(self, db)` (method)
- L426 `test_read_unknown_session_errors(self, db)` (method)
- L430 `test_read_truncates_large_session(self, db)` (method)
- L446 `TestCrossProfileRead` (class)
- L447 `_patch_profiles(self, monkeypatch, home, exists=True)` (method)
- L454 `test_profile_param_reads_other_db(self, db, tmp_path, monkeypatch)` (method)
- L473 `test_bare_id_locates_across_profiles(self, db, tmp_path, monkeypatch)` (method)
- L495 `test_unknown_profile_errors(self, db, monkeypatch, tmp_path)` (method)
- L501 `test_combined_value_autosplits(self, db, tmp_path, monkeypatch)` (method)
