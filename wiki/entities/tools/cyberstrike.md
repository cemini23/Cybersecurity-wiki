---
title: "CyberStrike — AI-augmented offensive security harness"
type: entity
tags: [tool, llm-automation, pentest, red-team, bug-bounty, agpl, conditional-go, mcp, ollama]
keywords: [CyberStrike, cyberstrike.io, Bolt, HackBrowser, scope_check, AGPL-3.0, OpenCode fork, anomalyco]
related:
  - sources/github-cyberstrike.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/operator-lab-playbook.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/pre-release-product-pentest.md
  - concepts/bug-bounty.md
  - concepts/agent-vm-sandboxing.md
  - concepts/responsible-disclosure.md
  - concepts/agentic-offensive-security-kill-chain.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/pentest-ai.md
  - entities/tools/strix.md
  - entities/tools/ollama.md
  - entities/tools/iron-proxy.md
  - entities/tools/cua.md
  - concepts/ai-pentest-harness-landscape.md
  - sources/github-strix.md
  - entities/tools/pentestgpt.md
  - entities/tools/cai-framework.md
  - entities/tools/hexstrike-ai.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
phase_0_verdict: "CONDITIONAL-GO 2026-08-02 — AGPL-3.0 verified; shallow clone ~219MB; no host npm -g; VM/Docker only; scope_check is advisory not hard-gate"
wire_status: deferred
wire_target: "Ask before host CLI/MCP wire; lab VM + written scope required; AGPL network clause for any SaaS/embed"
---

## Relations
- @entities/tools/cai-framework.md
- @entities/tools/pentestgpt.md
- @sources/github-strix.md — Strix upstream source stub
- @sources/github-cyberstrike.md — Phase-0 provenance (repo snapshot + LICENSE/SECURITY notes)
- @concepts/llm-pentest-automation.md — Tier-1/2 methodology; CyberStrike is a productized sibling harness
- @concepts/ai-for-cybersecurity.md — LLM × offensive tooling context
- @concepts/operator-lab-playbook.md — friend/operator start-here path; CyberStrike sits in the AI + Tier-2 lane
- @concepts/local-abliterated-llm-pentest-stack.md — Ollama / LM Studio offline path CyberStrike documents
- @concepts/owned-target-whitehat-lab.md — required practice surface before any public program use
- @concepts/pre-release-product-pentest.md — owned-product lane (authorized)
- @concepts/bug-bounty.md — only with program scope + rate limits; automation duplicate risk
- @concepts/agent-vm-sandboxing.md — **required** — upstream SECURITY.md: no sandbox
- @concepts/responsible-disclosure.md — ethics floor
- @concepts/agentic-offensive-security-kill-chain.md — agent-phishing / kill-chain risk class for agentic pentest tools
- @entities/tools/pentest-ai-agents.md — MIT Claude Code agent collection (lighter; compare before adopting both)
- @entities/tools/pentest-ai.md — MIT MCP + `ptai` CLI sibling product
- @entities/tools/strix.md — Apache-2.0 Docker-sandbox peer (CONDITIONAL-GO Phase-0 clone; contrast containment)
- @concepts/ai-pentest-harness-landscape.md — harness decision matrix (license / containment / lane)
- @entities/tools/ollama.md — local inference CyberStrike can target
- @entities/tools/iron-proxy.md — egress allowlist for lab / Bolt workers
- @entities/tools/cua.md — Apple-side VM isolation option

## Raw Concept

Phase-0 audit 2026-08-02 for operator-lab coverage (friend beefy-box / owned-server / product / bounty path). Repo: [github.com/CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike). npm: `@cyberstrike-io/cyberstrike`. Site: https://cyberstrike.io. Default branch `main`; development branch `dev` (AGENTS.md).

**Local adoption (clone only):** `raw-sources/repos/CyberStrike` — shallow `--depth 1` on `dev` @ `93a51658` (2026-07-23 tip at clone); ~219MB; ~7,656 `SKILL.md` files under `.cyberstrike/skill/`. Host CLI **not** installed (see brief).

## Narrative

### What it is

CyberStrike is an **AI-augmented offensive security harness** (TypeScript/Bun monorepo): TUI + optional web UI, 13+ specialized agents, large skill corpus (OWASP/WSTG, CIS, MITRE, post-exploit lanes), built-in tools, MCP integrations, HackBrowser, and **Bolt** remote tool execution (Ed25519-paired servers). It is explicitly marketed for pentest / bug bounty / red-team automation and supports **150+ LLM providers** including **Ollama** and **LM Studio** for offline use. [CONFIRMED — README + local clone]

### Provenance

