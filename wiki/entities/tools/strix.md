---
title: "Strix — multi-agent AI pentest harness (usestrix/strix)"
type: entity
tags: [tool, llm-automation, pentest, red-team, apache, docker, sandbox, conditional-go]
keywords: [Strix, usestrix, Docker sandbox, PoC validation, Ollama, Apache-2.0]
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
maturity: draft
created: 2026-08-02
updated: 2026-08-02
phase_0_verdict: "CONDITIONAL-GO / REFERENCE 2026-08-02 — Apache-2.0 desk claim; Docker sandbox + PoC validation marketing; NO local clone until Phase-0"
wire_status: deferred
wire_target: "REFERENCE only — do not clone; ask before Phase-0 clone or any runtime wire"
---

## Relations
- @sources/github-strix-omlx.md — Strix local MLX/Ollama wrapper
- @sources/github-strix.md — thin source stub (retrieved 2026-08-02)
- @concepts/ai-pentest-harness-landscape.md — harness pick matrix (CyberStrike vs Strix vs MIT peers)
- @concepts/llm-pentest-automation.md — Tier-1/2 methodology umbrella
- @concepts/operator-lab-playbook.md — operator start-here; Strix is a sandbox-first orchestration option
- @concepts/agent-vm-sandboxing.md — complements upstream Docker sandbox; still isolate lab networks
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

Thin stub opened 2026-08-02 while building @concepts/ai-pentest-harness-landscape.md. Repo: [github.com/usestrix/strix](https://github.com/usestrix/strix). **No local clone** (operator gate). Desk claims only until Phase-0.

## Narrative

### What it is (desk)

Strix is an **AI multi-agent penetration testing harness** positioned around:

- **Apache-2.0** license (permissive vs CyberStrike AGPL)
- **Docker sandbox** for agent tool execution (containment-first vs CyberStrike’s explicit no-sandbox)
- **PoC validation** loop (reduce false-positive “AI found XSS” noise)
- **Ollama** (and other LLM providers) for local / offline assist

Treat marketing claims as **[TENTATIVE]** until Phase-0 README/LICENSE/clone audit.

### Landscape position

See @concepts/ai-pentest-harness-landscape.md. Prefer Strix over CyberStrike when **license permissiveness + Docker isolation + PoC validation** matter more than skill-catalog scale / Bolt remote workers. Prefer MIT `pentest-ai-agents` / `pentest-ai` when you already run Claude Code or MCP and do not need a separate full harness product.

### Phase-0 / adoption gate

**CONDITIONAL-GO / REFERENCE (2026-08-02)**

- **Do not clone** under `raw-sources/repos/` until an explicit Phase-0 is ordered
- No host install, no MCP wire, no PATH install
- When Phase-0 runs: LICENSE SPDX via `gh api`, sandbox design review, failure-mode audit (scope hard-gate? network egress from Docker? secret handling?), then GO / CONDITIONAL-GO / NO-GO

## Snippets

```text
Repo: https://github.com/usestrix/strix
License (claimed): Apache-2.0
Local path: NONE — REFERENCE only (2026-08-02)
```

## Dead Ends

- **Cloning “just to peek”** against the no-clone gate — wait for Phase-0.
- **Assuming Docker sandbox = authorized testing** — authorization is still required.
- **Treating as drop-in CyberStrike replacement** — different product surface; compare via landscape matrix.
