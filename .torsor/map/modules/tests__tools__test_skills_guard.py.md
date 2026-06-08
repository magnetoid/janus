---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skills_guard.py

Symbols in `tests/tools/test_skills_guard.py`.

- L9 `_can_symlink()` (function) — Check if we can create symlinks (needs admin/dev-mode on Windows).
- L45 `TestResolveTrustLevel` (class)
- L46 `test_official_source_provenance_resolves_to_builtin(self)` (method)
- L49 `test_trusted_repos(self)` (method)
- L54 `test_nvidia_skills_is_trusted(self)` (method)
- L62 `test_trusted_repo_sibling_prefixes_are_not_trusted(self)` (method)
- L67 `test_official_github_namespace_does_not_resolve_to_builtin(self)` (method)
- L71 `test_skills_sh_wrapped_trusted_repos(self)` (method)
- L75 `test_common_skills_sh_prefix_typo_still_maps_to_trusted_repo(self)` (method)
- L78 `test_community_default(self)` (method)
- L88 `TestDetermineVerdict` (class)
- L89 `test_no_findings_safe(self)` (method)
- L92 `test_critical_finding_dangerous(self)` (method)
- L96 `test_high_finding_caution(self)` (method)
- L100 `test_medium_finding_safe(self)` (method)
- L104 `test_low_finding_safe(self)` (method)
- L114 `TestShouldAllowInstall` (class)
- L115 `_result(self, trust, verdict, findings=None)` (method)
- L124 `test_safe_community_allowed(self)` (method)
- L128 `test_caution_community_blocked(self)` (method)
- L134 `test_caution_trusted_allowed(self)` (method)
- L139 `test_trusted_dangerous_blocked_without_force(self)` (method)
- L144 `test_builtin_dangerous_allowed_without_force(self)` (method)
- L150 `test_force_overrides_caution(self)` (method)
- L156 `test_dangerous_blocked_without_force(self)` (method)
- L161 `test_force_does_not_override_dangerous_for_community(self)` (method)
- L172 `test_force_does_not_override_dangerous_for_trusted_message(self)` (method)
- L181 `test_non_dangerous_block_keeps_force_hint(self)` (method)
- L194 `test_force_does_not_override_dangerous_for_trusted(self)` (method)
- L204 `test_safe_agent_created_allowed(self)` (method)
- L208 `test_caution_agent_created_allowed(self)` (method) — Agent-created skills with caution verdict (e.g. docker refs) should pass.
- L215 `test_dangerous_agent_created_asks(self)` (method) — Agent-created skills with dangerous verdict return None (ask for confirmation)
- L226 `test_force_overrides_dangerous_for_agent_created(self)` (method)
- L240 `TestScanFile` (class)
- L241 `test_safe_file(self, tmp_path)` (method)
- L247 `test_detect_curl_env_exfil(self, tmp_path)` (method)
- L253 `test_detect_prompt_injection(self, tmp_path)` (method)
- L259 `test_detect_multi_word_system_prompt_override(self, tmp_path)` (method)
- L273 `test_detect_multi_word_fake_policy_variants(self, tmp_path, text, pattern_id)` (method)
- L279 `test_detect_rm_rf_root(self, tmp_path)` (method)
- L285 `test_detect_reverse_shell(self, tmp_path)` (method)
- L291 `test_detect_invisible_unicode(self, tmp_path)` (method)
- L297 `test_nonscannable_extension_skipped(self, tmp_path)` (method)
- L303 `test_detect_hardcoded_secret(self, tmp_path)` (method)
- L309 `test_detect_eval_string(self, tmp_path)` (method)
- L315 `test_deduplication_per_pattern_per_line(self, tmp_path)` (method)
- L329 `TestScanSkill` (class)
- L330 `test_safe_skill(self, tmp_path)` (method)
- L342 `test_dangerous_skill(self, tmp_path)` (method)
- L352 `test_trusted_source(self, tmp_path)` (method)
- L360 `test_single_file_scan(self, tmp_path)` (method)
- L374 `TestCheckStructure` (class)
- L375 `test_too_many_files(self, tmp_path)` (method)
- L381 `test_oversized_single_file(self, tmp_path)` (method)
- L387 `test_binary_file_detected(self, tmp_path)` (method)
- L393 `test_symlink_escape(self, tmp_path)` (method)
- L405 `test_symlink_prefix_confusion_blocked(self, tmp_path)` (method) — A symlink resolving to a sibling dir with a shared prefix must be caught.
- L429 `test_symlink_within_skill_dir_allowed(self, tmp_path)` (method) — A symlink that stays within the skill directory is fine.
- L441 `test_clean_structure(self, tmp_path)` (method)
- L453 `TestFormatScanReport` (class)
- L454 `test_clean_report(self)` (method)
- L461 `test_dangerous_report(self)` (method)
- L475 `TestContentHash` (class)
- L476 `test_hash_directory(self, tmp_path)` (method)
- L483 `test_hash_single_file(self, tmp_path)` (method)
- L489 `test_hash_deterministic(self, tmp_path)` (method)
- L495 `test_hash_changes_with_content(self, tmp_path)` (method)
- L509 `TestUnicodeCharName` (class)
- L510 `test_known_chars(self)` (method)
- L514 `test_unknown_char(self)` (method)
- L524 `TestSymlinkPrefixConfusionRegression` (class) — Demonstrate the old startswith() bug vs the is_relative_to() fix.
- L533 `test_old_startswith_misses_prefix_confusion(self, tmp_path)` (method) — Old check fails: sibling dir with shared prefix passes startswith.
- L548 `test_is_relative_to_catches_prefix_confusion(self, tmp_path)` (method) — New check catches: is_relative_to correctly rejects sibling dir.
- L563 `test_legitimate_subpath_passes_both(self, tmp_path)` (method) — Both old and new checks correctly allow real subpaths.
- L586 `TestFalsePositiveReductions` (class) — Patterns that previously flagged benign, intrinsic skill content.
- L589 `test_cat_write_heredoc_into_env_is_not_a_read(self, tmp_path)` (method)
- L597 `test_cat_read_env_still_flagged(self, tmp_path)` (method)
- L603 `test_allowed_tools_frontmatter_is_low_severity(self, tmp_path)` (method)
- L612 `test_allowed_tools_does_not_make_skill_dangerous(self, tmp_path)` (method)
- L622 `test_os_environ_get_nonsecret_config_read_clean(self, tmp_path)` (method)
- L628 `test_os_environ_get_secret_named_still_critical(self, tmp_path)` (method)
- L636 `test_os_environ_bare_access_still_flagged(self, tmp_path)` (method)
- L648 `TestSkillIgnore` (class)
- L649 `test_directory_pattern_excludes_subtree(self, tmp_path)` (method)
- L659 `test_glob_pattern(self, tmp_path)` (method)
- L666 `test_comments_and_blanks_skipped(self, tmp_path)` (method)
- L671 `test_clawhubignore_honored(self, tmp_path)` (method)
- L676 `test_ignore_file_itself_always_excluded(self, tmp_path)` (method)
- L681 `test_skill_md_never_ignorable(self, tmp_path)` (method)
- L687 `test_scan_skill_honors_ignore_for_findings(self, tmp_path)` (method)
- L701 `test_scan_skill_without_ignore_flags_artifact(self, tmp_path)` (method)
- L711 `test_ignored_files_not_counted_in_structure(self, tmp_path)` (method)
