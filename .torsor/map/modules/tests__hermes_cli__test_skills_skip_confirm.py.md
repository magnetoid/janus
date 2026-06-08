---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_skills_skip_confirm.py

Symbols in `tests/hermes_cli/test_skills_skip_confirm.py`.

- L17 `TestHandleSkillsSlashInstallFlags` (class) — Test flag parsing in handle_skills_slash for install.
- L20 `test_yes_flag_sets_skip_confirm(self)` (method)
- L29 `test_y_flag_sets_skip_confirm(self)` (method)
- L37 `test_force_flag_sets_force(self)` (method)
- L47 `test_no_flags_still_skips_confirm(self)` (method) — Slash commands always skip confirmation — input() hangs in TUI.
- L57 `test_default_defers_cache_invalidation(self)` (method) — Without --now, cache invalidation is deferred to next session.
- L66 `test_now_flag_invalidates_cache(self)` (method) — --now opts into immediate cache invalidation.
- L76 `TestHandleSkillsSlashUninstallFlags` (class) — Test flag parsing in handle_skills_slash for uninstall.
- L79 `test_yes_flag_sets_skip_confirm(self)` (method)
- L87 `test_y_flag_sets_skip_confirm(self)` (method)
- L95 `test_no_flags_still_skips_confirm(self)` (method) — Slash commands always skip confirmation — input() hangs in TUI.
- L104 `test_default_defers_cache_invalidation(self)` (method) — Without --now, cache invalidation is deferred to next session.
- L113 `test_now_flag_invalidates_cache(self)` (method) — --now opts into immediate cache invalidation.
- L123 `TestDoInstallSkipConfirm` (class) — Test that do_install respects skip_confirm parameter.
- L127 `test_without_skip_confirm_prompts_user(self, mock_input)` (method) — Without skip_confirm, input() is called for confirmation.
- L144 `TestDoUninstallSkipConfirm` (class) — Test that do_uninstall respects skip_confirm parameter.
- L147 `test_skip_confirm_bypasses_input(self)` (method) — With skip_confirm=True, input() should not be called.
- L157 `test_without_skip_confirm_calls_input(self)` (method) — Without skip_confirm, input() should be called.
- L166 `test_without_skip_confirm_cancel(self)` (method) — Without skip_confirm, answering 'n' should cancel.
