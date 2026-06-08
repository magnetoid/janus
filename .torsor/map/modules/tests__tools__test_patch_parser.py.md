---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_patch_parser.py

Symbols in `tests/tools/test_patch_parser.py`.

- L12 `TestParseUpdateFile` (class)
- L13 `test_basic_update(self)` (method)
- L38 `test_multiple_hunks(self)` (method)
- L59 `TestParseAddFile` (class)
- L60 `test_add_file(self)` (method)
- L82 `TestParseDeleteFile` (class)
- L83 `test_delete_file(self)` (method)
- L95 `TestParseMoveFile` (class)
- L96 `test_move_file(self)` (method)
- L109 `TestParseInvalidPatch` (class)
- L110 `test_empty_patch_returns_empty_ops(self)` (method)
- L115 `test_no_begin_marker_still_parses(self)` (method)
- L126 `test_multiple_operations(self)` (method)
- L145 `TestApplyUpdate` (class)
- L146 `test_preserves_non_prefix_pipe_characters_in_unmodified_lines(self)` (method)
- L190 `TestAdditionOnlyHunks` (class) — Regression tests for #3081 — addition-only hunks were silently dropped.
- L193 `test_addition_only_hunk_with_context_hint(self)` (method) — A hunk with only + lines should insert at the context hint location.
- L229 `test_addition_only_hunk_without_context_hint(self)` (method) — A hunk with only + lines and no context hint appends at end of file.
- L258 `TestReadFileRaw` (class) — Bug 1 regression tests — files > 2000 lines and lines > 2000 chars.
- L261 `test_apply_update_file_over_2000_lines(self)` (method) — A hunk targeting line 2200 must not truncate the file to 2000 lines.
- L298 `test_apply_update_preserves_long_lines(self)` (method) — A line > 2000 chars must be preserved verbatim after an unrelated hunk.
- L329 `TestValidationPhase` (class) — Bug 2 regression tests — validation prevents partial apply.
- L332 `test_validation_failure_writes_nothing(self)` (method) — If one hunk is invalid, no files should be written.
- L370 `test_all_valid_operations_applied(self)` (method) — When all operations are valid, all files are written.
- L405 `TestApplyDelete` (class) — Tests for _apply_delete producing a real unified diff.
- L408 `test_delete_diff_contains_removed_lines(self)` (method) — _apply_delete must embed the actual file content in the diff, not a placeholder.
- L440 `test_delete_diff_fallback_on_empty_file(self)` (method) — An empty file should produce the fallback comment diff.
- L462 `TestCountOccurrences` (class)
- L463 `test_basic(self)` (method)
- L471 `TestParseErrorSignalling` (class) — Bug 3 regression tests — parse_v4a_patch must signal errors, not swallow them.
- L474 `test_update_with_no_hunks_returns_error(self)` (method) — An UPDATE with no hunk lines is a malformed patch and should error.
- L484 `test_move_without_destination_returns_error(self)` (method) — A MOVE without '->' syntax should not silently produce a broken operation.
- L500 `test_valid_patch_returns_no_error(self)` (method) — A well-formed patch must still return err=None.
- L514 `TestV4ALspDiagnosticsPropagation` (class) — V4A patches must surface ``WriteResult.lsp_diagnostics`` from the
- L526 `_build_ops_writing(self, path: str, content: str)` (method) — Build a single ADD operation that writes ``content`` to ``path``.
- L541 `test_lsp_diagnostics_propagated_from_write_file_on_add(self)` (method) — ADD op: ``WriteResult.lsp_diagnostics`` flows through to
- L564 `test_lsp_diagnostics_propagated_from_write_file_on_update(self)` (method) — UPDATE op: ``WriteResult.lsp_diagnostics`` flows through to
- L598 `test_lsp_diagnostics_none_when_no_blocks_emitted(self)` (method) — When no underlying ``write_file`` produced diagnostics, the
- L617 `test_lsp_diagnostics_combined_across_multiple_files(self)` (method) — When several files in one V4A patch produce diagnostics,
