---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/qqbot/keyboards.py

Symbols in `gateway/platforms/qqbot/keyboards.py`.

- L58 `KeyboardButtonPermission` (class) — Button permission metadata. ``type=2`` means all users can click.
- L62 `to_dict(self)` (method)
- L67 `KeyboardButtonAction` (class) — What happens when the button is clicked.
- L84 `to_dict(self)` (method)
- L94 `KeyboardButtonRenderData` (class) — Visual rendering of a button.
- L105 `to_dict(self)` (method)
- L114 `KeyboardButton` (class) — One button in a keyboard.
- L125 `to_dict(self)` (method)
- L135 `KeyboardRow` (class)
- L138 `to_dict(self)` (method)
- L143 `KeyboardContent` (class)
- L146 `to_dict(self)` (method)
- L151 `InlineKeyboard` (class) — Top-level keyboard payload — goes into ``MessageToCreate.keyboard``.
- L155 `to_dict(self)` (method)
- L161 `parse_approval_button_data(button_data: str)` (function) — Parse approval ``button_data`` into ``(session_key, decision)``.
- L174 `parse_update_prompt_button_data(button_data: str)` (function) — Parse update-prompt ``button_data`` into ``'y'`` or ``'n'``.
- L184 `_make_callback_button(btn_id: str, label: str, visited_label: str, data: str, style: int, group_id: str)` (function)
- L204 `build_approval_keyboard(session_key: str)` (function) — Build the 3-button approval keyboard.
- L247 `build_update_prompt_keyboard()` (function) — Build a Yes/No keyboard for update confirmation prompts.
- L278 `ApprovalRequest` (class) — Structured approval-request display data.
- L300 `build_approval_text(req: ApprovalRequest)` (function) — Render an :class:`ApprovalRequest` into the message body (markdown).
- L307 `_build_exec_text(req: ApprovalRequest)` (function)
- L323 `_build_plugin_text(req: ApprovalRequest)` (function)
- L349 `ApprovalSender` (class) — Send an approval-request message with an inline keyboard.
- L357 `__init__(self, post_c2c: PostMessageFn, post_group: PostMessageFn, log_tag: str='QQBot')` (method)
- L367 `send(self, chat_type: str, chat_id: str, req: ApprovalRequest, msg_id: Optional[str]=None)` (method) — Send an approval message to *chat_id*.
- L417 `InteractionEvent` (class) — Parsed ``INTERACTION_CREATE`` event payload.
- L445 `operator_openid(self)` (method) — Best available operator openid (group → member; c2c → user).
- L454 `parse_interaction_event(raw: Dict[str, Any])` (function) — Parse a raw ``INTERACTION_CREATE`` dispatch payload (``d``).
