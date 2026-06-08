---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_state_registry.py

Symbols in `tests/tools/test_file_state_registry.py`.

- L34 `_tmp_file(content: str='initial\n')` (function)
- L41 `FileStateRegistryUnitTests` (class) — Direct unit tests on the registry singleton.
- L44 `setUp(self)` (method)
- L48 `tearDown(self)` (method)
- L56 `_mk(self, content: str='x\n')` (method)
- L61 `test_record_read_then_check_stale_returns_none(self)` (method)
- L66 `test_sibling_write_flags_other_agent_as_stale(self)` (method)
- L77 `test_write_without_read_flagged(self)` (method)
- L84 `test_partial_read_flagged_on_write(self)` (method)
- L91 `test_external_mtime_drift_flagged(self)` (method)
- L103 `test_own_write_updates_stamp_so_next_write_is_clean(self)` (method)
- L110 `test_different_paths_dont_interfere(self)` (method)
- L118 `test_lock_path_serializes_same_path(self)` (method)
- L144 `test_lock_path_is_per_path_not_global(self)` (method)
- L166 `test_writes_since_filters_by_parent_read_set(self)` (method)
- L185 `test_writes_since_excludes_the_target_agent(self)` (method)
- L194 `test_kill_switch_env_var(self)` (method)
- L210 `FileToolsIntegrationTests` (class) — Integration through the real file_tools handlers.
- L217 `setUp(self)` (method)
- L221 `tearDown(self)` (method)
- L226 `_write_seed(self, name: str, content: str='seed\n')` (method)
- L232 `test_sibling_agent_write_surfaces_warning_through_handler(self)` (method)
- L247 `test_same_agent_consecutive_writes_no_false_warning(self)` (method)
- L255 `test_patch_tool_also_surfaces_sibling_warning(self)` (method)
- L278 `test_net_new_file_no_warning(self)` (method)
