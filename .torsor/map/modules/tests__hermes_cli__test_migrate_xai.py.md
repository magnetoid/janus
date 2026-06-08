---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_migrate_xai.py

Symbols in `tests/hermes_cli/test_migrate_xai.py`.

- L20 `trap_config(tmp_path: Path)` (function) — A config.yaml with retired models AND comments to verify round-trip.
- L48 `clean_config(tmp_path: Path)` (function)
- L59 `_parse(path: Path)` (function) — Load with ruamel for assertion convenience.
- L71 `TestNoOpPaths` (class)
- L72 `test_clean_config_returns_unchanged_result(self, clean_config: Path)` (method)
- L81 `test_empty_issues_list_is_noop(self, trap_config: Path)` (method)
- L87 `test_missing_file_raises(self, tmp_path: Path)` (method)
- L102 `TestApplyReplacement` (class)
- L103 `test_replaces_principal_model(self, trap_config: Path)` (method)
- L110 `test_adds_reasoning_effort_for_non_reasoning_variant(self, trap_config: Path)` (method)
- L117 `test_replaces_auxiliary_vision(self, trap_config: Path)` (method)
- L123 `test_replaces_delegation(self, trap_config: Path)` (method)
- L129 `test_replaces_image_gen_plugin(self, trap_config: Path)` (method)
- L135 `test_does_not_touch_unrelated_slots(self, trap_config: Path)` (method)
- L150 `TestRoundTripPreservation` (class)
- L151 `test_preserves_top_of_file_comment(self, trap_config: Path)` (method)
- L157 `test_preserves_inline_comments_on_unmodified_lines(self, trap_config: Path)` (method)
- L164 `test_preserves_top_level_key_order(self, trap_config: Path)` (method)
- L181 `TestBackup` (class)
- L182 `test_backup_is_written_by_default(self, trap_config: Path)` (method)
- L190 `test_backup_filename_prefixed(self, trap_config: Path)` (method)
- L196 `test_no_backup_when_disabled(self, trap_config: Path)` (method)
- L203 `test_no_backup_when_no_changes(self, clean_config: Path)` (method)
- L214 `TestIdempotence` (class)
- L215 `test_apply_twice_is_safe(self, trap_config: Path)` (method)
