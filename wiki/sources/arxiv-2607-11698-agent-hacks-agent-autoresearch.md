---
title: Agent Hacks Agent (AHA) — autoresearch for production-agent red-teaming (arXiv 2607.11698)
type: source
tags: [source, arxiv, agent-security, red-teaming, claude-code, codex, autoresearch]
keywords: [2607.11698, aha, agent hacks agent, vulnerability concept graph, vcg, autoresearch, cityu]
related:
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - entities/tools/aha-auto-research-red-teaming.md
  - concepts/agent-data-injection-attacks.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - concepts/substrate-constraints-coding-agent-oversight.md
maturity: draft
read_status: read
created: 2026-07-16
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-07-16 — github.com/henrymao2004/Auto-research-red-teaming MIT ~169MB; Docker-sandboxed victims; lab-only authorized use"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

**Briefs:** `briefs/2026-07-16_aha-vcg-production-agent-red-team-handoff.md`, `briefs/2026-07-16_k176-aha-vcg-production-agent-red-team-prod.md`

## Relations

- @concepts/vulnerability-concept-graph-production-agent-red-teaming.md — VCG synthesis
- @entities/tools/aha-auto-research-red-teaming.md — Phase-0 + local clone

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming |
| Authors | Xutao Mao, Xiang Zheng, Cong Wang |
| Affiliation | City University of Hong Kong |
| arXiv | 2607.11698 |
| Code | [github.com/henrymao2004/Auto-research-red-teaming](https://github.com/henrymao2004/Auto-research-red-teaming) (MIT) |
| Local clone | `raw-sources/repos/Auto-research-red-teaming` (~169MB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.11698-agent-hacks-agent-autoresearch-for-production-ag.pdf` |
| Retrieved | 2026-07-16 |
| Read status | **read** (AHA loop + VCG + Claude Code/Codex eval) |

## Narrative

Production agents (Claude Code, Codex) fail as **real actions**, not just harmful text. AHA runs an autoresearch loop: hypothesize → falsify → attack in sandboxed harness → reflect → promote confirmed findings into a **Vulnerability Concept Graph (VCG)**.

Each VCG concept links: attacker-facing surface → unsafe trajectory via claim, enabling condition, falsifier, transfer prediction, evidence.

### Headline results [CONFIRMED from paper/README]

- Frozen VCG reusable single-shot: **47.0%** held-out ASR (+**14.2 pp** over strongest discovery baseline 32.8%)
- Cross-victim transfer ≈ **88%** of native ASR
- **8** recurring mechanism families; **claimed-authorization** core lit in **16/18** settings
- Scenarios: AgentHazard (direct), AgentDyn (indirect IPI), DTap (real env)

### Steal for Cemini

1. Red-team artifacts should be **mechanisms** (enabling conditions), not payload archives
2. Patch → re-run concept as regression check (pairs CAGE-1 Prebind + ADI)
3. Claimed-authorization failures are the shared core across coding agents

### Phase-0 (2026-07-16)

| Gate | Status |
|------|--------|
| License | **PASS** — MIT |
| Maturity | **PASS** — public 2026-07-07; paper 2026-07-13; ~24★; active |
| Size | **PASS** — ~169MB shallow clone (<500MB) |
| Failure mode (C2/agent RT) | Docker-sandboxed victims; stores harmful prompts — **lab / authorized only** |
| Overlap | Complements FuzzyAI (chat jailbreaks) + ADI + CAGE-1 |
| Verdict | **CONDITIONAL-GO** — local reference clone; run only against owned sandboxes |

## Snippets

> "These artifacts record where an attack landed, but not the enabling condition that made the agent trajectory unsafe, so they are hard to audit, patch against, or reuse after the setting changes."
[Source: arxiv-2607.11698 abstract]
