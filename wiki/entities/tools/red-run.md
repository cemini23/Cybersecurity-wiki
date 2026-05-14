---
title: "red-run — Claude Code agent-team distributed pentest orchestrator [cybersec cross-route]"
type: entity
category: tool
tags: [entity, tool, autonomous-pentest, sliver-c2, agent-team-coordination, tmux-pane-orchestration, k44, steal-from-gpl-poison]
keywords: [red-run, blacklanternsecurity, sliver-c2-backend, autonomous-pentest-agents, tmux-distribution, gpl-3-poison-pill]
related: []
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @ccc-wiki/entities/tools/red-run.md — CCC-side primary entity (agent-team orchestration use case)

## Raw Concept

K44 cross-route from CCC to Cybersec: the **autonomous pentest agent + Sliver C2 backend** combination. Operational concepts for coordinating distributed pentest operators across tmux panes via a centralized C2 infrastructure. **GPL-3.0, 160 stars**. K44 verdict: **Steal-from** (architectural patterns only; GPL prevents production embedding).

## Narrative

The Cybersec-relevant pattern is the **Sliver C2 + agent-team coordination model**: multiple autonomous pentest operators sharing intelligence and target state through a central C2 backend, each running in its own tmux pane with role-specific instructions.

License posture is identical to CCC-side: GPL-3.0 prevents any binary or library embedding into Cemini-shipped products. The Sliver C2 integration concept is replicable under MIT in a future Cemini-developed equivalent if pursued.

See @ccc-wiki/entities/tools/red-run.md for the full Phase-0 gate set.

## Snippets

> "Extract and document operational concepts for coordinating autonomous pentest agents utilizing the Sliver C2 backend infrastructure."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶396]
