---
title: "AIRGuard — runtime authority control for tool-using agents (MIT)"
type: entity
tags: [tool, ai-security, agent-guard, runtime, mcp, authority-control, mit, adopt]
keywords: [airguard, authority confusion, least privilege, agenttrap, dtap-150, runtime guard, sophie508]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/chaincaps.md
  - concepts/llm-pentest-automation.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
phase_0_verdict: "CONDITIONAL-GO 2026-06-01 — MIT verified; wrap MCP/tool calls pre-execution; lab on AgentTrap/DTAP-style tasks before client copilot assessments."
---

# AIRGuard — runtime authority control for tool-using agents (MIT)

## Relations

- @concepts/agent-runtime-guardrails.md — authority-confusion failure mode + enforcement model
- @concepts/ai-for-cybersecurity.md — defensive layer for agent deployments
- @concepts/llm-pentest-automation.md — pentest agents need action-time guards, not prompt-only policy
- @entities/tools/defenseclaw.md — enterprise-scale governance complement
- @entities/tools/nvidia-skillspector.md — pre-install skill audit vs runtime side-effect enforcement
- @entities/tools/chaincaps.md — composition IFC complement (flow budgets vs authority inheritance)
- @sources/arxiv-2605-28914-airguard-guarding-agent-actions.md — paper provenance
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — formal guardrail complement (ePCA)

## Raw Concept

Ingested from arXiv:2605.28914 (2026-06-01 daily digest). `Sophie508/AIRGuard` — MIT, runtime guard for heterogeneous tool/MCP calls.

## Narrative

AIRGuard operationalizes **least privilege at action time**: untrusted content may inform reasoning but cannot authorize side effects. Normalizes tool calls, narrows task authority to step authority, tracks source/target trust pools, simulates sensitive effects, audits cross-step sequences, blocks before execution.

**Import boundary**: workstation/lab agent assessments and internal copilot hardening only until Phase-0 replay on your MCP stack confirms utility tradeoffs (paper: 76% benign utility on DTAP-150 with Haiku 4.5).

**Complements**: ChainCaps (composition IFC), SkillSpector (skill supply chain), DefenseClaw (enterprise policy).

## Snippets

```bash
gh api repos/Sophie508/AIRGuard --jq '.license.spdx_id'   # MIT
```

Paper-reported: AgentTrap ASR 36.3% → 5.5% (Sonnet 4.6). `[TENTATIVE]` — re-verify on current model IDs.

## Dead Ends

- **Prompt-only "ignore untrusted instructions"** — paper ablation shows modest gain vs dedicated runtime layer.
- **Provenance without authority** — grounded arguments can still exceed user-authorized scope.
