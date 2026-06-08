---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skills_sync.py

Symbols in `tests/tools/test_skills_sync.py`.

- L21 `TestReadWriteManifest` (class)
- L22 `test_read_missing_manifest(self, tmp_path)` (method)
- L30 `test_write_and_read_roundtrip_v2(self, tmp_path)` (method)
- L40 `test_write_manifest_sorted(self, tmp_path)` (method)
- L51 `test_read_v1_manifest_migration(self, tmp_path)` (method) — v1 format (plain names, no hashes) should be read with empty hashes.
- L61 `test_read_manifest_ignores_blank_lines(self, tmp_path)` (method)
- L70 `test_read_manifest_mixed_v1_v2(self, tmp_path)` (method) — Manifest with both v1 and v2 lines (shouldn't happen but handle gracefully).
- L81 `TestDirHash` (class)
- L82 `test_same_content_same_hash(self, tmp_path)` (method)
- L91 `test_different_content_different_hash(self, tmp_path)` (method)
- L100 `test_empty_dir(self, tmp_path)` (method)
- L106 `test_nonexistent_dir(self, tmp_path)` (method)
- L111 `TestDiscoverBundledSkills` (class)
- L112 `test_finds_skills_with_skill_md(self, tmp_path)` (method)
- L126 `test_ignores_git_directories(self, tmp_path)` (method)
- L132 `test_nonexistent_dir_returns_empty(self, tmp_path)` (method)
- L137 `TestReadSkillName` (class)
- L138 `test_reads_name_from_frontmatter(self, tmp_path)` (method)
- L143 `test_falls_back_to_dir_name_without_frontmatter(self, tmp_path)` (method)
- L148 `test_falls_back_when_name_field_empty(self, tmp_path)` (method)
- L153 `test_handles_quoted_name(self, tmp_path)` (method)
- L158 `test_discover_uses_frontmatter_name(self, tmp_path)` (method)
- L168 `TestComputeRelativeDest` (class)
- L169 `test_preserves_category_structure(self)` (method)
- L175 `test_flat_skill(self)` (method)
- L182 `TestSyncSkills` (class)
- L183 `_setup_bundled(self, tmp_path)` (method) — Create a fake bundled skills directory.
- L194 `_patches(self, bundled, skills_dir, manifest_file)` (method) — Return context manager stack for patching sync globals.
- L204 `test_suppressed_builtin_not_reseeded(self, tmp_path)` (method) — A curator-pruned built-in in the suppression list must NOT be
- L224 `test_fresh_install_copies_all(self, tmp_path)` (method)
- L241 `test_fresh_install_records_origin_hashes(self, tmp_path)` (method) — After fresh install, manifest should have v2 format with hashes.
- L257 `test_user_deleted_skill_not_re_added(self, tmp_path)` (method) — Skill in manifest but not on disk = user deleted it. Don't re-add.
- L275 `test_unmodified_skill_gets_updated(self, tmp_path)` (method) — Skill in manifest + on disk + user hasn't modified = update from bundled.
- L298 `test_user_modified_skill_not_overwritten(self, tmp_path)` (method) — Skill modified by user should NOT be overwritten even if bundled changed.
- L324 `test_unchanged_skill_not_updated(self, tmp_path)` (method) — Skill in sync (user == bundled == origin) = no action needed.
- L344 `test_v1_manifest_migration_sets_baseline(self, tmp_path)` (method) — v1 manifest entries (no hash) should set baseline from user's current copy.
- L368 `test_v1_migration_then_bundled_update_detected(self, tmp_path)` (method) — After v1 migration, a subsequent sync should detect bundled updates.
- L395 `test_stale_manifest_entries_cleaned(self, tmp_path)` (method) — Skills in manifest that no longer exist in bundled dir get cleaned.
- L411 `test_does_not_overwrite_existing_unmanifested_skill(self, tmp_path)` (method) — New skill whose name collides with user-created skill = skipped.
- L426 `test_collision_does_not_poison_manifest(self, tmp_path)` (method) — Collision with an unmanifested user skill must NOT record bundled_hash.
- L460 `test_collision_does_not_trigger_false_user_modified_on_resync(self, tmp_path)` (method) — End-to-end: after a collision, a second sync must not flag user_modified.
- L484 `test_collision_prints_reset_hint(self, tmp_path, capsys)` (method) — Non-quiet sync must print a reset hint when a collision is skipped.
- L506 `test_backfills_official_optional_provenance_for_existing_identical_skill(self, tmp_path)` (method)
- L540 `test_does_not_backfill_optional_provenance_for_modified_skill(self, tmp_path)` (method)
- L560 `test_repair_official_optional_restores_reorganized_skill_with_backup(self, tmp_path)` (method)
- L593 `test_repair_official_optional_without_restore_does_not_replace_modified_copy(self, tmp_path)` (method)
- L616 `test_nonexistent_bundled_dir(self, tmp_path)` (method)
- L625 `test_failed_copy_does_not_poison_manifest(self, tmp_path)` (method) — If copytree fails, the skill must NOT be added to the manifest.
- L661 `test_failed_update_does_not_destroy_user_copy(self, tmp_path)` (method) — If copytree fails during update, the user's existing copy must survive.
- L695 `test_update_records_new_origin_hash(self, tmp_path)` (method) — After updating a skill, the manifest should record the new bundled hash.
- L718 `TestGetBundledDir` (class)
- L719 `test_env_var_override(self, tmp_path, monkeypatch)` (method) — HERMES_BUNDLED_SKILLS env var overrides the default path resolution.
- L726 `test_default_without_env_var(self, monkeypatch)` (method) — Without the env var, falls back to relative path from __file__.
- L732 `test_env_var_empty_string_ignored(self, monkeypatch)` (method) — Empty HERMES_BUNDLED_SKILLS should fall back to default.
- L739 `TestResetBundledSkill` (class) — Covers reset_bundled_skill() — the escape hatch for the 'user-modified' trap.
- L742 `_setup_bundled(self, tmp_path)` (method) — Create a minimal bundled skills tree with a single 'google-workspace' skill.
- L751 `_patches(self, bundled, skills_dir, manifest_file)` (method)
- L760 `test_reset_clears_stuck_user_modified_flag(self, tmp_path)` (method) — The core bug repro: copy-pasted bundled restore doesn't un-stick the flag; reset does.
- L795 `test_reset_restore_replaces_user_copy(self, tmp_path)` (method) — --restore nukes the user's copy and re-copies the bundled version.
- L817 `test_reset_nonexistent_skill_errors_gracefully(self, tmp_path)` (method) — Resetting a skill that's neither bundled nor in the manifest returns a clear error.
- L832 `test_reset_restore_when_bundled_removed_upstream(self, tmp_path)` (method) — If a skill was removed upstream, --restore should fail with a clear message.
- L848 `test_reset_no_op_when_already_clean(self, tmp_path)` (method) — If manifest has skill but user copy is in-sync, reset still safely clears + re-baselines.
- L869 `test_reset_restore_succeeds_on_readonly_nix_tree(self, tmp_path)` (method) — #34972: --restore must succeed even when the user copy is a fully
- L917 `test_reset_restore_preserves_manifest_on_rmtree_failure(self, tmp_path)` (method) — #34972: when the user copy genuinely cannot be removed, the manifest
- L952 `TestNoBundledSkillsOptOut` (class) — The .no-bundled-skills marker makes sync_skills() a no-op.
- L960 `_setup_bundled(self, tmp_path)` (method)
- L967 `test_marker_skips_sync(self, tmp_path)` (method)
- L987 `test_no_marker_seeds_normally(self, tmp_path)` (method)
- L1007 `TestOptOutToggleAndRemove` (class) — `hermes skills opt-out/opt-in` core: marker toggle + safe removal.
- L1010 `_setup_bundled(self, tmp_path)` (method)
- L1018 `test_marker_toggle(self, tmp_path)` (method)
- L1037 `test_remove_keeps_user_modified(self, tmp_path)` (method)
