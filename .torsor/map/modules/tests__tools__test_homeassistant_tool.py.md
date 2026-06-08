---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_homeassistant_tool.py

Symbols in `tests/tools/test_homeassistant_tool.py`.

- L46 `TestFilterAndSummarize` (class)
- L47 `test_no_filters_returns_all(self)` (method)
- L54 `test_domain_filter_lights(self)` (method)
- L60 `test_domain_filter_sensor(self)` (method)
- L66 `test_domain_filter_no_matches(self)` (method)
- L71 `test_area_filter_by_friendly_name(self)` (method)
- L78 `test_area_filter_by_area_attribute(self)` (method)
- L85 `test_area_filter_case_insensitive(self)` (method)
- L89 `test_combined_domain_and_area(self)` (method)
- L94 `test_summary_includes_friendly_name(self)` (method)
- L99 `test_empty_states_list(self)` (method)
- L103 `test_missing_attributes_handled(self)` (method)
- L115 `TestBuildServicePayload` (class)
- L116 `test_entity_id_only(self)` (method)
- L120 `test_data_only(self)` (method)
- L124 `test_entity_id_and_data(self)` (method)
- L133 `test_no_args_returns_empty(self)` (method)
- L137 `test_entity_id_param_takes_precedence_over_data(self)` (method)
- L151 `TestParseServiceResponse` (class)
- L152 `test_list_response_extracts_entities(self)` (method)
- L163 `test_empty_list_response(self)` (method)
- L168 `test_non_list_response(self)` (method)
- L174 `test_none_response(self)` (method)
- L179 `test_service_name_format(self)` (method)
- L189 `TestHandlerValidation` (class)
- L190 `test_get_state_missing_entity_id(self)` (method)
- L195 `test_get_state_empty_entity_id(self)` (method)
- L199 `test_call_service_missing_domain(self)` (method)
- L204 `test_call_service_missing_service(self)` (method)
- L209 `test_call_service_missing_both(self)` (method)
- L213 `test_call_service_empty_strings(self)` (method)
- L223 `TestDomainBlocklist` (class) — Verify dangerous HA service domains are blocked.
- L227 `test_blocked_domain_rejected(self, domain)` (method)
- L234 `test_safe_domain_not_blocked(self)` (method) — Safe domains like 'light' should not be blocked (will fail on network, not blocklist).
- L245 `test_blocked_domains_include_shell_command(self)` (method)
- L248 `test_blocked_domains_include_hassio(self)` (method)
- L251 `test_blocked_domains_include_rest_command(self)` (method)
- L260 `TestEntityIdValidation` (class) — Verify entity_id format validation prevents path traversal.
- L263 `test_valid_entity_id_accepted(self)` (method)
- L269 `test_path_traversal_rejected(self)` (method)
- L274 `test_special_chars_rejected(self)` (method)
- L280 `test_missing_domain_rejected(self)` (method)
- L284 `test_get_state_rejects_invalid_entity_id(self)` (method)
- L289 `test_call_service_rejects_invalid_entity_id(self)` (method)
- L298 `test_call_service_allows_no_entity_id(self)` (method) — Some services (like scene.turn_on) don't need entity_id.
- L313 `TestCallServiceStringData` (class) — data param may arrive as a JSON string (XML tool calling mode).
- L317 `test_string_data_deserialized(self, mock_run)` (method) — JSON string data is parsed into a dict before dispatch.
- L329 `test_dict_data_passthrough(self, mock_run)` (method) — Dict data (JSON tool calling mode) still works unchanged.
- L339 `test_invalid_json_string_returns_error(self)` (method) — Malformed JSON string in data returns a clear error.
- L351 `test_empty_string_data_becomes_none(self, mock_run)` (method) — Empty/whitespace string data is treated as None.
- L367 `TestServiceNameValidation` (class) — Verify domain/service format validation prevents path traversal in URL.
- L375 `test_valid_domain_names(self)` (method)
- L382 `test_valid_service_names(self)` (method)
- L388 `test_path_traversal_in_domain_rejected(self)` (method)
- L393 `test_path_traversal_in_service_rejected(self)` (method)
- L397 `test_blocked_domain_bypass_via_traversal_rejected(self)` (method) — Ensure shell_command/../light is rejected, not just checked against blocklist.
- L403 `test_slashes_rejected(self)` (method)
- L407 `test_dots_rejected(self)` (method)
- L411 `test_uppercase_rejected(self)` (method)
- L415 `test_special_chars_rejected(self)` (method)
- L420 `test_handler_rejects_traversal_domain(self)` (method) — _handle_call_service must reject domain with path traversal.
- L429 `test_handler_rejects_traversal_service(self)` (method) — _handle_call_service must reject service with path traversal.
- L438 `test_handler_rejects_blocklist_bypass_traversal(self)` (method) — Blocklist bypass via shell_command/../light must be caught by format validation.
- L454 `TestCheckAvailable` (class)
- L455 `test_unavailable_without_token(self, monkeypatch)` (method)
- L459 `test_available_with_token(self, monkeypatch)` (method)
- L463 `test_empty_token_is_unavailable(self, monkeypatch)` (method)
- L473 `TestGetHeaders` (class)
- L474 `test_bearer_token_format(self, monkeypatch)` (method)
- L486 `TestRegistration` (class)
- L487 `test_tools_registered_in_registry(self)` (method)
- L495 `test_tools_in_homeassistant_toolset(self)` (method)
- L502 `test_check_fn_gates_availability(self, monkeypatch)` (method) — Registry should exclude HA tools when HASS_TOKEN is not set.
- L511 `test_check_fn_includes_when_token_set(self, monkeypatch)` (method) — Registry should include HA tools when HASS_TOKEN is set.
