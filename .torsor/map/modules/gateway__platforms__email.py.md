---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/email.py

Symbols in `gateway/platforms/email.py`.

- L68 `_send_imap_id(imap: 'imaplib.IMAP4')` (function) — Send RFC 2971 IMAP ID command identifying this client.
- L91 `_is_automated_sender(address: str, headers: dict)` (function) — Return True if this email is from an automated/noreply source.
- L102 `check_email_requirements()` (function) — Check if email platform dependencies are available.
- L113 `_decode_header_value(raw: str)` (function) — Decode an RFC 2047 encoded email header into a plain string.
- L125 `_extract_text_body(msg: email_lib.message.Message)` (function) — Extract the plain-text body from a potentially multipart email.
- L163 `_strip_html(html: str)` (function) — Naive HTML tag stripper for fallback text extraction.
- L177 `_extract_email_address(raw: str)` (function) — Extract bare email address from 'Name <addr>' format.
- L185 `_extract_attachments(msg: email_lib.message.Message, skip_attachments: bool=False)` (function) — Extract attachment metadata and cache files locally.
- L245 `EmailAdapter` (class) — Email gateway adapter using IMAP (receive) and SMTP (send).
- L248 `__init__(self, config: PlatformConfig)` (method)
- L276 `_trim_seen_uids(self)` (method) — Keep only the most recent UIDs to prevent unbounded memory growth.
- L296 `connect(self)` (method) — Connect to the IMAP server and start polling for new messages.
- L333 `disconnect(self)` (method) — Stop polling and disconnect.
- L345 `_poll_loop(self)` (method) — Poll IMAP for new messages at regular intervals.
- L356 `_check_inbox(self)` (method) — Check INBOX for unseen messages and dispatch them.
- L364 `_fetch_new_messages(self)` (method) — Fetch new (unseen) messages from IMAP. Runs in executor thread.
- L431 `_dispatch_message(self, msg_data: Dict[str, Any])` (method) — Convert a fetched email into a MessageEvent and dispatch it.
- L503 `send(self, chat_id: str, content: str, reply_to: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Send an email reply to the given address.
- L521 `_send_email(self, to_addr: str, body: str, reply_to_msg_id: Optional[str]=None)` (method) — Send an email via SMTP. Runs in executor thread.
- L565 `send_typing(self, chat_id: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Email has no typing indicator — no-op.
- L568 `send_image(self, chat_id: str, image_url: str, caption: Optional[str]=None, reply_to: Optional[str]=None)` (method) — Send an image URL as part of an email body.
- L580 `send_multiple_images(self, chat_id: str, images: List[Tuple[str, str]], metadata: Optional[Dict[str, Any]]=None, human_delay: float=0.0)` (method) — Send a batch of images as a single email with multiple MIME attachments.
- L632 `_send_email_with_attachments(self, to_addr: str, body: str, file_paths: List[str])` (method) — Send an email with multiple file attachments via SMTP.
- L687 `send_document(self, chat_id: str, file_path: str, caption: Optional[str]=None, file_name: Optional[str]=None, reply_to: Optional[str]=None, **kwargs)` (method) — Send a file as an email attachment.
- L712 `_send_email_with_attachment(self, to_addr: str, body: str, file_path: str, file_name: Optional[str]=None)` (method) — Send an email with a file attachment via SMTP.
- L765 `get_chat_info(self, chat_id: str)` (method) — Return basic info about the email chat.
