---
title: "Safety Does Not Compose — non-decaying loop state for autonomous agents (arXiv 2608.27141)"
type: source
tags: [source, arxiv, agent-security, guardrails, loop-safety, tool-use, k312]
keywords: [2608.27141, LoopHarness, non-decaying loop state, trajectory-scoped monitor, composition failure, fragmented evidence, TPR = FPR, risk-score decay, irreversible action]
related:
  - concepts/non-decaying-loop-safety-state.md
maturity: draft
read_status: read
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "REFERENCE 2026-08-28 — safety-state design principle; policy only. No paper repo at hunt (name-collision getathelas/LoopHarness is an Apple OS — do NOT clone)."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K312)"
---

## Relations

- @concepts/non-decaying-loop-safety-state.md — primary steal (trajectory monitors do not compose)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents |
| Authors | Chenhao Wu et al. (UCAS / NTU / JD.com / PKU / Fudan / Fullive-AI) |
| arXiv | 2608.27141 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.27141-safety-does-not-compose-non-decaying-loop-state.pdf` |
| Retrieved | 2026-08-28 |
| Read status | read (abstract + central result) |
| Public code | **none matching at hunt** — `getathelas/LoopHarness` is an Apple OS, not this paper; `penguinliao/loopharness` / `bekzodaka/loopharness.ai` also unrelated. No clone. |

## Narrative

**Problem:** LLM agents running as **autonomous loops** repeatedly discover work, plan, execute tool calls, verify, and persist state across many unattended iterations. Most agent safeguards are defined over a **single trajectory**, and their safety state is **re-initialized** when the next trajectory begins.

**Central result (separation):** against an attack whose **evidence is fragmented across several iterations**, every **trajectory-scoped monitor has a true-positive rate equal to its false-positive rate** — however expressive it is — because the evidence it needs never appears in the window it sees. A monitor that **retains cross-iteration state** separates the two perfectly.

**The naive repair is insufficient:** carrying a **geometrically decaying risk score** does not help, because the **cooling-off** period a patient adversary must wait is a **constant** that does **not grow with the horizon N**.

**LoopHarness (K312):** restores a **persistent, non-decaying safety state at the loop level**. Under **mediated commits** and an arbiter **detection floor δM**, it bounds the expected number of **unauthorized irreversible actions**.

**Why filed (K312):** this is the **loop-level** counterpart to K307 StepGuard (which is a **step-level** pre-execution guard — and in this wiki StepGuard stays **K307**, not the CCC K312). The key distinction: per-turn/per-trajectory guards (including a step guard) do not compose across iterations; you need **non-decaying loop state** that survives trajectory boundaries. Pairs K239 execution fidelity (block before irreversible effect). **No matching repo at hunt** → REFERENCE / policy only; no runtime wire; no clone.

## Snippets

> The agent safeguards in wide use are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. [Source: arXiv 2608.27141 abstract]

> Against an attack whose evidence is fragmented across several iterations, every trajectory-scoped monitor has a true-positive rate equal to its false-positive rate … whereas a monitor retaining cross-iteration state separates the two perfectly. [Source: arXiv 2608.27141 abstract]

> The obvious repair of carrying a geometrically decaying risk score is insufficient, because the cooling-off period a patient adversary must wait is a constant that does not grow with the horizon N. [Source: arXiv 2608.27141 abstract]
