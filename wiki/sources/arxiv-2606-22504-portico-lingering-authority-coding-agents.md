---
title: PORTICO — revocable capabilities against lingering authority (arXiv 2606.22504)
type: source
tags: [source, arxiv, agent-security, coding-agents, capabilities, portico, least-privilege]
keywords: [2606.22504, portico, lingering authority, revocable capabilities, coding agents, task contract]
related:
  - concepts/lingering-authority-revocable-capabilities.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/agentic-containment-principles.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - concepts/ai-for-cybersecurity.md

maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
phase_0_verdict: "Reference 2026-06-24 — PORTICO reference monitor described in paper; no public PORTICO repo found 2026-06-24; steal task-contract + epoch-bound handle pattern"
---

## Relations

- @concepts/lingering-authority-revocable-capabilities.md — lingering authority + revocation synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents |
| Author | Igor Santos-Grueiro |
| Affiliation | International University of La Rioja |
| arXiv | 2606.22504 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.22504-pdf-revocable-resource-and-effect-capabilities-f.pdf` |
| Retrieved | 2026-06-24 |
| Read status | **read** (abstract, PORTICO lifecycle, closure-slice experiment, stale-write audit) |

## Narrative

Coding agents often hold **broad tool authority for an entire task** when a resource is needed only for one subgoal. **Lingering authority**: a temporary capability remains **visible to the planner** after the subgoal episode closes — distinct from sandbox reachability (file may still exist) vs **planner-interface exposure**.

**PORTICO** reference monitor:

- Compiles explicit **task contract** → initial capabilities, grant rules, closure predicates, global deny rules
- **Request–grant–invoke** lifecycle with epoch-bound opaque handles
- **Closure** removes handles from next planner interface; rejects stale replay before side effects

### Headline controlled results

| Comparator | Post-closure reuse | Stale-write forbidden effects |
|------------|-------------------|------------------------------|
| PORTICO | **rejects 10/10** | **0/6 executed** |
| Non-revoking (same grants) | permits 10/10 | 6/6 executed |

Pre-closure: matched task success and scope compliance. Broad request exposure (same policy, all tools visible): zero forbidden effects but **67→84 blocked proposals** — planner still wastes cycles on over-exposed authority.

Orthogonal to SPI/DCI/AIRGuard — addresses **temporal authority visibility**, complementing @concepts/agent-least-privilege-tool-selection.md (which tool among authorized options).

`[TENTATIVE]` — controlled coding tasks + 6 live model traces; production harness not replicated.

## Snippets

> "Lingering authority: a temporary resource/effect capability remains exposed after the episode that justified it has closed."

> "PORTICO then rejects 10/10 post-closure reuses, while the comparator permits 10/10."

[Source: arxiv-2606.22504-pdf-revocable-resource-and-effect-capabilities-f.pdf]
