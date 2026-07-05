---
title: HCP — MCP execution-control security invariants (arXiv 2606.29073)
type: source
tags: [source, arxiv, mcp, execution-control, capability-system, hcp, confused-deputy]
keywords: [2606.29073, handle-capability-protocol, hcp, eight-invariants, tool-poisoning, data-pipe, grant-backed-approval]
related:
  - entities/tools/handle-capability-protocol.md
  - concepts/mcp-execution-control-invariants.md
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
read_status: read
created: 2026-07-04
updated: 2026-07-04
phase_0_verdict: "CONDITIONAL-GO 2026-07-04 — MIT, github.com/SymbolicLight-AGI/handle-capability-protocol 0★; reference runtime + benchmark artifact"
---

**Briefs:** `briefs/2026-07-04_hcp-mcp-execution-control-handoff.md`, `briefs/2026-07-04_prod-mcp-eight-invariants-checklist.md`

## Relations

- @entities/tools/handle-capability-protocol.md — HCP reference runtime entity
- @concepts/mcp-execution-control-invariants.md — eight-invariant synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes |
| Author | Ting Liu (SymbolicLight Research) |
| arXiv | 2606.29073 |
| Code | `github.com/SymbolicLight-AGI/handle-capability-protocol` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.29073-hcp-mcp-execution-control-invariants.pdf` |
| Retrieved | 2026-07-04 |
| Read status | **read** (8 invariants, 10-case benchmark, B0/B1/B2 baselines, ablations, microbenchmark) |

## Narrative

MCP standardizes **connection** (hosts, clients, servers, JSON-RPC, tool metadata). This paper argues agents also need an **execution-control layer** — explicit, testable invariants for what happens after a tool is reachable.

### Eight invariants (HCP)

| ID | Invariant | Runtime behavior |
|----|-----------|------------------|
| **I1** | Metadata non-authority | Tool descriptions/prompts cannot grant capabilities |
| **I2** | Grant-backed approval | User approval binds to explicit grants, not blanket consent |
| **I3** | Canonical resources | Resources have stable identity; confused-deputy paths rejected |
| **I4** | Principal binding | Actions attributed to invoking principal |
| **I5** | Scoped capability invocation | Capabilities invoked only within declared scope |
| **I6** | Source-and-target data-flow authorization | Data-pipe moves checked for class + principal |
| **I7** | Deny-path audit | Denials produce forensic audit entries |
| **I8** | Explicit protocol state | Initialize/version gates before method dispatch |

HCP models execution through **principals, resources, grants, capabilities, handles, policy decisions, data-pipe checks, audit entries**.

### Benchmark (10 cases × 3 baselines)

| Baseline | Description | Attacks permitted |
|----------|-------------|-------------------|
| **B0** | Naive connection-layer | **10/10** |
| **B1** | Connection mitigation (metadata lint, session checks, per-call approvals) | **6/10** |
| **B2** | HCP execution-control runtime | **0/10** + audit evidence |

**Attack classes modeled:** tool poisoning (metadata → exfil/send), confused deputy (cross-principal resource access), approval fatigue (broad approval without grant), data-pipe PII leakage, transport/session state violations.

**B1 gaps [CONFIRMED]:** metadata lint + per-call approval still permits tool-poisoning and approval-fatigue cases; confused-deputy partially blocked by server identity checks only.

### vs wiki stack

| Layer | Existing wiki | HCP contribution |
|-------|---------------|------------------|
| Admission | @concepts/mcp-security-posture.md attestation/allowlist | Post-admission execution invariants |
| Intent | @concepts/intent-governed-tool-authorization.md IGAC certificates | Grant-backed approval (I2) + principal binding (I4) |
| Composition IFC | @entities/tools/chaincaps.md flow budgets | Source-target data-pipe auth (I6) |
| Runtime authority | @entities/tools/airguard.md action-time guard | Scoped capability + deny audit (I5, I7) |
| Provenance | @concepts/agent-execution-provenance.md | Explicit audit completeness scoring |

### Phase-0 (2026-07-04)

| Gate | Status |
|------|--------|
| License | **MIT** |
| Maturity | **0★**, pushed 2026-06-27; reproducibility artifact present |
| Domain fit | MCP execution-control reference — complements connection-layer hardening |
| Verdict | **CONDITIONAL-GO** — adopt invariant checklist + benchmark for prod-mcp eval; not production dependency until broader review |

## Snippets

> "Across 10 benchmark cases, the naive baseline permits all modeled attacks, the mitigation baseline permits 6 of 10, and HCP blocks all 10 while preserving audit evidence."
[Source: arxiv-2606.29073-hcp-mcp-execution-control-invariants.pdf abstract]

> "A runtime can block a bad call by raising an exception, but that does not by itself establish forensic evidence."
[Source: arxiv-2606.29073-hcp-mcp-execution-control-invariants.pdf §6.4]
