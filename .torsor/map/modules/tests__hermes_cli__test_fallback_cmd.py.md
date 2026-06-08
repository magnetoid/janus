---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_fallback_cmd.py

Symbols in `tests/hermes_cli/test_fallback_cmd.py`.

- L17 `isolated_home(tmp_path, monkeypatch)` (function)
- L25 `_write_config(home: Path, data: dict)` (function)
- L30 `_read_config(home: Path)` (function)
- L39 `TestReadChain` (class)
- L40 `test_returns_empty_list_when_unset(self)` (method)
- L44 `test_reads_new_list_format(self)` (method)
- L57 `test_merges_new_and_legacy_formats(self)` (method)
- L70 `test_legacy_duplicate_is_deduplicated_after_merge(self)` (method)
- L82 `test_migrates_legacy_single_dict(self)` (method)
- L87 `test_skips_incomplete_entries(self)` (method)
- L99 `test_returns_copies_not_aliases(self)` (method)
- L111 `TestExtractFallback` (class)
- L112 `test_extracts_from_default_field(self)` (method)
- L120 `test_extracts_optional_base_url_and_api_mode(self)` (method)
- L135 `test_returns_none_without_provider(self)` (method)
- L139 `test_returns_none_without_model(self)` (method)
- L143 `test_returns_none_for_non_dict(self)` (method)
- L153 `TestListCommand` (class)
- L154 `test_list_empty(self, isolated_home, capsys)` (method)
- L162 `test_list_with_entries(self, isolated_home, capsys)` (method)
- L179 `test_list_migrates_legacy_for_display(self, isolated_home, capsys)` (method)
- L194 `TestAddCommand` (class)
- L195 `test_add_appends_new_entry(self, isolated_home, capsys)` (method)
- L233 `test_add_rejects_duplicate(self, isolated_home, capsys)` (method)
- L258 `test_add_rejects_same_as_primary(self, isolated_home, capsys)` (method)
- L280 `test_add_preserves_primary_when_picker_changes_it(self, isolated_home)` (method) — The picker mutates config["model"]; fallback_add must restore the primary.
- L317 `test_add_noop_when_picker_cancelled(self, isolated_home, capsys)` (method)
- L338 `test_add_noop_when_picker_clears_model(self, isolated_home, capsys)` (method) — Simulate picker explicitly clearing model.default (unusual but possible).
- L363 `TestRemoveCommand` (class)
- L364 `test_remove_empty_chain(self, isolated_home, capsys)` (method)
- L371 `test_remove_selected_entry(self, isolated_home, capsys)` (method)
- L394 `test_remove_cancel_keeps_chain(self, isolated_home)` (method)
- L414 `TestClearCommand` (class)
- L415 `test_clear_empty_chain(self, isolated_home, capsys)` (method)
- L422 `test_clear_with_confirmation(self, isolated_home, capsys, monkeypatch)` (method)
- L438 `test_clear_cancelled(self, isolated_home, monkeypatch)` (method)
- L454 `TestDispatcher` (class)
- L455 `test_no_subcommand_lists(self, isolated_home, capsys)` (method)
- L462 `test_list_alias(self, isolated_home, capsys)` (method)
- L469 `test_remove_alias(self, isolated_home, capsys)` (method)
- L476 `test_unknown_subcommand_exits(self, isolated_home)` (method)
- L487 `TestArgparseWiring` (class) — Verify `hermes fallback` is wired into main.py's argparse tree.
- L494 `test_fallback_help_lists_subcommands(self)` (method)
