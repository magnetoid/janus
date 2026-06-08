---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/creative/comfyui/scripts/run_workflow.py

Symbols in `skills/creative/comfyui/scripts/run_workflow.py`.

- L75 `WorkflowRunError` (class) — Raised when a workflow run fails (validation, execution, timeout).
- L78 `__init__(self, status: str, message: str, **details: Any)` (method)
- L84 `to_dict(self)` (method)
- L90 `ComfyRunner` (class)
- L91 `__init__(self, host: str=DEFAULT_LOCAL_HOST, api_key: str | None=None, client_id: str | None=None, partner_key: str | None=None)` (method)
- L105 `headers(self)` (method)
- L111 `_url(self, path: str)` (method)
- L115 `check_server(self)` (method)
- L128 `upload_image(self, path: Path, *, image_type: str='input', overwrite: bool=True, endpoint: str='/upload/image', extra_form: dict | None=None)` (method) — Upload an image file via multipart. Returns server-side ref dict.
- L157 `upload_mask(self, path: Path, original_ref: dict)` (method) — Upload an inpaint mask, linked to a previously uploaded source image.
- L173 `submit(self, workflow: dict)` (method)
- L188 `poll_status(self, prompt_id: str, *, timeout: float=300.0, initial_interval: float=1.5, max_interval: float=8.0)` (method)
- L246 `monitor_ws(self, prompt_id: str, *, timeout: float=300.0, on_progress: Any=None)` (method) — Connect to /ws and listen until execution_success / execution_error.
- L345 `get_outputs(self, prompt_id: str)` (method)
- L377 `download_output(self, *, filename: str, subfolder: str, file_type: str, output_dir: Path, preserve_subfolder: bool=True, overwrite: bool=False)` (method) — Stream a single output to disk. Path-traversal-safe.
- L429 `cancel(self, prompt_id: str | None=None)` (method)
- L445 `_inline_schema(workflow: dict)` (function) — Generate schema using the sibling extract_schema module.
- L451 `load_schema(schema_path: str | None, workflow: dict)` (function)
- L458 `inject_params(workflow: dict, schema: dict, args: dict, *, randomize_seed_if_unset: bool=False)` (function) — Inject user args into the workflow. Returns (new_workflow, warnings).
- L506 `download_outputs(runner: ComfyRunner, outputs: dict, output_dir: Path, *, preserve_subfolder: bool=True, overwrite: bool=False)` (function) — Walk the outputs dict and download every file. Cloud uses `video` (singular);
- L557 `parse_input_image_arg(spec: str)` (function) — Parse `name=path` (or `path` alone, defaulting to name='image').
- L565 `main(argv: list[str] | None=None)` (function)
