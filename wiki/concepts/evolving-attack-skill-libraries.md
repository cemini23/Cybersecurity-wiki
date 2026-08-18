---
title: "Evolving attack-skill libraries (lab eval primitive)"
type: concept
tags: [concept, methodology, llm-security, skills, red-team, k283]
keywords: [evolving skills, attack skill library, JailbreakSkill, diagnose-refine-discover, dual ASR]
related:
  - sources/arxiv-2608-16465-jailbreakskill.md
  - entities/tools/jailbreakskill.md
  - concepts/skill-misevolution.md
  - concepts/self-evolving-runtime-defense.md
  - concepts/safety-harness-evolution.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/agent-skill-injection.md
  - concepts/llm-adversarial-fuzzing.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemini-cybersec-agent-audit.mdc (K283)"
---

## Relations

- @sources/arxiv-2608-16465-jailbreakskill.md
- @entities/tools/jailbreakskill.md — NO-GO clone (null SPDX)
- @concepts/skill-misevolution.md — defense pair: practice can make a library unsafe
- @concepts/self-evolving-runtime-defense.md — HARD defense loop
- @concepts/safety-harness-evolution.md — SHE artifact ownership
- @concepts/skillsec-lifecycle-agent-skill-security.md — author/pack/install/invoke/evolve stages
- @concepts/agent-skill-injection.md
- @concepts/llm-adversarial-fuzzing.md

## Raw Concept

How do automated red-teams scale once attack strategies stop being one-off prompts and become a reusable, evolving skill library?

## Narrative

**Reuse + evolution.** Static jailbreak catalogs scatter across prompts. A skill-centric loop packages strategies as agent-ready skills, then uses attack experience to diagnose failures, refine or combine skills, and discover new ones. Report **dual ASR** (benchmark + transfer/novelty), not a single headline.

**Not a prod auto-evolve.** Evolving attack skills are a **lab eval primitive**. HITL write ≠ retrieval-time safety (`@concepts/skill-misevolution.md`). Do not promote/refine `.cursor/skills` from an attack-skill evolution run. No LIVE third-party targets. No wiki payloads.

**Dual-ID:** Cybersec K283 JailbreakSkill ≠ CCC K283 Twin.

## Snippets

> JailbreakSkill packages existing attack strategies into modular, agent-ready skills that can be directly reused and adaptively selected across tasks and target models. Beyond reuse, it closes the loop between attacking and learning. [Source: arXiv 2608.16465 abstract]
