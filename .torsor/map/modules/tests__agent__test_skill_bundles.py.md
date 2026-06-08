---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_skill_bundles.py

Symbols in `tests/agent/test_skill_bundles.py`.

- L22 `_make_bundle_yaml(bundles_dir: Path, slug: str, skills: list[str], description: str='', instruction: str='', name: str | None=None)` (function)
- L46 `_make_skill(skills_dir: Path, name: str, body: str='Do the thing.')` (function)
- L56 `bundles_env(tmp_path, monkeypatch)` (function) — Isolated bundles dir + skills dir.
- L72 `TestSlugify` (class)
- L73 `test_basic(self)` (method)
- L76 `test_underscores(self)` (method)
- L79 `test_strips_invalid_chars(self)` (method)
- L82 `test_collapses_hyphens(self)` (method)
- L85 `test_empty(self)` (method)
- L90 `TestScanBundles` (class)
- L91 `test_empty_dir(self, bundles_env)` (method)
- L96 `test_finds_bundle(self, bundles_env)` (method)
- L104 `test_skips_invalid_yaml(self, bundles_env)` (method)
- L113 `test_skips_bundle_without_skills(self, bundles_env)` (method)
- L120 `test_duplicate_slug_first_wins(self, bundles_env)` (method)
- L132 `test_uses_filename_as_fallback_name(self, bundles_env)` (method)
- L141 `TestGetSkillBundles` (class)
- L142 `test_returns_cache(self, bundles_env)` (method)
- L150 `test_rescans_on_change(self, bundles_env)` (method)
- L164 `TestResolveBundleCommandKey` (class)
- L165 `test_exact_match(self, bundles_env)` (method)
- L171 `test_underscore_alias(self, bundles_env)` (method) — Telegram converts hyphens to underscores in command names.
- L178 `test_unknown(self, bundles_env)` (method)
- L182 `test_empty(self, bundles_env)` (method)
- L186 `TestBuildBundleInvocationMessage` (class)
- L187 `test_loads_all_skills(self, bundles_env)` (method)
- L203 `test_skips_missing_skills(self, bundles_env)` (method)
- L216 `test_unknown_bundle_returns_none(self, bundles_env)` (method)
- L220 `test_no_loadable_skills_returns_none(self, bundles_env)` (method)
- L227 `test_includes_user_instruction(self, bundles_env)` (method)
- L239 `test_includes_bundle_instruction(self, bundles_env)` (method)
- L252 `test_dedupes_skills(self, bundles_env)` (method)
- L263 `TestSaveAndDeleteBundle` (class)
- L264 `test_save_creates_file(self, bundles_env)` (method)
- L275 `test_save_refuses_overwrite_by_default(self, bundles_env)` (method)
- L280 `test_save_overwrites_with_force(self, bundles_env)` (method)
- L287 `test_save_requires_skills(self, bundles_env)` (method)
- L291 `test_save_requires_name(self, bundles_env)` (method)
- L295 `test_delete_removes_file(self, bundles_env)` (method)
- L302 `test_delete_missing_raises(self, bundles_env)` (method)
- L307 `TestReloadBundles` (class)
- L308 `test_reports_added_and_removed(self, bundles_env)` (method)
- L327 `TestListBundles` (class)
- L328 `test_sorted_by_slug(self, bundles_env)` (method)
