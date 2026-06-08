---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_status_bar.py

Symbols in `tests/cli/test_cli_status_bar.py`.

- L9 `_make_cli(model: str='anthropic/claude-sonnet-4-20250514')` (function)
- L18 `_attach_agent(cli_obj, *, input_tokens: int | None=None, output_tokens: int | None=None, cache_read_tokens: int=0, cache_write_tokens: int=0, prompt_tokens: int, completion_tokens: int, total_tokens: int, api_calls: int, context_tokens: int, context_length: int, compressions: int=0)` (function)
- L55 `TestCLIStatusBar` (class)
- L56 `test_context_style_thresholds(self)` (method)
- L65 `test_build_status_bar_text_for_wide_terminal(self)` (method)
- L84 `test_post_compression_sentinel_does_not_render_negative(self)` (method) — Right after a compression, last_prompt_tokens is parked at the -1
- L107 `test_input_height_counts_wide_characters_using_cell_width(self)` (method)
- L149 `test_input_height_uses_prompt_toolkit_width_over_shutil(self)` (method)
- L193 `test_build_status_bar_text_no_cost_in_status_bar(self)` (method)
- L207 `test_build_status_bar_text_collapses_for_narrow_terminal(self)` (method)
- L225 `test_build_status_bar_text_handles_missing_agent(self)` (method)
- L233 `test_compression_count_shown_in_wide_status_bar(self)` (method)
- L249 `test_compression_count_hidden_when_zero(self)` (method)
- L265 `test_compression_count_shown_in_medium_status_bar(self)` (method)
- L281 `test_compression_count_hidden_in_narrow_status_bar(self)` (method)
- L297 `test_compression_count_style_thresholds(self)` (method)
- L307 `test_compression_count_in_wide_fragments(self)` (method)
- L327 `test_compression_count_absent_from_fragments_when_zero(self)` (method)
- L345 `test_minimal_tui_chrome_threshold(self)` (method)
- L351 `test_bottom_input_rule_hides_on_narrow_terminals(self)` (method)
- L358 `test_input_rules_hide_after_resize_until_next_input(self)` (method) — When _status_bar_suppressed_after_resize is set, both rules hide.
- L375 `test_scrollback_box_width_returns_viewport_width(self)` (method) — Decorative scrollback boxes use the full viewport width.
- L397 `test_agent_spacer_reclaimed_on_narrow_terminals(self)` (method)
- L406 `test_spinner_line_hidden_on_narrow_terminals(self)` (method)
- L415 `test_spinner_height_uses_display_width_for_wide_characters(self)` (method)
- L422 `test_spinner_elapsed_format_is_fixed_width_to_reduce_wrap_jitter(self)` (method)
- L440 `test_voice_status_bar_compacts_on_narrow_terminals(self)` (method)
- L452 `test_voice_recording_status_bar_compacts_on_narrow_terminals(self)` (method)
- L468 `test_voice_status_bar_renders_configured_ctrl_letter(self)` (method)
- L483 `test_voice_recording_status_bar_renders_configured_named_key(self)` (method)
- L494 `test_voice_status_bar_falls_back_to_ctrl_b_without_cache(self)` (method)
- L508 `test_voice_status_bar_renders_malformed_config_as_default(self)` (method)
- L525 `TestCLIUsageReport` (class)
- L526 `test_show_usage_includes_estimated_cost(self, capsys)` (method)
- L551 `test_show_usage_marks_unknown_pricing(self, capsys)` (method)
- L570 `test_zero_priced_provider_models_stay_unknown(self, capsys)` (method)
- L590 `TestStatusBarWidthSource` (class) — Ensure status bar fragments don't overflow the terminal width.
- L593 `_make_wide_cli(self)` (method)
- L606 `test_fragments_fit_within_announced_width(self)` (method) — Total fragment text length must not exceed the width used to build them.
- L625 `test_fragments_use_pt_width_over_shutil(self)` (method) — When prompt_toolkit reports a width, shutil.get_terminal_size must not be used.
- L639 `test_fragments_fall_back_to_shutil_when_no_app(self)` (method) — Outside a TUI context (no running app), shutil must be used as fallback.
- L651 `test_build_status_bar_text_uses_pt_width(self)` (method) — _build_status_bar_text() must also prefer prompt_toolkit width.
- L667 `test_explicit_width_skips_pt_lookup(self)` (method) — An explicit width= argument must bypass both PT and shutil lookups.
