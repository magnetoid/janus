---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_approval_buttons.py

Symbols in `tests/gateway/test_telegram_approval_buttons.py`.

- L22 `_ensure_telegram_mock()` (function) — Wire up the minimal mocks required to import TelegramAdapter.
- L53 `_make_adapter(extra=None)` (function) — Create a TelegramAdapter with mocked internals.
- L62 `_AuthRunner` (class) — Minimal runner shim for callback auth tests.
- L65 `__init__(self, authorized: bool)` (method)
- L69 `_handle_message(self, event)` (method)
- L72 `_is_user_authorized(self, source)` (method)
- L81 `TestTelegramExecApproval` (class) — Test the send_exec_approval method sends InlineKeyboard buttons.
- L85 `test_sends_inline_keyboard(self)` (method)
- L109 `test_stores_approval_state(self)` (method)
- L127 `test_sends_in_thread(self)` (method)
- L144 `test_retries_without_thread_when_thread_not_found(self)` (method)
- L172 `test_not_connected(self)` (method)
- L181 `test_disable_link_previews_sets_preview_kwargs(self)` (method)
- L198 `test_send_update_prompt_escapes_dynamic_prompt(self)` (method)
- L221 `test_truncates_long_command(self)` (method)
- L238 `TestTelegramApprovalCallback` (class) — Test the approval callback handling in _handle_callback_query.
- L242 `test_resolves_approval_on_click(self)` (method)
- L274 `test_resume_typing_after_inline_approval(self)` (method) — Clicking an inline approval button must un-pause the chat's typing.
- L307 `test_typing_stays_paused_when_resolve_returns_zero(self)` (method) — If resolve_gateway_approval reports 0 resolves, the agent thread
- L335 `test_approval_callback_escapes_dynamic_user_name(self)` (method)
- L363 `test_deny_button(self)` (method)
- L390 `test_approval_callback_rejects_user_blocked_by_global_allowlist(self)` (method)
- L425 `test_already_resolved(self)` (method)
- L453 `test_model_picker_callback_not_affected(self)` (method) — Ensure model picker callbacks still route correctly.
- L476 `test_update_prompt_callback_not_affected(self, tmp_path)` (method) — Ensure update prompt callbacks still work.
- L507 `test_update_prompt_callback_rejects_unauthorized_user(self, tmp_path)` (method) — Update prompt buttons should honor TELEGRAM_ALLOWED_USERS.
- L534 `test_update_prompt_callback_rejects_user_blocked_by_global_allowlist(self, tmp_path)` (method)
- L567 `test_update_prompt_callback_allows_authorized_user(self, tmp_path)` (method) — Allowed Telegram users can still answer update prompt buttons.
