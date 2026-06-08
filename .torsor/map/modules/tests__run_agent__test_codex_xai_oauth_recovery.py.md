---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_codex_xai_oauth_recovery.py

Symbols in `tests/run_agent/test_codex_xai_oauth_recovery.py`.

- L55 `_make_codex_agent()` (function) — Build a minimal AIAgent wired for codex_responses streaming tests.
- L81 `test_codex_stream_wire_error_event_surfaces_stream_error_event(provider_message)` (function) — A wire ``type=error`` SSE frame raises ``_StreamErrorEvent`` with the
- L105 `test_codex_stream_retries_remote_protocol_error_once()` (function) — Transport errors (``httpx.RemoteProtocolError``) trigger a single retry.
- L133 `test_codex_stream_unrelated_runtimeerror_still_raises()` (function) — RuntimeErrors that aren't transport errors must propagate.
- L149 `test_codex_stream_truncated_no_terminal_event_raises()` (function) — Streams that end without a terminal event AND no items raise.
- L179 `test_summarize_api_error_decorates_xai_entitlement_403()` (function) — xAI's OAuth 403 must surface the X Premium+ gotcha + neutral causes.
- L213 `test_summarize_api_error_does_not_accuse_subscribers()` (function) — Hint must not confidently say the user has no subscription.
- L234 `test_summarize_api_error_decorates_xai_body_message()` (function) — SDK-style error with structured body must also get the hint.
- L255 `test_summarize_api_error_idempotent_for_entitlement_hint()` (function) — Decorating twice must not double up the hint.
- L267 `test_summarize_api_error_passes_through_unrelated_errors()` (function) — Non-xAI / non-entitlement errors must not be touched.
- L290 `test_classify_api_error_stream_event_grok_subscription_is_auth()` (function) — _StreamErrorEvent with xAI subscription message classifies as auth/non-retryable.
- L311 `test_classify_api_error_stream_event_resources_exhausted_grok_is_auth()` (function) — 'out of available resources' + 'grok' variant also classifies as auth.
- L324 `test_classify_api_error_stream_event_unrelated_not_reclassified()` (function) — An unrelated _StreamErrorEvent must not be caught by the xAI guard.
- L339 `_assistant_msg_with_encrypted_reasoning(text='hi from grok', encrypted='enc_blob')` (function)
- L354 `test_codex_reasoning_replay_default_includes_encrypted_content()` (function) — Native Codex backend (default) must still replay encrypted reasoning.
- L370 `test_codex_reasoning_replay_includes_encrypted_content_for_xai()` (function) — xAI must receive replayed encrypted reasoning items (May 2026 reversal).
- L403 `test_codex_transport_xai_request_includes_encrypted_content()` (function) — xAI ``include`` array must request ``reasoning.encrypted_content``.
- L426 `test_codex_transport_xai_replays_reasoning_in_input()` (function) — End-to-end: build_kwargs on xAI must replay prior encrypted reasoning.
- L450 `test_codex_transport_native_codex_still_replays_reasoning_in_input()` (function) — Regression guard: openai-codex must keep the existing replay path.
- L492 `test_is_entitlement_failure_matches_real_xai_bodies(message)` (function)
- L501 `test_is_entitlement_failure_false_for_status_other_than_401_403()` (function) — 200/429/500 must never be classified as entitlement, even if body matches.
- L513 `test_is_entitlement_failure_false_for_unrelated_auth_errors()` (function) — A real auth failure (expired token, wrong key) must keep refreshing.
- L532 `test_recover_with_credential_pool_skips_refresh_on_entitlement_403()` (function) — The recovery path must NOT call pool.try_refresh_current() on entitlement 403.
- L577 `test_recover_with_credential_pool_skips_refresh_on_bare_403_for_xai_oauth()` (function) — A bare HTTP 403 from ``xai-oauth`` (no keyword match) must NOT loop refresh.
- L627 `test_recover_with_credential_pool_still_refreshes_genuine_auth_failure()` (function) — Regression guard: legitimate auth errors must still trigger refresh.
- L684 `test_is_entitlement_failure_false_for_bad_credentials_wke_suffix()` (function) — 403 with ``[WKE=unauthenticated:bad-credentials]`` is auth, not entitlement.
- L703 `test_is_entitlement_failure_false_for_wke_suffix_in_normalized_shape()` (function) — The same body after ``_extract_api_error_context`` normalisation.
- L735 `test_is_entitlement_failure_false_for_any_wke_unauthenticated_variant(wke_variant)` (function)
- L747 `test_is_entitlement_failure_false_via_oauth2_validation_phrase_alone()` (function) — Second disambiguator: the "OAuth2 access token could not be
- L764 `test_is_entitlement_failure_wke_signal_overrides_entitlement_keywords()` (function) — Defensive: if a future xAI body somehow carries BOTH the WKE
- L784 `test_is_entitlement_failure_case_insensitive_wke_match()` (function) — Substring match is case-insensitive — the classifier lowercases
- L799 `test_recover_with_credential_pool_refreshes_on_xai_bad_credentials_403()` (function) — End-to-end #29344: a bad-credentials 403 from xai-oauth MUST
- L860 `test_recover_with_credential_pool_still_blocks_real_entitlement()` (function) — Companion regression guard for the #29344 fix: the original
- L912 `test_grok_4_3_context_length_is_1m()` (function) — grok-4.3 ships with 1M context per docs.x.ai/developers/models/grok-4.3.
- L937 `test_grok_4_still_resolves_to_256k()` (function) — Regression guard: grok-4 (non-.3) must still resolve to 256k.
- L965 `_stamped_assistant_msg(issuer_kind, *, text='hi', encrypted='enc_blob', rs_id='rs_001')` (function)
- L981 `test_cross_issuer_reasoning_is_dropped_on_replay()` (function) — Reasoning minted by one Responses endpoint must not be replayed to
- L1006 `test_same_issuer_reasoning_is_still_replayed()` (function) — Same-endpoint reasoning replay is the documented happy path (May 2026
- L1028 `test_unstamped_reasoning_is_replayed_for_backwards_compat()` (function) — Reasoning items persisted before this patch don't carry _issuer_kind.
- L1059 `test_normalize_codex_response_stamps_issuer_on_reasoning()` (function) — Reasoning captured from a response must be stamped with the issuer so
- L1088 `test_transport_round_trip_drops_foreign_reasoning()` (function) — Full transport flow: build_kwargs against codex_backend after grok turns
