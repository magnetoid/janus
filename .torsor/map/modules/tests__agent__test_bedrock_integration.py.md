---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_bedrock_integration.py

Symbols in `tests/agent/test_bedrock_integration.py`.

- L17 `TestProviderRegistry` (class) — Verify Bedrock is registered in PROVIDER_REGISTRY.
- L20 `test_bedrock_in_registry(self)` (method)
- L24 `test_bedrock_auth_type_is_aws_sdk(self)` (method)
- L29 `test_bedrock_has_no_api_key_env_vars(self)` (method) — Bedrock uses the AWS SDK credential chain, not API keys.
- L35 `test_bedrock_base_url_env_var(self)` (method)
- L41 `TestProviderAliases` (class) — Verify Bedrock aliases resolve correctly.
- L44 `test_aws_alias(self)` (method)
- L48 `test_aws_bedrock_alias(self)` (method)
- L52 `test_amazon_bedrock_alias(self)` (method)
- L56 `test_amazon_alias(self)` (method)
- L61 `TestProviderLabels` (class) — Verify Bedrock appears in provider labels.
- L64 `test_bedrock_label(self)` (method)
- L69 `TestModelCatalog` (class) — Verify Bedrock has a static model fallback list.
- L72 `test_bedrock_has_curated_models(self)` (method)
- L77 `test_bedrock_models_include_claude(self)` (method)
- L83 `test_bedrock_models_include_nova(self)` (method)
- L90 `TestResolveProvider` (class) — Verify resolve_provider() handles bedrock correctly.
- L93 `test_explicit_bedrock_resolves(self, monkeypatch)` (method) — When user explicitly requests 'bedrock', it should resolve.
- L100 `test_aws_alias_resolves_to_bedrock(self)` (method)
- L105 `test_amazon_bedrock_alias_resolves(self)` (method)
- L110 `test_auto_detect_with_aws_credentials(self, monkeypatch)` (method) — When AWS credentials are present and no other provider is configured,
- L130 `TestRuntimeProvider` (class) — Verify resolve_runtime_provider() handles bedrock correctly.
- L133 `test_bedrock_runtime_resolution(self, monkeypatch)` (method)
- L151 `test_bedrock_runtime_default_region(self, monkeypatch)` (method)
- L164 `test_bedrock_runtime_no_credentials_raises_on_auto_detect(self, monkeypatch)` (method) — When bedrock is auto-detected (not explicitly requested) and no
- L188 `test_bedrock_runtime_explicit_skips_credential_check(self, monkeypatch)` (method) — When user explicitly requests bedrock, trust boto3's credential chain
- L209 `TestProvidersModule` (class) — Verify bedrock is wired into hermes_cli/providers.py.
- L212 `test_bedrock_alias_in_providers(self)` (method)
- L218 `test_bedrock_transport_mapping(self)` (method)
- L222 `test_determine_api_mode_from_bedrock_url(self)` (method)
- L228 `test_label_override(self)` (method)
- L237 `TestErrorClassifierBedrock` (class) — Verify Bedrock error patterns are in the global error classifier.
- L240 `test_throttling_in_rate_limit_patterns(self)` (method)
- L244 `test_context_overflow_patterns(self)` (method)
- L253 `TestPackaging` (class) — Verify Bedrock remains a declared lazy optional dependency.
- L257 `_optional_dependencies()` (method)
- L264 `test_bedrock_extra_exists(self)` (method)
- L269 `test_bedrock_is_not_eager_installed_by_all_extra(self)` (method)
- L298 `TestBedrockPreserveDotsFlag` (class) — ``AIAgent._anthropic_preserve_dots`` must return True on Bedrock so
- L302 `test_bedrock_provider_preserves_dots(self)` (method)
- L308 `test_bedrock_runtime_us_east_1_url_preserves_dots(self)` (method) — Defense-in-depth: even without an explicit ``provider="bedrock"``,
- L320 `test_bedrock_runtime_ap_northeast_2_url_preserves_dots(self)` (method) — Reporter-reported region (ap-northeast-2) exercises the same
- L331 `test_non_bedrock_aws_url_does_not_preserve_dots(self)` (method) — Unrelated AWS endpoints (e.g. ``s3.us-east-1.amazonaws.com``)
- L344 `test_anthropic_native_still_does_not_preserve_dots(self)` (method) — Canary: adding Bedrock to the allowlist must not weaken the
- L354 `TestBedrockModelNameNormalization` (class) — End-to-end: ``normalize_model_name`` + the preserve-dots flag
- L359 `test_global_anthropic_inference_profile_preserved(self)` (method) — The reporter's exact model ID.
- L366 `test_us_anthropic_dated_inference_profile_preserved(self)` (method) — Regional + dated Sonnet inference profile.
- L374 `test_apac_anthropic_haiku_inference_profile_preserved(self)` (method) — APAC inference profile — same structural-dot shape.
- L381 `test_bedrock_prefix_preserved_without_preserve_dots(self)` (method) — Bedrock inference profile IDs are auto-detected by prefix and
- L391 `test_bare_foundation_model_id_preserved(self)` (method) — Non-inference-profile Bedrock IDs
- L403 `TestBedrockBuildAnthropicKwargsEndToEnd` (class) — Integration: calling ``build_anthropic_kwargs`` with a Bedrock-
- L410 `test_bedrock_inference_profile_survives_build_kwargs(self)` (method)
- L425 `test_bedrock_model_preserved_without_preserve_dots(self)` (method) — Bedrock inference profile IDs survive ``build_anthropic_kwargs``
- L442 `TestBedrockModelIdDetection` (class) — Tests for ``_is_bedrock_model_id`` and the auto-detection that
- L447 `test_bare_bedrock_id_detected(self)` (method)
- L451 `test_regional_us_prefix_detected(self)` (method)
- L455 `test_regional_global_prefix_detected(self)` (method)
- L459 `test_regional_eu_prefix_detected(self)` (method)
- L463 `test_openrouter_format_not_detected(self)` (method)
- L467 `test_bare_claude_not_detected(self)` (method)
- L471 `test_bare_bedrock_id_preserved_without_flag(self)` (method) — The primary bug from #12295: ``anthropic.claude-opus-4-7``
- L480 `test_openrouter_dots_still_converted(self)` (method) — Non-Bedrock dotted model names must still be converted.
- L485 `test_bare_bedrock_id_survives_build_kwargs(self)` (method) — End-to-end: bare Bedrock ID through ``build_anthropic_kwargs``
- L508 `TestAuxiliaryClientBedrockResolution` (class) — Verify resolve_provider_client handles Bedrock's aws_sdk auth type.
- L511 `test_bedrock_returns_client_with_credentials(self, monkeypatch)` (method) — With valid AWS credentials, Bedrock should return a usable client.
- L532 `test_bedrock_returns_none_without_credentials(self, monkeypatch)` (method) — Without AWS credentials, Bedrock should return (None, None) gracefully.
- L541 `test_bedrock_uses_configured_region(self, monkeypatch)` (method) — Bedrock client base_url should reflect AWS_REGION.
- L555 `test_bedrock_respects_explicit_model(self, monkeypatch)` (method) — When caller passes an explicit model, it should be used.
- L569 `test_bedrock_async_mode(self, monkeypatch)` (method) — Async mode should return an AsyncAnthropicAuxiliaryClient.
- L582 `test_bedrock_default_model_is_haiku(self, monkeypatch)` (method) — Default auxiliary model for Bedrock should be Haiku (fast, cheap).
