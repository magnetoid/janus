---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# batch_runner.py

Symbols in `batch_runner.py`.

- L71 `_normalize_tool_stats(tool_stats: Dict[str, Dict[str, int]])` (function) — Normalize tool_stats to include all possible tools with consistent schema.
- L101 `_normalize_tool_error_counts(tool_error_counts: Dict[str, int])` (function) — Normalize tool_error_counts to include all possible tools.
- L125 `_extract_tool_stats(messages: List[Dict[str, Any]])` (function) — Extract tool usage statistics from message history.
- L208 `_extract_reasoning_stats(messages: List[Dict[str, Any]])` (function) — Count how many assistant turns have reasoning vs no reasoning.
- L244 `_process_single_prompt(prompt_index: int, prompt_data: Dict[str, Any], batch_num: int, config: Dict[str, Any])` (function) — Process a single prompt with the agent.
- L400 `_process_batch_worker(args: Tuple)` (function) — Worker function to process a single batch of prompts.
- L527 `BatchRunner` (class) — Manages batch processing of agent prompts with checkpointing and statistics.
- L532 `__init__(self, dataset_file: str, batch_size: int, run_name: str, distribution: str='default', max_iterations: int=10, base_url: str=None, api_key: str=None, model: str='claude-opus-4-20250514', num_workers: int=4, verbose: bool=False, ephemeral_system_prompt: str=None, log_prefix_chars: int=100, providers_allowed: List[str]=None, providers_ignored: List[str]=None, providers_order: List[str]=None, provider_sort: str=None, openrouter_min_coding_score: Optional[float]=None, max_tokens: int=None, reasoning_config: Dict[str, Any]=None, prefill_messages: List[Dict[str, Any]]=None, max_samples: int=None)` (method) — Initialize the batch runner.
- L642 `_load_dataset(self)` (method) — Load dataset from JSONL file.
- L674 `_create_batches(self)` (method) — Split dataset into batches with indices.
- L688 `_load_checkpoint(self)` (method) — Load checkpoint data if it exists.
- L715 `_save_checkpoint(self, checkpoint_data: Dict[str, Any], lock: Optional[Lock]=None)` (method) — Save checkpoint data.
- L732 `_scan_completed_prompts_by_content(self)` (method) — Scan all batch files and extract completed prompts by their actual content.
- L776 `_filter_dataset_by_completed(self, completed_prompts: set)` (method) — Filter the dataset to exclude prompts that have already been completed.
- L810 `run(self, resume: bool=False)` (method) — Run the batch processing pipeline.
- L1147 `main(dataset_file: str=None, batch_size: int=None, run_name: str=None, distribution: str='default', model: str='anthropic/claude-sonnet-4.6', api_key: str=None, base_url: str='https://openrouter.ai/api/v1', max_turns: int=10, num_workers: int=4, resume: bool=False, verbose: bool=False, list_distributions: bool=False, ephemeral_system_prompt: str=None, log_prefix_chars: int=100, providers_allowed: str=None, providers_ignored: str=None, providers_order: str=None, provider_sort: str=None, max_tokens: int=None, reasoning_effort: str=None, reasoning_disabled: bool=False, prefill_messages_file: str=None, max_samples: int=None)` (function) — Run batch processing of agent prompts from a dataset.
