---
title: "Threat-preserving representation sensitivity in agent-security benchmarks"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.03585, k396]
related:
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/benchmark-shortcut-attack-pyramid-audit.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
read_status: read
created: 2026-10-06
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-06 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K396)"
---

## Relations

- @concepts/threat-preserving-representation-sensitivity.md — K408-K417 ingest / 2026-10-09
## Relations

- @concepts/threat-preserving-representation-sensitivity.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/benchmark-shortcut-attack-pyramid-audit.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Threat-preserving representation sensitivity in agent-security benchmarks |
| arXiv | 2610.03585 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.03585-threat-preserving-representation-sensitivity-in.pdf |
| Retrieved | 2026-10-06 |
| Read status | read (deep-read) |

## Narrative

**K396 — the strongest finding of the batch.** An agent-security ASR is routinely read as a property of the agent. It is not: it is a property of the **agent plus the agent-visible representation**. **Threat-preserving representation sensitivity (TPRS)** holds the task, harmful action, policy, ground truth, environment, and evaluation criteria fixed and changes only how the threat is *presented*: **ΔT(B,m) = ASR(T(B),m) − ASR(B,m)**. Across **28,904 agent runs** on three benchmarks the score moves in both directions. On **ASB**, renaming attacker tools to threat-**neutral** names **raises** committed ASR by **11.67 pp** (36.67%→48.34%) on GPT-5-mini and **13.21 pp** (20.85%→34.06%) on Haiku 4.5. On **MCPTox**, introducing threat-related names **lowers** ASR by **11.00 pp** / **4.11 pp**. On AgentDojo the effect is near zero. The shift is **not explainable by threat vocabulary alone** — a neutral name matched on token count, length, and casing reproduced **8.54 of 11.00** points. The sharpest reading: when the **attacker** picks the tool name (as on ASB), the benchmark's own naming choice is an unintentional defence, and the reported ASR **understates** what the attacker can get by 11.67–13.21 pp. Operator steal: **stop treating one ASR as a robustness certificate** — report sensitivity across a controlled set of threat-preserving representations, state when an attack counts as success, and measure benign utility under the same transformations. Pairs K388 (breaking level) and K321 (construct validity). **No attack payloads in wiki.**

## Snippets

> See arXiv 2610.03585 abstract. [Source: arXiv 2610.03585 (retrieved 2026-10-06)]
