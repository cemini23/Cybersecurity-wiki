---
title: "Trace-verified CTF agent eval — flag ≠ demonstrated exploit (K311)"
type: concept
tags: [concept, agent-security, ctf, offensive, evaluation, evidence, k311]
keywords: [CTF-ABACUS, trace-verified, solve profile, flag recovery, shortcut, faithful capability, process evidence, pentest-agent eval]
related:
  - sources/arxiv-2608-26237-ctf-abacus.md
  - sources/arxiv-2608-26086-ood-traceml.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/atobench-verification-chain-deception.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/security-agent-authority-auditability-slr.md
maturity: draft
created: 2026-08-28
updated: 2026-08-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K311)"
---

## Relations

- @sources/arxiv-2608-26237-ctf-abacus.md — source paper (trace-based agent auditing)
- @sources/arxiv-2608-26086-ood-traceml.md — contrast steal: outcome benches hide development process
- @concepts/faithful-agent-asr-measurement.md — same faithful capability-measurement lane (K271 REDAgentBench)
- @concepts/atobench-verification-chain-deception.md — verification-chain breakage on a live target (K278)
- @concepts/ai-redteam-evidential-ceiling.md — what a fixed-budget red-team eval can prove

## Raw Concept

Question: **is "the agent reached the flag" the same as "the agent performed the exploit"?** If not, CTF and agentic offensive-security evals systematically overstate capability.

## Narrative

A CTF/offensive benchmark score that counts a recovered flag as a win is **not** a capability measurement. The flag can be reached by **direct exposure, memorized recall, external lookup, guessing, or an unsupported claim** — none of which is demonstrated exploitation. CTF-ABACUS (K311, 2608.26237) reconstructs each run as an **evidence-grounded solve profile**: it splits agent actions into **pentest phases** and **categorical techniques**, records where exploitation happens and where the flag first appears, and checks whether the recovered flag is **backed by demonstrated behavior**.

**Result:** trace-verified exploits account for only **62–87% of recovered flags** across 1,435 attempts / 240 challenges / six models / two judge lenses. The rest are shortcuts with shallow evidence chains.

**Operator steal (authorized lab / product pentest harness):**
1. **Count a flag only when the trace shows exploitation.** For pentest/CTF-agent evals, record the evidence path (probe → enumerated finding → verified exploit → root cause) and gate "success" on the full chain, not the terminal flag.
2. **Distinguish intended-exploit success from shortcut recovery.** Challenge signatures (aggregate solve profiles) reveal which challenges an agent solved "the intended way" vs "the easy way" — this is the real capability signal.
3. **Report the trace, not just the score.** A fixed-budget eval that reports only ASR/flag-count overstates capability; add a trace-verified rate (pairs K271 faithful ASR).
4. **Do not treat activity as success** — an agent can stay active and produce a plausible report after its evidence path broke (pairs K278 ATOBench).
5. **Authorized-lab CTF eval only** — no LIVE third-party targets; no PoC payloads in wiki.

## Snippets

> Trace-verified exploits account for only 62-87% of recovered flags across benchmarks, while shortcut recoveries follow substantially shallower evidence chains. [Source: arXiv 2608.26237 abstract]

> Read this way, the gap becomes concrete … outcome-based benchmarks record this gap but not its cause, because they grade the final submission and discard the development process behind it. [Source: arXiv 2608.26086 TraceML abstract]
