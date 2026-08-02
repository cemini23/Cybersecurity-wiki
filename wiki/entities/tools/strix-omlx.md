---
title: "strix-omlx — Strix → local OMLX / Ollama / SGLang wrapper"
type: entity
tags: [tool, llm-automation, pentest, apple-silicon, omlx, ollama, abliterated, conditional-go]
keywords: [strix-omlx, sw30labs, OMLX, Heretic, MiniMax-M2, Apple Silicon, setup scripts, local LLM]
related:
  - sources/github-strix-omlx.md
  - entities/tools/strix.md
  - sources/github-strix.md
  - concepts/ai-pentest-harness-landscape.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/ollama.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/operator-lab-playbook.md
  - concepts/responsible-disclosure.md
  - concepts/agent-vm-sandboxing.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
phase_0_verdict: "CONDITIONAL-GO 2026-08-02 — Apache-2.0; shallow clone ~3.3MB; thin setup scripts only; no host install without operator OK"
wire_status: deferred
wire_target: "Ask before running setup-*.sh (pip install strix-agent into .strix-venv) or PATH; prefer reviewed Strix install + manual cli-config.json"
---

## Relations

- @sources/github-strix-omlx.md — Phase-0 provenance (clone path + sha)
- @entities/tools/strix.md — upstream harness this wraps (CONDITIONAL-GO)
- @sources/github-strix.md — Strix Phase-0 source snapshot
- @concepts/ai-pentest-harness-landscape.md — harness pick matrix; local-backend path
- @concepts/local-abliterated-llm-pentest-stack.md — OMLX / Ollama / abliterated model doctrine
- @entities/tools/ollama.md — Ollama backend script path
- @concepts/owned-target-whitehat-lab.md — only authorized/owned targets
- @concepts/operator-lab-playbook.md — operator start-here
- @concepts/responsible-disclosure.md — ethics floor
- @concepts/agent-vm-sandboxing.md — Docker sandbox still required for Strix tools

## Raw Concept

