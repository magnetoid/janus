---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_bedrock_model_picker.py

Symbols in `tests/hermes_cli/test_bedrock_model_picker.py`.

- L32 `_mock_botocore_session(*, return_value=None)` (function) — Patch botocore.session even when botocore is not installed.
- L54 `_mock_discover(region: str)` (function) — Return EU models for eu-* regions, US models otherwise.
- L63 `TestProviderModelIdsBedrock` (class) — provider_model_ids("bedrock") should use live Bedrock discovery.
- L66 `test_returns_live_discovered_model_ids(self, monkeypatch)` (method) — Live discovery result is returned as a flat list of model ID strings.
- L80 `test_region_determines_model_ids(self, monkeypatch)` (method) — Different regions produce different model ID prefixes (eu.* vs us.*).
- L94 `test_falls_back_to_static_list_when_discovery_empty(self, monkeypatch)` (method) — When discover_bedrock_models() returns [], fall back to curated static list.
- L106 `test_falls_back_to_static_list_on_exception(self, monkeypatch)` (method) — When discover_bedrock_models() raises, fall back gracefully.
- L117 `test_accepts_bedrock_aliases(self, monkeypatch)` (method) — Provider aliases (aws, aws-bedrock, amazon) should also trigger live discovery.
- L135 `TestListAuthenticatedProvidersBedrock` (class) — Bedrock should appear in the /model picker when AWS creds are present.
- L138 `test_bedrock_appears_with_aws_profile(self, monkeypatch)` (method) — Bedrock shows up when AWS_PROFILE is set.
- L153 `test_bedrock_uses_live_discovery_not_static_list(self, monkeypatch)` (method) — Model IDs come from discover_bedrock_models(), not the static _PROVIDER_MODELS table.
- L172 `test_bedrock_total_models_matches_discovery(self, monkeypatch)` (method) — total_models reflects the actual discovered count.
- L187 `test_bedrock_is_current_when_selected(self, monkeypatch)` (method) — is_current=True when current_provider matches bedrock.
- L202 `test_bedrock_not_shown_without_credentials(self, monkeypatch)` (method) — Bedrock must not appear when no AWS credentials are present.
- L219 `test_non_bedrock_picker_does_not_probe_full_aws_chain(self, monkeypatch)` (method) — Non-Bedrock provider discovery must not touch boto3's full credential chain.
- L243 `test_bedrock_falls_back_to_curated_when_discovery_fails(self, monkeypatch)` (method) — When discover_bedrock_models() raises, fall back to curated list without crashing.
- L259 `test_bedrock_no_duplicate_entries(self, monkeypatch)` (method) — Bedrock must appear at most once — not in both Section 1 and Section 2.
- L279 `TestBedrockRegionRouting` (class) — End-to-end: region from botocore profile is used for discovery, so EU/AP
- L283 `test_eu_region_from_botocore_profile_yields_eu_models(self)` (method) — When botocore resolves eu-central-1, picker shows eu.* model IDs.
- L301 `test_us_region_from_env_var_yields_us_models(self, monkeypatch)` (method) — Explicit AWS_REGION=us-east-1 returns us.* model IDs.
- L317 `test_env_var_takes_priority_over_botocore_profile(self, monkeypatch)` (method) — AWS_REGION env var wins over botocore profile region.
- L336 `TestBedrockOverlayRegistration` (class) — bedrock entry in HERMES_OVERLAYS is correctly configured.
- L339 `test_bedrock_overlay_exists(self)` (method)
- L343 `test_bedrock_overlay_transport(self)` (method)
- L347 `test_bedrock_overlay_auth_type(self)` (method)
- L351 `test_bedrock_label(self)` (method)
- L357 `test_bedrock_aliases_resolve(self)` (method)
