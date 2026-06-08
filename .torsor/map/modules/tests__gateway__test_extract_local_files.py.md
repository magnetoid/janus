---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_extract_local_files.py

Symbols in `tests/gateway/test_extract_local_files.py`.

- L22 `_extract(content: str, existing_files: set[str] | None=None)` (function) — Run extract_local_files with os.path.isfile mocked to return True
- L49 `TestBasicDetection` (class)
- L51 `test_absolute_path_image(self)` (method)
- L57 `test_tilde_path_image(self)` (method)
- L62 `test_video_extensions(self)` (method)
- L69 `test_image_extensions(self)` (method)
- L76 `test_document_extensions(self)` (method) — Documents (PDF, Word, plain text, etc.) ship as file uploads.
- L84 `test_spreadsheet_and_data_extensions(self)` (method) — Spreadsheets and structured data ship as file uploads.
- L92 `test_presentation_extensions(self)` (method) — Presentations ship as file uploads.
- L100 `test_audio_extensions(self)` (method) — Audio files are detected and routed by the gateway dispatch.
- L108 `test_archive_extensions(self)` (method) — Archives ship as file uploads.
- L116 `test_html_extension(self)` (method)
- L120 `test_chart_pdf_path(self)` (method) — Common case: agent renders a chart via matplotlib and references the file.
- L128 `test_case_insensitive_extension(self)` (method)
- L132 `test_multiple_paths(self)` (method)
- L142 `test_path_at_line_start(self)` (method)
- L146 `test_path_at_end_of_line(self)` (method)
- L150 `test_path_with_dots_in_directory(self)` (method)
- L154 `test_path_with_hyphens(self)` (method)
- L163 `TestIsfileGuard` (class)
- L165 `test_nonexistent_path_skipped(self)` (method) — Paths that don't exist on disk are not extracted.
- L174 `test_only_existing_paths_extracted(self)` (method) — Mix of existing and non-existing — only existing are returned.
- L189 `TestURLRejection` (class)
- L191 `test_https_url_not_matched(self)` (method) — Paths embedded in HTTP URLs must not be extracted.
- L200 `test_http_url_not_matched(self)` (method)
- L204 `test_file_url_not_matched(self)` (method)
- L214 `TestCodeBlockExclusion` (class)
- L216 `test_fenced_code_block_skipped(self)` (method)
- L222 `test_inline_code_skipped(self)` (method)
- L228 `test_path_outside_code_block_still_matched(self)` (method)
- L236 `test_mixed_inline_code_and_bare_path(self)` (method)
- L243 `test_multiline_fenced_block(self)` (method)
- L259 `TestDeduplication` (class)
- L261 `test_duplicate_paths_deduplicated(self)` (method)
- L266 `test_tilde_and_expanded_same_file(self)` (method) — ~/photos/a.png and /home/user/photos/a.png are the same file.
- L278 `TestTextCleanup` (class)
- L280 `test_path_removed_from_text(self)` (method)
- L286 `test_excessive_blank_lines_collapsed(self)` (method)
- L291 `test_no_paths_text_unchanged(self)` (method)
- L297 `test_tilde_form_cleaned_from_text(self)` (method) — The raw ~/... form should be removed, not the expanded /home/user/... form.
- L304 `test_only_path_in_text(self)` (method) — If the response is just a path, cleaned text is empty.
- L315 `TestEdgeCases` (class)
- L317 `test_empty_string(self)` (method)
- L322 `test_no_media_extensions(self)` (method) — Extensions outside the supported list should not be matched.
- L334 `test_path_with_spaces_not_matched(self)` (method) — Paths with spaces are intentionally not matched (avoids false positives).
- L352 `test_windows_drive_letter_paths_matched(self, content, expected)` (method) — Windows drive-letter paths (C:/..., C:\...) must be detected (#34632).
- L363 `test_relative_windows_path_not_matched(self)` (method) — A bare Windows-style filename without a drive letter must still
- L370 `test_relative_path_not_matched(self)` (method) — Relative paths like ./image.png should not match.
- L375 `test_bare_filename_not_matched(self)` (method) — Just 'image.png' without a path should not match.
- L380 `test_path_followed_by_punctuation(self)` (method) — Path followed by comma, period, paren should still match.
- L387 `test_path_in_parentheses(self)` (method)
- L391 `test_path_in_quotes(self)` (method)
- L395 `test_deep_nested_path(self)` (method)
