---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_yes_flag.py

Symbols in `tests/hermes_cli/test_update_yes_flag.py`.

- L18 `_make_run_side_effect(branch='main', verify_ok=True, commit_count='1', dirty=False)` (function) — Minimal subprocess.run side_effect for the update flow.
- L50 `TestUpdateYesConfigMigration` (class) — --yes auto-answers the config-migration prompt and skips API-key prompts.
- L59 `test_yes_auto_migrates_without_input(self, mock_run, _mock_which, _mock_missing_env, _mock_missing_cfg, _mock_version, mock_migrate, capsys)` (method)
- L98 `test_no_yes_flag_still_prompts_in_tty(self, mock_run, _mock_which, _mock_missing_env, _mock_missing_cfg, _mock_version, mock_migrate, capsys)` (method) — Regression guard: without --yes, the TTY prompt path still fires.
- L135 `TestUpdateYesStashRestore` (class) — --yes auto-restores the pre-update autostash without prompting.
