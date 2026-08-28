---
title: "Non-decaying loop safety state — trajectory monitors do not compose (K312)"
type: concept
tags: [concept, agent-security, guardrails, loop-safety, tool-use, k312]
keywords: [LoopHarness, non-decaying loop state, trajectory-scoped monitor, composition failure, fragmented evidence, cooling-off, irreversible action, loop monitor]
related:
  - sources/arxiv-2608-27141-safety-does-not-compose.md
  - concepts/step-level-agent-guardrails.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K312)"
---

## Relations

- @sources/arxiv-2608-27141-safety-does-not-compose.md — source paper (non-decaying loop state)
- @concepts/step-level-agent-guardrails.md — step-level guard (K307); complements, does not replace, loop state
- @concepts/agent-runtime-guardrails.md — guard placement in the agent stack

## Raw Concept

Question: **when an LLM agent runs as a long unattended loop across many tool-using trajectories, does a per-trajectory (or per-step) guard still protect it?**

## Narrative

**No — not by itself.** A safeguard defined over a single trajectory is **re-initialized** at each trajectory boundary. For an adversary that **fragments its evidence across several iterations** (probe in loop 1, stage in loop 3, trigger in loop 7), a trajectory-scoped monitor has **TPR = FPR**: the evidence never appears in the window it sees, so it is statistically indistinguishable from a coin flip. A monitor that **retains cross-iteration state at the loop level** separates the two.

**Why a decaying risk score fails:** carrying a **geometrically decaying risk score** only forces the adversary to wait out a **constant** cooling-off period. A patient adversary simply waits a fixed amount between loops — the delay does not scale with the horizon N, so it is not a real amortized defense.

**LoopHarness (K312)** restores a **persistent, non-decaying safety state at the loop level** and, under **mediated commits** + an arbiter **detection floor δM**, **bounds the expected number of unauthorized irreversible actions**.

**Operator steal (authorized lab / product pentest harness / MCP loops):**
1. **Do not reset the safety monitor each trajectory.** Loop-scoped tasks (batch agents, overnight harness runs, unattended tool loops) need state that persists across trajectories and grows with the horizon.
2. **Do not treat a per-turn/per-step guard as sufficient.** A pre-execution step guard (K307 StepGuard) is the right enforcement *point*, but it is **per-invocation**; an adversary that spreads evidence over many loop iterations defeats it. Combine a step/action gate with a **loop-level accumulator**.
3. **Persist a non-decaying safety state** for irreversible-effect tool loops (writes, sends, commits, API mutations) — not a decaying score/PID.
4. **Do not rely on a "wait a bit" cooling-off** — a constant interval is defeated by a patient adversary. Make the required wait scale with the accumulated risk / horizon.
5. **Do NOT clone `getathelas/LoopHarness`** (an Apple OS) or the `loopharness.ai`/`bing` name-collision repos. Policy only; no runtime wire.

## Snippets

> Every trajectory-scoped monitor has a true-positive rate equal to its false-positive rate … because the evidence it would need never appears in the window it sees, whereas a monitor retaining cross-iteration state separates the two perfectly. [Source: arXiv 2608.27141 abstract]
