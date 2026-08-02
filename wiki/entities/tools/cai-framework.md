---
title: "CAI — Cybersecurity AI framework (aliasrobotics/cai)"
type: entity
tags: [tool, llm-automation, pentest, multi-agent, reference, dual-license]
keywords: [CAI, aliasrobotics, cai-framework, Cybersecurity AI, research license, multi-agent]
related:
  - sources/github-cai-framework.md
  - concepts/ai-pentest-harness-landscape.md
  - concepts/llm-pentest-automation.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/agent-vm-sandboxing.md
  - entities/tools/strix.md
  - entities/tools/cyberstrike.md
  - entities/tools/hexstrike-ai.md
  - entities/tools/pentestgpt.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
phase_0_verdict: "REFERENCE 2026-08-02 — dual MIT + proprietary research-use license; large tree; no clone; commercial use restricted without Alias license"
wire_status: deferred
wire_target: "No host install; re-audit license before any lab trial"
---

## Relations

- @sources/github-cai-framework.md — desk Phase-0 provenance
- @concepts/ai-pentest-harness-landscape.md — peer row
- @concepts/llm-pentest-automation.md — Tier-1/2 methodology umbrella
- @concepts/owned-target-whitehat-lab.md — only authorized surfaces if ever trialed
- @concepts/agent-vm-sandboxing.md — isolation floor for multi-agent frameworks
- @entities/tools/strix.md — Apache sandbox peer
- @entities/tools/cyberstrike.md — AGPL product peer
- @entities/tools/hexstrike-ai.md — MCP peer
- @entities/tools/pentestgpt.md — research/agentic peer

## Raw Concept

Desk Phase-0 (2026-08-02). Canonical repo: [github.com/aliasrobotics/cai](https://github.com/aliasrobotics/cai). **No local clone** — GitHub size ~207MB + dual-license complexity.

## Narrative

### What it is

**Cybersecurity AI (CAI)** is Alias Robotics’ multi-agent framework for building offensive and defensive AI automation (“framework for AI Security”). Community edition advertised via `pip install cai-framework`; Professional Edition is a paid commercial product with unrestricted-model marketing. Multiple arXiv papers attached. [CONFIRMED — README head 2026-08-02]

### Desk signals

| Signal | Value |
|--------|--------|
| License | **Dual / complex** — MIT for portions derived from openai-agents-python; **Alias proprietary Research-Use** for additions under `src/cai` — **commercial/professional/production use prohibited** without commercial license [CONFIRMED — LICENSE file via API] |
| GitHub SPDX | `NOASSERTION` (matches dual-license reality) |
| Stars | ~9.6k (2026-08-02) |
| Pushed | 2026-07-14 |
| GitHub size | ~207MB — clone only if operator explicitly needs full tree |
| Shape | Framework + agents + model zoo; research + pro editions |
| Containment | Framework-level; no Strix-style Docker sandbox claim in desk skim [TENTATIVE] |
| Scope model | Soft / operator responsibility; multi-agent kill-chain demos historically weak on hard allowlists [TENTATIVE] |
| Local LLM | “300+ AI models” claim; community path may include local — verify before rely [TENTATIVE] |

### Failure modes

1. **License trap for consulting/product** — research-use Alias code is **not** a free MIT green light for paid pentest productization. Prefer Apache/MIT-clear tools (Strix, pentest-ai-agents) for client work.
2. **Large tree** — default REFERENCE; do not shallow-clone “just in case.”
3. **Edition confusion** — Community vs PRO; do not paste engagement secrets into any hosted Alias service without a data decision.
4. **CVE / security history noise** — third-party repos reference CAI framework CVEs; treat as signal to re-audit before install, not as auto NO-GO malware smell. [TENTATIVE]

### Phase-0 verdict

**REFERENCE (2026-08-02)** — useful for landscape literacy and academic multi-agent patterns; **not** first-line adopt. **No clone.** If operator later wants a lab trial: full license counsel-style read, isolated VM only, written scope, re-verify commercial restrictions.

## Snippets

```text
Canonical: github.com/aliasrobotics/cai
License: MIT (upstream portions) + Alias Research-Use (src/cai) — commercial restricted
Verdict: REFERENCE — no clone 2026-08-02 (~207MB + dual license)
```
