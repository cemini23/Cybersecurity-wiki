---
title: Self-evolving runtime defense (HARD) — evolve gates vs policy from held-out failures
type: concept
tags: [concept, agent-security, harness-evolution, defense, k237]
keywords: [HARD, self-evolving defense, gate evolver, policy evolver, held-out eval, over-restriction]
related:
  - sources/arxiv-2608-12977-self-evolving-security.md
  - sources/arxiv-2608-12851-skill-misevolution.md
  - concepts/skill-misevolution.md
  - concepts/safety-harness-evolution.md
  - concepts/self-evolving-agent-security.md
  - concepts/harnessopt-bench.md
  - concepts/ai-for-cybersecurity.md
  - "@osint-wiki/concepts/self-evolving-runtime-defense.md"
  - sources/arxiv-2608-16465-jailbreakskill.md
  - concepts/evolving-attack-skill-libraries.md
  - concepts/safeevolve-harness-policy-co-evolution.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + SHE HITL (do not unattended auto-evolve prod harness)"
---

## Relations

- @sources/arxiv-2608-12977-self-evolving-security.md — HARD paper
- @concepts/skill-misevolution.md — offense-side pair (skills worsen with practice)
- @concepts/safety-harness-evolution.md — SHE: which artifacts may evolve, under what validation
- @concepts/self-evolving-agent-security.md — MLAS: self-evolution removes session-reset safety

## Raw Concept

How do you improve a lab harness's runtime defenses from failed attack traces without memorizing the bench or wrecking utility?

## Narrative

HARD loop: (1) run attack tasks against a harnessed agent; (2) judge each trajectory (outcome ≤0.5 = attack success; keep `security_awareness` to split recognized-but-executed vs never-recognized — different repair: **gate** vs **policy**); (3) evolve per category on deterministic train/test splits, held-out-only eval, batched failures; (4) redeploy.

**Gate** only for high-confidence, low-FP, pre-execution-matchable action *shapes* — never staging paths shared with benign tasks. **Policy** otherwise. Literal regex gates rot; prefer anti-obfuscation / cumulative-intent abstractions. **Over-restriction is a measured failure** (utility collapse). Lab only; HITL + rollback before mutating a live Cursor/Claude harness. Pairs SHE (name the owning artifact) and misevolution (do not let the *skill library* evolve from poisoned successes). [Source: arXiv:2608.12977]
