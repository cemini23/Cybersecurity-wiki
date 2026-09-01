---
title: "EvoSkill Injection — red-teaming autonomous skill generation (arXiv 2608.30429)"
type: source
tags: [source, arxiv, agent-security, skill-injection, red-team, lab-only, k317]
keywords: [2608.30429, EvoSkill Injection, SARGE, EvoSkillBench, EvoSkillSafetyBench, self-evolving agents, persistent capability corruption]
related:
  - concepts/evoskill-injection-self-evolving-agents.md
  - concepts/experience-driven-redteam-skill-evolution.md
  - concepts/agent-skill-injection.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
phase_0_verdict: "REFERENCE 2026-09-01 — no public SPDX repo at hunt; benches promised. No malicious trajectories in wiki. Lab eval only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + agent-audit.mdc (K317)"
---

## Relations

- @concepts/evoskill-injection-self-evolving-agents.md — primary steal (skill pipeline = attack surface)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents |
| Authors | Doyun Kim, Chanwoo Kim, Sugyeong Eo, Yeo-Chan Yoon, Chanjun Park |
| arXiv | 2608.30429 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.30429-evoskill-injection-red-teaming-autonomous-skill.pdf |
| Retrieved | 2026-09-01 |
| Read status | read (abstract + threat model) |
| Public code | **none at hunt** — EvoSkillBench / EvoSkillSafetyBench referenced; no clone |

## Narrative

**EvoSkill Injection** targets the **autonomous skill generation and evolution pipeline** of self-evolving agents: adversarial interaction trajectories can cause the agent to **store malicious capabilities as legitimate skills**, which then **persistently activate** on later benign requests (retrieval-time harm).

**SARGE** red-team framework: iterative generation / escalation / reinforcement against a target self-evolving agent; **EvoSkillBench** (malicious trajectories for skill formation) + **EvoSkillSafetyBench** (post-attack retrieval/activation).

**Results (paper):** ASR ~43.5% generation / ~54.6% escalation / ~49.9% reinforcement; injected skills persistently retrieved and activated.

**Why filed (K317):** offense-side complement to `@concepts/skill-misevolution.md`, `@concepts/experience-driven-redteam-skill-evolution.md` (K313), `@concepts/agent-skill-injection.md`. **Lab only** — no trajectory payloads in wiki; never poison `.cursor/skills` from attack runs.

## Snippets

> Autonomous skill evolution introduces a new attack surface in which malicious capabilities are generated, stored, and reused as legitimate skills. [Source: arXiv 2608.30429 abstract]
