---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/profile_distribution.py

Symbols in `hermes_cli/profile_distribution.py`.

- L127 `DistributionError` (class) — Raised for distribution install/update failures.
- L137 `EnvRequirement` (class)
- L144 `from_dict(cls, data: Any)` (method)
- L159 `to_dict(self)` (method)
- L169 `DistributionManifest` (class)
- L186 `from_dict(cls, data: Any)` (method)
- L215 `to_dict(self)` (method)
- L238 `owned_paths(self)` (method) — Resolve which paths count as distribution-owned.
- L245 `_load_yaml(text: str)` (function)
- L253 `_dump_yaml(data: Any)` (function)
- L259 `read_manifest(profile_dir: Path)` (function) — Return the manifest for *profile_dir*, or None if it isn't a distribution.
- L271 `write_manifest(profile_dir: Path, manifest: DistributionManifest)` (function)
- L285 `_parse_semver(v: str)` (function) — Very small semver parser — major.minor.patch only.  Extra labels stripped.
- L299 `check_hermes_requires(spec: str, current_version: str)` (function) — Raise DistributionError if ``current_version`` does not satisfy ``spec``.
- L335 `_env_template_from_manifest(manifest: DistributionManifest)` (function) — Generate a ``.env.template`` body from env_requires.
- L359 `_looks_like_git_url(s: str)` (function)
- L375 `_git_clone(url: str, dest: Path)` (function)
- L392 `_stage_source(source: str, workdir: Path)` (function) — Resolve *source* to a local directory containing distribution.yaml.
- L435 `_reject_distribution_symlinks(staged: Path)` (function) — Reject symlinks before reading or copying distribution files.
- L455 `InstallPlan` (class) — Summary of what an install will do, surfaced for user confirmation.
- L467 `_has_cron_jobs(staged: Path)` (function)
- L478 `_count_skills(staged: Path)` (function)
- L487 `plan_install(source: str, workdir: Path, override_name: Optional[str]=None)` (function) — Stage *source* and produce a plan describing what install would do.
- L545 `_copy_dist_payload(staged: Path, target: Path, manifest: DistributionManifest, preserve_config: bool)` (function) — Copy distribution-owned files from *staged* into *target*.
- L594 `_bootstrap_user_dirs(target: Path)` (function) — Create the bootstrap dirs a fresh profile expects.
- L601 `install_distribution(source: str, name: Optional[str]=None, force: bool=False, create_alias: bool=False)` (function) — Install a distribution from *source* into a new profile.
- L644 `update_distribution(profile_name: str, force_config: bool=False)` (function) — Re-pull the distribution for an existing profile and apply updates.
- L701 `describe_distribution(profile_name: str)` (function) — Return a structured view of a profile's distribution metadata.
