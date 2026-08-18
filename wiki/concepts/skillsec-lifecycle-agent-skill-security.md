---
title: SkillSec lifecycle — agent skill security beyond execution
type: concept
tags: [concept, agent-security, skills, supply-chain, lifecycle]
keywords: [skillsec-eval, skill lifecycle, repository admission, semantic retrieval, skill evolution]
related:
  - sources/arxiv-2607-13987-agent-skill-security-skillsec-eval.md
  - concepts/agent-skill-injection.md
  - entities/tools/malskillbench.md
  - entities/tools/skillgate.md
  - concepts/mcp-security-posture.md
  - concepts/self-evolving-agent-security.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/skill-vetting.md"
  - concepts/coding-agent-supply-chain-install-gap.md
  - sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md
  - sources/arxiv-2608-12851-skill-misevolution.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608-16465-jailbreakskill.md
  - concepts/evolving-attack-skill-libraries.md
  - entities/tools/jailbreakskill.md
maturity: draft
created: 2026-07-16
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc"
---

## Relations

- @sources/arxiv-2607-13987-agent-skill-security-skillsec-eval.md — SkillSec-Eval paper
- @concepts/agent-skill-injection.md — K95 cluster; this page adds lifecycle stages
- @ccc-wiki/concepts/skill-vetting.md — Cemini Phase-0 skill audit (extend stages)
- @concepts/coding-agent-supply-chain-install-gap.md — sibling supply-chain admission (package install vs skill artifact)

## Raw Concept

Install-time skill scans miss admission, retrieval, planner selection, and post-install evolution. SkillSec-Eval frames the full lifecycle.

## Narrative

### Five-stage checklist (steal)

| Stage | Gate question |
|-------|----------------|
| **Admission** | Who published? Signed? Org allowlist? |
| **Retrieval** | Can metadata/embeddings boost a malicious skill into top-k? |
| **Selection** | Does planner trust description over capability truth? |
| **Execution** | Runtime PI / tool / workflow composition (MalSkillBench lane) |
| **Evolution** | Re-audit on update; pin versions; detect silent malice |

Empirical base: **327** real-world skills under SkillSec-Eval. [TENTATIVE on per-stage ASR — paper skim; adopt taxonomy first]

### Relation to existing wiki

- MalSkillBench / POISE → **execution** detectors
- SkillGuard / SkillGate → permission / admission
- Self-evolving agent safety → **evolution** lane
- SkillSec → unify into one lifecycle rubric for federation skill packs

## Snippets

See source abstract quote.
