---
title: Agent Skill Security — SkillSec-Eval lifecycle framework (arXiv 2607.13987)
type: source
tags: [source, arxiv, agent-security, skills, supply-chain, evaluation]
keywords: [2607.13987, skillsec-eval, agent skill security, skill lifecycle, camlis]
related:
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/agent-skill-injection.md
  - entities/tools/malskillbench.md
  - entities/tools/skillgate.md
  - concepts/mcp-security-posture.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/skill-vetting.md"
maturity: draft
read_status: read
created: 2026-07-16
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-16 — SkillSec-Eval taxonomy + 327-skill empirical study; no standalone installable product; steal lifecycle checklist"
wire_status: wont_wire
wire_target: "REFERENCE taxonomy — policy in agent-audit rule"
---

**Briefs:** `briefs/2026-07-16_skillsec-lifecycle-skill-security-handoff.md`, `briefs/2026-07-16_k177-skillsec-lifecycle-skill-security-prod.md`

## Relations

- @concepts/skillsec-lifecycle-agent-skill-security.md — synthesis
- @concepts/agent-skill-injection.md — K95 cluster extended by lifecycle stages beyond execution

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation |
| Authors | Sanket Badhe, Priyanka Tiwari |
| Venue | CAMLIS / PMLR (proceedings header) |
| arXiv | 2607.13987 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.13987-agent-skill-security-threat-models-attacks-defenses.pdf` |
| Retrieved | 2026-07-16 (manual fetch; was digest candidate, not auto-downloaded) |
| Read status | **read** (lifecycle taxonomy + SkillSec-Eval framing; 24 pp) |

## Narrative

Reusable agent skills change the trust model: metadata, permissions, workflows, and implementations evolve independently of the model. Prior work clusters on prompt injection and runtime execution; this paper argues **lifecycle stages beyond execution** are under-analyzed.

### Skill lifecycle threat surface

| Stage | Example risk |
|-------|----------------|
| Repository admission | Malicious skill enters marketplace / org registry |
| Semantic retrieval | Ranking/metadata steers planner toward attacker skill |
| Planner selection | Misleading descriptions / confused-deputy selection |
| Execution | Classic PI / tool misuse / workflow composition |
| Skill evolution | Benign install → malicious update (supply-chain) |

SkillSec-Eval instantiates the taxonomy against a repository of **327 real-world skills**. [Source: arXiv 2607.13987 abstract]

### Steal for Cemini

1. Extend skill-vetting / Phase-0 beyond install-time static scan to **admission → retrieval → selection → execution → evolution**
2. Treat skill updates as first-class re-audit events (pairs MalSkillBench + SkillGuard)
3. Marketplace / Discord-shared skills inherit software-supply-chain + semantic attack surfaces

### Phase-0 (2026-07-16)

| Gate | Status |
|------|--------|
| Installable product | **NONE** — evaluation framework paper |
| Verdict | **REFERENCE** — checklist + taxonomy adopt |

## Snippets

> "Our study demonstrates that vulnerabilities arise at multiple lifecycle stages beyond execution, highlighting the need for lifecycle-aware security analysis of reusable agent skills."
[Source: arxiv-2607.13987 abstract]
