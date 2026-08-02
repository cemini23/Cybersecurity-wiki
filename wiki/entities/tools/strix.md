---
title: "Strix — multi-agent AI pentest harness (usestrix/strix)"
type: entity
tags: [tool, llm-automation, pentest, red-team, apache, docker, sandbox, conditional-go]
keywords: [Strix, usestrix, Docker sandbox, PoC validation, Ollama, Apache-2.0, strix-agent, PostHog, Scarf]
related:
  - sources/github-strix.md
  - concepts/ai-pentest-harness-landscape.md
  - concepts/llm-pentest-automation.md
  - concepts/operator-lab-playbook.md
  - concepts/agent-vm-sandboxing.md
  - concepts/responsible-disclosure.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/bug-bounty.md
  - concepts/pre-release-product-pentest.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/cyberstrike.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/pentest-ai.md
  - entities/tools/ollama.md
  - sources/github-strix-omlx.md
  - entities/tools/strix-omlx.md
  - entities/tools/hexstrike-ai.md
  - entities/tools/cai-framework.md
  - entities/tools/pentestgpt.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
phase_0_verdict: "CONDITIONAL-GO 2026-08-02 — Apache-2.0 verified; shallow clone ~11MB; Docker sandbox real; telemetry default-on; no curl|sh; no host pipx until operator OK"
wire_status: deferred
wire_target: "Ask before host pipx/CLI or MCP wire; Docker + written scope required; STRIX_TELEMETRY=0 for lab"
---

## Relations
- @entities/tools/strix-omlx.md — local OMLX/Ollama/SGLang setup wrapper (CONDITIONAL-GO clone)
- @sources/github-strix-omlx.md — Strix local MLX/Ollama wrapper source
- @entities/tools/hexstrike-ai.md — MIT MCP peer (REFERENCE)
- @entities/tools/cai-framework.md — dual-license framework peer (REFERENCE)
- @entities/tools/pentestgpt.md — MIT research agent peer (REFERENCE)
- @sources/github-strix.md — Phase-0 provenance (repo snapshot + LICENSE/sandbox notes)
- @concepts/ai-pentest-harness-landscape.md — harness pick matrix (CyberStrike vs Strix vs MIT peers)
- @concepts/llm-pentest-automation.md — Tier-1/2 methodology umbrella
- @concepts/operator-lab-playbook.md — operator start-here; Strix is sandbox-first orchestration
- @concepts/agent-vm-sandboxing.md — complements Docker sandbox; still isolate lab networks
- @concepts/responsible-disclosure.md — ethics floor
- @concepts/owned-target-whitehat-lab.md — default practice surface
- @concepts/bug-bounty.md — only with program scope
- @concepts/pre-release-product-pentest.md — owned-product lane
- @concepts/local-abliterated-llm-pentest-stack.md — Ollama / local LLM re-point path
- @entities/tools/cyberstrike.md — AGPL no-sandbox sibling product (contrast)
- @entities/tools/pentest-ai-agents.md — MIT YAML agents alternative
- @entities/tools/pentest-ai.md — MIT MCP alternative
- @entities/tools/ollama.md — local inference path Strix can use

## Raw Concept

