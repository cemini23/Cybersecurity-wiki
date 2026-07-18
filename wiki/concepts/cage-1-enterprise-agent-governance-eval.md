---
title: CAGE-1 enterprise agent governance evaluation (Prebind Assurance)
type: concept
tags: [concept, enterprise, governance, evaluation, prebind, agent-security, harness]
keywords: [cage-1, prebind assurance, standing, twelve dimensions, 2607.03510, fail closed]
related:
  - sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-execution-provenance.md
  - concepts/intent-governed-tool-authorization.md
  - concepts/agentic-containment-principles.md
  - concepts/mcp-security-posture.md
  - concepts/agent-data-injection-attacks.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/multilingual-long-horizon-agent-evaluation.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md
  - "@ccc-wiki/concepts/cage-1-enterprise-agent-governance-eval.md"
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - entities/tools/aha-auto-research-red-teaming.md
  - sources/arxiv-2607-11698-agent-hacks-agent-autoresearch.md
  - concepts/physical-vs-content-danger-embodied-agents.md
  - sources/arxiv-2607-15218-prism-physical-vs-content-danger.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md
maturity: draft
created: 2026-07-10
updated: 2026-07-18
---

**Briefs:** `briefs/2026-07-10_cage-1-prebind-assurance-handoff.md`, `briefs/2026-07-10_prod-mcp-prebind-assurance-checklist.md`

## Relations

- @sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md — provenance (2607.03510)
- @concepts/mcp-execution-control-invariants.md — execution-control layer complements Prebind boundary
- @concepts/agent-data-injection-attacks.md — ADI forges trusted fields; Prebind catches before bind
- @concepts/coding-agent-supply-chain-install-gap.md — package install = Prebind-class bind (K179)
- @sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md — install-gap empirics

## Raw Concept

Ingest 2026-07-10: arXiv **2607.03510** — **CAGE-1** shifts enterprise agent evaluation from output quality to **governed action trust**. Central term: **Prebind Assurance** (prove control before binding consequence).

## Narrative

### Prebind vs trajectory security eval

| Eval type | When | Wiki peers |
|-----------|------|------------|
| **Prebind Assurance** (CAGE-1) | Before action becomes **binding** (payment, post, config write, entitlement change) | IGAC, HCP invariants, prod-mcp checklists |
| **Trajectory security** (SeClaw, AgentDojo) | Whether tool **path** was unsafe | @concepts/seclaw-agent-security-evaluation.md |
| **ADI isolation** (2607.05120) | Whether **trusted fields** were forged from untrusted data | @concepts/agent-data-injection-attacks.md |

### Twelve dimensions → offensive/defensive mapping [TENTATIVE]

| Dimension | Pentest / red-team lens | Blue / SOC lens |
|-----------|-------------------------|-----------------|
| Identity and Authority | Delegation abuse, confused deputy | RBAC, service-account scope |
| Policy Enforcement | Policy bypass via tool params | Runtime policy engines |
| Retrieval Trust | RAG poisoning, stale intel | Source authorization + freshness |
| Memory Integrity | Memory poisoning, scope creep | Scoped, revocable agent memory |
| Tool Safety | Tool misuse, SSRF, exfil chains | Allowlist, parameter validation, no-bind |
| Planning Control | Multi-step attack graphs | Risk thresholds on plans |
| Human Oversight | Social-engineering escalation gaps | Approval routing |
| Audit and Replayability | Covering tracks | Tamper-resistant correlated logs |
| Conflict/Boundary | Policy vs memory vs retrieval conflicts | Prebind before SoR write |
| Failure Behavior | Fail-open exploitation | Fail closed, quarantine, escalate |
| Operational Readiness | Shadow IT agents | Versioning, IR, decommission |
| Business Fitness | Risk vs reward of automation | Measurable value without unmanaged risk |

### Capability ≠ trust

> An agent may complete a task and still be unsuitable for production — correct answer from unauthorized context, right tool under wrong authority, workflow completed while losing evidence.

### prod-mcp steals

1. **No-bind objects** — prepared tool payloads held until grant/approval satisfied (maps HCP I2 grant-backed approval)
2. **Boundary receipts** — log attempted action + standing + policy version + outcome before side effects
3. **Replay exercises** — re-run same movement after authority/evidence change; expect hold→admit transition only when conditions met

### Name collision

**NOT** `lahlfors/cybernetic-governance-engine`. Sure CAGE-1 = **evaluation framework** only.

| Verdict | **REFERENCE** — adopt Prebind checklist; no product install |

## Snippets

> "Capability and trust are different properties."
> — [Source: arxiv-2607.03510 §5, retrieved 2026-07-10]

> "If an enterprise cannot prove what was admitted, held, narrowed, refused, or made non-effective before execution, it does not have custody over consequence formation."
> — [Source: arxiv-2607.03510 §10 trust barrier, retrieved 2026-07-10]
