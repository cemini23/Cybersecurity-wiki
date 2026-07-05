---
title: MCP execution-control invariants
type: concept
tags: [concept, mcp, execution-control, capability-system, runtime-security]
keywords: [hcp, eight-invariants, metadata-non-authority, grant-backed-approval, data-pipe, deny-path-audit]
related:
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
  - entities/tools/handle-capability-protocol.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-execution-provenance.md
  - concepts/intent-governed-tool-authorization.md
  - entities/tools/chaincaps.md
  - entities/tools/airguard.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-04
updated: 2026-07-04
---

**Briefs:** `briefs/2026-07-04_hcp-mcp-execution-control-handoff.md`, `briefs/2026-07-04_prod-mcp-eight-invariants-checklist.md`

## Relations

- @sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md — HCP paper + 10-case benchmark (2606.29073)
- @entities/tools/handle-capability-protocol.md — reference implementation

## Raw Concept

Ingest 2026-07-04: arXiv 2606.29073 separates **MCP connection** (reach a tool server) from **execution control** (authorize what the call may do). Connection-layer mitigations (metadata lint, session checks, per-call UI approval) block only **4/10** modeled attacks in the paper benchmark.

## Narrative

### Layer model

```
Connection layer (MCP)     → JSON-RPC, transports, tool registry, OAuth
Execution-control layer    → principals, grants, capabilities, data-pipe, audit
```

Wiki admission/DCI/SPI (@concepts/mcp-security-posture.md) gates **what enters the catalog**. Execution invariants gate **what each invocation may do** given catalog contents.

### Eight invariants → prod-mcp mapping [TENTATIVE]

| Invariant | Failure mode without it | prod-mcp / lazy-tool steal |
|-----------|-------------------------|----------------------------|
| **I1 Metadata non-authority** | Tool description becomes hidden invoke | Never parse tool metadata as policy; DCI + SPI |
| **I2 Grant-backed approval** | "Approve all" bypasses scope | Per-tool grants bound to user consent token |
| **I3 Canonical resources** | Path confusion / deputy reads | Stable resource IDs, not string prefixes alone |
| **I4 Principal binding** | Server acts as omnipotent deputy | Attribute every `tools/call` to session principal |
| **I5 Scoped invocation** | Capability creep mid-chain | ChainCaps/AIRGuard narrowing (@entities/tools/chaincaps.md) |
| **I6 Data-flow authorization** | PII from tool A → exfil tool B | Sink-specific budgets + class tags |
| **I7 Deny-path audit** | Silent block, no forensics | Log principal + capability + reason on deny |
| **I8 Protocol state** | Pre-init method dispatch | Strict MCP initialize/version gates |

### Benchmark takeaway

Practice-informed **B1** (lint + session + approvals) is insufficient for:
- **Tool poisoning** — metadata steers controller to exfil/send
- **Approval fatigue** — broad approval without grant
- **Data-pipe** — PII crossing class boundaries

HCP **B2** blocks all 10 with audit completeness — use as **regression oracle** when hardening prod-mcp, not as sole runtime.

### Eval pairing

| Eval | Measures |
|------|----------|
| SeClaw / AgentDojo | Security trajectories |
| ToolBench-X | Tool-environment unreliability |
| **HCP 10-case suite** | Execution invariant coverage |
| IGAC OpenPort | Intent–payload consistency |

## Snippets

> "MCP-style agent systems need an execution-control layer in addition to connection-layer conventions."
[Source: arxiv-2606.29073 conclusion — paraphrase anchor]
