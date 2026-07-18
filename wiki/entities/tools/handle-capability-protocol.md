---
title: Handle-Capability Protocol (HCP) — MCP execution-control reference runtime
type: entity
tags: [entity, tool, mcp, execution-control, capability-system, reference]
keywords: [hcp, handle-capability-protocol, symboliclight, mcp-runtime, eight-invariants]
related:
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
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
created: 2026-07-04
updated: 2026-07-18
phase_0_verdict: "CONDITIONAL-GO 2026-07-04 — MIT; github.com/SymbolicLight-AGI/handle-capability-protocol 0★; benchmark + reference runtime for invariant eval"
---

**Briefs:** `briefs/2026-07-04_hcp-mcp-execution-control-handoff.md`, `briefs/2026-07-04_prod-mcp-eight-invariants-checklist.md`

## Relations

- @sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md — paper + benchmark provenance
- @concepts/mcp-execution-control-invariants.md — eight-invariant methodology

## Raw Concept

| Field | Value |
|-------|-------|
| Name | Handle-Capability Protocol (HCP) |
| Repo | [SymbolicLight-AGI/handle-capability-protocol](https://github.com/SymbolicLight-AGI/handle-capability-protocol) |
| Author | SymbolicLight Research (Ting Liu) |
| License | MIT |
| Stars | 0 (2026-07-04) |

## Narrative

**Local clone (2026-07-18):** `raw-sources/repos/handle-capability-protocol` (~3.9MB, shallow). Reference runtime for I1–I8 invariant eval.


### Phase-0 audit verdict (2026-07-04): CONDITIONAL-GO

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | License | **PASS** | MIT |
| G1 | Artifact completeness | **PASS** | Reproducibility repo + 10-case benchmark per paper |
| G2 | Maturity | **PARTIAL** | 0★; academic reference runtime, not battle-tested |
| G3 | Overlap with wiki stack | **PARTIAL** | Complements AIRGuard/ChainCaps/IGAC — does not replace |
| G4 | prod-mcp fit | **CONDITIONAL** | Invariant checklist + benchmark oracle; not drop-in proxy yet |

### What HCP provides

Reference runtime implementing **eight execution invariants** for MCP-style agents: principals, resources, grants, capabilities, handles, policy decisions, data-pipe checks, audit entries. Sub-millisecond in-memory policy/invoke latency in paper microbenchmark [TENTATIVE — lab conditions only].

### Cemini adoption posture

- **GO** — run HCP benchmark cases against prod-mcp design; map gaps to I1–I8 checklist
- **NO-GO (yet)** — replace lazy-tool dispatch with HCP broker without integration spike
- Pair with @entities/tools/chaincaps.md (composition IFC) and @entities/tools/airguard.md (runtime authority)

## Snippets

> "Reference implementation and reproducibility artifacts for the Handle-Capability Protocol."
[Source: github.com/SymbolicLight-AGI/handle-capability-protocol README, retrieved 2026-07-04]
