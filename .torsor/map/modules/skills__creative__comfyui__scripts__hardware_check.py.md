---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/creative/comfyui/scripts/hardware_check.py

Symbols in `skills/creative/comfyui/scripts/hardware_check.py`.

- L54 `_run(cmd: list[str], timeout: int=8)` (function)
- L64 `is_wsl()` (function) — Return True when running under Windows Subsystem for Linux.
- L77 `is_rosetta()` (function) — Return True when Python is running translated under Rosetta on Apple Silicon.
- L88 `detect_nvidia()` (function) — Detect NVIDIA GPUs. Returns the GPU with the most VRAM, plus list of all.
- L127 `detect_rocm()` (function)
- L174 `detect_apple_silicon()` (function)
- L205 `detect_intel_arc()` (function)
- L221 `total_system_ram_gb()` (function)
- L254 `total_free_disk_gb(path: str='.')` (function)
- L262 `check_pytorch_cuda()` (function) — Optional PyTorch availability check. Only run when --check-pytorch is set.
- L286 `classify(gpu: dict | None, ram_gb: float, free_disk_gb: float, *, wsl: bool, rosetta: bool)` (function)
- L370 `build_report(*, check_pytorch: bool=False)` (function)
- L433 `_install_urls()` (function)
- L442 `main(argv: list[str] | None=None)` (function)
