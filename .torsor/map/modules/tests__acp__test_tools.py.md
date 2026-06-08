---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_tools.py

Symbols in `tests/acp/test_tools.py`.

- L31 `TestToolKindMap` (class)
- L32 `test_all_hermes_tools_have_kind(self)` (method) — Every common hermes tool should appear in TOOL_KIND_MAP.
- L37 `test_tool_kind_read_file(self)` (method)
- L40 `test_tool_kind_terminal(self)` (method)
- L43 `test_tool_kind_patch(self)` (method)
- L46 `test_tool_kind_write_file(self)` (method)
- L49 `test_tool_kind_web_search(self)` (method)
- L52 `test_tool_kind_execute_code(self)` (method)
- L55 `test_tool_kind_todo(self)` (method)
- L58 `test_tool_kind_skill_view(self)` (method)
- L61 `test_tool_kind_browser_navigate(self)` (method)
- L64 `test_unknown_tool_returns_other_kind(self)` (method)
- L73 `TestMakeToolCallId` (class)
- L74 `test_returns_string(self)` (method)
- L78 `test_starts_with_tc_prefix(self)` (method)
- L82 `test_ids_are_unique(self)` (method)
- L92 `TestBuildToolTitle` (class)
- L93 `test_terminal_title_includes_command(self)` (method)
- L97 `test_terminal_title_truncates_long_command(self)` (method)
- L103 `test_read_file_title(self)` (method)
- L107 `test_patch_title(self)` (method)
- L111 `test_search_title(self)` (method)
- L115 `test_web_search_title(self)` (method)
- L119 `test_skill_view_title_includes_skill_name(self)` (method)
- L123 `test_skill_view_title_includes_linked_file(self)` (method)
- L127 `test_execute_code_title_includes_first_code_line(self)` (method)
- L131 `test_skill_manage_title_includes_action_and_target(self)` (method)
- L138 `test_unknown_tool_uses_name(self)` (method)
- L148 `TestBuildToolStart` (class)
- L149 `test_build_tool_start_for_patch(self)` (method) — patch start should not duplicate the edit-approval diff.
- L165 `test_build_tool_start_for_write_file(self)` (method) — write_file start should not duplicate the edit-approval diff.
- L177 `test_auto_approved_edit_start_shows_diff_content(self)` (method) — Auto-approved edit starts need the diff because no approval card exists.
- L196 `test_build_tool_start_for_terminal(self)` (method) — terminal should produce text content with the command.
- L209 `test_build_tool_start_for_read_file(self)` (method) — read_file start should stay compact; completion carries file contents.
- L218 `test_build_tool_start_for_web_extract_is_compact(self)` (method) — web_extract start should stay compact; title identifies URLs.
- L228 `test_build_tool_start_for_browser_navigate(self)` (method) — browser_navigate should emit a polished start event.
- L238 `test_build_tool_start_for_search(self)` (method) — search_files should include pattern in content.
- L247 `test_build_tool_start_for_todo_is_human_readable(self)` (method)
- L254 `test_build_tool_start_for_skill_view_is_human_readable(self)` (method)
- L260 `test_build_tool_start_for_execute_code_shows_code_preview(self)` (method)
- L268 `test_build_tool_start_for_skill_manage_patch_shows_diff(self)` (method)
- L288 `test_build_tool_start_generic_fallback(self)` (method) — Unknown tools should get a generic text representation.
- L301 `TestBuildToolComplete` (class)
- L302 `test_build_tool_complete_for_terminal(self)` (method) — Completed terminal call should include output text.
- L313 `test_build_tool_complete_for_todo_is_checklist(self)` (method)
- L325 `test_build_tool_complete_for_skill_view_summarizes_content_without_raw_json(self)` (method)
- L340 `test_build_tool_complete_for_execute_code_formats_output(self)` (method)
- L347 `test_build_tool_complete_marks_success_false_as_failed(self)` (method)
- L351 `test_build_tool_complete_marks_ok_false_as_failed(self)` (method)
- L355 `test_build_tool_complete_marks_exit_code_nonzero_as_failed(self)` (method)
- L359 `test_build_tool_complete_marks_returncode_nonzero_as_failed(self)` (method)
- L363 `test_build_tool_complete_keeps_plain_error_text_completed(self)` (method)
- L367 `test_build_tool_complete_marks_raised_exception_prefix_as_failed(self)` (method) — The agent's tool executor wraps raised exceptions in a canonical
- L380 `test_build_tool_complete_does_not_match_error_word_alone(self)` (method) — Bare 'Error: ...' messages (without the unique 'Error executing
- L392 `test_build_tool_complete_marks_structured_polished_tool_error_as_failed(self)` (method)
- L396 `test_build_tool_complete_keeps_json_error_without_failure_flag_completed(self)` (method)
- L400 `test_build_tool_complete_for_skill_manage_summarizes_without_raw_json(self)` (method)
- L419 `test_build_tool_complete_for_read_file_formats_content(self)` (method)
- L431 `test_build_tool_complete_for_search_files_formats_matches(self)` (method)
- L445 `test_build_tool_complete_for_process_list_formats_table(self)` (method)
- L458 `test_build_tool_complete_for_delegate_task_summarizes_children(self)` (method)
- L471 `test_build_tool_complete_for_session_search_recent(self)` (method)
- L483 `test_build_tool_complete_for_memory_avoids_dumping_entries(self)` (method)
- L496 `test_build_tool_complete_for_web_extract_success_stays_compact(self)` (method)
- L505 `test_build_tool_complete_for_web_extract_error_shows_error(self)` (method)
- L517 `test_build_tool_complete_generically_formats_unknown_json_dict_without_raw_output(self)` (method)
- L530 `test_build_tool_complete_generically_formats_unknown_json_list_without_raw_output(self)` (method)
- L541 `test_build_tool_complete_generically_formats_nested_json_without_inline_blob(self)` (method)
- L559 `test_build_tool_complete_for_search_files_files_only_formats_file_list(self)` (method)
- L573 `test_build_tool_complete_truncates_large_output(self)` (method) — Very large outputs should be truncated.
- L582 `test_build_tool_complete_for_patch_summarizes_without_repeating_diff(self)` (method) — Completed patch calls should not duplicate the edit-approval diff.
- L596 `test_build_tool_complete_for_patch_falls_back_to_text_when_no_diff(self)` (method)
- L601 `test_build_tool_complete_for_write_file_summarizes_without_repeating_diff(self, tmp_path)` (method)
- L626 `TestExtractLocations` (class)
- L627 `test_extract_locations_with_path(self)` (method)
- L635 `test_extract_locations_without_path(self)` (method)
