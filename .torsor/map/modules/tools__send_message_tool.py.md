---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/send_message_tool.py

Symbols in `tools/send_message_tool.py`.

- L70 `_sanitize_error_text(text)` (function) — Redact secrets from error text before surfacing it to users/models.
- L78 `_error(message: str)` (function) — Build a standardized error payload with redacted content.
- L83 `_telegram_retry_delay(exc: Exception, attempt: int)` (function)
- L108 `_send_telegram_message_with_retry(bot, *, attempts: int=3, **kwargs)` (function)
- L158 `send_message_tool(args, **kw)` (function) — Handle cross-channel send_message tool calls.
- L168 `_handle_list()` (function) — Return formatted list of available messaging targets.
- L177 `_handle_send(args)` (function) — Send a message to a platform target.
- L354 `_parse_target_ref(platform_name: str, target_ref: str)` (function) — Parse a tool target into chat_id/thread_id and whether it is explicit.
- L423 `_describe_media_for_mirror(media_files)` (function) — Return a human-readable mirror summary when a message only contains media.
- L442 `_get_cron_auto_delivery_target()` (function) — Return the cron scheduler's auto-delivery target for the current run, if any.
- L457 `_maybe_skip_cron_duplicate_send(platform_name: str, chat_id: str, thread_id: str | None)` (function) — Skip redundant cron send_message calls when the scheduler will auto-deliver there.
- L488 `_send_via_adapter(platform, pconfig, chat_id, chunk, *, thread_id=None, media_files=None, force_document=False)` (function) — Send a message via a live gateway adapter, with a standalone fallback
- L583 `_send_to_platform(platform, pconfig, chat_id, message, thread_id=None, media_files=None, force_document=False)` (function) — Route a message to the appropriate platform sender.
- L827 `_is_telegram_thread_not_found(error: Exception)` (function) — Check if a Telegram error is a thread-not-found failure.
- L836 `_send_telegram(token, chat_id, message, media_files=None, thread_id=None, disable_link_previews=False, force_document=False)` (function) — Send via Telegram Bot API (one-shot, no polling needed).
- L1060 `_send_slack(token, chat_id, message, thread_ts=None)` (function) — Send via Slack Web API.
- L1085 `_send_whatsapp(extra, chat_id, message)` (function) — Send via the local WhatsApp bridge HTTP API.
- L1113 `_send_signal(extra, chat_id, message, media_files=None)` (function) — Send via signal-cli JSON-RPC API.
- L1294 `_send_email(extra, chat_id, message)` (function) — Send via SMTP (one-shot, no persistent connection needed).
- L1327 `_send_sms(auth_token, chat_id, message)` (function) — Send a single SMS via Twilio REST API.
- L1383 `_send_matrix(token, extra, chat_id, message)` (function) — Send via Matrix Client-Server API.
- L1427 `_send_matrix_via_adapter(pconfig, chat_id, message, media_files=None, thread_id=None)` (function) — Send via the Matrix adapter so native Matrix media uploads are preserved.
- L1487 `_send_dingtalk(extra, chat_id, message)` (function) — Send via DingTalk robot webhook.
- L1518 `_send_wecom(extra, chat_id, message)` (function) — Send via WeCom using the adapter's WebSocket send pipeline.
- L1545 `_send_weixin(pconfig, chat_id, message, media_files=None)` (function) — Send via Weixin iLink using the native adapter helper.
- L1566 `_send_bluebubbles(extra, chat_id, message)` (function) — Send via BlueBubbles iMessage server using the adapter's REST API.
- L1593 `_send_feishu(pconfig, chat_id, message, media_files=None, thread_id=None)` (function) — Send via Feishu/Lark using the adapter's send pipeline.
- L1650 `_check_send_message()` (function) — Gate send_message on gateway running (always available on messaging platforms).
- L1676 `_send_qqbot(pconfig, chat_id, message)` (function) — Send via QQBot using the REST API directly (no WebSocket needed).
- L1748 `_send_yuanbao(chat_id, message, media_files=None)` (function) — Send via Yuanbao using the running gateway adapter's WebSocket connection.
