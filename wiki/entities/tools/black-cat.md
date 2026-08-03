---
title: "0rangec3t/Black-cat — hypothesis-driven Claude Code red-team skill"
type: entity
tags: [tool, skill, red-team, llm, hypothesis-ledger, null-spdx, k220]
keywords: [black-cat, hypothesis evidence, case ledger, state machine, claude code skill]
related:
  - sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md
  - concepts/ai-pentest-harness-landscape.md
  - concepts/llm-pentest-automation.md
  - concepts/red-team-operations.md
  - entities/tools/offensive-claude.md
  - entities/tools/src-hunter-skill.md
  - entities/tools/raptor.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
cross-wiki-source: "@osint-wiki/sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md"
wire_status: wont_wire
wire_target: "null SPDX — pattern extract only; no clone"
---

# Black-cat — hypothesis-first red-team skill

## Relations

- @sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md — K220 parent
- @concepts/ai-pentest-harness-landscape.md — harness pattern peer
- @concepts/llm-pentest-automation.md — Tier methodology
- @concepts/red-team-operations.md — engagement model
- @entities/tools/offensive-claude.md — Claude Code offensive workstation peer
- @entities/tools/src-hunter-skill.md — MIT skill peer
- @entities/tools/raptor.md — no-license Steal-from peer (same SPDX caution)

## Raw Concept

OSINT K220 Extract (CCC) + cyber Steal-from pattern. Repo: https://github.com/0rangec3t/Black-cat  
OSINT twin: @osint-wiki/entities/tools/black-cat.md

## Narrative

| Field | Value |
|-------|--------|
| **License** | NOT FOUND [CONFIRMED gh 2026-08-03] |
| **Stars / push** | ~218 / 2026-08-03 |
| **Posture** | Steal-from patterns only — **no Phase-0 clone** |

Claude Code red-team skill using a **hypothesis→evidence state machine** (RECON ⇄ ENUMERATE ⇄ VALIDATE) instead of a one-way recon→scan→exploit pipeline. Ships JSONL case ledger + machine `verify --report` gate before REPORT (confirmed observation/reproduction/impact triangle).

**Steal:** ledger schema, falsification loops, explicit context routing, REPORT machine gate.  
**Do not:** vendor the repo (null SPDX); adopt “authorize once then default-do” without HITL for high-blast actions; invent tool output when commands fail.
