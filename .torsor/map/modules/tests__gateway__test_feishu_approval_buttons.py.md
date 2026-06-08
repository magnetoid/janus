---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_feishu_approval_buttons.py

Symbols in `tests/gateway/test_feishu_approval_buttons.py`.

- L23 `_ensure_feishu_mocks()` (function) — Provide stubs for lark-oapi / aiohttp.web so the import succeeds.
- L49 `_make_adapter()` (function) — Create a FeishuAdapter with mocked internals.
- L57 `_make_card_action_data(action_value: dict, chat_id: str='oc_12345', open_id: str='ou_user1', token: str='tok_abc')` (function) — Create a mock Feishu card action callback data object.
- L77 `_close_submitted_coro(coro, _loop)` (function) — Close scheduled coroutines in sync-handler tests to avoid unawaited warnings.
- L87 `TestFeishuExecApproval` (class) — Test send_exec_approval sends an interactive card.
- L91 `test_sends_interactive_card(self)` (method)
- L132 `test_stores_approval_state(self)` (method)
- L157 `test_not_connected(self)` (method)
- L166 `test_truncates_long_command(self)` (method)
- L188 `test_multiple_approvals_get_unique_ids(self)` (method)
- L215 `TestFeishuUpdatePrompt` (class) — Test send_update_prompt sends an interactive card.
- L219 `test_sends_interactive_card(self)` (method)
- L254 `test_stores_prompt_state(self)` (method)
- L279 `test_not_connected(self)` (method)
- L290 `test_send_failure_returns_error(self)` (method)
- L310 `TestResolveApproval` (class) — Test _resolve_approval pops state and calls resolve_gateway_approval.
- L314 `test_resolves_once(self)` (method)
- L329 `test_resolves_deny(self)` (method)
- L343 `test_resolves_session(self)` (method)
- L357 `test_resolves_always(self)` (method)
- L371 `test_already_resolved_drops_silently(self)` (method)
- L380 `test_unauthorized_click_does_not_resolve(self)` (method)
- L396 `test_chat_mismatch_does_not_resolve(self)` (method)
- L414 `TestNonApprovalCardAction` (class) — Non-approval card actions should still route as synthetic commands.
- L418 `test_routes_as_synthetic_command(self)` (method)
- L445 `_FakeCallBackCard` (class)
- L446 `__init__(self)` (method)
- L451 `_FakeP2Response` (class)
- L452 `__init__(self)` (method)
- L457 `_patch_callback_card_types(monkeypatch)` (function) — Provide real-ish P2CardActionTriggerResponse / CallBackCard for tests.
- L463 `TestCardActionCallbackResponse` (class) — Test that _on_card_action_trigger returns updated card inline.
- L466 `test_drops_action_when_loop_not_ready(self, _patch_callback_card_types)` (method)
- L478 `test_returns_card_for_approve_action(self, _patch_callback_card_types)` (method)
- L505 `test_returns_card_for_deny_action(self, _patch_callback_card_types)` (method)
- L527 `test_ignores_missing_approval_id(self, _patch_callback_card_types)` (method)
- L540 `test_no_card_for_non_approval_action(self, _patch_callback_card_types)` (method)
- L552 `test_falls_back_to_open_id_when_name_not_cached(self, _patch_callback_card_types)` (method)
- L573 `test_ignores_expired_cached_name(self, _patch_callback_card_types)` (method)
- L596 `test_rejects_approval_click_from_unauthorized_user(self, _patch_callback_card_types)` (method)
- L618 `test_rejects_approval_click_when_callback_chat_mismatches(self, _patch_callback_card_types)` (method)
- L641 `test_returns_card_for_update_prompt_yes(self, _patch_callback_card_types)` (method)
- L667 `test_returns_card_for_update_prompt_no(self, _patch_callback_card_types)` (method)
- L690 `test_ignores_missing_update_prompt_id(self, _patch_callback_card_types)` (method)
- L703 `test_already_resolved_update_prompt_returns_no_card(self, _patch_callback_card_types)` (method)
- L718 `test_update_prompt_schedule_failure_returns_no_card(self, _patch_callback_card_types)` (method)
- L738 `test_update_prompt_unauthorized_operator_returns_no_card(self, _patch_callback_card_types)` (method)
- L760 `test_update_prompt_empty_allowlists_fail_closed(self, _patch_callback_card_types)` (method)
- L782 `test_update_prompt_chat_mismatch_returns_no_card(self, _patch_callback_card_types)` (method)
- L807 `TestResolveUpdatePrompt` (class) — Test update prompt resolution persists the response file.
- L811 `test_writes_response_file(self, tmp_path, monkeypatch)` (method)
- L827 `test_overwrites_existing_response_file(self, tmp_path, monkeypatch)` (method)
- L844 `test_unknown_prompt_id_drops_silently(self, tmp_path, monkeypatch)` (method)
- L854 `test_chat_mismatch_does_not_write_response_file(self, tmp_path, monkeypatch)` (method)
