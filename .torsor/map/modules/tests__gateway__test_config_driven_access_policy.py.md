---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_config_driven_access_policy.py

Symbols in `tests/gateway/test_config_driven_access_policy.py`.

- L42 `_clear_auth_env(monkeypatch)` (function)
- L62 `_make_runner(platform: Platform, config: GatewayConfig, *, enforces: bool)` (function) — Build a bare GatewayRunner with one adapter for *platform*.
- L80 `_source(platform: Platform, *, chat_type: str='dm')` (function)
- L95 `test_base_adapter_defaults_to_not_owning_access_policy()` (function) — Adapters that don't override the property delegate to the gateway.
- L113 `test_own_policy_adapters_declare_the_flag(module_path, class_name)` (function) — The config-policy adapters override the flag to True.
- L131 `test_own_policy_platform_authorized_without_env_allowlist(monkeypatch, platform)` (function) — A message reaching the gateway from an own-policy adapter is trusted.
- L147 `test_own_policy_platform_authorized_for_group_chat(monkeypatch, platform)` (function) — Group traffic from an own-policy adapter is trusted the same way.
- L158 `test_non_owning_platform_still_default_denies(monkeypatch)` (function) — Adapters that don't own their policy keep the env-only default-deny.
- L169 `test_env_allowlist_still_takes_precedence_for_own_policy_platform(monkeypatch)` (function) — When an env allowlist IS set, it governs — adapter trust is a fallback.
- L195 `test_unknown_adapter_does_not_crash_trust_check(monkeypatch)` (function) — No adapter registered for the platform → safe default-deny.
- L220 `test_pairing_dm_policy_not_blanket_authorized(monkeypatch, platform)` (function) — An unpaired sender in ``dm_policy: pairing`` is NOT authorized.
- L232 `test_pairing_dm_policy_authorizes_paired_user(monkeypatch)` (function) — Once approved in the pairing store, the sender authorizes normally.
- L244 `test_pairing_carveout_reads_adapter_when_env_set(monkeypatch)` (function) — Env-only ``WECOM_DM_POLICY=pairing`` (absent from config.extra) is honored.
- L261 `test_pairing_dm_policy_group_chat_still_trusted(monkeypatch)` (function) — Pairing is DM-only — group traffic keeps the adapter-trust path.
- L289 `test_unauthorized_dm_behavior_follows_config_dm_policy(monkeypatch, dm_policy, expected)` (function) — A restrictive dm_policy drops unauthorized DMs; pairing opts back in.
- L300 `test_unauthorized_dm_behavior_open_policy_keeps_default(monkeypatch)` (function) — ``dm_policy: open`` is not restrictive → falls through to the default.
