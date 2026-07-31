---
title: AHA (Agent Hacks Agent) — Auto-research-red-teaming
type: entity
category: tool
tags: [entity, tool, agent-security, red-teaming, autoresearch, mit, conditional-go]
keywords: [aha, auto-research-red-teaming, vulnerability concept graph, claude code, codex, cityu]
related:
  - sources/arxiv-2607-11698-agent-hacks-agent-autoresearch.md
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - concepts/agent-data-injection-attacks.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - entities/tools/fuzzyai.md
  - entities/tools/pentest-ai-agents.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-16
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

## Relations

- @sources/arxiv-2607-11698-agent-hacks-agent-autoresearch.md — paper
- @concepts/vulnerability-concept-graph-production-agent-red-teaming.md — core concept
- @entities/tools/fuzzyai.md — chat/jailbreak fuzz; AHA targets tool-acting production agents

**Local clone:** `raw-sources/repos/Auto-research-red-teaming` (~169MB, gitignored under `raw-sources/`)

## Raw Concept

FOSS autoresearch harness that red-teams production-style coding agents overnight and accumulates a **Vulnerability Concept Graph**. MIT. Docker-sandboxed victims.

## Narrative

### Phase-0 audit verdict (2026-07-16): CONDITIONAL-GO (lab / authorized only)

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | License | **PASS** | MIT (`LICENSE`) |
| G1 | Maturity | **PASS** | Public 2026-07-07; arXiv 2026-07-13; active docs/AGENT.md |
| G2 | Size | **PASS** | ~169MB shallow clone (<500MB budget) |
| G3 | Failure mode | **WATCH** | Stores harmful prompts; drives real actions in sandboxed victims — misconfig = unsafe |
| G4 | Stack fit | **PASS** | Claude Code / Codex scenarios; VCG steals map to Prebind/ADI regression |
| G5 | Overlap | **PASS** | Complements FuzzyAI; not a duplicate |
| G6 | Telemetry | **PASS** | No phone-home flagged in SETUP/SECURITY skim |
| Verdict | **CONDITIONAL-GO** | Reference clone on laptop; run only vs owned Docker sandboxes with written auth |

### Ops notes

- Read `AGENT.md` + `SECURITY.md` before any run
- Requires Anthropic/OpenAI API keys + Docker
- Do **not** point at production TipDrop/Cemini agents without isolated sandbox + scope

### Final verdicts

- **Cybersec-wiki:** CONDITIONAL-GO — primary home
- **CCC:** REFERENCE + VCG pattern steal for harness regression
- **David/TipDrop:** adopt **claimed-authorization** checklist; do not run AHA against live Discord bots
