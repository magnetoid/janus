---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gui_command.py

Symbols in `tests/hermes_cli/test_gui_command.py`.

- L16 `_ns(**kw)` (function)
- L31 `_make_desktop_tree(tmp_path: Path)` (function)
- L39 `_make_packaged_executable(root: Path, monkeypatch, platform: str='darwin')` (function)
- L53 `test_gui_installs_packages_and_launches_desktop_app(tmp_path, monkeypatch)` (function)
- L80 `test_gui_forwards_desktop_environment_overrides(tmp_path, monkeypatch)` (function)
- L112 `test_gui_exits_when_npm_missing(tmp_path, monkeypatch, capsys)` (function)
- L124 `test_gui_skip_build_requires_existing_packaged_app(tmp_path, monkeypatch, capsys)` (function)
- L136 `test_gui_skip_build_launches_existing_packaged_app_without_npm(tmp_path, monkeypatch)` (function)
- L156 `test_gui_linux_configures_sandbox_before_launch(tmp_path, monkeypatch)` (function)
- L176 `test_gui_linux_rejects_symlink_sandbox(tmp_path, monkeypatch)` (function)
- L198 `test_gui_linux_skips_fixup_when_already_configured(tmp_path, monkeypatch)` (function)
- L225 `test_gui_source_mode_uses_renderer_build_and_electron(tmp_path, monkeypatch)` (function)
- L256 `test_gui_is_known_builtin_for_plugin_gating(argv)` (function)
- L264 `test_desktop_build_stamp_skips_build_when_up_to_date(tmp_path, monkeypatch)` (function) — When the stamp matches and the artifact exists, build is skipped entirely.
- L285 `test_desktop_force_build_overrides_stamp(tmp_path, monkeypatch)` (function) — --force-build forces a rebuild even when the stamp says up-to-date.
- L312 `test_compute_desktop_content_hash_stable(tmp_path, monkeypatch)` (function) — _compute_desktop_content_hash returns the same digest for identical trees.
- L326 `test_compute_desktop_content_hash_changes_on_edit(tmp_path, monkeypatch)` (function) — Editing a file under apps/desktop/ changes the hash.
- L340 `test_desktop_build_needed_detects_missing_artifact(tmp_path, monkeypatch)` (function) — Even with a valid stamp, missing artifact means build is needed.
- L354 `test_desktop_build_stamp_round_trip(tmp_path, monkeypatch)` (function) — Write stamp, then _desktop_build_needed returns False when artifact exists.
- L370 `test_compute_desktop_content_hash_works_without_gitignore(tmp_path, monkeypatch)` (function) — When no .gitignore exists, _compute_desktop_content_hash still works (matches everything).
- L388 `test_compute_desktop_content_hash_respects_gitignore(tmp_path, monkeypatch)` (function) — Files matched by .gitignore are excluded from the hash.
- L419 `_write_zip(path: Path)` (function)
- L427 `test_purge_electron_build_cache_clears_all_zips_and_unpacked_dir(tmp_path, monkeypatch)` (function) — Purge is unconditional: it removes every electron-*.zip (regardless of
- L460 `test_purge_electron_build_cache_empty_when_nothing_present(tmp_path, monkeypatch)` (function) — No cached zips and no unpacked dir → nothing removed, so the caller
- L471 `test_gui_retries_pack_once_after_purging_build_cache(tmp_path, monkeypatch)` (function) — First pack fails, purge clears the cache, second pack succeeds, launch.
- L501 `test_gui_does_not_retry_when_purge_finds_nothing(tmp_path, monkeypatch, capsys)` (function) — If the purge clears nothing, there's no point retrying — fail fast.
