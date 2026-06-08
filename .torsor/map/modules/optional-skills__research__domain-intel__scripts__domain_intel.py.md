---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/research/domain-intel/scripts/domain_intel.py

Symbols in `optional-skills/research/domain-intel/scripts/domain_intel.py`.

- L30 `subdomains(domain, include_expired=False, limit=200)` (function) — Find subdomains via Certificate Transparency logs.
- L66 `check_ssl(host, port=443, timeout=10)` (function) — Inspect the TLS certificate of a host.
- L155 `whois_lookup(domain)` (function) — Query WHOIS servers for domain registration info.
- L211 `dns_records(domain, types=None)` (function) — Resolve DNS records using system DNS + Google DoH.
- L250 `check_available(domain)` (function) — Check domain availability using passive signals (DNS + WHOIS + SSL).
- L338 `bulk_check(domains, checks=None, max_workers=5)` (function) — Run multiple checks across multiple domains in parallel.
- L365 `main()` (function)
