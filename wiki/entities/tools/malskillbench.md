---
title: MalSkillBench — runtime-verified malicious agent skills benchmark (Reference)
type: entity
tags: [tool, benchmark, agent-skills, supply-chain, reference, k109]
keywords: [malskillbench, lxyeternal, skill benchmark, code injection, prompt injection, docker verification]
related:
  - sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md
  - concepts/agent-skill-injection.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/defenseclaw.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - "@ccc-wiki/concepts/skill-vetting.md"
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - sources/arxiv-2607-13987-agent-skill-security-skillsec-eval.md
maturity: draft
created: 2026-06-09
updated: 2026-07-16
phase_0_verdict: "Reference 2026-06-09 — open dataset + baselines; verify LICENSE on GitHub before code import; lab Docker only."
---

## Relations

- @sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md — paper + methodology
- @concepts/agent-skill-injection.md — CI/PI taxonomy under test
- @entities/tools/nvidia-skillspector.md — evaluated detector (strong CI, weak PI)
- @entities/tools/defenseclaw.md — enterprise scan complement (not runtime-verified ground truth)
- @sources/arxiv-2606-01494-clawhub-security-signals.md — wild scanner disagreement context
- @sources/arxiv-2606-07943-poise-position-aware-skill-injection.md — stealth PI attacks benchmark gap

## Raw Concept

Daily digest ingest (2026-06-09). GitHub: [lxyeternal/MalSkillBench](https://github.com/lxyeternal/MalSkillBench) — 3,944 runtime-verified malicious skills + 4,000 benign; arXiv:2606.07131.

## Narrative

**Reference-tier** benchmark measuring **detector quality on hybrid agent skills** (executable scripts + agent-facing markdown). Closed-loop Generate-Verify-Feedback admits samples only when malicious behavior fires in Docker under syscall monitoring + LLM judge.

**Use cases (authorized lab):**
- Regression-test SkillSpector / defenseclaw skill-scanner before prod catalog changes
- Quantify CI vs PI detection gaps (98.4% vs collapse on PI for best skill-specific tool in paper)
- Avoid wild-only eval bias (up to 66-point recall swing)

**Phase-0:** verify LICENSE file before importing code; run verification pipeline only on isolated lab host — malicious skill corpus by design.

**Not** a substitute for human GO on skill install (@ccc-wiki/concepts/skill-vetting.md steps 1–10).

## Snippets

Dataset: 108 taxonomy cells — attack vector × behavior (B1–B15) × insertion strategy.

Wild tail: small **agent control-plane** attacks beyond crypto-theft campaign majority.

## Dead Ends

- **Production deployment of malicious corpus** — research artifact only; never sync to prod-mcp paths.
- **Wild sample alone for vendor marketing** — paper shows narrow wild distribution; use full benchmark for claims.
