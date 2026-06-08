---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/finance/dcf-model/scripts/validate_dcf.py

Symbols in `optional-skills/finance/dcf-model/scripts/validate_dcf.py`.

- L12 `DCFModelValidator` (class) — Validates DCF models for errors and quality issues
- L15 `__init__(self, excel_path: str)` (method)
- L33 `validate_all(self)` (method) — Run all validation checks
- L59 `check_sheet_structure(self)` (method) — Verify required sheets exist
- L70 `check_formula_errors(self)` (method) — Check for Excel formula errors in all sheets
- L108 `check_dcf_logic(self)` (method) — Validate DCF-specific logic and calculations
- L114 `_check_terminal_growth_vs_wacc(self)` (method) — Critical check: Terminal growth must be less than WACC
- L159 `_check_wacc_range(self)` (method) — Check if WACC is in reasonable range
- L188 `_check_terminal_value_proportion(self)` (method) — Check if terminal value is reasonable proportion of enterprise value
- L235 `validate_dcf_model(excel_path: str)` (function) — Validate a DCF model Excel file
- L249 `main()` (function) — Command-line interface
