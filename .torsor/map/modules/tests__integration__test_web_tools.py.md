---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/integration/test_web_tools.py

Symbols in `tests/integration/test_web_tools.py`.

- L40 `Colors` (class) — ANSI color codes for terminal output
- L53 `print_header(text: str)` (function) — Print a formatted header
- L60 `print_section(text: str)` (function) — Print a formatted section header
- L66 `print_success(text: str)` (function) — Print success message
- L71 `print_error(text: str)` (function) — Print error message
- L76 `print_warning(text: str)` (function) — Print warning message
- L81 `print_info(text: str, indent: int=0)` (function) — Print info message
- L87 `WebToolsTester` (class) — Test suite for web tools
- L90 `__init__(self, verbose: bool=False, test_llm: bool=True)` (method)
- L101 `log_result(self, test_name: str, status: str, details: str='')` (method) — Log test result
- L120 `test_environment(self)` (method) — Test environment setup and API keys
- L141 `test_web_search(self)` (method) — Test web search functionality
- L241 `test_web_extract(self, urls: List[str]=None)` (method) — Test web content extraction
- L346 `test_web_extract_with_llm(self, urls: List[str]=None)` (method) — Test web extraction with LLM processing
- L406 `run_all_tests(self)` (method) — Run all tests
- L449 `save_results(self)` (method) — Save test results to a JSON file
- L481 `main()` (function) — Main entry point
