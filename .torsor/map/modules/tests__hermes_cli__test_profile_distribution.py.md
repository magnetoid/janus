---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_profile_distribution.py

Symbols in `tests/hermes_cli/test_profile_distribution.py`.

- L43 `profile_env(tmp_path, monkeypatch)` (function)
- L51 `_make_staging_dir(root: Path, name: str='src', *, manifest: DistributionManifest=None)` (function) — Build a local distribution staging directory (what a git clone would
- L76 `_symlink_file_or_skip(link: Path, target: Path)` (function)
- L88 `TestManifestParsing` (class)
- L90 `test_minimal_manifest(self, tmp_path)` (method)
- L98 `test_full_manifest(self, tmp_path)` (method)
- L128 `test_missing_name_rejected(self, tmp_path)` (method)
- L133 `test_env_requires_not_list_rejected(self, tmp_path)` (method)
- L140 `test_read_manifest_returns_none_when_absent(self, tmp_path)` (method)
- L143 `test_owned_paths_default(self)` (method)
- L147 `test_owned_paths_explicit(self)` (method)
- L151 `test_roundtrip_write_read(self, tmp_path)` (method)
- L169 `TestVersionRequires` (class)
- L186 `test_check_matrix(self, spec, cur, ok)` (method)
- L193 `test_parse_semver_handles_prerelease(self)` (method)
- L197 `test_parse_semver_pads(self)` (method)
- L201 `test_parse_semver_rejects_garbage(self)` (method)
- L211 `TestEnvTemplate` (class)
- L213 `test_required_is_uncommented(self)` (method)
- L225 `test_optional_is_commented(self)` (method)
- L234 `test_empty_env_requires_is_header_only(self)` (method)
- L246 `TestLooksLikeGitUrl` (class)
- L257 `test_accepts_git_sources(self, src)` (method)
- L266 `test_rejects_non_git(self, src)` (method)
- L275 `TestInstall` (class)
- L277 `test_install_from_directory(self, profile_env)` (method)
- L289 `test_install_uses_manifest_name_when_no_override(self, profile_env)` (method)
- L296 `test_install_rejects_existing_without_force(self, profile_env)` (method)
- L302 `test_install_with_force_overwrites(self, profile_env)` (method)
- L309 `test_install_rejects_default_name(self, profile_env)` (method)
- L314 `test_install_rejects_non_distribution_directory(self, profile_env, tmp_path)` (method)
- L321 `test_install_rejects_unknown_source(self, profile_env, tmp_path)` (method)
- L325 `test_install_emits_env_example_when_manifest_has_env(self, profile_env)` (method)
- L337 `test_install_enforces_hermes_requires(self, profile_env, monkeypatch)` (method)
- L357 `TestUpdate` (class)
- L359 `test_update_preserves_user_data(self, profile_env)` (method)
- L386 `test_update_preserves_config_by_default(self, profile_env)` (method)
- L402 `test_update_force_config_overwrites(self, profile_env)` (method)
- L414 `test_update_missing_manifest_errors(self, profile_env)` (method)
- L427 `TestDescribe` (class)
- L429 `test_describe_existing_distribution(self, profile_env)` (method)
- L443 `test_describe_non_distribution_returns_empty(self, profile_env)` (method)
- L448 `test_describe_missing_profile_raises(self, profile_env)` (method)
- L458 `TestSecurity` (class)
- L460 `test_user_owned_exclude_covers_credentials(self)` (method)
- L467 `test_install_does_not_import_credentials_from_staging(self, profile_env)` (method) — If an author accidentally ships auth.json or .env in their
- L482 `test_install_rejects_symlinked_distribution_files(self, profile_env, tmp_path)` (method) — Distribution install must not follow symlinks to local files.
- L505 `TestInstalledAtStamp` (class)
- L507 `test_install_stamps_installed_at(self, profile_env)` (method)
- L517 `test_update_refreshes_installed_at(self, profile_env, monkeypatch)` (method)
- L547 `TestProfileInfoDistribution` (class)
- L549 `test_installed_distribution_shows_in_list(self, profile_env)` (method)
- L564 `test_plain_profile_has_no_distribution_fields(self, profile_env)` (method)
- L571 `test_malformed_manifest_does_not_break_list(self, profile_env)` (method)
- L589 `TestErrorSurfaces` (class)
- L591 `test_bad_profile_name_raises_valueerror_not_traceback(self, profile_env, tmp_path)` (method) — A manifest whose 'name' can't be used as a profile identifier
- L602 `test_path_traversal_name_rejected(self, profile_env, tmp_path)` (method)
