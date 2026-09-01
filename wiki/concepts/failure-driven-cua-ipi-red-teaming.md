---
title: "Failure-driven CUA IPI red-teaming — deterministic oracle, not LLM judge (K316)"
type: concept
tags: [concept, agent-security, red-team, cua, ipi, lab-only, k316]
keywords: [SIR, computer use agent, indirect prompt injection, failure-driven principles, deterministic oracle, joint success, RedTeamCUA, adaptive red team]
related:
  - sources/arxiv-2608-30207-sir-cua-self-improving-redteam.md
  - concepts/agent-vm-sandboxing.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-09-01
updated: 2026-09-01
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K316)"
---

## Relations

- @sources/arxiv-2608-30207-sir-cua-self-improving-redteam.md — SIR (2608.30207)
- @concepts/agent-vm-sandboxing.md — CUAs need VM/perimeter containment for IPI eval
- @concepts/faithful-agent-asr-measurement.md — state-grounded scoring vs trajectory self-report
- @concepts/ai-redteam-evidential-ceiling.md — adaptive adversaries change what static benches prove

## Raw Concept

Question: **how should we red-team OS-level computer-use agents against indirect prompt injection?**

## Narrative

Static, hand-authored injections **understate** adaptive IPI risk on **computer-use agents (CUAs)** that read untrusted screen content and act on a real OS. **SIR (K316, 2608.30207)** inverts typical self-improving attack loops: it **learns from refusals**, diagnoses defensive behaviors, and distills **named composable principles** (plain language) rather than only mining successful jailbreaks.

**Operator steal:**
1. **Score with deterministic VM/state oracles** — filesystem, permissions, services — not LLM judges (manipulable). Require **joint success** (adversarial + benign task) so “attack success” ≠ crashed benign workflow.
2. **Treat adaptive red-team as a lab primitive** — authorized targets only (RedTeamCUA-class sandboxes); **no injection/principle payloads in wiki**.
3. **Static CUA safety benchmarks can obscure cross-model robustness gaps** — adaptive search surfaces systematic differences (paper: large ASR drop Opus 4.6→4.8 on same pipeline).
4. Pairs K311/K271 faithful measurement — activity and plausible text ≠ verified compromise.

## Snippets

> A successful IPI is not merely an undesirable textual response: it can produce a concrete compromise of the underlying computer system. [Source: arXiv 2608.30207 §1, paraphrase]
