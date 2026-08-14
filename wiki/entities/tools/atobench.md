---
title: "ATOBench — deceptive-observation pentest-agent verification eval"
type: entity
tags: [tool, agent-security, pentest, benchmark, evaluation, deception, reference, k278]
keywords: [ATOBench, ATO, AOU, verification chain, deceptive observations, pentest agent eval, report grounding, evidence verifier]
related:
  - sources/arxiv-2608-12996-atobench-deceptive-observations.md
  - concepts/atobench-verification-chain-deception.md
  - entities/tools/redagentbench.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
phase_0_verdict: "REFERENCE 2026-08-14 — placeholder repo (github.com/daxtar2/ATOBench), 0-byte tree, no SPDX, 0 stars. Pattern steal only; re-check for real artifacts before local repro."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemin-cybersec-agent-audit.mdc (K278)"
---

## Relations

- @sources/arxiv-2608-12996-atobench-deceptive-observations.md — source paper
- @concepts/atobench-verification-chain-deception.md — synthesized concept
- @entities/tools/redagentbench.md — sibling agent-eval benchmark (K271)
- @concepts/llm-pentest-automation.md — the harness methodology being evaluated

## Raw Concept

ATOBench is an evaluation framework for autonomous penetration-testing agents that makes the **verification process observable under deceptive target responses**. It packages response changes as frozen AOU (Adversarial Target Observation Unit) contracts, pairs transformed (ATO) episodes with native episodes aligned at first contact, and reconstructs the path from later actions → recovered evidence → stopping → report claim.

## Narrative

**Status: REFERENCE (no code).** The `daxtar2/ATOBench` repo is a 29-byte README placeholder as of 2026-08-14 — no SPDX license, empty tree, 0 stars. The value is the **evaluation design**, not an artifact:

- 450 episodes / 225 matched pairs across 3 AOU contracts (JWT, SQLi, Basket) and 5 model routes
- Key result: SQLi ATO adds median 14 actions + 9 repetitions yet no route restores a supported finding → **activity ≠ verification**
- JWT keeps 44/45 supported reports when primary evidence survives to the report

Adopt the ATOBench pattern (frozen observation contracts + matched pairs + four-stage reconstruction) when auditing our own pentest-agent harnesses. **Local adoption: NO** — no code, no clone.

## Dead Ends

- Placeholder repo confirmed 2026-08-14 via `gh api`. Re-check GitHub before any local repro.

## Snippets

> ATOBench turns deceptive target observations into a reproducible probe of evidence handling in autonomous penetration testing. [Source: arXiv 2608.12996 abstract]
