---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_security_advisories.py

Symbols in `tests/hermes_cli/test_security_advisories.py`.

- L26 `fake_advisory()` (function) — A self-contained Advisory used across tests.
- L46 `isolated_home(tmp_path: Path, monkeypatch: pytest.MonkeyPatch)` (function) — Redirect HERMES_HOME so banner cache and config writes are sandboxed.
- L57 `patched_version(monkeypatch: pytest.MonkeyPatch)` (function) — Override _installed_version with a controllable lookup table.
- L69 `TestDetectCompromised` (class)
- L70 `test_no_match_returns_empty_list(self, fake_advisory, patched_version)` (method)
- L75 `test_exact_version_match(self, fake_advisory, patched_version)` (method)
- L83 `test_safe_version_does_not_match(self, fake_advisory, patched_version)` (method)
- L89 `test_empty_compromised_set_matches_any_version(self, patched_version)` (method)
- L113 `TestAck` (class)
- L114 `test_get_acked_ids_empty_when_no_config(self, monkeypatch)` (method)
- L122 `test_filter_unacked_strips_dismissed(self, fake_advisory, monkeypatch)` (method)
- L131 `test_filter_unacked_passes_through_unknown(self, fake_advisory, monkeypatch)` (method)
- L142 `test_ack_advisory_persists_id(self, isolated_home, monkeypatch)` (method)
- L162 `test_ack_advisory_rejects_blank(self, isolated_home)` (method)
- L172 `TestBannerCache` (class)
- L173 `test_first_call_returns_due_hits(self, fake_advisory, isolated_home, monkeypatch)` (method)
- L185 `test_second_call_within_window_suppresses(self, fake_advisory, isolated_home, monkeypatch)` (method)
- L199 `test_call_after_window_re_banners(self, fake_advisory, isolated_home, monkeypatch)` (method)
- L223 `test_acked_hits_never_banner(self, fake_advisory, isolated_home, monkeypatch)` (method)
- L240 `TestRendering` (class)
- L241 `test_short_banner_lines_includes_id_and_version(self, fake_advisory)` (method)
- L254 `test_full_remediation_text_contains_all_steps(self, fake_advisory)` (method)
- L267 `test_render_doctor_section_clean_state(self)` (method)
- L273 `test_render_doctor_section_with_unacked_hit(self, fake_advisory, monkeypatch)` (method)
- L287 `test_gateway_log_message_singular(self, fake_advisory, monkeypatch)` (method)
- L299 `test_gateway_log_message_returns_none_for_no_hits(self)` (method)
- L308 `TestRealCatalog` (class)
- L309 `test_advisories_well_formed(self)` (method) — Every shipped advisory must be self-consistent.
