---
title: "HexStrike AI — MCP security-tool orchestration (0x4m4/hexstrike-ai)"
type: entity
tags: [tool, llm-automation, pentest, mcp, reference]
keywords: [HexStrike, hexstrike-ai, MCP, 150 tools, FastMCP, 0x4m4, MIT]
related:
  - sources/github-hexstrike-ai.md
  - sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md
  - concepts/ai-pentest-harness-landscape.md
  - concepts/security-tool-orchestration-determinants.md
  - concepts/llm-pentest-automation.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/agent-vm-sandboxing.md
  - entities/tools/strix.md
  - entities/tools/cyberstrike.md
  - entities/tools/pentest-ai.md
  - entities/tools/cai-framework.md
  - entities/tools/pentestgpt.md
  - sources/github-cai-framework.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
phase_0_verdict: "REFERENCE 2026-08-02 — MIT SPDX; desk Phase-0 only; no clone until operator orders; no OS sandbox (MCP host runs tools)"
wire_status: deferred
wire_target: "Do not install host MCP server without operator OK + lab VM"
---

## Relations

- @sources/github-hexstrike-ai.md — desk Phase-0 provenance
- @sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md — empirical orchestration study using HexStrike
- @concepts/ai-pentest-harness-landscape.md — peer row in harness matrix
- @concepts/security-tool-orchestration-determinants.md — driving-client effect findings
- @concepts/llm-pentest-automation.md — Tier-1/2 methodology
- @concepts/owned-target-whitehat-lab.md — practice surface
- @concepts/agent-vm-sandboxing.md — required if tools execute on host
- @entities/tools/strix.md — Apache sandbox peer (prefer when isolation matters)
- @entities/tools/cyberstrike.md — AGPL full-product peer
- @entities/tools/pentest-ai.md — MIT MCP peer product

## Raw Concept

Desk Phase-0 (2026-08-02) for harness peer comparison. Canonical repo: [github.com/0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai). **No local clone** (REFERENCE default; size small but not first-line for this wiki).

## Narrative

### What it is

HexStrike AI is an **MCP server** that exposes 150+ offensive/security tools and multi-agent orchestration to MCP-compatible clients (Claude, GPT, Copilot, etc.). Marketing shape: autonomous pentest / bug-bounty / CTF automation via tool-calling, not a single TUI product like CyberStrike. [CONFIRMED — README head 2026-08-02]

### Desk signals

| Signal | Value |
|--------|--------|
| License | **MIT** (SPDX) [CONFIRMED — GitHub API] |
| Stars | ~10.7k (2026-08-02) |
| Pushed | 2026-04-27 |
| GitHub size | ~2.4MB (small) |
| Shape | MCP server + 12+ agents + large tool catalog |
| Containment | **No first-class OS sandbox** — README recommends isolated envs / dedicated security testing VMs; tools run under the MCP server process model [TENTATIVE — README ethics + isolation language] |
| Scope model | Soft / operator + MCP client gates; authorized-use section present [TENTATIVE] |
| Local LLM | Client-dependent (MCP client chooses model); not Ollama-first like CyberStrike/Strix docs [TENTATIVE] |

### Failure modes

1. **Tool blast radius on host** — 150+ tools (network, web, cloud, binary) with network access is a runaway risk without VM + egress allowlist.
2. **Star-count bias** — popularity ≠ hard scope enforcement.
3. **Fork noise** — many third-party HexStrike forks; use **0x4m4/hexstrike-ai** as canonical unless a fork has a clear license + audit.
4. **MCP trust** — binding HexStrike into a daily-driver Claude Desktop/Cursor without isolation violates agent-containment policy.

### Phase-0 verdict

**REFERENCE (2026-08-02)** — document for comparison and for the existing arXiv HexStrike orchestration study. **Do not clone or host-install** until operator orders a full Phase-0. Prefer @entities/tools/strix.md (Docker sandbox + Apache) or MIT @entities/tools/pentest-ai-agents.md for first-line adopt paths.

If later cloned: re-run LICENSE file read, install-path audit (no curl\|sh), and lab-only first runs.

## Snippets

```text
Canonical: github.com/0x4m4/hexstrike-ai — MIT — MCP + 150+ tools
Verdict: REFERENCE — no clone 2026-08-02
Related study: arXiv 2607.02873 (HexStrike-AI orchestration determinants)
```
