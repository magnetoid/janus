---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/video_gen/test_fal_plugin.py

Symbols in `tests/plugins/video_gen/test_fal_plugin.py`.

- L11 `_reset_registry()` (function)
- L17 `test_fal_provider_registers()` (function)
- L30 `test_fal_family_catalog()` (function) — Each family declares both endpoints. The catalog covers the
- L53 `test_kling_4k_uses_start_image_url()` (function) — Kling v3 4K's image-to-video endpoint expects start_image_url,
- L75 `test_fal_list_models_advertises_both_modalities()` (function)
- L86 `test_fal_unavailable_without_key(monkeypatch)` (function)
- L96 `test_fal_generate_requires_fal_key(monkeypatch)` (function)
- L108 `test_fal_available_via_gateway(monkeypatch)` (function)
- L121 `TestFamilyRouting` (class) — The headline behavior: image_url presence picks the endpoint.
- L125 `with_fake_fal(self, monkeypatch)` (method) — Stub fal_client.submit to capture which endpoint we hit.
- L156 `test_text_to_video_routes_to_text_endpoint(self, with_fake_fal)` (method)
- L169 `test_image_to_video_routes_to_image_endpoint(self, with_fake_fal)` (method)
- L182 `test_default_family_text_routing(self, with_fake_fal)` (method) — No model arg → DEFAULT_MODEL → text-to-video endpoint.
- L191 `test_default_family_image_routing(self, with_fake_fal)` (method)
- L202 `test_unknown_family_falls_back_to_default(self, with_fake_fal)` (method)
- L213 `test_premium_seedance_routing(self, with_fake_fal)` (method) — Sanity check the premium-tier seedance routes correctly.
- L227 `test_kling_4k_remaps_image_param(self, with_fake_fal)` (method) — Kling v3 4K image-to-video receives start_image_url, not image_url.
- L242 `TestPayloadBuilder` (class)
- L243 `test_drops_unsupported_keys(self)` (method) — Veo enum-clamps duration, supports aspect+resolution+audio+neg.
- L267 `test_pixverse_range_clamps_correctly(self)` (method)
- L284 `test_kling_4k_clamps_below_min(self)` (method)
- L301 `test_ltx_omits_duration_aspect_resolution(self)` (method) — LTX 2.3 doesn't declare duration/aspect/resolution enums —
- L325 `test_happy_horse_minimal_payload(self)` (method) — Happy Horse has sparse docs — payload should be minimal.
