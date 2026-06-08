---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_lazy_deps.py

Symbols in `tests/tools/test_lazy_deps.py`.

- L26 `TestSpecSafety` (class)
- L40 `test_safe_specs_pass(self, spec)` (method)
- L67 `test_unsafe_specs_rejected(self, spec)` (method)
- L77 `TestAllowlist` (class)
- L78 `test_unknown_feature_raises(self, monkeypatch)` (method)
- L83 `test_lazy_deps_keys_use_namespace_dot_name(self)` (method)
- L89 `test_every_lazy_dep_spec_passes_safety(self)` (method)
- L97 `test_feature_install_command_returns_pip_invocation(self)` (method)
- L103 `test_feature_install_command_unknown(self)` (method)
- L112 `TestSecurityGating` (class)
- L113 `test_disabled_via_config_raises(self, monkeypatch)` (method)
- L121 `test_disabled_via_env_var(self, monkeypatch)` (method)
- L130 `test_default_allows(self, monkeypatch)` (method)
- L138 `test_config_failure_fails_open(self, monkeypatch)` (method)
- L154 `TestEnsure` (class)
- L155 `test_already_satisfied_is_noop(self, monkeypatch)` (method)
- L166 `test_install_success_path(self, monkeypatch)` (method)
- L183 `test_install_failure_surfaces_pip_stderr(self, monkeypatch)` (method)
- L196 `test_install_succeeds_but_still_missing_raises(self, monkeypatch)` (method)
- L215 `TestIsAvailable` (class)
- L216 `test_unknown_feature_returns_false(self)` (method)
- L219 `test_satisfied_returns_true(self, monkeypatch)` (method)
- L224 `test_missing_returns_false(self, monkeypatch)` (method)
- L241 `TestIsSatisfiedVersionAware` (class)
- L242 `_fake_version(self, monkeypatch, installed_versions: dict)` (method) — Patch importlib.metadata.version() inside lazy_deps.
- L255 `test_exact_pin_match_returns_true(self, monkeypatch)` (method)
- L259 `test_exact_pin_mismatch_returns_false(self, monkeypatch)` (method)
- L264 `test_range_within_returns_true(self, monkeypatch)` (method)
- L268 `test_range_above_returns_false(self, monkeypatch)` (method)
- L273 `test_range_below_returns_false(self, monkeypatch)` (method)
- L277 `test_package_not_installed_returns_false(self, monkeypatch)` (method)
- L281 `test_bare_package_name_presence_is_enough(self, monkeypatch)` (method)
- L286 `test_extras_block_in_spec_is_stripped(self, monkeypatch)` (method)
- L292 `test_extras_block_mismatch_returns_false(self, monkeypatch)` (method)
- L302 `TestActiveFeatures` (class)
- L303 `test_no_packages_installed_returns_empty(self, monkeypatch)` (method)
- L307 `test_finds_features_with_at_least_one_package_installed(self, monkeypatch)` (method)
- L319 `test_multi_package_feature_active_if_any_present(self, monkeypatch)` (method)
- L330 `TestRefreshActiveFeatures` (class)
- L331 `test_no_active_features_returns_empty(self, monkeypatch)` (method)
- L335 `test_already_current_is_noop(self, monkeypatch)` (method)
- L347 `test_stale_pin_triggers_reinstall(self, monkeypatch)` (method)
- L362 `test_install_failure_recorded_not_raised(self, monkeypatch)` (method)
- L379 `test_lazy_installs_disabled_marked_skipped(self, monkeypatch)` (method)
- L390 `test_mixed_results_returns_per_feature_status(self, monkeypatch)` (method)
