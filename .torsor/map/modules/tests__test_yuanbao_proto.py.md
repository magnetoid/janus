---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_yuanbao_proto.py

Symbols in `tests/test_yuanbao_proto.py`.

- L57 `TestVarint` (class)
- L58 `test_small_values(self)` (method)
- L65 `test_zero(self)` (method)
- L70 `test_1_byte_boundary(self)` (method)
- L76 `test_known_values(self)` (method)
- L81 `test_multi_byte(self)` (method)
- L88 `test_partial_decode(self)` (method)
- L100 `TestConnCodec` (class)
- L101 `test_basic_round_trip(self)` (method)
- L109 `test_empty_data(self)` (method)
- L115 `test_all_cmd_types(self)` (method)
- L121 `test_large_seq_no(self)` (method)
- L126 `test_full_round_trip(self)` (method) — encode_conn_msg_full 含 cmd/msg_id/module
- L146 `test_fixed_bytes_simple(self)` (method) — encode_conn_msg(msg_type=0, seq_no=1, data=b"") 的固定编码。
- L165 `TestBizCodec` (class)
- L166 `test_round_trip(self)` (method)
- L181 `test_is_response_flag(self)` (method)
- L194 `test_empty_body(self)` (method)
- L205 `TestMsgBodyElement` (class)
- L206 `test_text_elem_round_trip(self)` (method)
- L216 `test_image_elem_round_trip(self)` (method)
- L238 `test_file_elem_round_trip(self)` (method)
- L252 `test_custom_elem_round_trip(self)` (method)
- L266 `test_empty_content(self)` (method)
- L272 `test_fixed_text_elem_bytes(self)` (method) — 固定 bytes 验证：TIMTextElem { text="hi" }
- L304 `TestDecodeInboundPush` (class)
- L305 `_build_inbound_push_bytes(self, from_account: str='user123', to_account: str='bot456', group_code: str='', msg_key: str='key-001', msg_seq: int=12345, text: str='Hello!')` (method) — 手工构造 InboundMessagePush bytes（与 proto 字段顺序一致）
- L335 `test_basic_c2c_text_message(self)` (method)
- L353 `test_group_message(self)` (method)
- L366 `test_returns_none_on_empty(self)` (method)
- L372 `test_multiple_msg_body_elements(self)` (method)
- L398 `TestEncodeOutbound` (class)
- L399 `test_encode_send_c2c_message(self)` (method)
- L416 `test_encode_send_group_message(self)` (method)
- L430 `test_c2c_biz_payload_contains_to_account(self)` (method) — 验证 biz payload 包含 to_account 字段
- L445 `test_group_biz_payload_contains_group_code(self)` (method)
- L464 `TestAuthAndPing` (class)
- L465 `test_encode_auth_bind(self)` (method)
- L483 `test_encode_ping(self)` (method)
- L490 `test_encode_push_ack(self)` (method)
- L511 `TestConstants` (class)
- L512 `test_pb_msg_types_keys(self)` (method)
- L519 `test_biz_services_keys(self)` (method)
- L524 `test_cmd_type_values(self)` (method)
- L530 `test_pkg_prefix(self)` (method)
- L540 `TestSeqNo` (class)
- L541 `test_monotonic(self)` (method)
- L548 `test_thread_safety(self)` (method)
- L573 `TestEndToEnd` (class)
- L574 `test_send_recv_c2c(self)` (method) — 模拟发送 C2C 消息，然后（在接收方）解码
- L606 `test_inbound_push_full_flow(self)` (method) — 构造服务端 push -> 解码入站消息
