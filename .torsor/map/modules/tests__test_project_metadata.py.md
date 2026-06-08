---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_project_metadata.py

Symbols in `tests/test_project_metadata.py`.

- L7 `_load_optional_dependencies()` (function)
- L14 `_load_package_data()` (function)
- L21 `test_matrix_extra_not_in_all()` (function) — The [matrix] extra pulls `mautrix[encryption]` -> `python-olm`,
- L48 `test_lazy_installable_extras_excluded_from_all()` (function) — Policy (2026-05-12): every extra that has a `LAZY_DEPS` entry
- L91 `test_dev_extra_excluded_from_all()` (function) — End-user installs should not pull test/lint/debug tooling.
- L102 `test_messaging_extra_includes_qrcode_for_weixin_setup()` (function)
- L109 `test_dingtalk_extra_includes_qrcode_for_qr_auth()` (function) — DingTalk's QR-code device-flow auth (hermes_cli/dingtalk_auth.py)
- L118 `test_feishu_extra_includes_qrcode_for_qr_login()` (function) — Feishu's QR login flow (gateway/platforms/feishu.py) needs the
- L127 `test_nemo_relay_extra_uses_official_0_3_distribution()` (function)
- L137 `test_dashboard_plugin_manifests_and_assets_are_packaged()` (function) — Bundled dashboard plugins need their manifests and built assets in
- L149 `test_nested_bundled_plugin_metadata_is_packaged()` (function) — Nested opt-in plugins need manifests and READMEs in wheel installs.