Phase-0 audit 2026-08-02 (operator-ordered full clone). Repo: [github.com/usestrix/strix](https://github.com/usestrix/strix). Site: https://strix.ai · Platform: https://app.strix.ai · Docs: https://docs.strix.ai · PyPI: `strix-agent`.

**Local adoption (clone only):** `raw-sources/repos/strix` — shallow `--depth 1` on `main` @ `dbc427d` (2026-08-02 tip at clone); ~11MB. Host CLI **not** installed (see brief).

## Narrative

### What it is

Strix is an **open-source AI multi-agent penetration testing harness** (Python ≥3.12, Textual TUI + local web viewer): agents run offensive tools **inside a Kali-based Docker sandbox**, with HTTP proxy (Caido), browser automation, shell, SAST/DAST tooling, skills corpus, and a PoC-oriented finding loop. Supports many LLM providers via LiteLLM including **Ollama** / OpenAI-compatible local endpoints. Separate commercial **Strix Platform** (`app.strix.ai`) is optional SaaS — not required for OSS CLI. [CONFIRMED — README + local clone]

### Provenance / packaging

| Signal | Value |
|--------|--------|
| Package name | `strix-agent` **1.4.1** (`pyproject.toml`) |
| CLI entry | `strix = strix.interface.main:main` |
| Default sandbox image | `ghcr.io/usestrix/strix-sandbox:1.2.0` (`STRIX_IMAGE`) |
| Runtime backend | `docker` (`STRIX_RUNTIME_BACKEND`) |
| Copyright (LICENSE) | Copyright 2025 OmniSecure Inc. |
| Classifier | Development Status :: 3 - Alpha |

### License

**Apache-2.0** (SPDX via GitHub API + LICENSE file + `pyproject.toml` `license = "Apache-2.0"`). Permissive for lab and most product consulting use; still respect NOTICE/attribution. Prefer over CyberStrike AGPL when embedding risk matters. [CONFIRMED]

### Maturity (at audit)

| Signal | Value |
|--------|--------|
| Stars / forks | ~46.6k★ / ~4.9k forks (2026-08-02) |
| Created | 2025-08-05 |
| Activity | High (push same day as audit; active docs / GHCR image / PyPI) |
| Bus factor | Org `usestrix` + commercial platform — strong community signal; still Alpha classifier |
| Star caution | Very high star count — treat as popularity, not proof of safe scope enforcement |

### Failure mode for class (LLM pentest harness)

Most-likely failure: **soft scope + default egress + telemetry**, not “missing scanners.”

1. **Docker sandbox ≠ authorized testing** — tools (nmap, nuclei, sqlmap, etc.) run in-container with network to reach targets. Isolation protects the *host process model*; it does **not** hard-block OOS internet hosts. [CONFIRMED — `docs/tools/sandbox.mdx` + `strix/runtime/docker_client.py`]
2. **Scope is instruction / mode soft** — `--instruction` / `--instruction-file` and PR `--scope-mode diff` guide agents; no CyberStrike-style hard allowlist gate found. Operator must pin targets + written scope. [CONFIRMED — docs/usage/instructions.mdx]
3. **Telemetry default-on** — PostHog + Scarf (and optional OTEL). Claims anonymized aggregates; still disable for sensitive labs: `STRIX_TELEMETRY=0`. [CONFIRMED — `strix/telemetry/README.md` + settings]
4. **`curl \| bash` install path** — README/docs lead with `curl -sSL https://strix.ai/install | bash`. Federation policy: **do not** use curl\|sh. Prefer reviewed `pipx install strix-agent` / `uv` from PyPI or editable install from this clone after operator OK. [CONFIRMED]
5. **Local LLM capability gap** — upstream docs warn most local models &lt;70B struggle with required native `tool_calls`; cloud models recommended for critical assessments. [CONFIRMED — docs/llm-providers/local.mdx]
6. **Sandbox still powerful** — container user `pentester` has sudo group; nmap gets `cap_net_raw`/`cap_net_admin`; first run pulls large Kali tool image. Use lab VLAN / `STRIX_DOCKER_SANDBOX_NETWORK` + resource caps (`STRIX_SANDBOX_MEM_LIMIT`, etc.).
7. **Cloud platform confusion** — OSS CLI vs `app.strix.ai` SaaS; do not paste engagement secrets into the hosted product without a separate data-handling decision.

### Wiki coverage comparison

| Dimension | Strix | @entities/tools/cyberstrike.md | @entities/tools/pentest-ai-agents.md |
|-----------|-------|--------------------------------|--------------------------------------|
| License | Apache-2.0 | AGPL-3.0 | MIT |
| Containment | Docker sandbox (upstream) | None (VM required) | Claude Code UX |
| Scope model | Instructions + PR diff-scope (soft) | Advisory `scope_check` | Tier 1/2 + YAML `requires_scope` |
| Local LLM | Ollama / OpenAI-compatible (capability caveats) | Ollama / LM Studio | Re-point prompts |
| Clone size (shallow) | ~11MB source | ~219MB | smaller agent YAML sets |

Prefer **Strix** when Apache + Docker sandbox matter; prefer **CyberStrike** for Bolt/skill-catalog TUI on a disposable VM; prefer **MIT agents** when you already live in Claude Code and want minimal new runtime.

### Landscape position

Full pick matrix: @concepts/ai-pentest-harness-landscape.md.

### Phase-0 verdict

**CONDITIONAL-GO (2026-08-02)**

- **Done:** LICENSE verified; shallow clone under `raw-sources/repos/strix`; sandbox/telemetry/install failure modes filed
- **Not done (human gates):** Docker Desktop/engine on lab host; install via pipx/uv (**not** curl\|sh); `STRIX_TELEMETRY=0`; written scope; first runs only against owned Juice Shop / staging
- **Wire:** deferred — ask before host CLI, PATH install, or MCP/Cursor wire
- **Do not:** host desktop “quick try” against public internet; mix bounty OOS with lab in one unscoped session

## Snippets

```text
Repo: https://github.com/usestrix/strix
SPDX: Apache-2.0
Package: strix-agent 1.4.1
Local: raw-sources/repos/strix @ dbc427d (main, depth=1, ~11MB)
Sandbox image default: ghcr.io/usestrix/strix-sandbox:1.2.0
Telemetry off: export STRIX_TELEMETRY=0
Local LLM example:
  export STRIX_LLM="ollama/qwen3-vl"
  export LLM_API_BASE="http://localhost:11434"
```

## Dead Ends

- **curl\|sh bootstrap** — policy NO; use pipx/uv or clone editable after review.
- **Assuming Docker sandbox = hard scope** — container can still scan whatever the agent targets.
- **Telemetry left at default in sensitive labs** — set `STRIX_TELEMETRY=0`.
- **Treating 46k★ as GO alone** — popularity ≠ safe autonomous spray.
