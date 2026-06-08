---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/honcho_plugin/test_cli.py

Symbols in `tests/honcho_plugin/test_cli.py`.

- L7 `TestResolveApiKey` (class) — Test _resolve_api_key with various config shapes.
- L10 `test_returns_api_key_from_root(self, monkeypatch)` (method)
- L16 `test_returns_api_key_from_host_block(self, monkeypatch)` (method)
- L23 `test_returns_local_for_base_url_without_api_key(self, monkeypatch)` (method)
- L31 `test_returns_local_for_base_url_env_var(self, monkeypatch)` (method)
- L38 `test_returns_empty_when_nothing_configured(self, monkeypatch)` (method)
- L45 `test_rejects_garbage_base_url_without_scheme(self, monkeypatch)` (method) — Obvious non-URL literals in baseUrl (typos) must not pass the guard.
- L58 `test_rejects_non_http_scheme_base_url(self, monkeypatch)` (method) — file:// / ftp:// / ws:// schemes are rejected as non-HTTP Honcho URLs.
- L79 `test_accepts_https_base_url(self, monkeypatch)` (method)
- L86 `test_accepts_legacy_schemeless_host(self, monkeypatch)` (method) — Legacy configs with schemeless host:port must not regress.
- L104 `TestCmdSetupLocalJwt` (class) — Local-deployment setup must allow configuring a JWT for AUTH_JWT_SECRET-backed Honcho servers.
- L107 `_run_setup(self, monkeypatch, tmp_path, initial_cfg, prompt_answers)` (method)
- L140 `test_local_setup_stores_jwt_under_host_block(self, monkeypatch, tmp_path)` (method) — Self-hosted users supplying a JWT must have it written under hosts.<host>.apiKey,
- L162 `test_local_setup_blank_jwt_keeps_local_no_auth(self, monkeypatch, tmp_path)` (method) — Blank JWT prompt response on a fresh local config must not introduce an apiKey
- L182 `TestCmdStatus` (class)
- L183 `test_reports_connection_failure_when_session_setup_fails(self, monkeypatch, capsys, tmp_path)` (method)
- L238 `TestCloneHonchoForProfile` (class) — Identity-key carryover during profile cloning.
- L247 `_setup_clone_env(self, monkeypatch, tmp_path, cfg)` (method)
- L261 `test_user_peer_aliases_carry_into_cloned_profile(self, monkeypatch, tmp_path)` (method)
- L277 `test_runtime_peer_prefix_carries_into_cloned_profile(self, monkeypatch, tmp_path)` (method)
- L293 `test_pin_peer_name_carries_into_cloned_profile(self, monkeypatch, tmp_path)` (method)
- L309 `test_unset_identity_keys_do_not_appear_in_cloned_profile(self, monkeypatch, tmp_path)` (method)
- L323 `TestSetupWizardDeploymentShape` (class) — The deployment-shape step writes pinPeerName / userPeerAliases /
- L336 `_run_setup(self, monkeypatch, tmp_path, *, answers, initial_cfg=None)` (method)
- L394 `test_single_shape_sets_pin_peer_name_and_clears_aliases(self, monkeypatch, tmp_path)` (method)
- L416 `test_multi_shape_leaves_pin_false_and_accepts_prefix(self, monkeypatch, tmp_path)` (method)
- L434 `test_hybrid_shape_aliases_operator_runtime_ids_to_peer_name(self, monkeypatch, tmp_path)` (method)
- L456 `test_skip_shape_preserves_existing_identity_config(self, monkeypatch, tmp_path)` (method)
- L473 `test_single_to_multi_steers_to_hybrid_by_default(self, monkeypatch, tmp_path)` (method) — Flipping single → multi triggers a warning that auto-steers the
- L500 `test_single_to_multi_yes_override_keeps_multi(self, monkeypatch, tmp_path)` (method) — Operator can override the steer by answering ``yes`` and accept
- L520 `test_host_pin_user_peer_true_is_detected_as_single(self, monkeypatch, tmp_path)` (method) — Host-level ``pinUserPeer: true`` must classify as ``single``.
- L543 `test_host_pin_user_peer_false_overrides_root_pin_peer_name(self, monkeypatch, tmp_path)` (method) — Host ``pinUserPeer: false`` outranks host ``pinPeerName`` in the
- L564 `test_root_user_peer_aliases_detected_as_hybrid(self, monkeypatch, tmp_path)` (method) — Root-level ``userPeerAliases`` must classify as ``hybrid`` even
- L580 `test_multi_does_not_override_root_user_peer_aliases(self, monkeypatch, tmp_path)` (method) — Explicit ``multi`` must leave the host ``userPeerAliases`` key
- L605 `test_single_scrubs_stale_pin_user_peer_false(self, monkeypatch, tmp_path)` (method) — Choosing ``single`` must drop any host-level ``pinUserPeer``,
- L627 `TestCloneCarriesPinUserPeer` (class) — ``pinUserPeer`` (canonical name for ``pinPeerName``) must survive a
- L634 `test_clone_inherits_host_pin_user_peer(self, monkeypatch, tmp_path)` (method)
