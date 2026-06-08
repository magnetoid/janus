---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_osv_check.py

Symbols in `tests/tools/test_osv_check.py`.

- L17 `TestInferEcosystem` (class)
- L18 `test_npx(self)` (method)
- L22 `test_uvx(self)` (method)
- L26 `test_pipx(self)` (method)
- L29 `test_unknown(self)` (method)
- L35 `TestParseNpmPackage` (class)
- L36 `test_simple(self)` (method)
- L39 `test_with_version(self)` (method)
- L42 `test_scoped(self)` (method)
- L47 `test_scoped_with_version(self)` (method)
- L50 `test_latest_ignored(self)` (method)
- L54 `TestParsePypiPackage` (class)
- L55 `test_simple(self)` (method)
- L58 `test_with_version(self)` (method)
- L61 `test_with_extras(self)` (method)
- L64 `test_extras_no_version(self)` (method)
- L68 `TestParsePackageFromArgs` (class)
- L69 `test_npm_skips_flags(self)` (method)
- L74 `test_pypi_skips_flags(self)` (method)
- L80 `test_empty_args(self)` (method)
- L83 `test_only_flags(self)` (method)
- L86 `test_package_equals_form(self)` (method)
- L95 `test_package_space_form(self)` (method)
- L103 `test_short_p_form(self)` (method)
- L111 `test_plain_positional_still_works(self)` (method)
- L118 `TestCheckPackageForMalware` (class)
- L119 `test_clean_package(self)` (method) — Clean package returns None (allow).
- L130 `test_malware_blocked(self)` (method) — Known malware package returns error string.
- L149 `test_network_error_fails_open(self)` (method) — Network errors allow the package (fail-open).
- L155 `test_non_npx_skipped(self)` (method) — Non-npx/uvx commands are skipped entirely.
- L160 `test_uvx_pypi(self)` (method) — uvx commands check PyPI ecosystem.
- L175 `TestLiveOsvQuery` (class) — Live integration test against the real OSV API. Skipped if offline.
- L182 `test_known_malware_package(self)` (method) — node-hide-console-windows has a real MAL- advisory.
- L195 `test_clean_package(self)` (method) — react should have zero MAL- advisories.
