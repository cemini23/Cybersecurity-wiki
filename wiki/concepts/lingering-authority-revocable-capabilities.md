---
title: Lingering authority and revocable capabilities
type: concept
tags: [concept, agent-security, least-privilege, capabilities, coding-agents, portico]
keywords: [lingering authority, portico, revocable capabilities, task contract, epoch-bound handles, 2606.22504]
related:
  - sources/arxiv-2606-22504-portico-lingering-authority-coding-agents.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/agentic-containment-principles.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/ai-for-cybersecurity.md
  - concepts/task-conditioned-excess-authority.md

maturity: draft
created: 2026-06-24
updated: 2026-07-31
wire_status: wont_wire
wire_target: "REFERENCE — PORTICO artifact pending"
---

## Relations

- @sources/arxiv-2606-22504-portico-lingering-authority-coding-agents.md — PORTICO reference monitor (2606.22504)
- @concepts/agent-least-privilege-tool-selection.md — orthogonal OPUR (which authorized tool)

## Raw Concept

Ingest 2026-06-24: arXiv:2606.22504 — **lingering authority** as temporal planner-interface exposure after subgoal closure.

## Narrative

### Failure mode

Coding agents receive broad read/write/git/network scopes for entire task. Subgoal completes (e.g. API file patched) but **serialization-file authority remains in planner manifest** — model can keep planning around stale capability even if execution monitor would block some calls.

Distinct from:
- **OPUR** — picks broader tool when narrow suffices (2606.20023)
- **AIRGuard** — narrows at execution time
- **Sandbox reachability** — file still on disk vs **visible to planner**

### PORTICO pattern

```
Task contract → initial caps + grant rules + closure predicates + deny rules
Request → grant (epoch-bound handle) → invoke → closure → handle removed from next interface
```

**Closure slice:** PORTICO rejects **10/10** post-closure replays; non-revoking comparator permits **10/10**; stale-write audit **0/6 vs 6/6** forbidden effects executed.

### Harness steal-from `[TENTATIVE]`

1. Compile per-task capability contract from user goal
2. Materialize grants as opaque epoch handles
3. On subgoal closure, **remove** from planner tool schema — not just ACL deny
4. Reject stale handle replay before side effects

See `briefs/2026-06-24_portico-lingering-authority-coding-agent-handoff.md`.

## Snippets

> "The exposed interface is therefore part of the security state."

[Source: arxiv-2606.22504]
