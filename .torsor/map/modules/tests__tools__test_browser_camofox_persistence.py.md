---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_camofox_persistence.py

Symbols in `tests/tools/test_browser_camofox_persistence.py`.

- L26 `_mock_response(status=200, json_data=None)` (function)
- L34 `_enable_persistence()` (function) — Return a patch context that enables managed persistence via config.
- L41 `_clear_session_state()` (function)
- L50 `TestManagedPersistenceToggle` (class)
- L51 `test_disabled_by_default(self)` (method)
- L56 `test_enabled_via_config_yaml(self)` (method)
- L61 `test_disabled_when_key_missing(self)` (method)
- L66 `test_disabled_on_config_load_error(self)` (method)
- L71 `TestEphemeralMode` (class) — Default behavior: random userId, no persistence.
- L74 `test_session_gets_random_user_id(self, tmp_path, monkeypatch)` (method)
- L82 `test_different_tasks_get_different_user_ids(self, tmp_path, monkeypatch)` (method)
- L90 `test_session_reuse_within_same_task(self, tmp_path, monkeypatch)` (method)
- L99 `TestManagedPersistenceMode` (class) — With managed_persistence: stable userId derived from Hermes profile.
- L102 `test_session_gets_stable_user_id(self, tmp_path, monkeypatch)` (method)
- L113 `test_same_user_id_after_session_drop(self, tmp_path, monkeypatch)` (method)
- L124 `test_same_user_id_across_tasks(self, tmp_path, monkeypatch)` (method)
- L135 `test_different_profiles_get_different_user_ids(self, tmp_path, monkeypatch)` (method)
- L148 `test_navigate_uses_stable_identity(self, tmp_path, monkeypatch)` (method)
- L168 `test_navigate_reuses_identity_after_close(self, tmp_path, monkeypatch)` (method)
- L196 `TestConfiguredCamofoxIdentity` (class) — Externally managed Camofox sessions can provide their own identity.
- L199 `test_env_identity_overrides_default_identity(self, tmp_path, monkeypatch)` (method)
- L219 `test_config_identity_is_used_when_env_is_absent(self, tmp_path, monkeypatch)` (method)
- L239 `test_env_identity_takes_precedence_over_config(self, tmp_path, monkeypatch)` (method)
- L262 `test_adopts_existing_tab_matching_session_key(self, tmp_path, monkeypatch)` (method)
- L280 `test_managed_persistence_can_opt_into_tab_adoption(self, tmp_path, monkeypatch)` (method)
- L293 `test_soft_cleanup_preserves_externally_managed_session(self, tmp_path, monkeypatch)` (method)
- L308 `TestVncUrlDiscovery` (class) — VNC URL is derived from the Camofox health endpoint.
- L311 `test_vnc_url_from_health_port(self, monkeypatch)` (method)
- L318 `test_vnc_url_none_when_headless(self, monkeypatch)` (method)
- L325 `test_vnc_url_rejects_invalid_port(self, monkeypatch)` (method)
- L332 `test_vnc_url_only_probed_once(self, monkeypatch)` (method)
- L341 `test_navigate_includes_vnc_hint(self, tmp_path, monkeypatch)` (method)
- L357 `TestCamofoxSoftCleanup` (class) — camofox_soft_cleanup drops local state only when managed persistence is on.
- L360 `test_returns_true_and_drops_session_when_enabled(self, tmp_path, monkeypatch)` (method)
- L374 `test_returns_false_when_disabled(self, tmp_path, monkeypatch)` (method)
- L389 `test_does_not_call_server_delete(self, tmp_path, monkeypatch)` (method) — Soft cleanup must never hit the Camofox /sessions DELETE endpoint.
