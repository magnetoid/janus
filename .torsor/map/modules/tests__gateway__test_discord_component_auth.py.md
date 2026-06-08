---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_component_auth.py

Symbols in `tests/gateway/test_discord_component_auth.py`.

- L32 `_clear_component_auth_env(monkeypatch)` (function)
- L47 `_interaction(user_id, role_ids=None, *, drop_user=False, drop_roles=False)` (function) — Build a mock interaction with the requested user/role shape.
- L66 `test_component_check_empty_allowlists_rejects_by_default(monkeypatch)` (function) — Button interactions must fail closed without an allowlist or allow-all.
- L83 `test_component_check_explicit_allow_all_passes(monkeypatch, env_name, env_value)` (function)
- L92 `test_component_check_user_in_user_allowlist_passes()` (function)
- L97 `test_component_check_user_not_in_user_allowlist_rejected()` (function)
- L102 `test_component_check_user_in_global_allowlist_passes(monkeypatch)` (function)
- L108 `test_component_check_global_allowlist_without_match_rejects(monkeypatch)` (function)
- L114 `test_component_check_wildcard_user_allowlist_passes()` (function)
- L122 `test_component_check_role_only_user_with_matching_role_passes()` (function) — Role-only deployment (DISCORD_ALLOWED_ROLES set, DISCORD_ALLOWED_USERS
- L132 `test_component_check_accepts_role_allowlist_sequences()` (function)
- L137 `test_component_check_role_only_user_without_matching_role_rejected()` (function) — Role-only deployment where the user has no matching role: reject.
- L144 `test_component_check_user_or_role_user_match()` (function) — Both allowlists set; user matches user allowlist: pass.
- L150 `test_component_check_user_or_role_role_match()` (function) — Both allowlists set; user not in user list but in role list: pass.
- L156 `test_component_check_user_or_role_neither_match()` (function) — Both allowlists set; user matches neither: reject.
- L165 `test_component_check_role_policy_with_no_roles_attr_rejects()` (function) — Role allowlist configured but interaction.user has no .roles
- L173 `test_component_check_missing_user_with_allowlist_rejects()` (function) — interaction.user is None with any allowlist configured: fail
- L187 `test_exec_approval_view_accepts_role_allowlist()` (function)
- L199 `test_exec_approval_view_role_default_is_empty_set()` (function) — Existing call sites that pass only allowed_user_ids must continue
- L208 `test_slash_confirm_view_accepts_role_allowlist()` (function)
- L219 `test_update_prompt_view_accepts_role_allowlist()` (function)
- L229 `test_model_picker_view_accepts_role_allowlist()` (function)
- L246 `test_clarify_choice_view_accepts_role_allowlist()` (function)
- L275 `test_views_empty_allowlists_reject_by_default(view_factory, monkeypatch)` (function)
- L283 `test_model_picker_view_empty_allowlists_reject_by_default(monkeypatch)` (function)
- L303 `test_view_empty_allowlists_allow_with_explicit_allow_all(monkeypatch)` (function)
