---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_base_url_hostname.py

Symbols in `tests/test_base_url_hostname.py`.

- L17 `test_empty_returns_empty_string()` (function)
- L22 `test_plain_host_without_scheme()` (function)
- L27 `test_https_url_extracts_hostname_only()` (function)
- L33 `test_hostname_case_insensitive()` (function)
- L37 `test_trailing_dot_stripped()` (function)
- L41 `test_path_containing_provider_host_is_not_the_hostname()` (function)
- L46 `test_host_suffix_is_not_the_provider()` (function)
- L51 `test_port_is_ignored()` (function)
- L55 `test_whitespace_stripped()` (function)
- L62 `TestBaseUrlHostMatchesExact` (class)
- L63 `test_exact_domain_matches(self)` (method)
- L67 `test_subdomain_matches(self)` (method)
- L76 `TestBaseUrlHostMatchesNegatives` (class) — The reason this helper exists — defend against substring collisions.
- L79 `test_path_segment_containing_domain_does_not_match(self)` (method)
- L84 `test_host_suffix_does_not_match(self)` (method)
- L90 `test_host_prefix_does_not_match(self)` (method)
- L95 `TestBaseUrlHostMatchesEdgeCases` (class)
- L96 `test_empty_base_url_returns_false(self)` (method)
- L100 `test_empty_domain_returns_false(self)` (method)
- L103 `test_case_insensitive(self)` (method)
- L107 `test_trailing_dot_on_domain_stripped(self)` (method)
- L111 `TestOllamaUrlHostCheck` (class) — GHSA-76xc-57q6-vm5m — ollama.com was using a raw substring match for
- L118 `test_ollama_com_path_injection_rejected(self)` (method) — http://evil.test/ollama.com/v1 — ollama.com appears in the path,
- L125 `test_ollama_com_subdomain_lookalike_rejected(self)` (method) — ollama.com.attacker.test is a separate host, not ollama.com.
- L131 `test_ollama_com_localtest_me_rejected(self)` (method) — ollama.com.localtest.me resolves to 127.0.0.1 via localtest.me
- L138 `test_ollama_ai_is_not_ollama_com(self)` (method) — Different TLD. ollama.ai is not ollama.com.
- L144 `test_localhost_ollama_port_is_not_ollama_com(self)` (method) — http://localhost:11434/v1 is a local Ollama install, but its
- L152 `test_genuine_ollama_com_matches(self)` (method)
- L157 `test_ollama_com_subdomain_matches(self)` (method)
