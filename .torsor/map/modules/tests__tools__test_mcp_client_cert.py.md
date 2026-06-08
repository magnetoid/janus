---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_client_cert.py

Symbols in `tests/tools/test_mcp_client_cert.py`.

- L28 `TestResolveClientCert` (class)
- L29 `test_returns_none_when_unset(self)` (method)
- L35 `test_string_form_single_pem(self, tmp_path)` (method)
- L44 `test_string_cert_with_separate_key(self, tmp_path)` (method)
- L58 `test_list_form_two_elements(self, tmp_path)` (method)
- L71 `test_list_form_with_passphrase(self, tmp_path)` (method)
- L84 `test_tilde_expansion(self, tmp_path, monkeypatch)` (method)
- L94 `test_missing_file_raises(self, tmp_path)` (method)
- L102 `test_missing_key_file_raises(self, tmp_path)` (method)
- L114 `test_list_with_bad_length_raises(self, tmp_path)` (method)
- L120 `test_list_plus_client_key_rejected(self, tmp_path)` (method)
- L134 `test_non_string_path_rejected(self)` (method)
- L140 `test_password_must_be_string(self, tmp_path)` (method)
- L159 `TestHTTPClientCert` (class)
- L160 `test_cert_forwarded_to_async_client(self, tmp_path)` (method) — When client_cert is set, the new-SDK HTTP path passes ``cert=``
- L220 `test_cert_tuple_forwarded(self, tmp_path)` (method) — List/tuple form resolves to a tuple in ``cert=``.
- L281 `test_no_cert_means_no_cert_kwarg(self)` (method) — When client_cert is unset, ``cert`` is not passed to ``httpx.AsyncClient``
- L335 `test_missing_cert_file_surfaces_clear_error(self, tmp_path)` (method) — A missing cert file fails fast with a server-scoped error message.
- L359 `patch_sse_client()` (function) — Replace ``sse_client`` with a MagicMock that records its kwargs.
- L400 `TestSSEClientCert` (class)
- L401 `test_no_factory_when_defaults(self, patch_sse_client)` (method) — With no cert and ssl_verify=True (default), the SDK's own factory is
- L428 `test_factory_injected_when_cert_set(self, patch_sse_client, tmp_path)` (method) — With client_cert set, an httpx_client_factory is injected that
- L478 `test_factory_forwards_custom_ca_bundle(self, patch_sse_client, tmp_path)` (method) — ssl_verify as a path is forwarded to the factory's httpx client.
