---
title: CAGE-1 — enterprise agent governance evaluation (arXiv 2607.03510)
type: source
tags: [source, arxiv, enterprise, governance, evaluation, prebind, agent-security]
keywords: [2607.03510, cage-1, prebind assurance, standing, twelve dimensions, roopam sure]
related:
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-execution-provenance.md
  - concepts/intent-governed-tool-authorization.md
  - concepts/agentic-containment-principles.md
  - concepts/mcp-security-posture.md
  - concepts/agent-data-injection-attacks.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md
  - "@ccc-wiki/concepts/cage-1-enterprise-agent-governance-eval.md"
maturity: draft
read_status: read
created: 2026-07-10
updated: 2026-07-10
phase_0_verdict: "REFERENCE 2026-07-10 — independent technical report (Roopam W. Sure); no installable product repo; steal Prebind Assurance + 12-dimension eval checklist; NOT lahlfors/cybernetic-governance-engine CAGE"
---

**Briefs:** `briefs/2026-07-10_cage-1-prebind-assurance-handoff.md`, `briefs/2026-07-10_prod-mcp-prebind-assurance-checklist.md`, `briefs/2026-07-10_k151-cage-1-prebind-assurance-prod.md`

## Relations

- @concepts/cage-1-enterprise-agent-governance-eval.md — synthesis
- @sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md — complementary long-horizon eval (same ingest batch)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CAGE-1: Control, Assurance, and Governance Evaluation for Enterprise Agentic AI |
| Author | Roopam W. Sure (independent technical report, July 2026) |
| arXiv | 2607.03510v1 [cs.SE] |
| Related canon | GKS-5 (governed knowledge), AGL-1 (enterprise AI governance layer) — same author |
| Code | **None** — framework paper; author publications at `roopamwsure.github.io/publications/` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.03510-2607-03510v1-cage-1-control-assurance-and-govern.pdf` |
| Retrieved | 2026-07-10 |
| Read status | **read** (12 dimensions, Prebind Assurance, Standing, maturity scoring, applied cases) |

## Narrative

CAGE-1 evaluates whether enterprise agents are **deployment-ready on governed action**, not task fluency alone. Third layer after governed knowledge (GKS-5) and enterprise governance control plane (AGL-1).

### Prebind Assurance

**Prebind Assurance** = evaluated ability to prove an agentic action is controlled **before** it becomes binding, effective, or operationally consequential.

**Standing** = time-specific authority held by user, agent, system, or approval chain to initiate, approve, or complete a movement.

Boundary outcomes before protected consequence forms: **admit, hold, narrow, refuse, escalate, quarantine, or render non-effective**.

Seven proof elements per boundary: attempted action, standing, condition pass/fail, boundary outcome, non-effective result, receipt, replay.

### Five evaluation layers

| Layer | Question |
|-------|----------|
| Capability | Can the agent perform the task? |
| Control | Within defined authority and policy? |
| Assurance | Can the org prove how/why it acted? |
| Prebind Assurance | Invalid actions stopped/narrowed before binding? |
| Operational trust | Safely scalable across users/workflows? |

### Twelve dimensions

Identity/Authority · Policy Enforcement · Retrieval Trust · Memory Integrity · Tool Safety · Planning Control · Human Oversight · Audit/Replayability · Conflict/Boundary Handling · Failure Behavior · Operational Readiness · Business Fitness.

Maturity **0–4** per dimension (Uncontrolled → Manual → Defined → Enforced → Assured). High-consequence agents need **Level 3–4** on risky dimensions before production.

**Decision output:** Approve, restrict, remediate, reject, or continue monitoring.

### Name collision [CONFIRMED]

**NOT** `lahlfors/cybernetic-governance-engine` (gateway product also abbreviates CAGE).

### Phase-0 (2026-07-10)

| Gate | Status |
|------|--------|
| Artifact | **NONE** — evaluation framework only |
| Domain fit | prod-mcp prebind gates, SOC runbooks, engagement governance |
| Verdict | **REFERENCE** — adopt checklist vocabulary; David K151 tipdrop |

## Snippets

> "Task success is not enough. Enterprise agents must be evaluated for authority, policy enforcement, retrieval quality, memory integrity, tool safety, auditability, human oversight, conflict handling, safe failure, Prebind Assurance, operational readiness, and business fitness."
> — [Source: arxiv-2607.03510 abstract, retrieved 2026-07-10]

> "Prebind Assurance: the system records what action was attempted, what standing existed, which condition passed or failed, what was held or refused, what became non-effective, what receipt proves the boundary held, and what replay confirms."
> — [Source: arxiv-2607.03510 executive summary, retrieved 2026-07-10]