CHANGELOG states it is a **fork of [anomalyco/opencode](https://github.com/anomalyco/opencode)** rebranded for offensive security (`opencode` → `cyberstrike` bin, unused OpenCode workflows removed). CI container docs still reference `ghcr.io/anomalyco` in places — treat as fork residue, not a second product. [CONFIRMED — CHANGELOG.md]

### License

**AGPL-3.0** (SPDX via GitHub API + LICENSE file copyright Cyberstrike 2026). Fine for personal/lab laptop use of unmodified binaries. **Red flag for product/SaaS:** network use of a modified CyberStrike (or embedding it in a hosted service) can trigger AGPL source-disclosure obligations. Do not embed in a closed commercial product without legal review. [CONFIRMED]

### Maturity (at audit)

| Signal | Value |
|--------|--------|
| Stars / forks | ~1.5k★ / ~239 forks (2026-08-02) |
| Created | 2026-02-14 |
| Activity | High (marketing site, Discord, npm publish workflow, frequent pushes) |
| Package version (in-tree) | `packages/cyberstrike` **1.1.15** |
| Bus factor | Org `CyberStrikeus` + commercial site — better than solo gist, still young product |

### Failure mode for class (LLM pentest harness)

Most-likely failure: **scope / containment**, not missing scanners.

1. **No sandbox** — `SECURITY.md`: permission prompts are UX awareness, not isolation. Shell, file, browser, and tool execution run with user privileges. [CONFIRMED]
2. **`scope_check` is advisory** — tool warns `OUT OF SCOPE` / “Do NOT perform active testing” but does not hard-block bash/nmap/nuclei. Methodology context *reminds* agents to call `scope_check`; enforcement is model + operator dependent. [CONFIRMED — `packages/cyberstrike/src/tool/scope-check.ts` + `methodology/context.ts`]
3. **Post-exploit + Bolt blast radius** — AWS/Azure/K8s/Windows/macOS/CI-CD hooks and remote Bolt workers expand impact if credentials or network path are wrong.
4. **Server / Cloudflare Tunnel** — web UI can be exposed; password optional with warning. Localhost convenience bypass for auth is documented — treat remote exposure as Tier-2 API.
5. **Catalog inflation** — “5,300+ models / 7,600+ skills” is inventory scale; skill quality and duplicate bounty noise still need human validation (@concepts/bug-bounty.md).

### Wiki coverage comparison

| Dimension | CyberStrike | @entities/tools/pentest-ai-agents.md | @entities/tools/pentest-ai.md |
|-----------|-------------|--------------------------------------|-------------------------------|
| License | AGPL-3.0 | MIT | MIT |
| Shape | Full TUI/web product + skills + Bolt | Claude Code YAML agents | MCP + `ptai` CLI |
| Local LLM | Ollama / LM Studio first-class | Re-point prompts | BYO LLM |
| Scope model | `--scope` + advisory `scope_check` | Tier 1/2 + YAML `requires_scope` | `strict_scope` / intensity flags |
| Containment | Explicitly none (VM recommended) | Claude Code permission UX | MCP client gates |

**Do not treat as drop-in replacement** for the MIT tools. Prefer CyberStrike when the friend wants a packaged multi-agent UI + Bolt remote workers + offline Ollama; prefer pentest-ai-agents / pentest-ai when AGPL or host install risk is unacceptable.

### Landscape position

Full pick matrix: @concepts/ai-pentest-harness-landscape.md.

| vs peer | CyberStrike stance |
|---------|-------------------|
| Strix (Apache-2.0, Docker sandbox, PoC validation) | Strix wins on license + upstream isolation; CyberStrike wins on skill catalog + Bolt + full TUI product |
| pentest-ai-agents (MIT YAML) | Prefer agents when already on Claude Code and AGPL is unacceptable |
| pentest-ai (MIT MCP) | Prefer when MCP + `ptai` is the orchestration surface |

**Lane defaults for this entity:** lab VM first; owned product only inside isolated VM; bounty only with pinned program scope. **CONDITIONAL-GO unchanged** — no host install, no hard scope gate.

### Phase-0 verdict

**CONDITIONAL-GO (2026-08-02)** for **authorized owned-lab / own-product / in-scope bounty** only, if:

- Run inside **VM or Docker** (@concepts/agent-vm-sandboxing.md), never bare host next to personal data
- Written scope before active testing (@concepts/owned-target-whitehat-lab.md)
- No host `npm i -g` until operator explicitly accepts AGPL + containment
- No federation MCP wire without a separate ask
- Bolt workers only on owned/trusted networks (+ @entities/tools/iron-proxy.md egress where useful)

**Not adopted as host CLI.** Clone under `raw-sources/repos/` is REFERENCE + lab source tree.

## Snippets

```bash
# Phase-0 verification (2026-08-02)
gh api repos/CyberStrikeus/CyberStrike --jq '.license.spdx_id'   # AGPL-3.0

# Local shallow clone (this wiki)
# raw-sources/repos/CyberStrike  (~219MB, branch dev @ 93a51658)

# Upstream quick start (LAB VM ONLY — do not run on personal host)
# npm i -g @cyberstrike-io/cyberstrike@latest && cyberstrike
```

From `SECURITY.md`:

> CyberStrike does **not** sandbox the agent. The permission system exists as a UX feature … If you need true isolation, run CyberStrike inside a Docker container or VM.

## Dead Ends

- **Assuming scope_check hard-blocks tools** — it warns; bash still runs if the agent/operator proceeds.
- **`npm i -g` on the MacBook host “just to try”** — violates containment gate; use a disposable VM.
- **Embedding CyberStrike in a closed SaaS / product** without AGPL counsel — network clause risk.
- **Equating skill count with engagement quality** — same duplicate-factory risk as unscoped Tier-2 automation (@concepts/llm-pentest-automation.md).