Phase-0 audit 2026-08-02 (operator-ordered). Repo: [github.com/sw30labs/strix-omlx](https://github.com/sw30labs/strix-omlx). Thin wrapper scripts that point **upstream Strix** at a **local** OpenAI-compatible endpoint (OMLX on Apple Silicon, Ollama, or SGLang on NVIDIA DGX) with an abliterated (“Heretic’d”) model.

**Local adoption (clone only):** `raw-sources/repos/strix-omlx` — shallow `--depth 1` on `main` @ `b623b9f` (2026-08-02 tip at clone); ~3.3MB. Host install **not** run.

## Narrative

### What it is

**strix-omlx is not Strix.** It is a small set of bash setup scripts + a generated `run-strix.sh` launcher around [usestrix/strix](https://github.com/usestrix/strix). All agent, tool, and sandbox behavior remains upstream. [CONFIRMED — README]

| Script | Backend | Default endpoint |
|--------|---------|------------------|
| `setup-strix-omlx.sh` | **OMLX** (local MLX, Apple Silicon) | `http://127.0.0.1:8000/v1` |
| `setup-strix-ollama.sh` | Ollama | `http://localhost:11434/v1` |
| `setup-strix-sglang-dgx.sh` | SGLang (NVIDIA DGX) | `http://localhost:30000/v1` |
| `run-strix.sh` | Generated; sources `~/.strix/cli-config.json` env | — |

OMLX / Ollama / SGLang are reached via LiteLLM’s `openai/` routing (`STRIX_LLM=openai/<model>`, `LLM_API_BASE`, `LLM_API_KEY`). Default OMLX model id documented: `MiniMax-M2.7-ultra-uncensored-heretic-oQ4-MLX` (Heretic abliteration of a MiniMax-M2 checkpoint). [CONFIRMED — README + setup script]

### Provenance / packaging

| Signal | Value |
|--------|--------|
| License | **Apache-2.0** (SPDX + LICENSE file; matches upstream Strix) [CONFIRMED] |
| Stars / size | **0★** / GitHub size ~1.1MB; local shallow clone ~3.3MB (2026-08-02) |
| Pushed | 2026-07-05 |
| Default branch | `main` @ `b623b9f` |
| Bus factor | Single-org thin wrapper (`sw30labs`); depends entirely on Strix + your local inference |

### How Strix → OMLX / Ollama / Heretic is wired

1. Operator already runs an OpenAI-compatible local server (OMLX admin dashboard at `:8000/admin/dashboard`, or Ollama, or SGLang).
2. Setup script checks Python ≥3.12, Docker (Strix sandbox), and (for OMLX path) macOS/Apple Silicon preference.
3. Script creates project `.strix-venv`, runs `pip install strix-agent`, writes `~/.strix/cli-config.json` with `STRIX_LLM` / `LLM_API_BASE` / `LLM_API_KEY`, generates `run-strix.sh`.
4. `run-strix.sh` activates venv, exports config env, execs `strix "$@"`.

This is **configuration glue**, not a new harness. Tool execution still happens inside Strix’s Docker sandbox (`usestrix/strix-sandbox`). [CONFIRMED — local clone]

### Failure modes (class: local-LLM wiring wrapper)

1. **Apple-primary OMLX path** — `setup-strix-omlx.sh` is for macOS Apple Silicon + OMLX/MLX. Ollama and SGLang scripts cover Linux/NVIDIA; do not assume one script works everywhere. [CONFIRMED]
2. **`pip install strix-agent` inside setup** — not curl\|sh of strix.ai, but still a **host-side install** into a local venv. Federation rule: do not run setup scripts without operator OK; prefer already-reviewed Strix install + hand-written `cli-config.json`. [CONFIRMED]
3. **No `STRIX_TELEMETRY=0` in wrapper** — setup scripts do not disable upstream Strix PostHog/Scarf telemetry. Operator must set `STRIX_TELEMETRY=0` manually (see @entities/tools/strix.md). [CONFIRMED — no TELEMETRY in clone]
4. **Abliterated model sourcing ethics** — Heretic/abliterated weights lower refusal; they do **not** change authorization. Only owned lab / written scope / in-program bounty. Do not treat “uncensored” as permission. Weight provenance and license of third-party abliterated uploads remain operator responsibility. [TENTATIVE — policy; not a code defect]
5. **Hardware reality** — README demos M3 Ultra-class unified memory (~245GB resident for the default MiniMax quant). Smaller Macs will not host that model; pick a VRAM/unified-memory-appropriate quant (@concepts/local-abliterated-llm-pentest-stack.md). [CONFIRMED — README screenshots]
6. **Soft scope remains Strix’s** — wrapper does not add hard target allowlists. Unauthorized `run-strix.sh --target https://…` is still illegal/out of policy.
7. **Home-dir config write** — setup writes `~/.strix/cli-config.json` (may include local API key default `test`). Review before running on a shared machine.

### Phase-0 verdict

**CONDITIONAL-GO (2026-08-02)** — clone and document only.

| Gate | Status |
|------|--------|
| LICENSE clear (Apache-2.0) | Pass |
| Size reasonable | Pass (~3.3MB) |
| Shallow clone | Done — `raw-sources/repos/strix-omlx` @ `b623b9f` |
| Host setup / pip / PATH | **Not done** — ask operator first |
| Telemetry off for lab | Operator must set on Strix side |
| First targets | Owned Juice Shop / DVWA / own staging only |

**REFERENCE alternative:** skip the scripts; manually point Strix at Ollama/OMLX per @entities/tools/strix.md + @concepts/local-abliterated-llm-pentest-stack.md.

### Wiki coverage comparison

Prefer **this wrapper** only when you want scripted OMLX/Ollama/SGLang `cli-config.json` generation. Prefer **manual Strix config** when you already have a reviewed install and refuse unsolicited `pip install`. Prefer **CyberStrike** only on a disposable lab VM (AGPL, no sandbox). Prefer **MIT agents** when staying inside Claude Code.

## Snippets

```text
# Phase-0 clone only (already done under raw-sources/repos/strix-omlx)
# Do NOT run setup-*.sh without operator approval.

# Manual equivalent (preferred over setup script):
export STRIX_TELEMETRY=0
export STRIX_LLM=openai/<your-local-model-id>
export LLM_API_BASE=http://127.0.0.1:8000/v1   # or :11434/v1 for Ollama
export LLM_API_KEY=test
# then: strix --target <owned-only>
```

```json
// ~/.strix/cli-config.json shape written by setup-strix-omlx.sh
{
  "env": {
    "STRIX_LLM": "openai/MiniMax-M2.7-ultra-uncensored-heretic-oQ4-MLX",
    "LLM_API_BASE": "http://127.0.0.1:8000/v1",
    "LLM_API_KEY": "test"
  }
}
```

[Source: github.com/sw30labs/strix-omlx README + setup-strix-omlx.sh @ b623b9f]

## Dead Ends

- **Running setup on daily-driver without Docker** — scripts exit; Strix requires sandbox image.
- **Assuming 0★ means malware** — thin wrapper; still verify LICENSE and script body (done Phase-0).
- **curl\|sh Strix install “because the wrapper is fine”** — still forbidden; wrapper uses pip, not strix.ai install script.
