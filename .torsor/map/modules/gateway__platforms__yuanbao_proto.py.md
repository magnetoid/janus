---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/yuanbao_proto.py

Symbols in `gateway/platforms/yuanbao_proto.py`.

- L34 `_dbg(label: str, data: bytes)` (function)
- L113 `next_seq_no()` (function) — 生成递增序列号（线程安全，溢出时归零）
- L133 `_encode_varint(value: int)` (function) — 将非负整数编码为 protobuf varint
- L150 `_decode_varint(data: bytes, pos: int)` (function) — 从 data[pos:] 解码 varint，返回 (value, new_pos)
- L166 `_encode_field(field_number: int, wire_type: int, value: bytes)` (function) — 编码一个 protobuf field（tag + value）
- L172 `_encode_string(s: str)` (function) — 编码 protobuf string 字段的 value 部分（length-prefixed UTF-8）
- L178 `_encode_bytes(b: bytes)` (function) — 编码 protobuf bytes 字段的 value 部分（length-prefixed）
- L183 `_encode_message(b: bytes)` (function) — 编码嵌套 message（length-prefixed）
- L188 `_parse_fields(data: bytes)` (function) — 解析 protobuf message 的所有字段，返回 [(field_number, wire_type, raw_value), ...]
- L225 `_fields_to_dict(fields: list)` (function) — 将 fields 列表转为 {field_number: [value, ...]} 字典（repeated 字段会有多个）
- L233 `_get_string(fdict: dict, fn: int, default: str='')` (function) — 从 fields dict 取第一个 string 字段
- L244 `_get_varint(fdict: dict, fn: int, default: int=0)` (function) — 从 fields dict 取第一个 varint 字段
- L255 `_get_bytes(fdict: dict, fn: int, default: bytes=b'')` (function) — 从 fields dict 取第一个 bytes/message 字段
- L266 `_get_repeated_bytes(fdict: dict, fn: int)` (function) — 取所有 repeated bytes/message 字段
- L293 `_encode_head(cmd_type: int, cmd: str, seq_no: int, msg_id: str, module: str, need_ack: bool=False, status: int=0)` (function) — 编码 ConnMsg.Head
- L321 `_decode_head(data: bytes)` (function) — 解码 ConnMsg.Head，返回 dict
- L335 `encode_conn_msg(msg_type: int, seq_no: int, data: bytes)` (function) — 编码 ConnMsg（简化接口，对应任务要求的签名）。
- L361 `decode_conn_msg(data: bytes)` (function) — 解码 ConnMsg，返回 {msg_type, seq_no, data, head}。
- L389 `encode_conn_msg_full(cmd_type: int, cmd: str, seq_no: int, msg_id: str, module: str, data: bytes, need_ack: bool=False)` (function) — 编码完整的 ConnMsg（含 cmd/msg_id/module 等 head 字段）。
- L429 `encode_biz_msg(service: str, method: str, req_id: str, body: bytes)` (function) — 将业务 payload 包装为 ConnMsg bytes。
- L452 `decode_biz_msg(data: bytes)` (function) — 解码 ConnMsg bytes，返回业务层信息。
- L497 `_encode_msg_content(content: dict)` (function)
- L524 `_decode_msg_content(data: bytes)` (function)
- L561 `_encode_msg_body_element(element: dict)` (function)
- L573 `_decode_msg_body_element(data: bytes)` (function)
- L585 `_encode_log_ext(trace_id: str)` (function)
- L591 `_decode_im_msg_seq(data: bytes)` (function) — Decode a single ImMsgSeq sub-message (field 17 of InboundMessagePush).
- L605 `_decode_log_ext(data: bytes)` (function)
- L637 `decode_inbound_push(data: bytes)` (function) — 解析入站消息推送的 biz payload（InboundMessagePush proto bytes）。
- L716 `_encode_send_c2c_req(to_account: str, from_account: str, msg_body: list, msg_id: str='', msg_random: int=0, msg_seq: Optional[int]=None, group_code: str='', trace_id: str='')` (function) — 编码 SendC2CMessageReq biz payload。
- L760 `_encode_send_group_req(group_code: str, from_account: str, msg_body: list, msg_id: str='', to_account: str='', random: str='', msg_seq: Optional[int]=None, ref_msg_id: str='', trace_id: str='')` (function) — 编码 SendGroupMessageReq biz payload。
- L808 `encode_send_c2c_message(to_account: str, msg_body: list, from_account: str, msg_id: str='', msg_random: int=0, msg_seq: Optional[int]=None, group_code: str='', trace_id: str='')` (function) — 编码 C2C 发消息请求，返回完整 ConnMsg bytes（可直接发送到 WebSocket）。
- L857 `encode_send_group_message(group_code: str, msg_body: list, from_account: str, msg_id: str='', to_account: str='', random: str='', msg_seq: Optional[int]=None, ref_msg_id: str='', trace_id: str='')` (function) — 编码群消息发送请求，返回完整 ConnMsg bytes（可直接发送到 WebSocket）。
- L912 `encode_auth_bind(biz_id: str, uid: str, source: str, token: str, msg_id: str, app_version: str='', operation_system: str='', bot_version: str='', route_env: str='')` (function) — 构造 auth-bind 请求 ConnMsg bytes。
- L966 `encode_ping(msg_id: str)` (function) — 构造 ping 请求 ConnMsg bytes（PingReq 为空消息）
- L978 `encode_push_ack(original_head: dict)` (function) — 构造 push ACK 回包
- L994 `encode_send_private_heartbeat(from_account: str, to_account: str, heartbeat: int=WS_HEARTBEAT_RUNNING)` (function) — 编码 SendPrivateHeartbeatReq，返回完整 ConnMsg bytes。
- L1021 `encode_send_group_heartbeat(from_account: str, group_code: str, heartbeat: int=WS_HEARTBEAT_RUNNING, send_time: int=0)` (function) — 编码 SendGroupHeartbeatReq，返回完整 ConnMsg bytes。
- L1059 `encode_query_group_info(group_code: str)` (function) — 编码 QueryGroupInfoReq，返回完整 ConnMsg bytes。
- L1076 `decode_query_group_info_rsp(data: bytes)` (function) — 解码 QueryGroupInfoRsp biz payload。
- L1131 `encode_get_group_member_list(group_code: str, offset: int=0, limit: int=200)` (function) — 编码 GetGroupMemberListReq，返回完整 ConnMsg bytes。
- L1157 `decode_get_group_member_list_rsp(data: bytes)` (function) — 解码 GetGroupMemberListRsp biz payload。
