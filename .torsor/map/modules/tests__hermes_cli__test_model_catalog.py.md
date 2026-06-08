---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_catalog.py

Symbols in `tests/hermes_cli/test_model_catalog.py`.

- L15 `isolated_home(tmp_path, monkeypatch)` (function) — Isolate HERMES_HOME + reset any module-level catalog cache per test.
- L30 `_valid_manifest()` (function)
- L55 `TestValidation` (class)
- L56 `test_accepts_well_formed_manifest(self, isolated_home)` (method)
- L60 `test_rejects_non_dict(self, isolated_home)` (method)
- L66 `test_rejects_missing_version(self, isolated_home)` (method)
- L72 `test_rejects_future_version(self, isolated_home)` (method)
- L78 `test_rejects_missing_providers(self, isolated_home)` (method)
- L84 `test_rejects_malformed_model_entry(self, isolated_home)` (method)
- L90 `test_rejects_non_string_model_id(self, isolated_home)` (method)
- L97 `TestFetchSuccess` (class)
- L98 `test_fetch_and_cache_writes_disk(self, isolated_home)` (method)
- L114 `test_second_call_uses_in_process_cache(self, isolated_home)` (method)
- L124 `test_force_refresh_always_refetches(self, isolated_home)` (method)
- L135 `TestFetchFailure` (class)
- L136 `test_network_failure_returns_empty_when_no_cache(self, isolated_home)` (method)
- L142 `test_network_failure_falls_back_to_disk_cache(self, isolated_home)` (method)
- L156 `test_fetch_failure_falls_back_to_stale_cache(self, isolated_home)` (method)
- L175 `TestFallbackChain` (class) — ``_fetch_manifest_with_fallback`` walks ``DEFAULT_CATALOG_FALLBACK_URLS``
- L189 `test_uses_primary_when_it_succeeds(self, isolated_home)` (method)
- L203 `test_falls_through_to_raw_github_on_primary_failure(self, isolated_home)` (method)
- L219 `test_returns_none_when_all_urls_fail(self, isolated_home)` (method)
- L229 `test_dedupes_when_primary_equals_fallback(self, isolated_home)` (method) — Operator who configured ``model_catalog.url`` to the raw GitHub URL
- L239 `test_get_catalog_uses_fallback_chain(self, isolated_home)` (method) — End-to-end: ``get_catalog`` routes through the fallback helper so
- L259 `TestCuratedAccessors` (class)
- L260 `test_openrouter_returns_tuples(self, isolated_home)` (method)
- L272 `test_nous_returns_ids(self, isolated_home)` (method)
- L280 `test_openrouter_returns_none_when_catalog_empty(self, isolated_home)` (method)
- L285 `test_nous_returns_none_when_catalog_empty(self, isolated_home)` (method)
- L291 `TestDisabled` (class)
- L292 `test_disabled_config_short_circuits(self, isolated_home)` (method)
- L310 `TestProviderOverride` (class)
- L311 `test_override_url_takes_precedence(self, isolated_home)` (method)
- L346 `TestIntegrationWithModelsModule` (class) — Exercise the fallback paths via the real callers in hermes_cli.models.
- L349 `test_curated_nous_ids_falls_back_to_hardcoded_on_empty_catalog(self, isolated_home)` (method)
- L360 `test_curated_nous_ids_prefers_manifest(self, isolated_home)` (method)
- L371 `test_picker_nous_row_uses_curated_list(self, tmp_path, monkeypatch)` (method) — The /model picker surfaces the curated ``_PROVIDER_MODELS["nous"]``
- L439 `TestManifestMatchesInRepoLists` (class) — Fail if the on-disk manifest is out of date relative to in-repo lists.
- L443 `_strip_volatile(catalog: dict)` (method) — Drop fields that always change (timestamps) for diff comparison.
- L449 `test_in_repo_lists_match_manifest(self)` (method) — ``scripts/build_model_catalog.py`` output must match the committed file.
