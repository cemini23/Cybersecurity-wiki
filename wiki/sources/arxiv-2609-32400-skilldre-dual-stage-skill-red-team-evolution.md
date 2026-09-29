---
title: "SkillDRE: dual-stage red-team evolution of agent skills via pre-execution and runtime feedback"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.32400, k378]
related:
  - concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md
  - concepts/agent-skill-injection.md
  - concepts/skill-misevolution.md
  - concepts/evoskill-injection-self-evolving-agents.md
  - concepts/skill-cascading-attacks-skill-based-agents.md
maturity: draft
read_status: read
created: 2026-09-29
updated: 2026-09-29
phase_0_verdict: "REFERENCE 2026-09-29 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K378)"
---

## Relations

- @concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md
- @concepts/agent-skill-injection.md
- @concepts/skill-misevolution.md
- @concepts/evoskill-injection-self-evolving-agents.md
- @concepts/skill-cascading-attacks-skill-based-agents.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SkillDRE: dual-stage red-team evolution of agent skills via pre-execution and runtime feedback |
| arXiv | 2609.32400 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.32400-skilldre-dual-stage-red-team-evolution-of-agent.pdf |
| Retrieved | 2026-09-29 |
| Read status | read (abstract + triage) |

## Narrative

**K378** — agent skills package instructions, code, and resources that improve from execution feedback; the same loop can evolve **malicious** skills. A candidate may pass **pre-execution scan** yet fail under **runtime defenses**, while a runtime repair can reintroduce scanner findings. **SkillDRE** holds a task-conditioned malicious objective and judge rule fixed, then evolves the skill implementation in a **dual-stage closed loop** (scanner-guided evolution ↔ runtime-guided refinement) while **preserving benign task capability**. SkillsBench (four victim models): paper reports average ASR **45.28%** (~**40.3%** above strongest baseline) with final skills clearing SkillScan findings. Repo `github.com/whfeLingYu/SkillDRE` is **REFERENCE — null SPDX; do not clone**. **No skill bodies or attack payloads in wiki.** **Runtime:** `scripts/k378_skilldre_precheck.py`. Pairs skill injection / misevolution / EvoSkill / K374 cascading.

## Snippets

> See arXiv 2609.32400 abstract. [Source: arXiv 2609.32400 (retrieved 2026-09-29)]
