---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_operations_edge_cases.py

Symbols in `tests/tools/test_file_operations_edge_cases.py`.

- L19 `TestIsLikelyBinary` (class) — Verify content-analysis logic after dead-code removal.
- L23 `ops(self)` (method)
- L26 `test_binary_extension_returns_true(self, ops)` (method) — Known binary extensions should short-circuit without content analysis.
- L31 `test_text_content_returns_false(self, ops)` (method) — Normal printable text should not be classified as binary.
- L36 `test_binary_content_returns_true(self, ops)` (method) — Content with >30% non-printable characters should be classified as binary.
- L43 `test_no_content_sample_returns_false(self, ops)` (method) — When no content sample is provided and extension is unknown → not binary.
- L47 `test_none_content_sample_returns_false(self, ops)` (method) — Explicit ``None`` content_sample should behave the same as missing.
- L51 `test_empty_string_content_sample_returns_false(self, ops)` (method) — Empty string is falsy, so content analysis should be skipped → not binary.
- L55 `test_threshold_boundary(self, ops)` (method) — Exactly 30% non-printable should NOT trigger binary classification (> 0.30, not >=).
- L61 `test_just_above_threshold(self, ops)` (method) — 301/1000 = 30.1% non-printable → should be binary.
- L66 `test_tabs_and_newlines_excluded(self, ops)` (method) — Tabs, carriage returns, and newlines should not count as non-printable.
- L71 `test_content_sample_longer_than_1000(self, ops)` (method) — Only the first 1000 characters should be analysed.
- L84 `TestCheckLintBracePaths` (class) — Verify _check_lint handles file paths with curly braces safely.
- L92 `ops(self)` (method)
- L97 `test_normal_path(self, ops)` (method) — Normal path without braces should work as before.
- L109 `test_path_with_curly_braces(self, ops)` (method) — Path containing ``{`` and ``}`` must not raise KeyError/ValueError.
- L121 `test_path_with_nested_braces(self, ops)` (method) — Path with complex brace patterns like ``{{var}}`` should be safe.
- L130 `test_unsupported_extension_skipped(self, ops)` (method) — Extensions without a linter should return a skipped result.
- L135 `test_missing_linter_skipped(self, ops)` (method) — When the linter binary is not installed, skip gracefully.
- L141 `test_lint_failure_returns_output(self, ops)` (method) — When the linter exits non-zero, result should capture output.
- L155 `TestCheckLintInproc` (class) — Verify in-process linters (.py via ast.parse, .json, .yaml, .toml).
- L163 `ops(self)` (method)
- L168 `test_python_inproc_clean(self, ops)` (method) — Valid Python content passes in-process ast.parse.
- L175 `test_python_inproc_syntax_error(self, ops)` (method) — Invalid Python content fails with SyntaxError + line info.
- L182 `test_python_inproc_content_explicit(self, ops)` (method) — When content is passed explicitly, the file is not re-read.
- L190 `test_json_inproc_clean(self, ops)` (method)
- L194 `test_json_inproc_error(self, ops)` (method)
- L199 `test_yaml_inproc_clean(self, ops)` (method)
- L203 `test_yaml_inproc_error(self, ops)` (method)
- L208 `test_toml_inproc_clean(self, ops)` (method)
- L212 `test_toml_inproc_error(self, ops)` (method)
- L218 `TestCheckLintDelta` (class) — Verify _check_lint_delta() filters pre-existing errors from post-edit output.
- L222 `ops(self)` (method)
- L227 `test_clean_post_no_pre_lint(self, ops)` (method) — Hot path: post-write is clean, pre-lint should be skipped entirely.
- L235 `test_new_file_reports_all_errors(self, ops)` (method) — No pre-content means no delta refinement — all post errors surface.
- L241 `test_broken_file_becomes_good(self, ops)` (method) — Post-clean short-circuits without any delta refinement.
- L246 `test_introduces_new_error_filters_pre(self, ops)` (method) — Delta filter drops pre-existing errors, surfaces only new ones.
- L254 `test_pre_existing_remains_flagged_but_not_new(self, ops)` (method) — Single-error parsers (ast) may miss that post is OK — be cautious.
- L270 `TestPaginationBounds` (class) — Invalid pagination inputs should not leak into shell commands.
- L273 `test_read_file_clamps_offset_and_limit_before_building_sed_range(self)` (method)
- L299 `test_search_clamps_offset_and_limit_before_building_head_pipeline(self)` (method)
- L328 `TestSearchContextParsing` (class)
- L329 `test_parse_search_context_line_prefers_rightmost_numeric_separator(self)` (method)
- L334 `test_search_with_rg_context_handles_filename_with_dash_digits(self)` (method)
- L360 `test_search_with_grep_context_handles_filename_with_dash_digits(self)` (method)
