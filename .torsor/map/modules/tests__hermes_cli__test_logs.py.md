---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_logs.py

Symbols in `tests/hermes_cli/test_logs.py`.

- L23 `TestParseSince` (class)
- L24 `test_hours(self)` (method)
- L29 `test_minutes(self)` (method)
- L34 `test_days(self)` (method)
- L39 `test_seconds(self)` (method)
- L44 `test_invalid_returns_none(self)` (method)
- L49 `test_whitespace_tolerance(self)` (method)
- L54 `TestParseLineTimestamp` (class)
- L55 `test_standard_format(self)` (method)
- L59 `test_no_timestamp(self)` (method)
- L63 `TestExtractLevel` (class)
- L64 `test_info(self)` (method)
- L67 `test_warning(self)` (method)
- L70 `test_error(self)` (method)
- L73 `test_debug(self)` (method)
- L76 `test_no_level(self)` (method)
- L84 `TestExtractLoggerName` (class)
- L85 `test_standard_line(self)` (method)
- L89 `test_nested_logger(self)` (method)
- L93 `test_warning_level(self)` (method)
- L97 `test_with_session_tag(self)` (method)
- L101 `test_with_session_tag_and_error(self)` (method)
- L105 `test_top_level_module(self)` (method)
- L109 `test_no_match(self)` (method)
- L113 `TestLineMatchesComponent` (class)
- L114 `test_gateway_component(self)` (method)
- L118 `test_gateway_nested(self)` (method)
- L122 `test_tools_component(self)` (method)
- L126 `test_agent_with_multiple_prefixes(self)` (method)
- L135 `test_no_match(self)` (method)
- L139 `test_with_session_tag(self)` (method)
- L143 `test_unparseable_line(self)` (method)
- L151 `TestMatchesFilters` (class)
- L152 `test_no_filters_passes_everything(self)` (method)
- L155 `test_level_filter(self)` (method)
- L161 `test_session_filter(self)` (method)
- L167 `test_component_filter(self)` (method)
- L175 `test_combined_filters(self)` (method) — All filters must pass for a line to match.
- L192 `test_since_filter(self)` (method)
- L208 `TestReadTail` (class)
- L209 `test_read_small_file(self, tmp_path)` (method)
- L218 `test_read_with_component_filter(self, tmp_path)` (method)
- L237 `test_empty_file(self, tmp_path)` (method)
- L248 `TestLogFiles` (class)
- L249 `test_known_log_files(self)` (method)
