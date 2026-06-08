---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_budget_config.py

Symbols in `tests/tools/test_budget_config.py`.

- L29 `TestModuleConstants` (class) — Verify documented default values haven't drifted.
- L32 `test_default_result_size(self)` (method)
- L35 `test_default_turn_budget(self)` (method)
- L38 `test_default_preview_size(self)` (method)
- L42 `TestPinnedThresholds` (class) — PINNED_THRESHOLDS – tools whose values must never be overridden.
- L45 `test_read_file_is_inf(self)` (method)
- L49 `test_pinned_is_not_empty(self)` (method)
- L58 `TestBudgetConfigDefaults` (class) — BudgetConfig() should match the module-level defaults exactly.
- L61 `test_default_result_size(self)` (method)
- L65 `test_default_turn_budget(self)` (method)
- L69 `test_default_preview_size(self)` (method)
- L73 `test_default_tool_overrides_empty(self)` (method)
- L77 `test_default_budget_singleton_matches(self)` (method) — DEFAULT_BUDGET should equal a freshly constructed BudgetConfig.
- L87 `TestBudgetConfigFrozen` (class) — Frozen dataclass must reject attribute mutation.
- L90 `test_cannot_set_default_result_size(self)` (method)
- L95 `test_cannot_set_turn_budget(self)` (method)
- L100 `test_cannot_set_preview_size(self)` (method)
- L105 `test_cannot_set_tool_overrides(self)` (method)
- L116 `TestBudgetConfigCustom` (class) — BudgetConfig can be created with non-default values.
- L119 `test_custom_values(self)` (method)
- L137 `TestResolveThreshold` (class) — Priority: pinned > tool_overrides > registry > default.
- L140 `test_pinned_wins_over_override(self)` (method) — Even if tool_overrides contains read_file, pinned value wins.
- L146 `test_tool_override_wins_over_default(self)` (method) — tool_overrides should be returned before falling back to registry.
- L153 `test_falls_back_to_registry(self, mock_registry)` (method) — When not pinned and not in overrides, delegate to registry.
- L164 `test_registry_receives_custom_default(self, mock_registry)` (method) — Custom default_result_size flows through to registry call.
- L173 `test_pinned_read_file_returns_inf(self)` (method) — Canonical case: read_file must always return inf.
