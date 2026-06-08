---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_trajectory_compressor.py

Symbols in `tests/test_trajectory_compressor.py`.

- L19 `test_import_loads_env_from_hermes_home(tmp_path, monkeypatch)` (function)
- L33 `test_generate_summary_kimi_omits_temperature()` (function) — Kimi models should have temperature omitted — server manages it.
- L57 `test_generate_summary_public_moonshot_kimi_k2_5_omits_temperature()` (function) — kimi-k2.5 on the public Moonshot API should not get a forced temperature.
- L82 `test_generate_summary_public_moonshot_cn_kimi_k2_5_omits_temperature()` (function) — kimi-k2.5 on api.moonshot.cn should not get a forced temperature.
- L112 `TestCompressionConfig` (class)
- L113 `test_defaults(self)` (method)
- L120 `test_from_yaml(self, tmp_path)` (method)
- L170 `test_from_yaml_partial(self, tmp_path)` (method) — Only specified sections override defaults.
- L180 `test_from_yaml_empty(self, tmp_path)` (method)
- L192 `TestTrajectoryMetrics` (class)
- L193 `test_to_dict(self)` (method)
- L210 `test_default_values(self)` (method)
- L223 `TestAggregateMetrics` (class)
- L224 `test_empty_to_dict(self)` (method)
- L231 `test_add_compressed_trajectory(self)` (method)
- L248 `test_add_skipped_trajectory(self)` (method)
- L258 `test_add_over_limit_trajectory(self)` (method)
- L269 `test_multiple_trajectories_aggregation(self)` (method)
- L286 `test_to_dict_no_division_by_zero(self)` (method) — Ensure no ZeroDivisionError with empty data.
- L299 `_make_compressor(config=None)` (function) — Create a TrajectoryCompressor with mocked tokenizer and summarizer.
- L312 `TestFindProtectedIndices` (class)
- L313 `test_basic_trajectory(self)` (method)
- L342 `test_short_trajectory_all_protected(self)` (method)
- L354 `test_protect_last_n_zero(self)` (method)
- L376 `test_no_system_turn(self)` (method)
- L388 `test_disable_protect_first_system(self)` (method)
- L411 `TestExtractTurnContent` (class)
- L412 `test_basic_extraction(self)` (method)
- L427 `test_long_content_truncated(self)` (method)
- L436 `test_empty_range(self)` (method)
- L448 `TestTokenCounting` (class)
- L449 `test_count_tokens_empty(self)` (method)
- L453 `test_count_tokens_basic(self)` (method)
- L458 `test_count_trajectory_tokens(self)` (method)
- L466 `test_count_turn_tokens(self)` (method)
- L475 `test_count_tokens_fallback_on_error(self)` (method)
- L482 `TestGenerateSummary` (class)
- L483 `test_generate_summary_handles_none_content(self)` (method)
- L496 `test_generate_summary_async_handles_none_content(self)` (method)
- L517 `_gpt_with_tool_call(label, tokens)` (function) — A 'gpt' turn carrying a <tool_call> marker, padded to ~`tokens` tokens.
- L524 `_tool_response(label, tokens)` (function) — A 'tool' turn carrying a <tool_response> marker, padded to ~`tokens` tokens.
- L531 `_count_marker(trajectory, marker)` (function)
- L535 `_paired_trajectory()` (function) — A 10-turn trajectory of gpt/tool pairs with one oversized middle gpt turn.
- L558 `_target_that_splits_after_index_4(tc, trajectory)` (function) — Pick a target so token accumulation breaks right after index 4 (a gpt).
- L567 `TestCompressionToolPairIntegrity` (class)
- L568 `_config(self)` (method)
- L574 `test_sync_compression_does_not_orphan_tool_markers(self)` (method)
- L596 `test_async_compression_does_not_orphan_tool_markers(self)` (method)
- L614 `test_snap_boundary_skips_tool_turn_forward(self)` (method)
- L622 `test_snap_boundary_falls_back_to_backward(self)` (method)
