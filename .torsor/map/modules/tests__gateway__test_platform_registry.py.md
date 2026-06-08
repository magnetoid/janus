---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_platform_registry.py

Symbols in `tests/gateway/test_platform_registry.py`.

- L14 `TestPlatformEnumDynamic` (class) — Test that Platform enum accepts unknown values for plugin platforms.
- L17 `test_builtin_members_still_work(self)` (method)
- L21 `test_dynamic_member_created(self)` (method)
- L26 `test_dynamic_member_identity_stable(self)` (method) — Same value returns same object (cached).
- L32 `test_dynamic_member_case_normalised(self)` (method) — Mixed case normalised to lowercase.
- L39 `test_dynamic_member_with_hyphens(self)` (method) — Registered plugin platforms with hyphens work once registered.
- L58 `test_dynamic_member_rejects_unregistered(self)` (method) — Arbitrary strings are rejected to prevent enum pollution.
- L63 `test_dynamic_member_rejects_non_string(self)` (method)
- L67 `test_dynamic_member_rejects_empty(self)` (method)
- L71 `test_dynamic_member_rejects_whitespace_only(self)` (method)
- L79 `TestPlatformRegistry` (class) — Test the PlatformRegistry itself.
- L82 `_make_entry(self, name='test', check_ok=True, validate_ok=True, factory_ok=True)` (method)
- L94 `test_register_and_get(self)` (method)
- L101 `test_get_unknown_returns_none(self)` (method)
- L105 `test_unregister(self)` (method)
- L113 `test_create_adapter_success(self)` (method)
- L120 `test_create_adapter_unknown_name(self)` (method)
- L124 `test_create_adapter_check_fails(self)` (method)
- L130 `test_create_adapter_validate_fails(self)` (method)
- L136 `test_create_adapter_factory_exception(self)` (method)
- L150 `test_create_adapter_no_validate(self)` (method) — When validate_config is None, skip validation.
- L165 `test_all_entries(self)` (method)
- L174 `test_plugin_entries(self)` (method)
- L189 `test_re_register_replaces(self)` (method)
- L207 `TestGatewayConfigPluginPlatform` (class) — Test that GatewayConfig parses and validates plugin platforms.
- L210 `test_from_dict_accepts_plugin_platform(self)` (method)
- L222 `test_get_connected_platforms_includes_registered_plugin(self)` (method) — Plugin platform with registry entry passes get_connected_platforms.
- L249 `test_get_connected_platforms_excludes_unregistered_plugin(self)` (method) — Plugin platform without registry entry is excluded.
- L261 `test_get_connected_platforms_excludes_invalid_config(self)` (method) — Plugin platform with failing validate_config is excluded.
- L291 `TestPlatformEntryExtendedFields` (class) — Test the auth, message length, and display fields on PlatformEntry.
- L294 `test_default_field_values(self)` (method)
- L308 `test_custom_auth_fields(self)` (method)
- L329 `TestCronPlatformResolution` (class) — Test that cron delivery accepts plugin platform names.
- L332 `test_builtin_platform_resolves(self)` (method) — Built-in platform names resolve via Platform() call.
- L337 `test_plugin_platform_resolves(self)` (method) — Plugin platform names create dynamic enum members.
- L342 `test_invalid_platform_type_rejected(self)` (method) — Non-string values are still rejected.
- L351 `TestPlatformsMerge` (class) — Test get_all_platforms() merges with registry.
- L354 `test_get_all_platforms_includes_builtins(self)` (method)
- L360 `test_get_all_platforms_includes_plugin(self)` (method)
- L379 `test_platform_label_plugin_fallback(self)` (method)
- L401 `TestApplyYamlConfigFnField` (class) — The hook field itself — defaults, custom values, signature.
- L404 `test_default_is_none(self)` (method)
- L413 `test_accepts_callable(self)` (method)
- L429 `TestApplyYamlConfigFnDispatch` (class) — End-to-end dispatch through load_gateway_config().
- L437 `_write_config(self, tmp_path, content: str)` (method)
- L443 `_register_hook(self, name, hook_fn)` (method)
- L457 `test_hook_can_mutate_environ(self, tmp_path, monkeypatch)` (method) — A hook that mutates os.environ has its env vars set after load.
- L482 `test_hook_returned_dict_merges_into_extra(self, tmp_path, monkeypatch)` (method) — A hook that returns a dict has it merged into PlatformConfig.extra.
- L507 `test_hook_receives_full_yaml_and_platform_subdict(self, tmp_path, monkeypatch)` (method) — Hook receives both the full yaml_cfg and its own platform sub-dict.
- L536 `test_hook_exception_swallowed(self, tmp_path, monkeypatch)` (method) — A misbehaving hook never aborts load_gateway_config().
- L584 `test_hook_skipped_when_platform_section_missing(self, tmp_path, monkeypatch)` (method) — Hook is NOT called when the platform's YAML section is absent.
- L606 `test_hook_skipped_when_platform_section_not_dict(self, tmp_path, monkeypatch)` (method) — Hook is NOT called when the platform's YAML section isn't a dict.
- L630 `test_env_var_takes_precedence_when_hook_uses_getenv_guard(self, tmp_path, monkeypatch)` (method) — The standard `not os.getenv(...)` guard preserves env > YAML.
- L659 `TestPluginPlatformSharedKeyBridge` (class) — Plugin-registered platforms get the same shared-key bridging as built-ins.
- L669 `_write_config(self, tmp_path, content: str)` (method)
- L675 `test_shared_keys_bridged_for_plugin_platform(self, tmp_path, monkeypatch)` (method) — A plugin platform's ``require_mention``/``dm_policy``/etc. flow into
- L712 `TestPluginEnablementGate` (class) — Plugin platforms must NOT auto-enable on check_fn alone (#31116).
- L724 `_write_config(self, tmp_path, content: str='')` (method)
- L730 `test_plugin_with_is_connected_false_is_NOT_enabled(self, tmp_path, monkeypatch)` (method) — check_fn=True + is_connected=False must NOT enable the platform.
- L766 `test_plugin_with_is_connected_true_is_enabled(self, tmp_path, monkeypatch)` (method) — check_fn=True + is_connected=True still enables the platform.
- L793 `test_plugin_without_is_connected_falls_back_to_check_fn(self, tmp_path, monkeypatch)` (method) — Legacy plugins that don't register is_connected keep working.
- L825 `test_is_connected_raises_does_not_enable(self, tmp_path, monkeypatch)` (method) — A buggy is_connected must not silently enable the platform.
- L858 `test_yaml_enabled_true_overrides_is_connected_false(self, tmp_path, monkeypatch)` (method) — Explicit YAML ``enabled: true`` wins over is_connected=False.
- L898 `test_is_connected_sees_env_seeded_extras(self, tmp_path, monkeypatch)` (method) — ``env_enablement_fn`` extras must be visible to ``is_connected``.
- L952 `test_is_connected_failed_gate_does_not_leak_extras(self, tmp_path, monkeypatch)` (method) — When the gate rejects, env-seeded extras must NOT leak onto
