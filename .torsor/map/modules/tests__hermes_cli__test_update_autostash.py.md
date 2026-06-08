---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_autostash.py

Symbols in `tests/hermes_cli/test_update_autostash.py`.

- L22 `_patch_managed_uv(request)` (function) — Make managed_uv helpers follow shutil.which mocking in tests.
- L42 `test_stash_local_changes_if_needed_returns_none_when_tree_clean(monkeypatch, tmp_path)` (function)
- L59 `test_stash_local_changes_if_needed_returns_specific_stash_commit(monkeypatch, tmp_path)` (function)
- L84 `test_resolve_stash_selector_returns_matching_entry(monkeypatch, tmp_path)` (function)
- L98 `test_restore_stashed_changes_prompts_before_applying(monkeypatch, tmp_path, capsys)` (function)
- L130 `test_restore_stashed_changes_can_skip_restore_and_keep_stash(monkeypatch, tmp_path, capsys)` (function)
- L150 `test_restore_stashed_changes_applies_without_prompt_when_disabled(monkeypatch, tmp_path, capsys)` (function)
- L178 `test_print_stash_cleanup_guidance_with_selector(capsys)` (function)
- L188 `test_restore_stashed_changes_keeps_going_when_stash_entry_cannot_be_resolved(monkeypatch, tmp_path, capsys)` (function)
- L218 `test_restore_stashed_changes_keeps_going_when_drop_fails(monkeypatch, tmp_path, capsys)` (function)
- L247 `test_restore_stashed_changes_always_resets_on_conflict(monkeypatch, tmp_path, capsys)` (function) — Conflicts always auto-reset (no prompt) and return False, even interactively.
- L281 `test_restore_stashed_changes_auto_resets_non_interactive(monkeypatch, tmp_path, capsys)` (function) — Non-interactive mode auto-resets without prompting and returns False
- L307 `test_stash_local_changes_if_needed_raises_when_stash_ref_missing(monkeypatch, tmp_path)` (function)
- L329 `_setup_update_mocks(monkeypatch, tmp_path)` (function) — Common setup for cmd_update tests.
- L342 `test_cmd_update_retries_optional_extras_individually_when_all_fails(monkeypatch, tmp_path, capsys)` (function) — When .[all] fails, update should keep base deps and retry extras individually.
- L392 `test_cmd_update_succeeds_with_extras(monkeypatch, tmp_path)` (function) — When .[all] succeeds, no fallback should be attempted.
- L421 `test_install_with_optional_fallback_honors_custom_group(monkeypatch)` (function) — Termux update path should target .[termux-all] when requested.
- L451 `test_install_heartbeat_prints_when_dependency_install_is_silent(monkeypatch, capsys)` (function) — Long quiet installs should emit periodic heartbeat lines.
- L473 `_make_update_side_effect(current_branch='main', commit_count='3', ff_only_fails=False, reset_fails=False, fetch_fails=False, fetch_stderr='')` (function) — Build a subprocess.run side_effect for cmd_update tests.
- L514 `test_cmd_update_falls_back_to_reset_when_ff_only_fails(monkeypatch, tmp_path, capsys)` (function) — When --ff-only fails (diverged history), update resets to origin/{branch}.
- L532 `test_cmd_update_no_reset_when_ff_only_succeeds(monkeypatch, tmp_path)` (function) — When --ff-only succeeds, no reset is attempted.
- L550 `test_cmd_update_switches_to_main_from_feature_branch(monkeypatch, tmp_path, capsys)` (function) — When on a feature branch, update checks out main before pulling.
- L568 `test_cmd_update_switches_to_main_from_detached_head(monkeypatch, tmp_path, capsys)` (function) — When in detached HEAD state, update checks out main before pulling.
- L585 `test_cmd_update_restores_stash_and_branch_when_already_up_to_date(monkeypatch, tmp_path, capsys)` (function) — When on a feature branch with no updates, stash is restored and branch switched back.
- L619 `test_cmd_update_no_checkout_when_already_on_main(monkeypatch, tmp_path)` (function) — When already on main, no checkout is needed.
- L637 `test_cmd_update_network_error_shows_friendly_message(monkeypatch, tmp_path, capsys)` (function) — Network failures during fetch show a user-friendly message.
- L654 `test_cmd_update_auth_error_shows_friendly_message(monkeypatch, tmp_path, capsys)` (function) — Auth failures during fetch show a user-friendly message.
- L675 `test_cmd_update_skips_stash_restore_when_reset_fails(monkeypatch, tmp_path, capsys)` (function) — When reset --hard fails, stash restore is skipped with a helpful message.
- L709 `_setup_setting_test(monkeypatch, tmp_path, mode)` (function) — Common wiring: real stash returns a ref, restore + discard are
- L738 `test_non_interactive_discard_throws_changes_away(monkeypatch, tmp_path)` (function) — Gateway/chat-app update with discard mode drops the stash, never restores.
- L748 `test_non_interactive_stash_restores_changes(monkeypatch, tmp_path)` (function) — Gateway/chat-app update with the default stash mode restores, never discards.
- L758 `test_interactive_update_ignores_discard_setting(monkeypatch, tmp_path)` (function) — An interactive (TTY) terminal update always restores — the discard
- L773 `test_non_interactive_defaults_to_stash_when_setting_absent(monkeypatch, tmp_path)` (function) — A config with no update section falls back to stash (safe default).
- L785 `test_bootstrap_marker_not_autostashed_by_update(tmp_path)` (function) — #38529: the Desktop bootstrap marker must be git-ignored so that
