---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_plugin_skills.py

Symbols in `tests/test_plugin_skills.py`.

- L18 `TestParseQualifiedName` (class)
- L19 `test_with_colon(self)` (method)
- L26 `test_without_colon(self)` (method)
- L33 `test_multiple_colons_splits_on_first(self)` (method)
- L40 `test_empty_string(self)` (method)
- L48 `TestIsValidNamespace` (class)
- L49 `test_valid(self)` (method)
- L57 `test_invalid(self)` (method)
- L70 `TestPluginSkillRegistry` (class)
- L72 `pm(self, monkeypatch)` (method)
- L80 `test_register_and_find(self, pm, tmp_path)` (method)
- L95 `test_list_plugin_skills(self, pm, tmp_path)` (method)
- L107 `test_remove_plugin_skill(self, pm, tmp_path)` (method)
- L119 `TestPluginContextRegisterSkill` (class)
- L121 `ctx(self, tmp_path, monkeypatch)` (method)
- L135 `test_happy_path(self, ctx, tmp_path)` (method)
- L143 `test_rejects_colon_in_name(self, ctx, tmp_path)` (method)
- L149 `test_rejects_invalid_chars(self, ctx, tmp_path)` (method)
- L155 `test_rejects_missing_file(self, ctx, tmp_path)` (method)
- L163 `TestSkillViewQualifiedName` (class)
- L165 `_isolate(self, tmp_path, monkeypatch)` (method) — Fresh plugin manager + empty SKILLS_DIR for each test.
- L178 `_register_skill(self, tmp_path, plugin='superpowers', name='writing-plans', content=None)` (method)
- L188 `test_resolves_plugin_skill(self, tmp_path)` (method)
- L198 `test_invalid_namespace_returns_error(self, tmp_path)` (method)
- L205 `test_empty_namespace_returns_error(self, tmp_path)` (method)
- L212 `test_bare_name_still_uses_flat_tree(self, tmp_path, monkeypatch)` (method)
- L224 `test_plugin_exists_but_skill_missing(self, tmp_path)` (method)
- L234 `test_plugin_not_found_falls_through(self, tmp_path)` (method)
- L241 `test_category_qualified_local_skill_falls_through(self, tmp_path, monkeypatch)` (method)
- L258 `test_stale_entry_self_heals(self, tmp_path)` (method)
- L270 `TestSkillViewPluginGuards` (class)
- L272 `_isolate(self, tmp_path, monkeypatch)` (method)
- L286 `_reg(self, tmp_path, content, plugin='myplugin', name='foo')` (method)
- L295 `test_disabled_plugin(self, tmp_path, monkeypatch)` (method)
- L305 `test_platform_mismatch(self, tmp_path)` (method)
- L315 `test_injection_logged_but_served(self, tmp_path, caplog)` (method)
- L329 `TestBundleContextBanner` (class)
- L331 `_isolate(self, tmp_path, monkeypatch)` (method)
- L342 `_setup_bundle(self, tmp_path, skills=('foo', 'bar', 'baz'))` (method)
- L352 `test_banner_present(self, tmp_path)` (method)
- L359 `test_banner_lists_siblings_not_self(self, tmp_path)` (method)
- L374 `test_single_skill_no_sibling_line(self, tmp_path)` (method)
- L382 `test_original_content_preserved(self, tmp_path)` (method)
