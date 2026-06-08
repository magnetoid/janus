---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/wecom_crypto.py

Symbols in `gateway/platforms/wecom_crypto.py`.

- L22 `WeComCryptoError` (class)
- L26 `SignatureError` (class)
- L30 `DecryptError` (class)
- L34 `EncryptError` (class)
- L38 `PKCS7Encoder` (class)
- L42 `encode(cls, text: bytes)` (method)
- L50 `decode(cls, decrypted: bytes)` (method)
- L61 `_sha1_signature(token: str, timestamp: str, nonce: str, encrypt: str)` (function)
- L66 `WXBizMsgCrypt` (class) — Minimal WeCom callback crypto helper compatible with BizMsgCrypt semantics.
- L69 `__init__(self, token: str, encoding_aes_key: str, receive_id: str)` (method)
- L84 `verify_url(self, msg_signature: str, timestamp: str, nonce: str, echostr: str)` (method)
- L88 `decrypt(self, msg_signature: str, timestamp: str, nonce: str, encrypt: str)` (method)
- L114 `encrypt(self, plaintext: str, nonce: Optional[str]=None, timestamp: Optional[str]=None)` (method)
- L126 `_encrypt_bytes(self, raw: bytes)` (method)
- L140 `_random_nonce(length: int=10)` (method)
