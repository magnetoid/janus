<p align="center">
  <img src="assets/banner.png" alt="Janus Agent" width="100%">
</p>

# Janus Agent ☤

<p align="center">
  <a href="https://github.com/magnetoid/janus"><img src="https://img.shields.io/badge/Docs-GitHub-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://discord.gg/NousResearch"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/magnetoid/janus/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://github.com/magnetoid/janus"><img src="https://img.shields.io/badge/Built%20by-Imba%20Labs-blueviolet?style=for-the-badge" alt="Built by Imba Labs"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/Lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

**The self-improving AI agent built by [Imba Labs](https://github.com/magnetoid/janus).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — [Nous Portal](https://portal.nousresearch.com), [OpenRouter](https://openrouter.ai) (200+ models), [NovitaAI](https://novita.ai) (AI-native cloud for Model API, Agent Sandbox, and GPU Cloud), [NVIDIA NIM](https://build.nvidia.com) (Nemotron), [Xiaomi MiMo](https://platform.xiaomimimo.com), [z.ai/GLM](https://z.ai), [Kimi/Moonshot](https://platform.moonshot.ai), [MiniMax](https://www.minimax.io), [Hugging Face](https://huggingface.co), OpenAI, or your own endpoint. Switch with `janus model` — no code changes, no lock-in.

<table>
<tr><td><b>A real terminal interface</b></td><td>Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.</td></tr>
<tr><td><b>Lives where you do</b></td><td>Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.</td></tr>
<tr><td><b>A closed learning loop</b></td><td>Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. <a href="https://github.com/plastic-labs/honcho">Honcho</a> dialectic user modeling. Compatible with the <a href="https://agentskills.io">agentskills.io</a> open standard.</td></tr>
<tr><td><b>Scheduled automations</b></td><td>Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.</td></tr>
<tr><td><b>Delegates and parallelizes</b></td><td>Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.</td></tr>
<tr><td><b>Runs anywhere, not just your laptop</b></td><td>Six terminal backends — local, Docker, SSH, Singularity, Modal, and Daytona. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster.</td></tr>
<tr><td><b>Research-ready</b></td><td>Batch trajectory generation, trajectory compression for training the next generation of tool-calling models.</td></tr>
</table>

---

## Quick Install

Janus installs from source. (Hosted one-line installers will follow once Imba Labs has install hosting.)

### Linux, macOS, WSL2, Termux

```bash
git clone https://github.com/magnetoid/janus.git
cd janus
./setup-janus.sh     # installs uv, creates the venv, installs .[all], symlinks ~/.local/bin/janus
```

On Termux, install the curated `.[termux]` extra instead of `.[all]` (the full extra pulls Android-incompatible voice dependencies):

```bash
git clone https://github.com/magnetoid/janus.git && cd janus
uv venv .venv --python 3.11 && source .venv/bin/activate
uv pip install -e ".[termux]"
```

### Windows (native, PowerShell)

Native Windows runs Janus without WSL — CLI, gateway, TUI, and tools all work natively. Clone the repo and run the setup from Git Bash:

```powershell
git clone https://github.com/magnetoid/janus.git
cd janus
bash setup-janus.sh
```

Native Windows install lives under `%LOCALAPPDATA%\janus`; WSL2 installs under `~/.janus` as on Linux. The only Janus feature that currently needs WSL2 specifically is the browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway both run natively). Found a bug? Please [file issues](https://github.com/magnetoid/janus/issues).

After installation:

```bash
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
janus              # start chatting!
```

---

## Getting Started

```bash
janus              # Interactive CLI — start a conversation
janus model        # Choose your LLM provider and model
janus tools        # Configure which tools are enabled
janus config set   # Set individual config values
janus gateway      # Start the messaging gateway (Telegram, Discord, etc.)
janus setup        # Run the full setup wizard (configures everything at once)
janus claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
janus update       # Update to the latest version
janus doctor       # Diagnose any issues
```

📖 **[Full documentation →](https://github.com/magnetoid/janus)**

---

## Skip the API-key collection — Nous Portal

Janus works with whatever provider you want — that's not changing. But if you'd rather not collect five separate API keys for the model, web search, image generation, TTS, and a cloud browser, **[Nous Portal](https://portal.nousresearch.com)** covers all of them under one subscription:

- **300+ models** — pick any of them with `/model <name>`
- **Tool Gateway** — web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI), cloud browser (Browser Use), all routed through your sub. No extra accounts.

One command from a fresh install:

```bash
janus setup --portal
```

That logs you in via OAuth, sets Nous as your provider, and turns on the Tool Gateway. Check what's wired up any time with `janus portal info`. Full details on the [Tool Gateway docs page](https://github.com/magnetoid/janus).

You can still bring your own keys per-tool whenever you want — the gateway is per-backend, not all-or-nothing.

---

## CLI vs Messaging Quick Reference

Janus has two entry points: start the terminal UI with `janus`, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action                         | CLI                                           | Messaging platforms                                                              |
| ------------------------------ | --------------------------------------------- | -------------------------------------------------------------------------------- |
| Start chatting                 | `janus`                                      | Run `janus gateway setup` + `janus gateway start`, then send the bot a message |
| Start fresh conversation       | `/new` or `/reset`                            | `/new` or `/reset`                                                               |
| Change model                   | `/model [provider:model]`                     | `/model [provider:model]`                                                        |
| Set a personality              | `/personality [name]`                         | `/personality [name]`                                                            |
| Retry or undo the last turn    | `/retry`, `/undo`                             | `/retry`, `/undo`                                                                |
| Compress context / check usage | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]`                                        |
| Browse skills                  | `/skills` or `/<skill-name>`                  | `/<skill-name>`                                                                  |
| Interrupt current work         | `Ctrl+C` or send a new message                | `/stop` or send a new message                                                    |
| Platform-specific status       | `/platforms`                                  | `/status`, `/sethome`                                                            |

For the full command lists, see the [CLI guide](https://github.com/magnetoid/janus) and the [Messaging Gateway guide](https://github.com/magnetoid/janus).

---

## Documentation

All documentation lives at **[hermes-agent.nousresearch.com/docs](https://github.com/magnetoid/janus)**:

| Section                                                                                             | What's Covered                                             |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [Quickstart](https://github.com/magnetoid/janus)                 | Install → setup → first conversation in 2 minutes          |
| [CLI Usage](https://github.com/magnetoid/janus)                              | Commands, keybindings, personalities, sessions             |
| [Configuration](https://github.com/magnetoid/janus)                | Config file, providers, models, all options                |
| [Messaging Gateway](https://github.com/magnetoid/janus)                | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| [Security](https://github.com/magnetoid/janus)                          | Command approval, DM pairing, container isolation          |
| [Tools & Toolsets](https://github.com/magnetoid/janus)            | 40+ tools, toolset system, terminal backends               |
| [Skills System](https://github.com/magnetoid/janus)              | Procedural memory, Skills Hub, creating skills             |
| [Memory](https://github.com/magnetoid/janus)                     | Persistent memory, user profiles, best practices           |
| [MCP Integration](https://github.com/magnetoid/janus)               | Connect any MCP server for extended capabilities           |
| [Cron Scheduling](https://github.com/magnetoid/janus)              | Scheduled tasks with platform delivery                     |
| [Context Files](https://github.com/magnetoid/janus)       | Project context that shapes every conversation             |
| [Architecture](https://github.com/magnetoid/janus)             | Project structure, agent loop, key classes                 |
| [Contributing](https://github.com/magnetoid/janus)             | Development setup, PR process, code style                  |
| [CLI Reference](https://github.com/magnetoid/janus)                  | All commands and flags                                     |
| [Environment Variables](https://github.com/magnetoid/janus) | Complete env var reference                                 |

---

## Migrating from OpenClaw

If you're coming from OpenClaw, Janus can automatically import your settings, memories, skills, and API keys.

**During first-time setup:** The setup wizard (`janus setup`) automatically detects `~/.openclaw` and offers to migrate before configuration begins.

**Anytime after install:**

```bash
janus claw migrate              # Interactive migration (full preset)
janus claw migrate --dry-run    # Preview what would be migrated
janus claw migrate --preset user-data   # Migrate without secrets
janus claw migrate --overwrite  # Overwrite existing conflicts
```

What gets imported:

- **SOUL.md** — persona file
- **Memories** — MEMORY.md and USER.md entries
- **Skills** — user-created skills → `~/.janus/skills/openclaw-imports/`
- **Command allowlist** — approval patterns
- **Messaging settings** — platform configs, allowed users, working directory
- **API keys** — allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
- **TTS assets** — workspace audio files
- **Workspace instructions** — AGENTS.md (with `--workspace-target`)

See `janus claw migrate --help` for all options, or use the `openclaw-migration` skill for an interactive agent-guided migration with dry-run previews.

---

## Contributing

We welcome contributions! See the [Contributing Guide](https://github.com/magnetoid/janus) for development setup, code style, and PR process.

Quick start for contributors — clone and go with `setup-janus.sh`:

```bash
git clone https://github.com/magnetoid/janus.git
cd janus-agent
./setup-janus.sh     # installs uv, creates venv, installs .[all], symlinks ~/.local/bin/janus
./janus              # auto-detects the venv, no need to `source` first
```

Manual path (equivalent to the above):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

---

## Community

- 💬 [Discord](https://discord.gg/NousResearch)
- 📚 [Skills Hub](https://agentskills.io)
- 🐛 [Issues](https://github.com/magnetoid/janus/issues)
- 🔌 [computer-use-linux](https://github.com/avifenesh/computer-use-linux) — Linux desktop-control MCP server for Janus and other MCP hosts, with AT-SPI accessibility trees, Wayland/X11 input, screenshots, and compositor window targeting.
- 🔌 [JanusClaw](https://github.com/AaronWong1999/janusclaw) — Community WeChat bridge: Run Janus Agent and OpenClaw on the same WeChat account.

---

## License

MIT — see [LICENSE](LICENSE).

Built by [Imba Labs](https://nousresearch.com).
