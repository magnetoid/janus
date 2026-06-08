---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# scripts/sample_and_compress.py

Symbols in `scripts/sample_and_compress.py`.

- L39 `load_dataset_from_hf(dataset_name: str)` (function) — Load a dataset from HuggingFace.
- L81 `_init_tokenizer_worker(tokenizer_name: str)` (function) — Initialize tokenizer in worker process.
- L88 `_count_tokens_for_entry(entry: Dict)` (function) — Count tokens for a single entry (used in parallel processing).
- L117 `sample_from_datasets(datasets: List[str], total_samples: int, min_tokens: int=16000, tokenizer_name: str='moonshotai/Kimi-K2-Thinking', seed: int=42, num_proc: int=8)` (function) — Load all datasets, filter by token count, then randomly sample from combined pool.
- L224 `save_samples_for_compression(samples: List[Dict[str, Any]], output_dir: Path, batch_size: int=100)` (function) — Save samples to JSONL files for trajectory compression.
- L258 `run_compression(input_dir: Path, output_dir: Path, config_path: str)` (function) — Run trajectory compression on the sampled data.
- L287 `merge_output_to_single_jsonl(input_dir: Path, output_file: Path)` (function) — Merge all JSONL files in a directory into a single JSONL file.
- L316 `main(total_samples: int=2500, output_name: str='compressed_agentic', datasets: str=None, config: str='configs/trajectory_compression.yaml', seed: int=42, batch_size: int=100, min_tokens: int=16000, num_proc: int=8, skip_download: bool=False)` (function) — Sample trajectories from HuggingFace datasets and run compression.
