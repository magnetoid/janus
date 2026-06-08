---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/browser_tool.py

Symbols in `tools/browser_tool.py`.

- L135 `_discover_homebrew_node_dirs()` (function) — Find Homebrew versioned Node.js bin directories (e.g. node@20, node@24).
- L157 `_browser_candidate_path_dirs()` (function) — Return ordered browser CLI PATH candidates shared by discovery and execution.
- L166 `_merge_browser_path(existing_path: str='')` (function) — Prepend browser-specific PATH fallbacks without reordering existing entries.
- L200 `_get_command_timeout()` (function) — Return the configured browser command timeout from config.yaml.
- L225 `_get_vision_model()` (function) — Model for browser_vision (screenshot analysis — multimodal).
- L230 `_get_extraction_model()` (function) — Model for page snapshot text summarization — same as web_extract.
- L235 `_resolve_cdp_override(cdp_url: str)` (function) — Normalize a user-supplied CDP endpoint into a concrete connectable URL.
- L284 `_get_cdp_override()` (function) — Return a normalized CDP URL override, or empty string.
- L312 `_get_dialog_policy_config()` (function) — Read ``browser.dialog_policy`` + ``browser.dialog_timeout_s`` from config.
- L348 `_ensure_cdp_supervisor(task_id: str)` (function) — Start a CDP supervisor for ``task_id`` if an endpoint is reachable.
- L396 `_stop_cdp_supervisor(task_id: str)` (function) — Stop the CDP supervisor for ``task_id`` if one exists. No-op otherwise.
- L446 `_is_legacy_provider_registry_overridden()` (function) — Return True when a test has patched ``_PROVIDER_REGISTRY`` to a custom value.
- L470 `_ensure_browser_plugins_loaded()` (function) — Idempotently trigger plugin discovery so the browser registry is populated.
- L489 `_get_cloud_provider()` (function) — Return the configured cloud browser provider, or None for local mode.
- L597 `_browser_install_hint()` (function)
- L603 `_requires_real_termux_browser_install(browser_cmd: str)` (function)
- L607 `_termux_browser_install_error()` (function)
- L614 `_is_local_mode()` (function) — Return True when the browser tool will use a local browser backend.
- L621 `_is_local_backend()` (function) — Return True when the browser runs locally (no cloud provider).
- L638 `_get_browser_engine()` (function) — Return the configured browser engine (``auto``, ``lightpanda``, or ``chrome``).
- L686 `_should_inject_engine(engine: str)` (function) — Return True when the engine flag should be added to agent-browser commands.
- L699 `_using_lightpanda_engine()` (function) — Return True when local browser commands are configured for Lightpanda.
- L704 `_lightpanda_fallback_reason(engine: str, command: str, result: Dict[str, Any])` (function) — Return the user-visible reason a Lightpanda result needs Chrome fallback.
- L756 `_needs_lightpanda_fallback(engine: str, command: str, result: Dict[str, Any])` (function) — Check if a Lightpanda result should trigger an automatic Chrome fallback.
- L761 `_annotate_lightpanda_fallback(result: Dict[str, Any], reason: str)` (function) — Add a user-visible Chrome fallback warning to a browser command result.
- L788 `_copy_fallback_warning(target: Dict[str, Any], result: Dict[str, Any])` (function) — Copy browser fallback metadata from an internal result into a tool response.
- L797 `_run_chrome_fallback_command(task_id: str, command: str, args: List[str], timeout: int)` (function) — Run a browser command in a temporary Chrome session at the current URL.
- L962 `_chrome_fallback_screenshot(task_id: str, args: List[str], timeout: int)` (function) — Take a screenshot using a temporary Chrome session.
- L971 `_auto_local_for_private_urls()` (function) — Return whether a cloud-configured install should auto-spawn a local
- L1000 `_url_is_private(url: str)` (function) — Return True when the URL's host resolves to a private/LAN/loopback address.
- L1063 `_navigation_session_key(task_id: str, url: str)` (function) — Pick the session key that should handle ``url`` for ``task_id``.
- L1093 `_is_local_sidecar_key(session_key: str)` (function) — Return True when ``session_key`` is a hybrid-routing local sidecar.
- L1098 `_last_session_key(task_id: str)` (function) — Return the session key to use for a non-nav browser tool call.
- L1111 `_allow_private_urls()` (function) — Return whether the browser is allowed to navigate to private/internal addresses.
- L1136 `_socket_safe_tmpdir()` (function) — Return a short temp directory path suitable for Unix domain sockets.
- L1196 `_emergency_cleanup_all_sessions()` (function) — Emergency cleanup of all active browser sessions.
- L1247 `_cleanup_inactive_browser_sessions()` (function) — Clean up browser sessions that have been inactive for longer than the timeout.
- L1275 `_write_owner_pid(socket_dir: str, session_name: str)` (function) — Record the current hermes PID as the owner of a browser socket dir.
- L1293 `_reap_orphaned_browser_sessions()` (function) — Scan for orphaned agent-browser daemon processes from previous runs.
- L1407 `_browser_cleanup_thread_worker()` (function) — Background thread that periodically cleans up inactive browser sessions.
- L1434 `_start_browser_cleanup_thread()` (function) — Start the background cleanup thread if not already running.
- L1450 `_stop_browser_cleanup_thread()` (function) — Stop the background cleanup thread.
- L1458 `_update_session_activity(task_id: str)` (function) — Update the last activity timestamp for a session.
- L1626 `_create_local_session(task_id: str)` (function)
- L1639 `_create_cdp_session(task_id: str, cdp_url: str)` (function) — Create a session that connects to a user-supplied CDP endpoint.
- L1653 `_get_session_info(task_id: Optional[str]=None)` (function) — Get or create session info for the given session key.
- L1753 `_find_agent_browser()` (function) — Find the agent-browser CLI executable.
- L1856 `_extract_screenshot_path_from_text(text: str)` (function) — Extract a screenshot file path from agent-browser human-readable output.
- L1877 `_run_browser_command(task_id: str, command: str, args: List[str]=None, timeout: Optional[int]=None, _engine_override: Optional[str]=None)` (function) — Run an agent-browser CLI command using our pre-created Browserbase session.
- L2200 `_extract_relevant_content(snapshot_text: str, user_task: Optional[str]=None)` (function) — Use LLM to extract relevant content from a snapshot based on the user's task.
- L2256 `_truncate_snapshot(snapshot_text: str, max_chars: int=8000)` (function) — Structure-aware truncation for snapshots.
- L2291 `browser_navigate(url: str, task_id: Optional[str]=None)` (function) — Navigate to a URL in the browser.
- L2499 `browser_snapshot(full: bool=False, task_id: Optional[str]=None, user_task: Optional[str]=None)` (function) — Get a text-based snapshot of the current page's accessibility tree.
- L2568 `browser_click(ref: str, task_id: Optional[str]=None)` (function) — Click on an element.
- L2605 `browser_type(ref: str, text: str, task_id: Optional[str]=None)` (function) — Type text into an input field.
- L2645 `browser_scroll(direction: str, task_id: Optional[str]=None)` (function) — Scroll the page.
- L2694 `browser_back(task_id: Optional[str]=None)` (function) — Navigate back in browser history.
- L2726 `browser_press(key: str, task_id: Optional[str]=None)` (function) — Press a keyboard key.
- L2761 `browser_console(clear: bool=False, expression: Optional[str]=None, task_id: Optional[str]=None)` (function) — Get browser console messages and JavaScript errors, or evaluate JS in the page.
- L2823 `_browser_eval(expression: str, task_id: Optional[str]=None)` (function) — Evaluate a JavaScript expression in the page context and return the result.
- L2929 `_camofox_eval(expression: str, task_id: Optional[str]=None)` (function) — Evaluate JS via Camofox's /tabs/{tab_id}/eval endpoint (if available).
- L2963 `_maybe_start_recording(task_id: str)` (function) — Start recording if browser.record_sessions is enabled in config.
- L2995 `_maybe_stop_recording(task_id: str)` (function) — Stop recording if one is active for this session.
- L3012 `browser_get_images(task_id: Optional[str]=None)` (function) — Get all images on the current page.
- L3073 `browser_vision(question: str, annotate: bool=False, task_id: Optional[str]=None)` (function) — Take a screenshot of the current page for visual inspection.
- L3347 `_cleanup_old_screenshots(screenshots_dir, max_age_hours=24)` (function) — Remove browser screenshots older than max_age_hours to prevent disk bloat.
- L3371 `_cleanup_old_recordings(max_age_hours=72)` (function) — Remove browser recordings older than max_age_hours to prevent disk bloat.
- L3393 `cleanup_browser(task_id: Optional[str]=None)` (function) — Clean up browser session(s) for a task.
- L3434 `_cleanup_single_browser_session(task_id: str)` (function) — Internal: reap a single browser session by its exact session key.
- L3511 `cleanup_all_browsers()` (function) — Clean up all active browser sessions.
- L3552 `_chromium_search_roots()` (function) — Directories to scan for a Chromium / headless-shell build.
- L3580 `_chromium_installed()` (function) — Return True when a usable Chromium (or headless-shell) build is on disk.
- L3642 `_running_in_docker()` (function) — Best-effort detection of whether we're inside a Docker container.
- L3653 `check_browser_requirements()` (function) — Check if browser tool requirements are met.
- L3711 `check_browser_vision_requirements()` (function) — Whether ``browser_vision`` should be advertised to the model.
