---
title: "Practice Makes Unsafe — skill misevolution in self-improving LLM agents (2608.12851)"
type: source
tags: [source, arxiv, agent-security, skills, self-evolution, k237]
keywords: [2608.12851, skill misevolution, SKILLMISEVO, SAFEEVOLVE, C-ASR, skill poisoning]
related:
  - concepts/skill-misevolution.md
  - sources/arxiv-2608-12977-self-evolving-security.md
  - concepts/self-evolving-runtime-defense.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/self-evolving-agent-security.md
  - concepts/safety-harness-evolution.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - "@osint-wiki/sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: skimmed
---

## Relations

- @concepts/skill-misevolution.md — cyber synthesis
- @sources/arxiv-2608-12977-self-evolving-security.md — HARD defense-side pair
- @osint-wiki/sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md — primary ingest (OSINT K237)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12851, "Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents" |
| Retrieved | 2026-08-14 via OSINT digest → cyber brief `briefs/2026-08-14_k237-self-evolving-defense-misevolution.md` |
| Location | OSINT archive (`cemini-egress-fi` osint/); cyber holds synthesis only |
| Code | `github.com/henrymao2004/misevolve` — Phase-0 hunt before clone; REFERENCE unless SPDX + <500MB |

## Narrative

Inbound from OSINT K237. **Skill misevolution**: a self-improving agent writes an unsafe shortcut from a "successful" trajectory into a persistent SKILL.md; later fresh sessions retrieve it after the original attack input is gone. Bench: 21/21 evolved configs authored unsafe artifacts; 15 retained fresh-session harm. Eval must split **authoring / retrieval / execution** gates — a terminal ASR cannot tell a clean library from an unused poison skill. Cyber wire: no unattended auto-evolve of `.cursor/skills/*`; HITL on write does not cover retrieval-time harm. [Source: arXiv:2608.12851]
