---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/lazy_deps.py

Symbols in `tools/lazy_deps.py`.

- L197 `FeatureUnavailable` (class) — A lazily-installable feature is missing and cannot be made available.
- L204 `__init__(self, feature: str, missing: tuple[str, ...], reason: str)` (method)
- L210 `_format(self)` (method)
- L220 `_InstallResult` (class)
- L231 `_allow_lazy_installs()` (function) — Return the ``security.allow_lazy_installs`` config flag.
- L250 `_spec_is_safe(spec: str)` (function) — Reject pip specs that contain URLs, paths, or shell metacharacters.
- L261 `_pkg_name_from_spec(spec: str)` (function) — Extract the bare package name from a pip spec.
- L271 `_specifier_from_spec(spec: str)` (function) — Extract just the version-specifier portion of a pip spec.
- L285 `_is_satisfied(spec: str)` (function) — Is ``spec`` already satisfied in the current env?
- L329 `_is_present(spec: str)` (function) — Cheap presence-only check (package name installed at any version).
- L349 `_venv_pip_install(specs: tuple[str, ...], *, timeout: int=300)` (function) — Install ``specs`` into the active venv using uv → pip → ensurepip ladder.
- L411 `feature_specs(feature: str)` (function) — Return the registered specs for a feature, or raise KeyError.
- L418 `feature_missing(feature: str)` (function) — Return the subset of specs for ``feature`` not currently installed.
- L423 `ensure(feature: str, *, prompt: bool=True)` (function) — Make sure all packages for ``feature`` are importable.
- L523 `is_available(feature: str)` (function) — Return True if the feature's deps are already satisfied.
- L530 `feature_install_command(feature: str)` (function) — Return the ``pip install`` command a user could run manually, or None.
- L538 `active_features()` (function) — Return the list of features the user has ever lazy-installed.
- L555 `refresh_active_features(*, prompt: bool=False)` (function) — Re-run ``ensure`` for every feature the user has previously activated.
- L589 `ensure_and_bind(feature: str, importer: Callable[[], dict[str, Any]], target_globals: dict, *, prompt: bool=False)` (function) — Ensure a feature is installed, then rebind names into the caller's globals.
