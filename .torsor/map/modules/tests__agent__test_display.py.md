---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_display.py

Symbols in `tests/agent/test_display.py`.

- L20 `reset_tool_preview_max_len()` (function)
- L26 `TestBuildToolPreview` (class) — Tests for build_tool_preview defensive handling and normal operation.
- L29 `test_none_args_returns_none(self)` (method) — PR #453: None args should not crash, should return None.
- L33 `test_empty_dict_returns_none(self)` (method) — Empty dict has no keys to preview.
- L37 `test_known_tool_with_primary_arg(self)` (method) — Known tool with its primary arg should return a preview string.
- L43 `test_web_search_preview(self)` (method)
- L48 `test_read_file_preview(self)` (method)
- L53 `test_unknown_tool_with_fallback_key(self)` (method) — Unknown tool but with a recognized fallback key should still preview.
- L59 `test_unknown_tool_no_matching_key(self)` (method) — Unknown tool with no recognized keys should return None.
- L64 `test_long_value_truncated(self)` (method) — Preview should truncate long values.
- L71 `test_process_tool_with_none_args(self)` (method) — Process tool special case should also handle None args.
- L75 `test_process_tool_normal(self)` (method)
- L80 `test_todo_tool_read(self)` (method)
- L85 `test_todo_tool_with_todos(self)` (method)
- L90 `test_memory_tool_add(self)` (method)
- L95 `test_memory_replace_missing_old_text_marked(self)` (method)
- L102 `test_session_search_preview(self)` (method)
- L107 `test_false_like_args_zero(self)` (method) — Non-dict falsy values should return None, not crash.
- L114 `TestCuteToolMessagePreviewLength` (class)
- L115 `test_terminal_preview_unlimited_when_config_is_zero(self)` (method)
- L124 `test_terminal_preview_uses_positive_configured_limit(self)` (method)
- L134 `test_search_files_preview_uses_positive_configured_limit_not_default(self)` (method)
- L143 `test_path_preview_uses_positive_configured_limit_not_default(self)` (method)
- L152 `test_write_file_lint_error_result_is_not_marked_failed(self)` (method)
- L162 `test_patch_lsp_diagnostics_result_is_not_marked_failed(self)` (method)
- L174 `TestEditDiffPreview` (class)
- L175 `test_extract_edit_diff_for_patch(self)` (method)
- L180 `test_render_inline_unified_diff_colors_added_and_removed_lines(self)` (method)
- L196 `test_extract_edit_diff_ignores_non_edit_tools(self)` (method)
- L199 `test_extract_edit_diff_uses_local_snapshot_for_write_file(self, tmp_path)` (method)
- L220 `test_render_edit_diff_with_delta_invokes_printer(self)` (method)
- L236 `test_render_edit_diff_with_delta_skips_without_diff(self)` (method)
- L244 `test_render_edit_diff_with_delta_handles_renderer_errors(self, monkeypatch)` (method)
- L258 `test_summarize_rendered_diff_sections_truncates_large_diff(self)` (method)
- L266 `test_summarize_rendered_diff_sections_limits_file_count(self)` (method)
