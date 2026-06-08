---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# mini_swe_runner.py

Symbols in `mini_swe_runner.py`.

- L43 `_effective_temperature_for_model(model: str, base_url: Optional[str]=None)` (function) — Return a fixed temperature for models with strict sampling contracts.
- L117 `create_environment(env_type: str='local', image: str='python:3.11-slim', cwd: str='/tmp', timeout: int=60, **kwargs)` (function) — Create an execution environment using Hermes-Agent's built-in backends.
- L157 `MiniSWERunner` (class) — Agent runner that uses Hermes-Agent's built-in execution environments
- L163 `__init__(self, model: str='anthropic/claude-sonnet-4.6', base_url: str=None, api_key: str=None, env_type: str='local', image: str='python:3.11-slim', cwd: str='/tmp', max_iterations: int=15, command_timeout: int=60, verbose: bool=False)` (method) — Initialize the Mini-SWE Runner.
- L243 `_create_env(self)` (method) — Create the execution environment.
- L254 `_cleanup_env(self)` (method) — Cleanup the execution environment.
- L263 `_execute_command(self, command: str, timeout: int=None)` (method) — Execute a command in the environment.
- L291 `_format_tools_for_system_message(self)` (method) — Format tool definitions for the system message.
- L304 `_convert_to_hermes_format(self, messages: List[Dict[str, Any]], user_query: str, completed: bool)` (method) — Convert internal message format to Hermes trajectory format.
- L414 `run_task(self, task: str)` (method) — Run a single task and return the result with trajectory.
- L579 `run_batch(self, prompts: List[str], output_file: str)` (method) — Run multiple tasks and save trajectories to a JSONL file.
- L636 `main(task: str=None, prompts_file: str=None, output_file: str='swe-runner-test1.jsonl', model: str='claude-sonnet-4-20250514', base_url: str=None, api_key: str=None, env: str='local', image: str='python:3.11-slim', cwd: str='/tmp', max_iterations: int=15, timeout: int=60, verbose: bool=False)` (function) — Run SWE tasks with Hermes trajectory format output.
