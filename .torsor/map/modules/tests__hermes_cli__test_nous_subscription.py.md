---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_nous_subscription.py

Symbols in `tests/hermes_cli/test_nous_subscription.py`.

- L17 `_account(*, logged_in: bool, paid: bool | None=None)` (function)
- L26 `_pool_account()` (function) — A $0 subscriber with a live free tool pool (no paid access).
- L37 `test_get_nous_subscription_features_recognizes_direct_exa_backend(monkeypatch)` (function)
- L58 `test_get_nous_subscription_features_force_fresh_forwards_account_request(monkeypatch)` (function)
- L80 `test_get_nous_subscription_features_prefers_managed_modal_in_auto_mode(monkeypatch)` (function)
- L102 `test_get_nous_subscription_features_marks_browser_use_as_managed_when_gateway_ready(monkeypatch)` (function)
- L128 `test_get_nous_subscription_features_uses_direct_browserbase_when_no_managed_gateway(monkeypatch)` (function) — When direct Browserbase keys are set and no managed gateway is available,
- L159 `test_get_nous_subscription_features_prefers_camofox_over_managed_browser_use(monkeypatch)` (function)
- L187 `test_get_nous_subscription_features_requires_agent_browser_for_browserbase(monkeypatch)` (function)
- L213 `test_get_nous_subscription_features_does_not_treat_quoted_false_as_gateway_opt_in(monkeypatch)` (function)
- L237 `test_get_gateway_eligible_tools_ignores_quoted_false_opt_in(monkeypatch)` (function)
- L260 `_stub_browser_probes(monkeypatch, *, has_agent_browser, chromium, lightpanda=False)` (function) — Common monkeypatches for local-browser readiness scenarios.
- L282 `test_local_browser_unavailable_without_chromium(monkeypatch)` (function) — agent-browser present but Chromium absent must NOT advertise local browser.
- L302 `test_local_browser_available_with_chromium(monkeypatch)` (function)
- L314 `test_local_browser_available_with_lightpanda_without_chromium(monkeypatch)` (function) — Lightpanda is text-only and needs no Chromium, so it stays available.
- L332 `test_default_local_browser_unavailable_without_chromium(monkeypatch)` (function) — The implicit (no cloud_provider) local fallthrough is gated on Chromium too.
- L342 `test_cloud_browserbase_available_without_local_chromium(monkeypatch)` (function) — Cloud providers host their own Chromium, so the new local gate must not
- L368 `test_get_gateway_eligible_tools_pool_excludes_video(monkeypatch)` (function) — A free-tool-pool user is offered the covered tools but NOT video gen.
- L387 `test_get_gateway_eligible_tools_empty_when_not_entitled(monkeypatch)` (function) — A logged-in free user with no pool and no paid access gets nothing.
- L400 `_capture_checklist(monkeypatch, *, selected_idx)` (function) — Patch prompt_checklist to capture its args and return chosen indices.
- L419 `test_prompt_enable_tool_gateway_pool_offers_covered_tools_only(monkeypatch)` (function) — Pool user's checklist lists web/image/tts/browser and never video.
- L439 `test_prompt_enable_tool_gateway_writes_only_selected(monkeypatch)` (function) — Selecting a subset writes use_gateway only for those tools.
- L461 `test_prompt_enable_tool_gateway_paid_user_offers_video(monkeypatch)` (function) — Paid users still get video gen in the offer (regression guard).
- L479 `test_apply_nous_managed_defaults_writes_video_gen_config(monkeypatch)` (function) — apply_nous_managed_defaults must write video_gen.provider and
- L501 `test_apply_nous_managed_defaults_writes_image_gen_config(monkeypatch)` (function) — apply_nous_managed_defaults must write image_gen.use_gateway
- L521 `test_apply_nous_managed_defaults_skips_fal_tools_when_key_present(monkeypatch)` (function) — When FAL_KEY is set, apply_nous_managed_defaults should not touch
- L543 `test_apply_nous_managed_defaults_preserves_existing_video_gen_section(monkeypatch)` (function) — When video_gen config already exists as a dict, the function should
- L574 `test_ensure_nous_portal_access_fast_path_when_already_paid(monkeypatch)` (function) — Already-entitled users return True without any login prompt.
- L593 `test_ensure_nous_portal_access_logs_in_then_grants(monkeypatch)` (function) — Logged-out user logs in, then entitlement re-check shows paid access.
- L607 `test_ensure_nous_portal_access_returns_false_when_login_declined(monkeypatch)` (function)
- L617 `test_ensure_nous_portal_access_false_when_logged_in_but_unpaid(monkeypatch)` (function) — Logged in already but no paid access — no login attempt, returns False.
