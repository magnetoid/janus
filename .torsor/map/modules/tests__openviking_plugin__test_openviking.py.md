---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/openviking_plugin/test_openviking.py

Symbols in `tests/openviking_plugin/test_openviking.py`.

- L8 `FakeVikingClient` (class)
- L9 `__init__(self, responses)` (method)
- L13 `get(self, path, params=None, **kwargs)` (method)
- L21 `TestOpenVikingSummaryUriNormalization` (class)
- L22 `test_normalize_summary_uri_maps_pseudo_files_to_parent_directory(self)` (method)
- L29 `TestOpenVikingRead` (class)
- L30 `test_overview_read_normalizes_uri_and_unwraps_result(self)` (method)
- L52 `test_full_read_keeps_original_uri(self)` (method)
- L74 `test_overview_file_uri_routes_straight_to_content_read_via_stat_probe(self)` (method) — Pre-check via fs/stat: file URIs skip the directory-only endpoint entirely.
- L103 `test_overview_dir_uri_skips_stat_when_pseudo_summary(self)` (method) — Pseudo-URI path already resolves to dir, so no stat probe needed.
- L123 `test_overview_directory_uri_uses_stat_probe_then_overview(self)` (method) — Non-pseudo directory URI: stat → isDir=True → summary endpoint.
- L149 `test_overview_file_uri_falls_back_via_exception_when_stat_indeterminate(self)` (method) — If fs/stat raises or returns unknown shape, legacy exception fallback still kicks in.
- L182 `test_summary_uri_error_does_not_fallback_and_raises(self)` (method)
- L204 `TestOpenVikingBrowse` (class)
- L205 `test_list_browse_unwraps_and_normalizes_entry_shapes(self)` (method)
- L236 `TestOpenVikingMemoryUriBuilder` (class) — Regression tests for _build_memory_uri — fixes #36969.
- L243 `_make_provider(self, user='alice', agent='coder')` (method)
- L249 `test_uri_layout_includes_agent_segment(self)` (method) — URI must contain /agent/{agent}/ between user and memories.
- L256 `test_uri_uses_configured_agent_not_default(self)` (method) — _agent value must be interpolated — not hardcoded to 'hermes'.
- L263 `test_uri_slug_is_twelve_hex_chars_and_unique(self)` (method) — Slug must be 12 hex chars and differ between calls.
- L275 `test_uri_subdir_placed_correctly_for_all_categories(self)` (method) — All five category subdirs must appear between memories/ and slug.
