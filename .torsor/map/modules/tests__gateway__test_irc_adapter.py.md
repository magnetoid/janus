---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_irc_adapter.py

Symbols in `tests/gateway/test_irc_adapter.py`.

- L23 `TestIRCProtocolHelpers` (class)
- L25 `test_parse_simple_command(self)` (method)
- L31 `test_parse_prefixed_message(self)` (method)
- L37 `test_parse_numeric_reply(self)` (method)
- L43 `test_parse_nick_collision(self)` (method)
- L47 `test_extract_nick_full_prefix(self)` (method)
- L50 `test_extract_nick_bare(self)` (method)
- L57 `TestIRCAdapterInit` (class)
- L59 `test_init_from_env(self, monkeypatch)` (method)
- L76 `test_init_from_config_extra(self, monkeypatch)` (method)
- L100 `test_env_overrides_config(self, monkeypatch)` (method)
- L112 `TestIRCAdapterSend` (class)
- L115 `adapter(self, monkeypatch)` (method)
- L132 `test_send_not_connected(self, adapter)` (method)
- L138 `test_send_success(self, adapter)` (method)
- L154 `test_send_splits_long_messages(self, adapter)` (method)
- L168 `TestIRCAdapterMessageParsing` (class)
- L171 `adapter(self, monkeypatch)` (method)
- L191 `test_handle_ping(self, adapter)` (method)
- L203 `test_handle_welcome(self, adapter)` (method)
- L212 `test_handle_nick_collision(self, adapter)` (method)
- L225 `test_handle_addressed_channel_message(self, adapter)` (method) — Messages addressed to the bot (nick: msg) should be dispatched.
- L245 `test_ignores_unaddressed_channel_message(self, adapter)` (method)
- L258 `test_handle_dm(self, adapter)` (method) — DMs (target == bot nick) should always be dispatched.
- L275 `test_ignores_own_messages(self, adapter)` (method)
- L288 `test_ctcp_action_converted(self, adapter)` (method) — CTCP ACTION (/me) should be converted to text.
- L303 `test_allowed_users_case_insensitive(self, monkeypatch)` (method) — Allowlist should match nicks case-insensitively.
- L336 `test_unauthorized_user_blocked(self, monkeypatch)` (method) — Nicks not in allowlist should be ignored.
- L367 `test_nick_collision_retry(self, adapter)` (method) — Multiple 433 responses should keep incrementing the suffix.
- L383 `TestIRCAdapterSplitting` (class)
- L385 `test_split_respects_byte_limit(self)` (method) — Multi-byte characters should not exceed IRC byte limit.
- L398 `test_split_prefers_word_boundary(self)` (method)
- L410 `TestIRCProtocolHelpersExtra` (class)
- L412 `test_parse_malformed_no_space(self)` (method) — A line starting with : but no space should not crash.
- L419 `test_parse_empty(self)` (method)
- L426 `TestIRCAdapterMarkdown` (class)
- L428 `test_strip_bold(self)` (method)
- L431 `test_strip_italic(self)` (method)
- L434 `test_strip_code(self)` (method)
- L437 `test_strip_link(self)` (method)
- L441 `test_strip_image(self)` (method)
- L449 `TestIRCRequirements` (class)
- L451 `test_check_requirements_with_env(self, monkeypatch)` (method)
- L456 `test_check_requirements_missing_server(self, monkeypatch)` (method)
- L461 `test_check_requirements_missing_channel(self, monkeypatch)` (method)
- L466 `test_validate_config_from_extra(self, monkeypatch)` (method)
- L473 `test_validate_config_missing(self, monkeypatch)` (method)
- L484 `TestIRCPluginRegistration` (class) — Test the register() entry point.
- L487 `test_register_adds_to_registry(self, monkeypatch)` (method)
- L506 `_FakeIRCConnection` (class) — A scripted reader/writer pair used to simulate an IRC server.
- L514 `__init__(self, scripted_lines)` (method)
- L521 `write(self, data: bytes)` (method)
- L524 `drain(self)` (method)
- L527 `close(self)` (method)
- L530 `wait_closed(self)` (method)
- L533 `is_closing(self)` (method)
- L537 `readuntil(self, separator: bytes=b'\r\n')` (method)
- L545 `read(self, n: int=-1)` (method)
- L549 `TestIRCStandaloneSend` (class)
- L552 `test_standalone_send_completes_handshake_and_sends_privmsg(self, monkeypatch)` (method)
- L587 `test_standalone_send_returns_error_when_unconfigured(self, monkeypatch)` (method)
- L603 `test_standalone_send_returns_error_on_registration_timeout(self, monkeypatch)` (method)
- L639 `test_standalone_send_rejects_crlf_in_chat_id(self, monkeypatch)` (method)
- L658 `test_standalone_send_strips_crlf_from_message_body(self, monkeypatch)` (method)
- L690 `test_standalone_send_joins_channel_before_privmsg(self, monkeypatch)` (method)
