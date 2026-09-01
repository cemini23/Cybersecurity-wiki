---
title: "SIR — self-improving red-teaming for computer-use agents (arXiv 2608.30207)"
type: source
tags: [source, arxiv, agent-security, red-team, cua, ipi, lab-only, k316]
keywords: [2608.30207, SIR, computer use agent, CUA, indirect prompt injection, IPI, failure-driven principles, deterministic oracle, RedTeamCUA]
related:
  - concepts/failure-driven-cua-ipi-red-teaming.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
phase_0_verdict: "REFERENCE 2026-09-01 — HF space TrustSafeAI/SIR WATCH; no attack-principle payloads in wiki. Authorized-lab CUA eval only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + agent-audit.mdc (K316)"
---

## Relations

- @concepts/failure-driven-cua-ipi-red-teaming.md — primary steal (learn from failures; deterministic VM oracle)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SIR: Self-improving Red-teaming for Computer Use Agents |
| Authors | Chen Xiong, Zhiyuan He, Pin-Yu Chen, Stjepan Picek, Tsung-Yi Ho |
| arXiv | 2608.30207 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.30207-sir-self-improving-red-teaming-for-compute-use-a.pdf |
| Retrieved | 2026-09-01 |
| Read status | read (abstract + method) |
| Public artifact | HF space `TrustSafeAI/SIR`; no SPDX paper repo at hunt |

## Narrative

**SIR** is a black-box **indirect prompt injection (IPI)** red-team framework for **OS-level computer-use agents (CUAs)**. Unlike static hand-written injections, SIR composes stealthy on-screen injections from reusable **plain-language principles** and runs an outer loop that **learns from failed trajectories** — diagnosing why the victim refused and distilling bypasses into named principles reapplied across tasks.

**Eval discipline:** scores attacks with a **fully deterministic oracle** on filesystem/service/permission state (RedTeamCUA-style), not an LLM judge. Requires **joint success**: adversarial objective **and** benign user task complete — hijack ≠ task abort.

**Key results (paper):** compositional search + feedback raises ASR vs static baseline (e.g. 4%→22% Claude Opus 4.8; 0%→28% Gemini 3.5 Flash). Principles transfer across victim architectures.

**Why filed (K316):** adaptive CUA red-team at OS boundary pairs `@concepts/agent-vm-sandboxing.md`, faithful measurement (state oracle), and lab IPI eval. **Authorized lab only** — no principle/injection payloads in wiki; no LIVE third-party CUAs.

## Snippets

> Attack outcomes are evaluated using a fully deterministic oracle rather than an LLM judge. [Source: arXiv 2608.30207 abstract]

> SIR learns from its failures … distills a bypass into a reusable attack principle stated in plain language. [Source: arXiv 2608.30207 abstract, paraphrase]
