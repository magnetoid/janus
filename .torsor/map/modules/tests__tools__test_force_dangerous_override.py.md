---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_force_dangerous_override.py

Symbols in `tests/tools/test_force_dangerous_override.py`.

- L9 `_old_should_allow(verdict, trust_level, force)` (function) — Simulate the BROKEN old logic.
- L35 `_new_should_allow(verdict, trust_level, force)` (function) — Simulate the FIXED logic.
- L57 `TestPolicyPrecedenceForDangerousVerdicts` (class)
- L58 `test_builtin_dangerous_is_allowed_by_policy(self)` (method)
- L61 `test_trusted_dangerous_is_blocked_without_force(self)` (method)
- L64 `test_force_overrides_dangerous_for_community(self)` (method)
- L67 `test_force_overrides_dangerous_for_trusted(self)` (method)
- L70 `test_force_still_overrides_caution(self)` (method)
- L73 `test_caution_community_blocked_without_force(self)` (method)
- L76 `test_safe_always_allowed(self)` (method)
- L80 `test_old_code_happened_to_allow_forced_dangerous_community(self)` (method)
