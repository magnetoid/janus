---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/test_security_guidance_plugin.py

Symbols in `tests/plugins/test_security_guidance_plugin.py`.

- L28 `_isolate_env(tmp_path, monkeypatch)` (function)
- L41 `_repo_root()` (function)
- L45 `_load_patterns()` (function) — Import patterns.py in isolation (no plugin glue).
- L56 `_load_plugin_init()` (function) — Import the plugin __init__.py with patterns.py as a sibling.
- L80 `TestPatternsData` (class)
- L81 `test_has_at_least_one_rule(self)` (method)
- L85 `test_every_rule_has_required_fields(self)` (method)
- L94 `test_rule_names_are_unique(self)` (method)
- L99 `test_rule_id_enum_in_sync(self)` (method)
- L107 `test_rule_names_to_mask_packs_bits(self)` (method)
- L119 `TestScanContent` (class)
- L120 `test_pickle_load_in_py_warns(self)` (method)
- L128 `test_pickle_load_in_md_skipped_by_path_filter(self)` (method)
- L135 `test_method_call_eval_does_not_trip(self)` (method) — model.eval() / redis.eval() / spec.eval() must not match eval_injection.
- L141 `test_bare_eval_in_py_warns(self)` (method)
- L146 `test_subprocess_shell_true_warns(self)` (method)
- L153 `test_dangerously_set_inner_html_warns(self)` (method)
- L160 `test_github_workflow_path_check_fires_on_path_alone(self)` (method) — github_actions_workflow has no regex/substring — fires on path.
- L168 `test_non_workflow_path_doesnt_trip_workflow_rule(self)` (method)
- L173 `test_empty_content_returns_no_findings(self)` (method)
- L177 `test_huge_content_skipped(self)` (method)
- L189 `TestTransformToolResultHook` (class)
- L190 `test_warns_on_write_file_with_dangerous_content(self)` (method)
- L207 `test_no_warn_on_clean_content(self)` (method)
- L217 `test_no_warn_when_result_is_error(self)` (method)
- L229 `test_patch_tool_new_string_scanned(self)` (method)
- L242 `test_untargeted_tool_skipped(self)` (method)
- L254 `test_disable_kill_switch(self, monkeypatch)` (method)
- L265 `test_block_mode_makes_transform_hook_quiet(self, monkeypatch)` (method) — In block mode, pre_tool_call handles the warning; the transform
- L279 `TestPreToolCallHook` (class)
- L280 `test_no_block_in_warn_mode(self)` (method)
- L285 `test_blocks_in_block_mode_on_dangerous_pattern(self, monkeypatch)` (method)
- L295 `test_no_block_in_block_mode_on_clean_content(self, monkeypatch)` (method)
- L301 `test_untargeted_tool_skipped(self, monkeypatch)` (method)
- L312 `TestPluginDiscovery` (class)
- L313 `test_loads_via_plugin_manager(self, _isolate_env, monkeypatch)` (method) — End-to-end: enable in config.yaml and verify the PluginManager
