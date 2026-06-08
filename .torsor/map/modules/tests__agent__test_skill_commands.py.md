---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_skill_commands.py

Symbols in `tests/agent/test_skill_commands.py`.

- L18 `_make_skill(skills_dir, name, frontmatter_extra='', body='Do the thing.', category=None)` (function) — Helper to create a minimal skill directory with SKILL.md.
- L41 `_symlink_category(skills_dir: Path, linked_root: Path, category: str)` (function) — Create a category symlink under skills_dir pointing outside the tree.
- L53 `TestScanSkillCommands` (class)
- L54 `test_finds_skills(self, tmp_path)` (method)
- L61 `test_empty_dir(self, tmp_path)` (method)
- L66 `test_excludes_incompatible_platform(self, tmp_path)` (method) — macOS-only skills should not register slash commands on Linux.
- L79 `test_includes_matching_platform(self, tmp_path)` (method) — macOS-only skills should register slash commands on macOS.
- L90 `test_universal_skill_on_any_platform(self, tmp_path)` (method) — Skills without platforms field should register on any platform.
- L101 `test_excludes_disabled_skills(self, tmp_path)` (method) — Disabled skills should not register slash commands.
- L116 `test_finds_skills_in_symlinked_category_dir(self, tmp_path)` (method)
- L130 `test_loads_skill_invocation_from_symlinked_skill_dir(self, tmp_path)` (method) — Slash commands should load skills symlinked under the local skills dir.
- L154 `test_get_skill_commands_rescans_when_platform_scope_changes(self, tmp_path)` (method) — Platform-specific disabled-skill caches must not leak across platforms.
- L206 `test_get_skill_commands_rescans_when_session_platform_changes(self, tmp_path)` (method) — ``HERMES_SESSION_PLATFORM`` from the gateway session context must
- L272 `test_get_skill_commands_rescans_when_leaving_platform_scope(self, tmp_path, monkeypatch)` (method) — Returning to no-platform-scope (CLI / cron / RL) after a gateway
- L308 `test_get_skill_commands_does_not_rescan_when_platform_unchanged(self, tmp_path)` (method) — Same-platform back-to-back calls must hit the cache, not rescan.
- L338 `test_special_chars_stripped_from_cmd_key(self, tmp_path)` (method) — Skill names with +, /, or other special chars produce clean cmd keys.
- L354 `test_allspecial_name_skipped(self, tmp_path)` (method) — Skill with name consisting only of special chars is silently skipped.
- L367 `test_slash_in_name_stripped_from_cmd_key(self, tmp_path)` (method) — Skill names with / chars produce clean cmd keys.
- L381 `TestResolveSkillCommandKey` (class) — Telegram bot-command names disallow hyphens, so the menu registers
- L387 `test_hyphenated_form_matches_directly(self, tmp_path)` (method)
- L393 `test_underscore_form_resolves_to_hyphenated_skill(self, tmp_path)` (method) — /claude_code from Telegram autocomplete must resolve to /claude-code.
- L400 `test_single_word_command_resolves(self, tmp_path)` (method)
- L406 `test_unknown_command_returns_none(self, tmp_path)` (method)
- L413 `test_empty_command_returns_none(self, tmp_path)` (method)
- L418 `test_hyphenated_command_is_not_mangled(self, tmp_path)` (method) — A user-typed /foo-bar (hyphen) must not trigger the underscore fallback.
- L428 `TestBuildPreloadedSkillsPrompt` (class)
- L429 `test_builds_prompt_for_multiple_named_skills(self, tmp_path)` (method)
- L443 `test_reports_missing_named_skills(self, tmp_path)` (method)
- L455 `TestBuildSkillInvocationMessage` (class)
- L456 `test_loads_skill_by_stored_path_when_frontmatter_name_differs(self, tmp_path)` (method)
- L480 `test_builds_message(self, tmp_path)` (method)
- L489 `test_returns_none_for_unknown(self, tmp_path)` (method)
- L495 `test_returns_none_when_skill_load_fails(self, tmp_path)` (method)
- L503 `test_uses_shared_skill_loader_for_secure_setup(self, tmp_path, monkeypatch)` (method)
- L542 `test_gateway_still_loads_skill_but_returns_setup_guidance(self, tmp_path, monkeypatch)` (method)
- L581 `test_preserves_remaining_remote_setup_warning(self, tmp_path, monkeypatch)` (method)
- L607 `test_supporting_file_hint_uses_file_path_argument(self, tmp_path)` (method)
- L620 `TestSkillDirectoryHeader` (class) — The activation message must expose the absolute skill directory and
- L625 `test_header_contains_absolute_skill_dir(self, tmp_path)` (method)
- L635 `test_supporting_files_shown_with_absolute_paths(self, tmp_path)` (method)
- L652 `TestTemplateVarSubstitution` (class) — ``${HERMES_SKILL_DIR}`` and ``${HERMES_SESSION_ID}`` in SKILL.md body
- L656 `test_substitutes_skill_dir(self, tmp_path)` (method)
- L671 `test_substitutes_session_id_when_available(self, tmp_path)` (method)
- L686 `test_leaves_session_id_token_when_missing(self, tmp_path)` (method)
- L700 `test_disable_template_vars_via_config(self, tmp_path)` (method)
- L721 `TestInlineShellExpansion` (class) — Inline ``!`cmd`` snippets in SKILL.md run before the agent sees the
- L725 `test_inline_shell_is_off_by_default(self, tmp_path)` (method)
- L740 `test_inline_shell_runs_when_enabled(self, tmp_path)` (method)
- L761 `test_inline_shell_runs_in_skill_directory(self, tmp_path)` (method) — Inline snippets get the skill dir as CWD so relative paths work.
- L782 `test_inline_shell_timeout_does_not_break_message(self, tmp_path)` (method)
