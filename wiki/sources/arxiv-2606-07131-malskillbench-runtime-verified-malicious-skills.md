---
title: MalSkillBench — runtime-verified malicious agent skills benchmark (arXiv 2606.07131)
type: source
tags: [source, arxiv, agent-skills, benchmark, supply-chain, code-injection, prompt-injection]
keywords: [2606.07131, malskillbench, skill supply chain, runtime verification, clawhub, skillsmp]
related:
  - entities/tools/malskillbench.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/defenseclaw.md
  - concepts/agent-skill-injection.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - sources/arxiv-2606-01567-skill-injection-defenses-enablers.md
  - "@ccc-wiki/concepts/skill-vetting.md"
maturity: draft
read_status: read
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @entities/tools/malskillbench.md — open benchmark artifact (GitHub `lxyeternal/MalSkillBench`)
- @entities/tools/nvidia-skillspector.md — skill-specific detector evaluated (98.4% CI recall, PI collapse)
- @entities/tools/defenseclaw.md — supply-chain scanner class (sees half of hybrid skill)
- @concepts/agent-skill-injection.md — CI + PI attack vectors on SKILL.md packages
- @concepts/agent-runtime-guardrails.md — layered scan before install
- @sources/arxiv-2606-01494-clawhub-security-signals.md — wild scanner disagreement baseline
- @sources/arxiv-2606-07943-poise-position-aware-skill-injection.md — stealth PI complement

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills |
| Authors | Wenbo Guo, Wei Zeng, Chengwei Liu, et al. (NTU, Sichuan U, …) |
| arXiv | 2606.07131 |
| Code | https://github.com/lxyeternal/MalSkillBench |
| Location | `raw-sources/arxiv-2606.07131-malskillbench-a-runtime-verified-benchmark-of-ma.pdf` |
| Retrieved | 2026-06-09 |
| Read status | **read** |

## Narrative

First **runtime-verified** benchmark for malicious **agent skills** (SKILL.md + scripts + tool permissions). Skills are hybrid artifacts — neither pure code nor pure prompt — so wild-only evals and single-domain scanners systematically mis-rank detectors [CONFIRMED].

### Dataset

| Split | Count | Notes |
|-------|-------|-------|
| Malicious (verified) | **3,944** | 108-cell taxonomy (attack vector × behavior × insertion strategy) |
| Generated+verified | 3,214 | Generate-Verify-Feedback; Docker sandbox + syscall monitor + LLM judge |
| In-the-wild | 703 | Narrow: 86.6% one crypto-theft behavior, 81% two accounts |
| Benign (matched) | 4,000 | |

### Taxonomy highlights

- **Vectors:** Code Injection (CI) vs Prompt Injection (PI) vs mixed
- **Behaviors B1–B15:** B1–B9 code-level (CI or PI); B10–B15 agent-reasoning (PI-only)
- **CI yield 94.5%** vs **PI yield 75.8%** — PI harder to verify and detect

### Detector findings [CONFIRMED]

1. Strongest skill-specific tool: **98.4% recall on CI**, collapses on PI and agent-control attacks
2. **Wild-only scoring** swings rankings up to **66 recall points** (VirusTotal near-bottom → top)
3. Supply-chain scanners + PI defenses each see **one half** of a skill; no combo recovers code↔instruction relationship
4. Detection requires **joint reasoning** over task intent, code, and instructions

### Cemini relevance

Use before `@ccc-wiki/concepts/skill-vetting.md` GO — complement static SkillSpector/defenseclaw with MalSkillBench-style **runtime verification** on suspicious skills in lab VLAN only.

## Snippets

> "Detecting malicious skills therefore requires reasoning jointly over task intent, code, and instructions."
> — [Source: arxiv-2606.07131 abstract, retrieved 2026-06-09]

> "Wild-only scoring swings the ranking by up to 66 recall points."
> — [Source: arxiv-2606.07131 abstract, retrieved 2026-06-09]

## Dead Ends

- **Wild ClawHub sample as ground truth** — dominated by one campaign; mis-estimates PI and agent-control coverage.
- **Single-scanner allow/block** — paper confirms no one tool covers hybrid skill surface; keep layered vetting from ClawHub study (2606.01494).
