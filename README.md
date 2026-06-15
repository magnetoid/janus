<div align="center">
<pre>
     ██╗ █████╗ ███╗   ██╗██╗   ██╗███████╗
     ██║██╔══██╗████╗  ██║██║   ██║██╔════╝
     ██║███████║██╔██╗ ██║██║   ██║███████╗
██   ██║██╔══██║██║╚██╗██║██║   ██║╚════██║
╚█████╔╝██║  ██║██║ ╚████║╚██████╔╝███████║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
</pre>
<strong>The self-improving AI agent · by Imba Labs</strong>
</div>

# Janus Agent 

<p align="center">
  <a href="https://github.com/magnetoid/janus"><img src="https://img.shields.io/badge/Docs-GitHub-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://discord.gg/imbalabs"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/magnetoid/janus/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://github.com/magnetoid/janus"><img src="https://img.shields.io/badge/Built%20by-Imba%20Labs-blueviolet?style=for-the-badge" alt="Built by Imba Labs"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/Lang-中文-red?style=for-the-badge" alt="中文"></a>
</p>

**The self-improving AI agent built by [Imba Labs](https://github.com/magnetoid/janus).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — [Janus Portal](https://portal.imbalabs.com), [OpenRouter](https://openrouter.ai) (200+ models), [NovitaAI](https://novita.ai) (AI-native cloud for Model API, Agent Sandbox, and GPU Cloud), [NVIDIA NIM](https://build.nvidia.com) (Nemotron), [Xiaomi MiMo](https://platform.xiaomimimo.com), [z.ai/GLM](https://z.ai), [Kimi/Moonshot](https://platform.moonshot.ai), [MiniMax](https://www.minimax.io), [Hugging Face](https://huggingface.co), OpenAI, or your own endpoint. Switch with `janus model` — no code changes, no lock-in.

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
./setup-janus.sh
```

`setup-janus.sh` installs uv, creates the venv, installs the `.[all]` extra, and symlinks `janus` into `~/.local/bin`. (Paste the commands one per line — don't append a `#` comment after `./setup-janus.sh`, as interactive zsh treats the unquoted `.[all]` as a glob and aborts with `no matches found`.)

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
janus migrate hermes # Import a previous Hermes Agent install (~/.hermes)
janus claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
janus update       # Update to the latest version
janus doctor       # Diagnose any issues
```

📖 **[Full documentation →](website/docs/getting-started/quickstart.md)**

---

## Self-Learning & Proactive Agency

Janus doesn't just respond — it *learns* and *initiates*. These are unique to Janus:

| Capability | What it does | Try it |
| --- | --- | --- |
| **Daily memory journal** | Every saved memory is mirrored into an append-only, dated, git/Obsidian-readable `memories/daily/*.md` log. | `janus memory log` · `/memory log` |
| **Memory mining** | Re-reads a finished session and distills durable facts the agent didn't explicitly save. | `janus memory mine` · `/memory mine` |
| **Procedure mining** | Drafts reusable **skills** (`SKILL.md` + script) from multi-step work that succeeded — for your review. | `janus skills mine` |
| **Aspirations** | A long-term north-star Janus holds across sessions: drafts a roadmap and **checks in weekly** on your progress. | `janus aspire set "<goal>"` · `/aspire` |
| **Interest discovery** | Track a field (e.g. design); a weekly job researches the latest and **asks before** folding it into memory/skills. | `janus interest add "<field>"` · `/interest` |
| **Model-strengths routing** | Learns (via web research) which models lead per task, then feeds **Mixture-of-Agents** the best models for that task. | `janus models research <task>` |
| **Auto-mining** | Opt-in: on session end, memory/procedure mining fire automatically. | `memory.session_mining: true` in config |
| **Dialectic deliberation** | Two-headed reasoning on demand: an advocate and an opponent argue, an arbiter rules on the stronger argument — and reports when a question is genuinely **frame-dependent** (half full *and* half empty) instead of feigning confidence. | `deliberate` tool (`moa` toolset) |
| **Red-team learning gate** | Opt-in: mined facts/skills must survive an advocate/skeptic/arbiter exchange before being learned; session outcomes need a two-judge quorum. Bad input to the learning loop compounds — this filters it at the door. | `learning.dialectic.enabled: true` |
| **Evals** | Replayable behavior regression checks (prompt + deterministic assertions). Run before/after a skill, memory, or model change to verify the agent actually improved. | `janus evals init` · `janus evals run` |

The slash variants (`/memory`, `/aspire`, `/interest`) work from the messaging gateway (Telegram, Discord, …) and the TUI too.

---

## Skip the API-key collection — Janus Portal

Janus works with whatever provider you want — that's not changing. But if you'd rather not collect five separate API keys for the model, web search, image generation, TTS, and a cloud browser, **[Janus Portal](https://portal.imbalabs.com)** covers all of them under one subscription:

- **300+ models** — pick any of them with `/model <name>`
- **Tool Gateway** — web search (Firecrawl), image generation (FAL), text-to-speech (OpenAI), cloud browser (Browser Use), all routed through your sub. No extra accounts.

One command from a fresh install:

```bash
janus setup --portal
```

That logs you in via OAuth, sets Nous as your provider, and turns on the Tool Gateway. Check what's wired up any time with `janus portal info`. Full details on the [Tool Gateway docs page](website/docs/user-guide/features/tool-gateway.md).

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

For the full command lists, see the [CLI guide](website/docs/reference/cli-commands.md) and the [Messaging Gateway guide](website/docs/user-guide/messaging/index.md).

---

## Documentation

All documentation lives at **[github.com/magnetoid/janus](website/docs/getting-started/quickstart.md)**:

| Section                                                                                             | What's Covered                                             |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [Quickstart](website/docs/getting-started/quickstart.md)                 | Install → setup → first conversation in 2 minutes          |
| [CLI Usage](website/docs/reference/cli-commands.md)                              | Commands, keybindings, personalities, sessions             |
| [Configuration](website/docs/user-guide/configuration.md)                | Config file, providers, models, all options                |
| [Messaging Gateway](website/docs/user-guide/messaging/index.md)                | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| [Security](website/docs/user-guide/security.md)                          | Command approval, DM pairing, container isolation          |
| [Tools & Toolsets](website/docs/user-guide/features/tools.md)            | 40+ tools, toolset system, terminal backends               |
| [Skills System](website/docs/user-guide/features/skills.md)              | Procedural memory, Skills Hub, creating skills             |
| [Memory](website/docs/user-guide/features/memory.md)                     | Persistent memory, user profiles, best practices           |
| [MCP Integration](website/docs/user-guide/features/mcp.md)               | Connect any MCP server for extended capabilities           |
| [Cron Scheduling](website/docs/user-guide/features/cron.md)              | Scheduled tasks with platform delivery                     |
| [Context Files](website/docs/user-guide/features/context-files.md)       | Project context that shapes every conversation             |
| [Architecture](website/docs/developer-guide/architecture.md)             | Project structure, agent loop, key classes                 |
| [Contributing](website/docs/developer-guide/contributing.md)             | Development setup, PR process, code style                  |
| [CLI Reference](website/docs/reference/cli-commands.md)                  | All commands and flags                                     |
| [Environment Variables](website/docs/reference/environment-variables.md) | Complete env var reference                                 |

---

## Upgrading from Hermes Agent

Janus is the new name for **Hermes Agent** — same agent, same on-disk layout, just rebranded. If you have an older install with data in `~/.hermes`, Janus imports it for you (non-destructively — your `~/.hermes` is left untouched until you choose to delete it).

**During first-time setup:** `janus setup` detects `~/.hermes` (or `$HERMES_HOME`) and offers to import your config, memory, skills, sessions, and learning data before configuration begins, then offers to remove the old directory.

**Anytime after install:**

```bash
janus migrate hermes              # Preview, then import ~/.hermes into ~/.janus
janus migrate hermes --dry-run    # Preview only — no changes
janus migrate hermes --overwrite  # Overwrite items that already exist in Janus
janus migrate hermes --source PATH  # Point at a Hermes home elsewhere
```

Top-level directories (`memories/`, `skills/`, `sessions/`, `learning/`, …) are **merged** (new files copied in, existing ones kept); singular files (`config.yaml`, `.env`) are skipped if already present unless `--overwrite`. Inside `config.yaml`/`.env`, `HERMES_HOME` becomes `JANUS_HOME` and `.hermes` paths become `.janus` — but **Nous Hermes model IDs** (`hermes-3-*`, `Hermes-4-*`, `nous-hermes-*`) and the `nous` provider slug are preserved so your model config keeps working.

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

We welcome contributions! See the [Contributing Guide](website/docs/developer-guide/contributing.md) for development setup, code style, and PR process.

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

- 💬 [Discord](https://discord.gg/imbalabs)
- 📚 [Skills Hub](https://agentskills.io)
- 🐛 [Issues](https://github.com/magnetoid/janus/issues)

- 

---

## License

MIT — see [LICENSE](LICENSE).

Built by [Imba Labs](https://imbalabs.com).
