---
title: "ATOBench — verification-chain evaluation under deceptive target observations"
type: concept
tags: [concept, agent-security, pentest, evaluation, deception, verification, k278]
keywords: [ATOBench, verification chain, adversarial target observation, AOU, evidence handling, report grounding, deceptive observations, CHeaT, pentest agent eval, activity vs verification]
related:
  - sources/arxiv-2608-12996-atobench-deceptive-observations.md
  - concepts/llm-pentest-automation.md
  - concepts/agent-decoy-defense-autonomous-pentest.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - entities/tools/redagentbench.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/agent-execution-provenance.md
  - entities/tools/atobench.md
  - concepts/measurement-integrity-mcp-security-eval.md
maturity: draft
created: 2026-08-14
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemin-cybersec-agent-audit.mdc (K278)"
---

## Relations

- @sources/arxiv-2608-12996-atobench-deceptive-observations.md — the source paper
- @concepts/llm-pentest-automation.md — the harness methodology ATOBench evaluates
- @concepts/agent-decoy-defense-autonomous-pentest.md — the defense side of the same coin (CHeaT/AgentSnare)
- @concepts/faithful-agent-asr-measurement.md — faithful ASR (K271) requires the verification-chain object ATOBench provides
- @entities/tools/redagentbench.md — sibling executable agent-eval benchmark (K271)
- @concepts/ai-redteam-evidential-ceiling.md — final-outcome metrics cannot certify the process
- @concepts/agent-execution-provenance.md — evidence tracing lineage; ATOBench's source-linked reconstruction is the applied form

## Raw Concept

How do deceptive target responses change an autonomous pentest agent's verification process — and how do you evaluate that process rather than just the final report? Answer: run matched Native/ATO episode pairs under registered observation-contract interventions, align at first contact, and reconstruct the path from later actions → recovered evidence → stopping decision → final claim.

## Narrative

### The problem with outcome-only eval

A pentest agent's target response serves two roles: it guides the next action **and** supports the final vulnerability claim. A deceptive response can redirect both. Existing benchmarks (PentestGPT, AutoPenBench, PentestEval) measure milestones/final findings — they treat target responses as faithful evidence. ATOBench's central observation: **a run may stay active, repeat many probes, or even produce a plausible report after its evidence chain has broken.** Final outcomes and action counts cannot distinguish "active" from "verifying."

### The ATO evaluation design

1. **AOU contracts** — freeze a target security fact + a deception mechanism + intervention boundary/dose + recovery/contradiction path + trajectory/report criteria. Three contracts: JWT (exploit proof), SQLi (resource ownership), Basket (reusable artifacts).
2. **Matched pairs** — Native vs ATO episodes in the same environment, aligned at the first affected response. Task, target, vulnerability, tools, budget stay fixed; only the visible evidence changes.
3. **Four-stage reconstruction** — later actions, recovered evidence, stopping decision, final claim; source-linked so report correctness is interpreted against source-level ground truth, not generic task completion.

### Findings that transfer

- **Activity masks broken verification.** SQLi ATO episodes added a median of 14 actions + 9 repetitions yet *no* model route restored a supported finding. High action counts are not evidence of verification.
- **Recovery depends on usable evidence + preserving it through reporting.** JWT kept 44/45 supported reports because primary evidence survived to the report; SQLi's evidence path broke.
- **Evaluate activity and verification separately** — they are orthogonal axes. This pairs with the faithful-ASR tuple `(harness, judging, cue, judge)` from K271 REDAgentBench: ATOBench is the *offensive-pentest-specific* version of the same insight.

### Cemini application

- **Lab eval only, authorized targets.** The framework is paper-artifact-only at retrieval (repo is a placeholder) — do not clone; steal the *pattern*.
- When auditing our own pentest-agent harnesses (K270/K271 lineage): add a **verification-chain trace** — record not just the final claim but the evidence path that supports it, and flag runs where activity rose while evidence support dropped.
- For defender-side work: ATOBench is the eval complement to CHeaT-style deception. If we build decoy-response lab tests, ATOBench's matched-pair + frozen-contract design is the reproducible evaluation structure.

## Dead Ends

- ATOBench GitHub is a 29-byte README placeholder (no SPDX, 0 stars) as of 2026-08-14 — **do not** attempt a clone or local repro until real artifacts ship. [NEEDS VERIFICATION 2026-09-14]

## Snippets

> ATOBench turns deceptive target observations into a reproducible probe of evidence handling in autonomous penetration testing. This process-level view extends offensive pentest agent evaluation beyond final outcomes. [Source: arXiv 2608.12996 abstract]
