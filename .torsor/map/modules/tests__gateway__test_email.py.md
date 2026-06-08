---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_email.py

Symbols in `tests/gateway/test_email.py`.

- L26 `TestConfigEnvOverrides` (class) — Verify email config is loaded from environment variables.
- L35 `test_email_config_loaded_from_env(self)` (method)
- L50 `test_email_home_channel_loaded(self)` (method)
- L59 `test_email_not_loaded_without_env(self)` (method)
- L65 `TestCheckRequirements` (class) — Verify check_email_requirements function.
- L74 `test_requirements_met(self)` (method)
- L81 `test_requirements_not_met(self)` (method)
- L86 `test_requirements_empty_env(self)` (method)
- L91 `TestHelperFunctions` (class) — Test email parsing helper functions.
- L94 `test_decode_header_plain(self)` (method)
- L98 `test_decode_header_encoded(self)` (method)
- L105 `test_extract_email_address_with_name(self)` (method)
- L112 `test_extract_email_address_bare(self)` (method)
- L119 `test_extract_email_address_uppercase(self)` (method)
- L126 `test_strip_html_basic(self)` (method)
- L135 `test_strip_html_br_tags(self)` (method)
- L142 `test_strip_html_entities(self)` (method)
- L149 `TestExtractTextBody` (class) — Test email body extraction from different message formats.
- L152 `test_plain_text_body(self)` (method)
- L158 `test_html_body_fallback(self)` (method)
- L165 `test_multipart_prefers_plain(self)` (method)
- L173 `test_multipart_html_only(self)` (method)
- L180 `test_empty_body(self)` (method)
- L187 `TestExtractAttachments` (class) — Test attachment extraction and caching.
- L190 `test_no_attachments(self)` (method)
- L197 `test_document_attachment(self, mock_cache)` (method)
- L217 `test_image_attachment(self, mock_cache)` (method)
- L236 `TestDispatchMessage` (class) — Test email message dispatch logic.
- L239 `_make_adapter(self)` (method) — Create an EmailAdapter with mocked env vars.
- L255 `test_self_message_filtered(self)` (method) — Messages from the agent's own address should be skipped.
- L276 `test_subject_included_in_text(self)` (method) — Subject should be prepended to body for non-reply emails.
- L312 `test_reply_subject_not_duplicated(self)` (method) — Re: subjects should not be prepended to body.
- L340 `test_empty_body_handled(self)` (method) — Email with no body should dispatch '(empty email)'.
- L367 `test_image_attachment_sets_photo_type(self)` (method) — Email with image attachment should set message type to PHOTO.
- L396 `test_source_built_correctly(self)` (method) — Session source should have correct chat_id and user info.
- L426 `test_non_allowlisted_sender_dropped(self)` (method) — Senders not in EMAIL_ALLOWED_USERS should be dropped before dispatch.
- L453 `test_allowlisted_sender_proceeds(self)` (method) — Senders in EMAIL_ALLOWED_USERS should proceed to dispatch normally.
- L484 `test_empty_allowlist_allows_all(self)` (method) — When EMAIL_ALLOWED_USERS is not set, all senders should proceed.
- L512 `TestThreadContext` (class) — Test email reply threading logic.
- L515 `_make_adapter(self)` (method)
- L527 `test_thread_context_stored_after_dispatch(self)` (method) — After dispatching a message, thread context should be stored.
- L555 `test_reply_uses_re_prefix(self)` (method) — Reply subject should have Re: prefix.
- L576 `test_reply_does_not_double_re(self)` (method) — If subject already has Re:, don't add another.
- L594 `test_no_thread_context_uses_default_subject(self)` (method) — Without thread context, subject should be 'Re: Hermes Agent'.
- L609 `TestSendMethods` (class) — Test email send methods.
- L612 `_make_adapter(self)` (method)
- L624 `test_send_calls_smtp(self)` (method) — send() should use SMTP to deliver email.
- L643 `test_send_failure_returns_error(self)` (method) — SMTP failure should return SendResult with error.
- L658 `test_send_image_includes_url(self)` (method) — send_image should include image URL in email body.
- L674 `test_send_document_with_attachment(self)` (method) — send_document should send email with file attachment.
- L706 `test_send_typing_is_noop(self)` (method) — send_typing should do nothing for email.
- L713 `test_get_chat_info(self)` (method) — get_chat_info should return email address as chat info.
- L728 `TestConnectDisconnect` (class) — Test IMAP/SMTP connection lifecycle.
- L731 `_make_adapter(self)` (method)
- L743 `test_connect_success(self)` (method) — Successful IMAP + SMTP connection returns True.
- L767 `test_connect_imap_failure(self)` (method) — IMAP connection failure returns False.
- L777 `test_connect_smtp_failure(self)` (method) — SMTP connection failure returns False.
- L790 `test_disconnect_cancels_poll(self)` (method) — disconnect() should cancel the polling task.
- L806 `TestFetchNewMessages` (class) — Test IMAP message fetching logic.
- L809 `_make_adapter(self)` (method)
- L821 `test_fetch_skips_seen_uids(self)` (method) — Already-seen UIDs should not be fetched again.
- L850 `test_fetch_no_unseen_messages(self)` (method) — No unseen messages returns empty list.
- L862 `test_fetch_handles_imap_error(self)` (method) — IMAP errors should be caught and return empty list.
- L871 `test_fetch_extracts_sender_name(self)` (method) — Sender name should be extracted from 'Name <addr>' format.
- L899 `TestPollLoop` (class) — Test the async polling loop.
- L902 `_make_adapter(self)` (method)
- L915 `test_check_inbox_dispatches_messages(self)` (method) — _check_inbox should fetch and dispatch new messages.
- L949 `TestSendEmailStandalone` (class) — Test the standalone _send_email function in send_message_tool.
- L958 `test_send_email_tool_success(self)` (method) — _send_email should use verified STARTTLS when sending.
- L987 `test_send_email_tool_failure(self)` (method) — SMTP failure should return error dict.
- L1001 `test_send_email_tool_not_configured(self)` (method) — Missing config should return error.
- L1014 `TestSmtpConnectionCleanup` (class) — Verify SMTP connections are closed even when send_message raises.
- L1024 `_make_adapter(self)` (method)
- L1036 `test_smtp_quit_called_on_send_message_failure(self)` (method) — SMTP quit() must be called even when send_message() raises.
- L1055 `test_smtp_close_called_when_quit_also_fails(self)` (method) — If both send_message() and quit() fail, close() is the fallback.
- L1069 `TestImapConnectionCleanup` (class) — Verify IMAP connections are closed even when fetch raises.
- L1079 `_make_adapter(self)` (method)
- L1091 `test_imap_logout_called_on_uid_fetch_failure(self)` (method) — IMAP logout() must be called even when uid fetch raises.
- L1118 `test_imap_logout_called_on_early_return(self)` (method) — IMAP logout() must be called even when returning early (no unseen).
- L1131 `TestImapIdExtensionForNetEase` (class) — Regression for #22271: 163/NetEase mailbox requires the RFC 2971
- L1138 `_make_adapter(self)` (method)
- L1150 `test_connect_sends_imap_id_after_login(self)` (method) — connect() must call xatom('ID', ...) after LOGIN for 163 support.
- L1179 `test_fetch_new_messages_sends_imap_id_after_login(self)` (method) — _fetch_new_messages must also send ID — it opens its own IMAP session.
- L1195 `test_send_imap_id_swallows_errors_for_non_supporting_servers(self)` (method) — Servers that reject ID must not break the connection.
