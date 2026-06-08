---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_cmd_update.py

Symbols in `tests/hermes_cli/test_cmd_update.py`.

- L12 `_make_run_side_effect(branch='main', verify_ok=True, commit_count='0')` (function) — Build a side_effect function for subprocess.run that simulates git commands.
- L38 `mock_args()` (function)
- L52 `_patch_managed_uv(request)` (function) — Make managed_uv helpers follow shutil.which mocking in tests.
- L73 `TestCmdUpdatePip` (class) — Regression tests for pip-install update flows.
- L78 `test_update_pip_exports_virtualenv_from_sys_prefix(self, mock_run, _mock_which, mock_args, monkeypatch)` (method)
- L96 `test_update_pip_does_not_export_virtualenv_for_system_python(self, mock_run, _mock_which, mock_args, monkeypatch)` (method)
- L112 `TestCmdUpdateBranchFallback` (class) — cmd_update falls back to main when current branch has no remote counterpart.
- L117 `test_update_falls_back_to_main_when_branch_not_on_remote(self, mock_run, _mock_which, mock_args, capsys)` (method)
- L141 `test_update_uses_current_branch_when_on_remote(self, mock_run, _mock_which, mock_args, capsys)` (method)
- L162 `test_update_already_up_to_date(self, mock_run, _mock_which, mock_args, capsys)` (method)
- L181 `test_update_on_fork_checks_upstream_when_origin_up_to_date(self, mock_run, _mock_which, mock_args, capsys)` (method) — Regression for issue #26172: forks whose local HEAD already matches
- L208 `test_update_refreshes_repo_and_tui_node_dependencies(self, mock_run, mock_which, mock_args)` (method)
- L304 `test_update_non_interactive_runs_safe_config_migrations(self, mock_args, capsys)` (method) — Dashboard/web updates apply non-interactive migrations before restart.
- L334 `TestCmdUpdateMigrationPrompt` (class) — The config-migration prompt names what changed and skips the prompt
- L344 `test_version_bump_only_applies_silently_without_prompt(self, mock_args, capsys)` (method) — Only the version moved → apply non-interactively, never prompt.
- L374 `test_new_options_are_listed_by_name_before_prompt(self, mock_args, capsys)` (method) — New env/config keys are printed by name so the user can decide.
- L411 `TestCmdUpdateProfileSkillSync` (class) — cmd_update syncs bundled skills to all profiles, including the active one.
- L420 `test_active_profile_included_in_skill_sync(self, mock_run, _mock_which, mock_args, capsys)` (method)
- L458 `test_single_profile_default_is_synced(self, mock_run, _mock_which, mock_args, capsys)` (method)
- L486 `TestCmdUpdateBranchFlag` (class) — ``hermes update --branch <name>`` targets the requested branch.
- L493 `_branch_side_effect(self, current_branch, target_branch, *, checkout_fails=False, track_fails=False, commit_count='0')` (method) — Mock side-effect that knows about checkout/track behavior.
- L530 `test_branch_flag_pulls_against_named_branch(self, mock_run, _mock_which, capsys)` (method) — --branch bb/gui makes rev-list and pull target origin/bb/gui.
- L552 `test_branch_flag_defaults_to_main_when_none(self, mock_run, _mock_which, capsys)` (method) — No --branch (or --branch=None) preserves the historical 'main' default.
- L567 `test_branch_flag_switches_from_different_branch(self, mock_run, _mock_which, capsys)` (method) — When HEAD is on main and --branch=bb/gui, switch to bb/gui first.
- L587 `test_branch_flag_tracks_remote_when_branch_absent_locally(self, mock_run, _mock_which, capsys)` (method) — If local lacks the branch but origin has it, fall back to ``checkout -B``.
- L609 `test_branch_flag_fails_when_branch_missing_everywhere(self, mock_run, _mock_which, capsys)` (method) — If branch doesn't exist locally OR on origin, exit non-zero with clear error.
- L629 `TestCmdUpdateCheckBranchFlag` (class) — ``hermes update --check --branch <name>`` honors the branch override.
- L640 `_check_side_effect(self, target_branch: str, *, verify_ok: bool=True, commit_count: str='0', upstream_fetch_ok: bool=True)` (method) — Mock side-effect for the _cmd_update_check git pipeline.
- L683 `test_check_branch_compares_against_named_origin_branch(self, mock_run, _mock_method, capsys)` (method) — --check --branch bb/gui compares against origin/bb/gui, never origin/main.
- L706 `test_check_branch_missing_on_origin_exits_cleanly(self, mock_run, _mock_method, capsys)` (method) — If origin/<branch> doesn't exist, surface a friendly error and exit 1.
- L737 `test_check_default_main_still_prefers_upstream(self, mock_run, _mock_method, capsys)` (method) — No --branch (or --branch=None) preserves the upstream-then-origin probe.
- L758 `test_check_branch_warns_on_pypi_install(self, mock_run, _mock_pypi, _mock_method, capsys)` (method) — PyPI install + --branch=<non-main> surfaces a warning instead of silent drop.
- L771 `TestCmdUpdateZipBranchRefusal` (class) — ``hermes update --branch=<non-main>`` must refuse on the ZIP fallback path.
- L780 `test_zip_fallback_refuses_non_main_branch(self, capsys)` (method)
- L795 `test_is_termux_env_true_for_termux_prefix()` (function)
- L801 `test_is_termux_env_false_for_non_termux_prefix()` (function)
- L807 `test_load_installable_optional_extras_supports_termux_group(tmp_path, monkeypatch)` (function)
