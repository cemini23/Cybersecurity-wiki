---
title: "EvoSkill Injection — skill-generation pipeline as attack surface (K317)"
type: concept
tags: [concept, agent-security, skill-injection, red-team, lab-only, k317]
keywords: [EvoSkill Injection, SARGE, persistent capability corruption, self-evolving agents, skill bank, retrieval-time harm, skill misevolution]
related:
  - sources/arxiv-2608-30429-evoskill-injection.md
  - concepts/skill-misevolution.md
  - concepts/experience-driven-redteam-skill-evolution.md
  - concepts/evolving-attack-skill-libraries.md
  - concepts/agent-skill-injection.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-09-01
updated: 2026-09-01
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K317)"
---

## Relations

- @sources/arxiv-2608-30429-evoskill-injection.md — EvoSkill Injection + SARGE (2608.30429)
- @concepts/skill-misevolution.md — defense-side: skills can worsen; govern authoring/retrieval/execution
- @concepts/experience-driven-redteam-skill-evolution.md — K313 validation ratchet (offense-side distill)
- @concepts/agent-skill-injection.md — skill supply-chain / poisoning context

## Raw Concept

Question: **what changes when agents autonomously write their own skills from experience?**

## Narrative

Manual skill libraries face **external poisoning** and retrieval attacks. **Self-evolving agents** add **EvoSkill Injection (K317)**: the **generation/evolution pipeline itself** can internalize adversarial trajectories as **durable skills** that reactivate on semantically related benign prompts (EvoSkillSafetyBench design).

**Operator steal:**
1. **Treat skill authoring + evolution as a security boundary** — HITL on write does **not** cover retrieval-time activation of a poisoned skill (pairs misevolution triple gates).
2. **Never auto-evolve `.cursor/skills` from red-team trajectories** — lab eval only; no malicious trajectory bodies in wiki.
3. **Measure persistence** — single-turn harm ASR is insufficient; score **stored → retrieved → activated** on downstream benign-looking queries.
4. Pairs K283/K313 evolving attack-skill libraries vs defense-side skill governance.

## Snippets

> A single malicious skill can repeatedly influence future agent behaviors, causing persistent capability corruption even under benign user requests. [Source: arXiv 2608.30429 abstract, paraphrase]
