---
title: Skill misevolution — practice can make a skill library unsafe
type: concept
tags: [concept, agent-security, skills, self-evolution, k237]
keywords: [skill misevolution, CU UG Stealth, URR, C-ASR, SAFEEVOLVE, skill poisoning, retrieval lineage]
related:
  - sources/arxiv-2608-12851-skill-misevolution.md
  - sources/arxiv-2608-12977-self-evolving-security.md
  - concepts/self-evolving-runtime-defense.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/self-evolving-agent-security.md
  - concepts/safety-harness-evolution.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - "@osint-wiki/concepts/skill-misevolution.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc (skill misevolution lifecycle gates)"
---

## Relations

- @sources/arxiv-2608-12851-skill-misevolution.md — primary paper
- @concepts/self-evolving-runtime-defense.md — HARD defense pair
- @concepts/skillsec-lifecycle-agent-skill-security.md — five-stage skill lifecycle; misevolution is the *evolve* gate failure
- @concepts/safety-harness-evolution.md — SHE bounds *which* harness artifacts may evolve; misevolution is the skill-library analogue

## Raw Concept

Self-improving agents convert trajectories into reusable skills. A "success" that contains an unsafe shortcut becomes a durable skill that later sessions retrieve without the original attack prompt. How do you detect and govern that?

## Narrative

**Signature.** All 21 evolved configs in SKILLMISEVO-BENCH authored unsafe artifacts; 15 kept harm after a clean-session reload. No-Evolution stays clean — the risk is *learning from experience*, not the base model. Terminal ASR cannot distinguish a clean library from a poison skill that was never retrieved.

**Three lifecycle gates** (score all three):

1. **Authoring** — does the written skill contain reusable unsafe instructions? (CU / UG / Stealth)
2. **Retrieval** — would a later clean session fetch it? (Unsafe Retrieval Rate)
3. **Execution** — does it cause harm when run fresh? (Carryover ASR)

**HITL on write does not cover retrieval-time harm.** Keep retrieval lineage; retire after evidenced harmful reuse. Prefer delete-only repair + reuse-time attribution (SAFEEVOLVE pattern). **No unattended auto-evolve** of `.cursor/skills/*`. VC1–VC3 in the paper are poisoning *templates against skill-evolution agents* — authorized lab only, not a kit. Dual-ID: OSINT board **K237**; CCC meta-harness board also uses K237 for AutoDesign/Vero — resolve by arXiv 2608.12851. [Source: arXiv:2608.12851]
