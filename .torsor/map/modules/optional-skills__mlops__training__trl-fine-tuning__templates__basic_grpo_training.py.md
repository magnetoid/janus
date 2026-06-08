---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/mlops/training/trl-fine-tuning/templates/basic_grpo_training.py

Symbols in `optional-skills/mlops/training/trl-fine-tuning/templates/basic_grpo_training.py`.

- L39 `get_dataset(split='train')` (function) — Load and prepare your dataset.
- L66 `extract_xml_tag(text: str, tag: str)` (function) — Extract content between XML tags.
- L72 `extract_answer(text: str)` (function) — Extract the final answer from structured output.
- L78 `correctness_reward_func(prompts, completions, answer, **kwargs)` (function) — Reward correct answers.
- L87 `format_reward_func(completions, **kwargs)` (function) — Reward proper XML format.
- L96 `incremental_format_reward_func(completions, **kwargs)` (function) — Incremental reward for partial format compliance.
- L126 `setup_model_and_tokenizer()` (function) — Load model and tokenizer with optimizations.
- L140 `get_peft_config()` (function) — LoRA configuration for parameter-efficient training.
- L155 `main()` (function) — Main training function.
