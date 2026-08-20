---
title: Intent-governed tool authorization (IGAC)
type: concept
tags: [concept, agent-security, authorization, mcp, least-privilege, igac]
keywords: [igac, intent certificate, manifest filtering, openport, session narrowing, 2606.22916]
related:
  - sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/chaincaps.md
  - entities/tools/airguard.md
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
  - concepts/mcp-execution-control-invariants.md
  - entities/tools/handle-capability-protocol.md
  - sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/task-conditioned-excess-authority.md
maturity: draft
created: 2026-06-24
updated: 2026-07-31
wire_status: wont_wire
wire_target: "REFERENCE — IGAC artifact pending"
---

## Relations

- @sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md — IGAC paper (2606.22916)
- @concepts/mcp-security-posture.md — admission layer complement

## Raw Concept

Ingest 2026-06-24: arXiv:2606.22916 — **Intent-Governed Access Control** for server-side agent tool authorization.

## Narrative

### Authorization gap

| Question | Traditional OAuth/MCP scope | IGAC adds |
|----------|----------------------------|-----------|
| Can credential call tool? | ✓ | — |
| Is call justified by **current user request**? | — | ✓ |

Example: read+export integration authorized statically — user asks for summary only → export tools should be **filtered from manifest** and export payloads rejected.

### Components

1. **Intent certificates** — session-scoped authority ceiling from parsed user goal
2. **Monotone narrowing** — intent can only shrink static grants
3. **Intent-aware manifest filtering** — planner sees reduced tool surface
4. **Intent–tool–payload consistency** — arg-level check before invoke

Mapped to **OpenPort** substrate in paper. Pilot: static auth still allowed **85.71%** of high-risk requests immediately — IGAC layering required.

### prod-mcp positioning

Sits **above** attested admission (2605.24248) and **before** planner:
- Admission: which servers/tools enter catalog
- **IGAC:** which subset matches current user intent
- AIRGuard/ChainCaps: runtime execution/composition

See `briefs/2026-06-24_igac-intent-governed-tool-auth-handoff.md`.

`[TENTATIVE]` — OpenPort pilot; Claude Code / lazy-tool mapping not lab-tested.

## Snippets

> "User intent may only reduce the authority granted by static integration credentials."

[Source: arxiv-2606.22916]
