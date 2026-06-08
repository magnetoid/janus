---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skill_usage.py

Symbols in `tests/tools/test_skill_usage.py`.

- L11 `_bump_view_many(hermes_home: str, skill_name: str, iterations: int)` (function)
- L20 `skills_home(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with a clean skills/ dir for each test.
- L41 `_write_skill(skills_dir: Path, name: str, category: str='')` (function) — Create a minimal SKILL.md with a name: frontmatter field.
- L65 `test_empty_usage_returns_empty_dict(skills_home)` (function)
- L70 `test_save_and_load_roundtrip(skills_home)` (function)
- L79 `test_save_is_atomic_no_partial_tmp_files(skills_home)` (function)
- L88 `test_get_record_missing_returns_empty_record(skills_home)` (function)
- L98 `test_get_record_backfills_missing_keys(skills_home)` (function)
- L107 `test_load_usage_handles_corrupt_file(skills_home)` (function)
- L117 `test_bump_view_increments_and_timestamps(skills_home)` (function)
- L126 `test_bump_use_increments_and_timestamps(skills_home)` (function)
- L134 `test_bump_patch_increments_and_timestamps(skills_home)` (function)
- L142 `test_bump_on_empty_name_is_noop(skills_home)` (function)
- L148 `test_bumps_do_not_corrupt_other_skills(skills_home)` (function)
- L158 `test_concurrent_bump_view_preserves_all_updates(skills_home)` (function)
- L186 `test_set_state_active(skills_home)` (function)
- L192 `test_set_state_archived_records_timestamp(skills_home)` (function)
- L200 `test_set_state_invalid_is_noop(skills_home)` (function)
- L208 `test_restoring_from_archive_clears_timestamp(skills_home)` (function)
- L216 `test_set_pinned(skills_home)` (function)
- L224 `test_forget_removes_record(skills_home)` (function)
- L236 `test_agent_created_excludes_bundled(skills_home)` (function)
- L251 `test_agent_created_excludes_hub_installed(skills_home)` (function)
- L268 `test_agent_created_excludes_hub_installed_frontmatter_name(skills_home)` (function)
- L314 `test_is_agent_created(skills_home)` (function)
- L328 `test_agent_created_skips_archive_and_hub_dirs(skills_home)` (function)
- L348 `test_archive_skill_moves_directory(skills_home)` (function)
- L362 `test_archive_refuses_bundled_skill(skills_home)` (function)
- L373 `test_archive_refuses_hub_skill(skills_home)` (function)
- L387 `test_archive_missing_skill_returns_error(skills_home)` (function)
- L394 `test_restore_skill_moves_back(skills_home)` (function)
- L407 `test_restore_skill_finds_nested_archive_subdir(skills_home)` (function) — Skills archived under nested category subdirs (e.g.
- L426 `test_restore_skill_finds_nested_timestamped_prefix(skills_home)` (function) — Prefix-match path (timestamped dupes) must also descend into nested
- L442 `test_archive_collision_gets_suffix(skills_home)` (function)
- L460 `test_agent_created_report_includes_marked_skills_with_defaults(skills_home)` (function)
- L477 `test_manual_skill_with_usage_is_not_curator_managed(skills_home)` (function)
- L488 `test_agent_created_report_excludes_bundled_and_hub(skills_home)` (function)
- L507 `test_agent_created_report_derives_activity_from_view_and_patch(skills_home, monkeypatch)` (function)
- L533 `test_bump_view_tracks_bundled_skill(skills_home)` (function) — Telemetry IS recorded for bundled skills (observability), but the record
- L553 `test_bump_patch_tracks_hub_skill(skills_home)` (function)
- L573 `test_bump_use_tracks_hub_skill(skills_home)` (function)
- L589 `test_set_state_no_op_for_bundled_skill(skills_home)` (function) — State transitions on bundled skills must not land in the sidecar.
- L600 `test_restore_refuses_to_shadow_bundled_skill(skills_home)` (function) — If a bundled skill now occupies the name, refuse to restore.
- L618 `test_end_to_end_telemetry_tracked_but_lifecycle_refused(skills_home)` (function) — The combined guarantee under decoupled telemetry/curation:
- L677 `test_usage_report_covers_all_provenance(skills_home)` (function) — usage_report() surfaces every skill with provenance, unlike the
