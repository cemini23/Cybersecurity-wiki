---
title: "JailbreakSkill — evolving attack-skill library (NO-GO clone)"
type: entity
tags: [tool, red-team, skills, no-go, k283]
keywords: [JailbreakSkill, BattleWen, null SPDX, evolving skills]
related:
  - sources/arxiv-2608-16465-jailbreakskill.md
  - concepts/evolving-attack-skill-libraries.md
  - concepts/skill-misevolution.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/agent-skill-injection.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "NO-GO clone 2026-08-18 — github.com/BattleWen/JailbreakSkill license:null / no LICENSE file (~5MB, 6 stars). Pattern steal only. Do not copy skills/ into .cursor/skills."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemini-cybersec-agent-audit.mdc (K283)"
---

## Relations

- @sources/arxiv-2608-16465-jailbreakskill.md
- @concepts/evolving-attack-skill-libraries.md
- @concepts/skill-misevolution.md
- @concepts/skillsec-lifecycle-agent-skill-security.md
- @concepts/agent-skill-injection.md

## Raw Concept

Public tree for the JailbreakSkill paper. Null SPDX → no clone, no adopt shelf.

## Narrative

Pattern steal: diagnose → refine/combine/discover; dual ASR + generalization. Do not vendor the skill bodies. Dual-ID: Cybersec K283 ≠ CCC K283 Twin.

## Local adoption

| Field | Value |
|-------|-------|
| Verdict | NO-GO clone (null SPDX) |
| Path | **must not exist** (`raw-sources/repos/JailbreakSkill`, `.local/adopts/JailbreakSkill`) |
| LICENSE | none |
| Wire | K283 policy only |
