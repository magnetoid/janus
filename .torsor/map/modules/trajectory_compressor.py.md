---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# trajectory_compressor.py

Symbols in `trajectory_compressor.py`.

- L59 `_effective_temperature_for_model(model: str, requested_temperature: float, base_url: Optional[str]=None)` (function) — Apply fixed model temperature contracts to direct client calls.
- L83 `CompressionConfig` (class) — Configuration for trajectory compression.
- L126 `from_yaml(cls, yaml_path: str)` (method) — Load configuration from YAML file.
- L183 `TrajectoryMetrics` (class) — Metrics for a single trajectory compression.
- L205 `to_dict(self)` (method)
- L228 `AggregateMetrics` (class) — Aggregate metrics across all trajectories.
- L256 `add_trajectory_metrics(self, metrics: TrajectoryMetrics)` (method) — Add a trajectory's metrics to the aggregate.
- L280 `to_dict(self)` (method)
- L332 `TrajectoryCompressor` (class) — Compresses agent trajectories to fit within a target token budget.
- L344 `__init__(self, config: CompressionConfig)` (method) — Initialize the compressor.
- L362 `_init_tokenizer(self)` (method) — Initialize HuggingFace tokenizer for token counting.
- L374 `_init_summarizer(self)` (method) — Initialize LLM routing for summarization (sync and async).
- L419 `_get_async_client(self)` (method) — Return an AsyncOpenAI client bound to the current event loop.
- L435 `_detect_provider(self)` (method) — Detect the provider name from the configured base_url.
- L464 `count_tokens(self, text: str)` (method) — Count tokens in text using the configured tokenizer.
- L474 `count_trajectory_tokens(self, trajectory: List[Dict[str, str]])` (method) — Count total tokens in a trajectory.
- L478 `count_turn_tokens(self, trajectory: List[Dict[str, str]])` (method) — Count tokens for each turn in a trajectory.
- L482 `_find_protected_indices(self, trajectory: List[Dict[str, str]])` (method) — Find indices of protected turns.
- L531 `_is_boundary_clean(trajectory: List[Dict[str, str]], idx: int)` (method) — Return True if a region boundary at ``idx`` does not split a turn pair.
- L544 `_snap_boundary(cls, trajectory: List[Dict[str, str]], idx: int, min_idx: int, max_idx: int)` (method) — Move a compression boundary onto the nearest clean turn boundary.
- L569 `_extract_turn_content_for_summary(self, trajectory: List[Dict[str, str]], start: int, end: int)` (method) — Extract content from turns to be summarized.
- L596 `_coerce_summary_content(content: Any)` (method) — Normalize summary-model output to a safe string.
- L603 `_ensure_summary_prefix(summary: str)` (method) — Normalize summary text to include the expected prefix exactly once.
- L610 `_generate_summary(self, content: str, metrics: TrajectoryMetrics)` (method) — Generate a summary of the compressed turns using OpenRouter.
- L679 `_generate_summary_async(self, content: str, metrics: TrajectoryMetrics)` (method) — Generate a summary of the compressed turns using OpenRouter (async version).
- L748 `compress_trajectory(self, trajectory: List[Dict[str, str]])` (method) — Compress a single trajectory to fit within target token budget.
- L884 `compress_trajectory_async(self, trajectory: List[Dict[str, str]])` (method) — Compress a single trajectory to fit within target token budget (async version).
- L998 `process_entry_async(self, entry: Dict[str, Any])` (method) — Process a single JSONL entry (async version).
- L1019 `process_entry(self, entry: Dict[str, Any])` (method) — Process a single JSONL entry.
- L1046 `process_directory(self, input_dir: Path, output_dir: Path)` (method) — Process all JSONL files in a directory using async parallel processing.
- L1057 `_process_directory_async(self, input_dir: Path, output_dir: Path)` (method) — Async implementation of directory processing with parallel API calls.
- L1252 `_print_summary(self)` (method) — Print comprehensive compression summary statistics.
- L1361 `main(input: str, output: str=None, config: str='configs/trajectory_compression.yaml', target_max_tokens: int=None, tokenizer: str=None, sample_percent: float=None, seed: int=42, dry_run: bool=False)` (function) — Compress agent trajectories to fit within a target token budget.
