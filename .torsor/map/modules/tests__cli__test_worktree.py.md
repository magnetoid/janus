---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_worktree.py

Symbols in `tests/cli/test_worktree.py`.

- L15 `git_repo(tmp_path)` (function) — Create a temporary git repo for testing.
- L49 `git_repo_no_remote(tmp_path)` (function) — Create a temporary git repo with no configured remotes.
- L72 `git_repo_remote_no_tracking(tmp_path)` (function) — Create a temporary git repo with a remote but no remote-tracking refs.
- L102 `_git_repo_root(cwd=None)` (function) — Test version of _git_repo_root.
- L117 `_setup_worktree(repo_root)` (function) — Test version of _setup_worktree — creates a worktree.
- L142 `_has_unpushed_commits(worktree_path, timeout=10)` (function) — Test version of the worktree unpushed-commit helper.
- L165 `_cleanup_worktree(info)` (function) — Test version of _cleanup_worktree.
- L196 `TestGitRepoDetection` (class) — Test git repo root detection.
- L199 `test_detects_git_repo(self, git_repo)` (method)
- L204 `test_detects_subdirectory(self, git_repo)` (method)
- L211 `test_returns_none_outside_repo(self, tmp_path)` (method)
- L219 `TestWorktreeCreation` (class) — Test worktree setup.
- L222 `test_creates_worktree(self, git_repo)` (method)
- L236 `test_worktree_has_own_branch(self, git_repo)` (method)
- L247 `test_worktree_is_independent(self, git_repo)` (method) — Two worktrees from the same repo are independent.
- L262 `test_worktrees_dir_created(self, git_repo)` (method)
- L267 `test_worktree_has_repo_files(self, git_repo)` (method) — Worktree should contain the repo's tracked files.
- L274 `TestWorktreeCleanup` (class) — Test worktree cleanup on exit.
- L277 `test_clean_worktree_removed(self, git_repo)` (method)
- L286 `test_dirty_worktree_cleaned_when_no_unpushed(self, git_repo)` (method) — Dirty working tree without unpushed commits is cleaned up.
- L309 `test_worktree_with_unpushed_commits_kept(self, git_repo)` (method) — Worktree with unpushed commits is preserved.
- L326 `test_clean_worktree_removed_without_remote(self, git_repo_no_remote)` (method) — Clean worktrees in repos without remotes should still be removed.
- L337 `test_clean_worktree_removed_without_remote_tracking_refs(self, git_repo_remote_no_tracking)` (method) — Configured remotes without fetched refs should not block cleanup.
- L350 `test_branch_deleted_on_cleanup(self, git_repo)` (method)
- L363 `test_cleanup_nonexistent_worktree(self, git_repo)` (method) — Cleanup should handle already-removed worktrees gracefully.
- L374 `TestWorktreeInclude` (class) — Test .worktreeinclude file handling.
- L377 `test_copies_included_files(self, git_repo)` (method) — Files listed in .worktreeinclude should be copied to the worktree.
- L415 `test_ignores_comments_and_blanks(self, git_repo)` (method) — Comments and blank lines in .worktreeinclude should be skipped.
- L427 `TestGitignoreManagement` (class) — Test that .worktrees/ is added to .gitignore.
- L430 `test_adds_to_gitignore(self, git_repo)` (method) — Creating a worktree should add .worktrees/ to .gitignore.
- L452 `test_does_not_duplicate_gitignore_entry(self, git_repo)` (method) — If .worktrees/ is already in .gitignore, don't add again.
- L462 `TestMultipleWorktrees` (class) — Test running multiple worktrees concurrently (the core use case).
- L465 `test_ten_concurrent_worktrees(self, git_repo)` (method) — Create 10 worktrees — simulating 10 parallel agents.
- L511 `TestWorktreeDirectorySymlink` (class) — Test .worktreeinclude with directories (symlinked).
- L514 `test_symlinks_directory(self, git_repo)` (method) — Directories in .worktreeinclude should be symlinked.
- L546 `TestStaleWorktreePruning` (class) — Test _prune_stale_worktrees garbage collection.
- L549 `test_prunes_old_clean_worktree(self, git_repo)` (method) — Old clean worktrees should be removed on prune.
- L599 `test_keeps_recent_worktree(self, git_repo)` (method) — Recent worktrees should NOT be pruned.
- L622 `test_keeps_old_worktree_with_unpushed_commits(self, git_repo)` (method) — Old worktrees (24-72h) with unpushed commits should NOT be pruned.
- L646 `test_prunes_old_clean_worktree_without_remote(self, git_repo_no_remote)` (method) — Old clean worktrees in repos without remotes should not be kept.
- L686 `test_prunes_old_clean_worktree_without_remote_tracking_refs(self, git_repo_remote_no_tracking)` (method) — Old clean worktrees with no fetched remote refs should be pruned.
- L730 `test_force_prunes_very_old_worktree(self, git_repo)` (method) — Worktrees older than 72h should be force-pruned regardless.
- L774 `TestEdgeCases` (class) — Test edge cases for robustness.
- L777 `test_no_commits_repo(self, tmp_path)` (method) — Worktree creation should fail gracefully on a repo with no commits.
- L786 `test_not_a_git_repo(self, tmp_path)` (method) — Repo detection should return None for non-git directories.
- L793 `test_worktrees_dir_already_exists(self, git_repo)` (method) — Should work fine if .worktrees/ already exists.
- L801 `TestCLIFlagLogic` (class) — Test the flag/config OR logic from main().
- L804 `test_worktree_flag_triggers(self)` (method) — --worktree flag should trigger worktree creation.
- L812 `test_w_flag_triggers(self)` (method) — -w flag should trigger worktree creation.
- L820 `test_config_triggers(self)` (method) — worktree: true in config should trigger worktree creation.
- L828 `test_none_set_no_trigger(self)` (method) — No flags and no config should not trigger.
- L837 `TestTerminalCWDIntegration` (class) — Test that TERMINAL_CWD is correctly set to the worktree path.
- L840 `test_terminal_cwd_set(self, git_repo)` (method) — After worktree setup, TERMINAL_CWD should point to the worktree.
- L853 `test_terminal_cwd_is_valid_git_repo(self, git_repo)` (method) — The TERMINAL_CWD worktree should be a valid git working tree.
- L865 `TestOrphanedBranchPruning` (class) — Test cleanup of orphaned hermes/* and pr-* branches.
- L868 `test_prunes_orphaned_hermes_branch(self, git_repo)` (method) — hermes/hermes-* branches with no worktree should be deleted.
- L920 `test_prunes_orphaned_pr_branch(self, git_repo)` (method) — pr-* branches should be deleted during pruning.
- L959 `test_preserves_active_worktree_branch(self, git_repo)` (method) — Branches with active worktrees should NOT be pruned.
- L975 `test_preserves_main_branch(self, git_repo)` (method) — main branch should never be pruned.
- L992 `TestSystemPromptInjection` (class) — Test that the agent gets worktree context in its system prompt.
- L995 `test_prompt_note_format(self, git_repo)` (method) — Verify the system prompt note contains all required info.
