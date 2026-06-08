---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_console.py

Symbols in `tests/tools/test_browser_console.py`.

- L16 `TestBrowserConsole` (class) — browser_console() returns console messages + JS errors in one call.
- L19 `test_returns_console_messages_and_errors(self)` (method)
- L51 `test_passes_clear_flag(self)` (method)
- L63 `test_no_clear_by_default(self)` (method)
- L74 `test_empty_console_and_errors(self)` (method)
- L86 `test_handles_failed_commands(self)` (method)
- L102 `TestBrowserConsoleSchema` (class) — browser_console is properly registered in the tool registry.
- L105 `test_schema_in_browser_schemas(self)` (method)
- L111 `test_schema_has_clear_param(self)` (method)
- L120 `TestBrowserConsoleToolsetWiring` (class) — browser_console must be reachable via toolset resolution.
- L123 `test_in_browser_toolset(self)` (method)
- L127 `test_in_hermes_core_tools(self)` (method)
- L131 `test_in_legacy_toolset_map(self)` (method)
- L135 `test_in_registry(self)` (method)
- L144 `TestBrowserVisionAnnotate` (class) — browser_vision supports annotate parameter.
- L147 `test_schema_has_annotate_param(self)` (method)
- L155 `test_annotate_false_no_flag(self)` (method) — Without annotate, screenshot command has no --annotate flag.
- L176 `test_annotate_true_adds_flag(self)` (method) — With annotate=True, screenshot command includes --annotate.
- L197 `TestBrowserVisionConfig` (class)
- L198 `_setup_screenshot(self, tmp_path)` (method)
- L205 `test_browser_vision_uses_configured_temperature_and_timeout(self, tmp_path)` (method)
- L229 `test_browser_vision_defaults_temperature_when_config_omits_it(self, tmp_path)` (method)
- L253 `test_browser_vision_native_fast_path_returns_multimodal(self, tmp_path)` (method) — supports_vision override → screenshot attached natively, no aux call.
- L292 `test_browser_vision_text_mode_blocks_native_fast_path(self, tmp_path)` (method) — Explicit text routing → aux LLM used even with supports_vision.
- L334 `TestRecordSessionsConfig` (class) — browser.record_sessions config option.
- L337 `test_default_config_has_record_sessions(self)` (method)
- L344 `test_maybe_start_recording_disabled(self)` (method) — Recording doesn't start when config says record_sessions: false.
- L357 `test_maybe_stop_recording_noop_when_not_recording(self)` (method) — Stopping when not recording is a no-op.
- L371 `TestDogfoodSkill` (class) — Dogfood skill files exist and have correct structure.
- L375 `_skill_dir(self)` (method)
- L381 `test_skill_md_exists(self)` (method)
- L384 `test_taxonomy_exists(self)` (method)
- L389 `test_report_template_exists(self)` (method)
- L394 `test_skill_md_has_frontmatter(self)` (method)
- L401 `test_skill_references_browser_console(self)` (method)
- L406 `test_skill_references_annotate(self)` (method)
- L411 `test_taxonomy_has_severity_levels(self)` (method)
- L421 `test_taxonomy_has_categories(self)` (method)
