---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_credential_files.py

Symbols in `tests/tools/test_credential_files.py`.

- L23 `_clean_state()` (function) — Reset module state between tests.
- L33 `TestRegisterCredentialFiles` (class)
- L34 `test_dict_with_path_key(self, tmp_path)` (method)
- L48 `test_dict_with_name_key_fallback(self, tmp_path)` (method) — Skills use 'name' instead of 'path' — both should work.
- L64 `test_string_entry(self, tmp_path)` (method)
- L76 `test_missing_file_reported(self, tmp_path)` (method)
- L88 `test_path_takes_precedence_over_name(self, tmp_path)` (method) — When both path and name are present, path wins.
- L104 `TestSkillsDirectoryMount` (class)
- L105 `test_returns_mount_when_skills_dir_exists(self, tmp_path)` (method)
- L119 `test_returns_none_when_no_skills_dir(self, tmp_path)` (method)
- L130 `test_custom_container_base(self, tmp_path)` (method)
- L139 `test_symlinks_are_sanitized(self, tmp_path)` (method) — Symlinks in skills dir should be excluded from the mount.
- L164 `test_no_symlinks_returns_original_dir(self, tmp_path)` (method) — When no symlinks exist, the original dir is returned (no copy).
- L177 `TestIterSkillsFiles` (class)
- L178 `test_returns_files_skipping_symlinks(self, tmp_path)` (method)
- L199 `test_empty_when_no_skills_dir(self, tmp_path)` (method)
- L206 `TestPathTraversalSecurity` (class) — Path traversal and absolute path rejection.
- L218 `test_dotdot_traversal_rejected(self, tmp_path, monkeypatch)` (method) — '../sensitive' must not escape HERMES_HOME.
- L232 `test_deep_traversal_rejected(self, tmp_path, monkeypatch)` (method) — '../../etc/passwd' style traversal must be rejected.
- L248 `test_absolute_path_rejected(self, tmp_path, monkeypatch)` (method) — Absolute paths must be rejected regardless of whether they exist.
- L263 `test_legitimate_file_still_works(self, tmp_path, monkeypatch)` (method) — Normal files inside HERMES_HOME must still be registered.
- L277 `test_nested_subdir_inside_hermes_home_allowed(self, tmp_path, monkeypatch)` (method) — Files in subdirectories of HERMES_HOME must be allowed.
- L290 `test_symlink_traversal_rejected(self, tmp_path, monkeypatch)` (method) — A symlink inside HERMES_HOME pointing outside must be rejected.
- L318 `TestConfigPathTraversal` (class) — terminal.credential_files in config.yaml must also reject traversal.
- L321 `_write_config(self, hermes_home: Path, cred_files: list)` (method)
- L326 `test_config_traversal_rejected(self, tmp_path, monkeypatch)` (method) — '../secret' in config.yaml must not escape HERMES_HOME.
- L341 `test_config_absolute_path_rejected(self, tmp_path, monkeypatch)` (method) — Absolute paths in config.yaml must be rejected.
- L354 `test_config_legitimate_file_works(self, tmp_path, monkeypatch)` (method) — Normal files inside HERMES_HOME via config must still mount.
- L372 `TestCacheDirectoryMounts` (class) — Tests for get_cache_directory_mounts() and iter_cache_files().
- L375 `test_returns_existing_cache_dirs(self, tmp_path, monkeypatch)` (method) — Existing cache dirs are returned with correct container paths.
- L388 `test_skips_nonexistent_dirs(self, tmp_path, monkeypatch)` (method) — Dirs that don't exist on disk are not returned.
- L400 `test_legacy_dir_names_resolved(self, tmp_path, monkeypatch)` (method) — Old-style dir names (e.g. document_cache) are resolved correctly.
- L418 `test_empty_hermes_home(self, tmp_path, monkeypatch)` (method) — No cache dirs → empty list.
- L427 `TestMapCachePathToContainer` (class) — Tests for map_cache_path_to_container() — the backend-agnostic mapper.
- L430 `test_maps_path_under_cache_dir(self, tmp_path, monkeypatch)` (method)
- L442 `test_custom_container_base_for_remote_home(self, tmp_path, monkeypatch)` (method)
- L454 `test_returns_none_when_outside_cache_dirs(self, tmp_path, monkeypatch)` (method)
- L461 `test_returns_none_when_no_cache_dirs_exist(self, tmp_path, monkeypatch)` (method)
- L469 `TestIterCacheFiles` (class) — Tests for iter_cache_files().
- L472 `test_enumerates_files(self, tmp_path, monkeypatch)` (method) — Regular files in cache dirs are returned.
- L486 `test_skips_symlinks(self, tmp_path, monkeypatch)` (method) — Symlinks inside cache dirs are skipped.
- L501 `test_nested_files(self, tmp_path, monkeypatch)` (method) — Files in subdirectories are included with correct relative paths.
- L514 `test_empty_cache(self, tmp_path, monkeypatch)` (method) — No cache dirs → empty list.
