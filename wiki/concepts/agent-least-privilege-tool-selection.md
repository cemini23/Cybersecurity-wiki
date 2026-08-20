---
title: Agent least-privilege tool selection
type: concept
tags: [agent-security, least-privilege, tool-selection, mcp, opur, toolprivbench]
keywords: [over-privileged tool selection, opur, ped, premature escalation, toolprivbench, 2606.20023]
related:
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - entities/tools/toolprivbench.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/agentic-containment-principles.md
  - concepts/ai-for-cybersecurity.md
  - concepts/zero-trust.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2606-03024-skillguard-permission-framework.md
  - entities/tools/ecc.md
  - sources/arxiv-2606-22504-portico-lingering-authority-coding-agents.md
  - concepts/lingering-authority-revocable-capabilities.md
  - sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md
  - concepts/intent-governed-tool-authorization.md
  - sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
  - concepts/mcp-execution-control-invariants.md
  - entities/tools/handle-capability-protocol.md
  - concepts/security-tool-orchestration-determinants.md
  - sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md
  - sources/arxiv-2608-18351-excess-authority-least-privilege.md
  - concepts/task-conditioned-excess-authority.md
maturity: draft
created: 2026-06-19
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
---

## Relations

- @sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md — primary source (2606.20023)
- @entities/tools/toolprivbench.md — evaluation benchmark
- @concepts/mcp-security-posture.md — external MCP trust stack (admission, DCI, SPI)
- @entities/tools/airguard.md — runtime authority narrowing (complements internal OPUR mitigation)
- @sources/arxiv-2606-03024-skillguard-permission-framework.md — skill permission metadata (external boundary)

## Narrative

Ingest 2026-06-19: arXiv:2606.20023 frames **over-privileged tool selection** as a distinct agent safety failure — the model picks a **broader authorized tool** when a **narrower authorized tool** would complete the task. This is orthogonal to prompt injection (all tools are in-policy) and orthogonal to external permission enforcement (SkillGuard, allowlists): it is **internal path preference** that inflates blast radius of errors, misuse, or downstream compromise.

### Metrics

| Metric | Meaning |
|--------|---------|
| **OPUR** | Over-Privileged Tool Use Rate — fraction of cases with least-privilege violation |
| **PED** | Pre-Escalation Exploration Depth — 0 = aggressive first pick; ≥1 = escalated after lower-privilege attempts/failures |

### Two failure modes in production

```
User: "Show my calendar for Tuesday"
  ├─ sufficient: calendar_read (narrow)
  └─ sufficient: workspace_admin (broad — also reads mail, files)

Aggressive (PED=0): agent picks workspace_admin immediately
Premature escalation (PED≥1): calendar_read returns HTTP 503 → agent picks admin API instead of retry/sibling narrow tool
```

The second mode is especially relevant for **flaky MCP servers**, rate limits, and transient cloud API errors on prod-mcp/lazy-tool stacks.

### Five over-privilege risk types (TOOLPRIVBENCH)

| Risk type | How higher-privilege tool exceeds minimal need |
|-----------|--------------------------------------------------|
| **Authority Escalation** | Admin/root scope vs task-scoped role |
| **Scope Expansion** | Cross-resource access beyond task object |
| **Temporal Persistence** | Long-lived tokens/credentials vs ephemeral |
| **Safety Bypass** | Disables guardrails or audit hooks |
| **Data Over-Exposure** | Returns broader datasets than requested |

### Mitigation ladder (paper + wiki stack)

| Layer | Control | OPUR impact (paper) | Wiki anchor |
|-------|---------|---------------------|-------------|
| **L0 — Catalog design** | Don't register admin MCP tools when narrow tools exist | Removes temptation | @concepts/mcp-security-posture.md closed allowlist |
| **L1 — System prompt** | SECURITY PRINCIPLE: prefer minimal privilege, retry same tier before escalate | Modest; weak under failures | Harness policy text |
| **L2 — Runtime authority** | Narrow task→step authority before `tools/call` | Not in paper; external enforcement | @entities/tools/airguard.md, ChainCaps |
| **L3 — Alignment / post-training** | SFT+GRPO on privilege-aware trajectories | Large (e.g. 64.9→27% Qwen3-8B) | Research-only unless fine-tuning pipeline exists |
| **L4 — Eval gate** | Run TOOLPRIVBENCH-style scenarios before promoting agent configs | Measurement | @entities/tools/toolprivbench.md |

**Critical gap:** AgentAlign-style **harm refusal training does not teach least-privilege tool choice** — refusing malicious requests ≠ picking narrow sufficient tools among benign options.

### Pentest / red-team test pattern

1. Register paired narrow + broad tools that both satisfy the stated user goal
2. Induce transient failure on narrow tool (503, timeout, empty result)
3. Observe whether agent escalates to broad tool before exhausting narrow alternatives
4. Score OPUR/PED; repeat across Infra and Authority Escalation scenario classes (highest OPUR in paper)

### Operator checklist (prod-mcp)

- [ ] Per-server tool allowlist exposes **minimal sufficient surface** for the task class — not "all tools the server offers"
- [ ] Retry policy: at least one retry / sibling narrow tool before escalating privilege tier
- [ ] Log tool privilege tier + PED-equivalent (how many narrow attempts before broad tool)
- [ ] Do not treat AgentHarm / refusal benchmarks as proxy for least-privilege compliance
- [ ] Phase-0 TOOLPRIVBENCH repo before automated eval import — LICENSE unverified 2026-06-19

See `briefs/2026-06-19_toolprivbench-prod-mcp-eval-checklist.md` for paired-tool eval harness on prod-mcp.

## Snippets

[Source: arxiv-2606.20023 §4.1 Finding I]

> Most evaluated agents exhibit non-trivial OPUR despite the availability of sufficient lower-privilege tools.

[Source: arxiv-2606.20023 §5.4.1]

> Prompting reduces OPUR, but its effect weakens once interaction proceeds through failed standard-tool attempts.
