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
  - entities/tools/agentredguard.md
  - concepts/llm-pentest-automation.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - entities/tools/seclaw-eval.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/agent-least-privilege-tool-selection.md
  - entities/tools/toolprivbench.md
  - sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md
  - concepts/agent-probabilistic-datalog-verification.md
  - concepts/intent-governed-tool-authorization.md
  - concepts/lingering-authority-revocable-capabilities.md
  - sources/arxiv-2606-22504-portico-lingering-authority-coding-agents.md
  - sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
  - concepts/mcp-execution-control-invariants.md
  - entities/tools/handle-capability-protocol.md

maturity: draft
created: 2026-06-01
updated: 2026-07-18
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
- @entities/tools/agentredguard.md — integration/tool-response guard (compare in lab)
- @sources/arxiv-2605-28914-airguard-guarding-agent-actions.md — paper provenance
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — formal guardrail complement (ePCA)
- @sources/arxiv-2606-02240-agentredbench.md — SaaS read→write indirect injection benchmark

## Raw Concept

Ingested from arXiv:2605.28914 (2026-06-01 daily digest). `Sophie508/AIRGuard` — MIT, runtime guard for heterogeneous tool/MCP calls.

## Narrative

**Local clone (2026-07-18):** `raw-sources/repos/AIRGuard` (~5.1MB, shallow; `Sophie508/AIRGuard`, MIT).


AIRGuard operationalizes **least privilege at action time**: untrusted content may inform reasoning but cannot authorize side effects. Normalizes tool calls, narrows task authority to step authority, tracks source/target trust pools, simulates sensitive effects, audits cross-step sequences, blocks before execution.

**Import boundary**: workstation/lab agent assessments and internal copilot hardening only until Phase-0 replay on your MCP stack confirms utility tradeoffs (paper: 76% benign utility on DTAP-150 with Haiku 4.5).

**Complements**: ChainCaps (composition IFC), SkillSpector (skill supply chain), DefenseClaw (enterprise policy).

**2606.20023 gap:** AIRGuard narrows authority at execution time; TOOLPRIVBENCH shows models still **prefer** broader tools before the guard fires if both remain authorized — pair runtime guards with minimal tool catalogs and OPUR eval (`briefs/2026-06-19_toolprivbench-prod-mcp-eval-checklist.md`).

## Snippets

```bash
gh api repos/Sophie508/AIRGuard --jq '.license.spdx_id'   # MIT
```

Paper-reported: AgentTrap ASR 36.3% → 5.5% (Sonnet 4.6). `[TENTATIVE]` — re-verify on current model IDs.

## Dead Ends

- **Prompt-only "ignore untrusted instructions"** — paper ablation shows modest gain vs dedicated runtime layer.
- **Provenance without authority** — grounded arguments can still exceed user-authorized scope.
