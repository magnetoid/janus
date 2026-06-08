---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_skills_hub.py

Symbols in `tests/hermes_cli/test_skills_hub.py`.

- L11 `_DummyLockFile` (class)
- L12 `__init__(self, installed)` (method)
- L15 `list_installed(self)` (method)
- L20 `hub_env(monkeypatch, tmp_path)` (function) — Set up isolated hub directory paths and return (monkeypatch, tmp_path).
- L52 `three_source_env(monkeypatch, hub_env)` (function) — Populate hub/builtin/local skills for source-classification tests.
- L65 `_capture(source_filter: str='all')` (function) — Run do_list into a string buffer and return the output.
- L73 `_capture_check(monkeypatch, results, name=None)` (function)
- L83 `_capture_update(monkeypatch, results)` (function)
- L106 `test_do_list_initializes_hub_dir(monkeypatch, hub_env)` (function)
- L124 `test_do_list_distinguishes_hub_builtin_and_local(three_source_env)` (function)
- L133 `test_do_list_filter_local(three_source_env)` (function)
- L141 `test_do_list_filter_hub(three_source_env)` (function)
- L149 `test_do_list_filter_builtin(three_source_env)` (function)
- L157 `test_do_list_renders_status_column(three_source_env, monkeypatch)` (function) — Every list row should carry an enabled/disabled status (new in PR that
- L171 `test_do_list_marks_disabled_skills(three_source_env, monkeypatch)` (function)
- L187 `test_do_list_enabled_only_hides_disabled(three_source_env, monkeypatch)` (function)
- L206 `test_do_list_platform_env_is_ignored(three_source_env, monkeypatch)` (function) — `hermes skills list` reads the active profile's config via
- L225 `test_do_check_reports_available_updates(monkeypatch)` (function)
- L236 `test_do_check_handles_no_installed_updates(monkeypatch)` (function)
- L242 `test_do_update_reinstalls_outdated_skills(monkeypatch)` (function)
- L252 `test_handle_skills_slash_search_accepts_chatconsole_without_status_errors()` (function)
- L267 `test_do_install_scans_with_resolved_identifier(monkeypatch, tmp_path, hub_env)` (function)
- L320 `test_do_install_scans_official_bundles_with_source_provenance(monkeypatch, tmp_path, hub_env)` (function)
- L374 `test_do_install_preserves_nested_official_optional_path(monkeypatch, tmp_path, hub_env)` (function)
- L413 `_make_url_bundle_fetcher(name='', awaiting_name=True, url='https://example.com/SKILL.md')` (function) — Return a fake source that simulates ``UrlSource.fetch`` for a
- L439 `_install_mocks(monkeypatch, tmp_path, source_factory, category_hint='')` (function) — Wire the minimum set of monkeypatches for a do_install dry run.
- L474 `test_url_install_uses_name_override_on_non_interactive_surface(monkeypatch, tmp_path, hub_env)` (function)
- L488 `test_url_install_rejects_invalid_name_override(monkeypatch, tmp_path, hub_env)` (function)
- L503 `test_url_install_actionable_error_on_non_interactive_with_no_name(monkeypatch, tmp_path, hub_env)` (function)
- L520 `test_url_install_prompts_interactively_when_tty(monkeypatch, tmp_path, hub_env)` (function)
- L538 `test_url_install_prompts_category_and_uses_typed_value(monkeypatch, tmp_path, hub_env)` (function)
- L564 `test_url_install_cancel_name_prompt_aborts(monkeypatch, tmp_path, hub_env)` (function)
- L584 `test_existing_categories_skips_top_level_skills(monkeypatch, tmp_path, hub_env)` (function)
- L606 `test_existing_categories_returns_empty_when_skills_dir_missing(monkeypatch, tmp_path, hub_env)` (function)
- L620 `test_browse_skills_dedup_uses_identifier_not_name(monkeypatch)` (function) — browse_skills() must not collapse browse-sh skills that share a task name.
- L673 `test_do_search_identifier_column_does_not_truncate_long_slug()` (function) — The Identifier column must use overflow='fold', not the default ellipsis.
- L723 `test_do_search_json_flag_emits_full_identifiers(capsys)` (function) — `--json` must print a parseable array with full identifiers and skip the table.
