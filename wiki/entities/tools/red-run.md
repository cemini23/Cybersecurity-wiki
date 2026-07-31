---
title: "red-run — Claude Code agent-team distributed pentest orchestrator [reference-only cross-route]"
type: entity
category: tool
tags: [entity, tool, autonomous-pentest, sliver-c2-wrapper, agent-team-coordination, k44, reference-only-phase-0-2026-05-14, gpl-3-poison-pill, evasion-features-auto-reject]
keywords: [red-run, blacklanternsecurity, sliver-c2-backend, autonomous-pentest-agents, AMSI-ETW-evasion, AVR-EDR-evasion, agent-teams-api-NOT-tmux, gpl-3-poison-pill]
related:
  - concepts/red-team-operations.md
  - concepts/adversary-emulation.md
  - "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
  - "@ccc-wiki/entities/tools/red-run.md"
maturity: validated
created: 2026-05-14
updated: 2026-07-31
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @concepts/red-team-operations.md — offensive-security landscape context for AI-assisted red-team orchestration
- @concepts/adversary-emulation.md — adversary-emulation framing for autonomous pentest agents
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @ccc-wiki/entities/tools/red-run.md — CCC-side primary entity (agent-team orchestration use case)

## Raw Concept

K44 cross-route from CCC to Cybersec: the **autonomous pentest agent + Sliver C2 wrapper** combination. **GPL-3.0, 162 stars verified (claim 160), single-author (kevinoriley: 272/280 commits), last push 2026-04-01**. Cybersec-side Phase-0 verdict: **REFERENCE-ONLY** (Cemini does not adopt offensive tooling for its own stack).

## Narrative

### Phase-0 audit verdict (2026-05-14): REFERENCE-ONLY

The Cybersec relevance is observational: red-run is a notable exemplar of agent-team red-team orchestration using the standard Claude Code agent-teams API + `sliver-py` gRPC wrapper to Sliver C2. **It is NOT a candidate for Cemini-stack adoption** — Cemini is a defensive-oriented quant-finance stack; offensive tooling is out-of-scope regardless of license.

**Critical findings (full audit at @ccc-wiki/entities/tools/red-run.md)**:

- **License**: GPL-3.0 CONFIRMED (no commercial dual-license)
- **Evasion features = auto-reject signal**: `skills/evasion/av-edr-evasion/SKILL.md` covers AMSI bypass, ETW patching, CrowdStrike/SentinelOne evasion (`opsec: high`). Cemini does not adopt evasion tactics
- **Sliver C2 = wrapper**: `sliver-py` gRPC client, no Sliver code embedded (Sliver itself is BSD-3-Clause but irrelevant — red-run's wrapper IS GPL-3.0)
- **K44 framing correction**: K44 said "tmux pane orchestration" — incorrect. red-run uses the standard Claude Code agent-teams API (`TeamCreate` / `Agent(team_name=…)` / `SendMessage`), not tmux

### Cybersec-wiki posture

- **Document as reference** for AI-assisted red-team orchestration patterns in the offensive-security landscape
- **DO NOT recommend adoption** by Cemini-side defensive workflows
- **Cross-reference to CCC-wiki** for the four extractable orchestration patterns (lead-router, single-writer state-mgr, enum/ops split, semantic skill-router) — those are domain-neutral and clean-room re-implementable under MIT in CCC's defensive context

### Responsible-use note

Repo carries an explicit CFAA / "CTF and lab use only" / written-permission disclaimer. Anyone running red-run for offensive purposes outside an authorized engagement is in legal jeopardy. The cybersec-wiki entry exists to document the technique landscape, not to enable unauthorized use.

See @ccc-wiki/entities/tools/red-run.md for the full G0–G9 gate set, DO-NOT-EXTRACT blocklist, and clean-room patterns.

## Snippets

> "Extract and document operational concepts for coordinating autonomous pentest agents utilizing the Sliver C2 backend infrastructure."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶396 — Phase-0 audit confirms the agent-teams + Sliver wrapper but flags evasion features as auto-reject signal. Reference-only for Cybersec-wiki; orchestration patterns clean-room re-implementable in CCC-wiki only.]
