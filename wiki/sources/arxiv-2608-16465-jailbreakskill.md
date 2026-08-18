---
title: "JailbreakSkill — reusable and ever-evolving attack skills (arXiv 2608.16465)"
type: source
tags: [source, arxiv, llm-security, red-team, skills, k283]
keywords: [2608.16465, JailbreakSkill, evolving skills, ASR, AdvBench, HarmBench, document-completion]
related:
  - concepts/evolving-attack-skill-libraries.md
  - entities/tools/jailbreakskill.md
  - concepts/skill-misevolution.md
  - concepts/self-evolving-runtime-defense.md
  - concepts/safety-harness-evolution.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/agent-skill-injection.md
  - concepts/llm-adversarial-fuzzing.md
maturity: draft
read_status: read
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "NO-GO clone 2026-08-18 — github.com/BattleWen/JailbreakSkill has no LICENSE / null SPDX (~5MB, 6 stars). Pattern steal only. Dual-ID: Cybersec K283 ≠ CCC K283 Twin."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemini-cybersec-agent-audit.mdc (K283)"
---

**Briefs:** `briefs/2026-08-18_k283-jailbreakskill.md`

## Relations

- @concepts/evolving-attack-skill-libraries.md — synthesized concept (offense-side evolving skills)
- @entities/tools/jailbreakskill.md — NO-GO clone entity
- @concepts/skill-misevolution.md — defense-side pair: skills worsen with practice
- @concepts/self-evolving-runtime-defense.md — HARD defense evolution
- @concepts/safety-harness-evolution.md — SHE: which artifacts may evolve
- @concepts/skillsec-lifecycle-agent-skill-security.md
- @concepts/agent-skill-injection.md
- @concepts/llm-adversarial-fuzzing.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Skills |
| Authors | Xiaoyu Wen, Jiajia Li, Zhida He, Peng Yu, Chenxu Wang, Han Qi, Ziyuan Zhou, Cheng Jin, Ying Wen, Xingcheng Xu, Shuyue Hu, Tianhang Zheng, Chaochao Lu, Qiaosheng Zhang (Shanghai AI Lab et al.) |
| arXiv | 2608.16465 (v1 2026-08-18) |
| Code | `github.com/BattleWen/JailbreakSkill` — **no LICENSE** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.16465-jailbreakskill-scaling-automated-red-teaming-wit.pdf` |
| Retrieved | 2026-08-18 |
| Read status | read (full extract) |

## Narrative

JailbreakSkill packages existing attack strategies as modular agent-ready skills and closes a loop: diagnose → refine / combine / discover skills → grow the library. Reported macro-average ASR lift **+17.5 pp AdvBench** and **+13.4 pp HarmBench**, including **+48.6 pp vs GPT-5.4** on AdvBench. A novel evolved skill is described as reframing a request as an unfinished document-completion task. Several evolved skills reportedly transfer to unseen prompts/models. [TENTATIVE] single source; no local repro.

This is the **offense-side** evolving-skill library. `@concepts/skill-misevolution.md` is the defense-side finding that skills can worsen. Do **not** copy `evolved_skill_examples/` or SKILL.md attack bodies into this wiki or `.cursor/skills`. Authorized lab only; report dual ASR + novelty/generalization.

**Cybersec K283** (≠ CCC K283 Twin).

## Snippets

> This evolution lifts macro-average ASR by 17.5 percentage points on AdvBench and 13.4 points on HarmBench, including a 48.6-point gain against GPT-5.4 on AdvBench, while yielding novel attack strategies such as reframing a direct request as an unfinished document-completion task. [Source: arXiv 2608.16465 abstract]
