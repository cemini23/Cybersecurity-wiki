---
title: "Refusal-under-knowledge and per-turn withhold contracts for LLM agents"
type: concept
tags: [methodology, llm-security, guardrail, refusal, harness, agent-audit, llm-eval, trust-boundary]
keywords: [refusal-under-knowledge, withhold contract, hint ladder, policy core, deterministic detector, LLM judge, over-help ladder, Socratic, per-turn contract, injection-proof]
related:
  - sources/arxiv-2608-12292-tutor-withhold-refusal-contract.md
  - concepts/agent-runtime-guardrails.md
  - concepts/concept2scenario-refusal-suppression.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/safety-harness-evolution.md
  - concepts/recognition-enforcement-gap-instruction-arbitration.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K276)"
---

# Refusal-under-knowledge and per-turn withhold contracts for LLM agents

## Relations

- @sources/arxiv-2608-12292-tutor-withhold-refusal-contract.md — the source paper (deployed tutor, UW Bothell)
- @concepts/agent-runtime-guardrails.md — per-turn contracts are a concrete enforcement paradigm inside runtime guardrails
- @concepts/concept2scenario-refusal-suppression.md — refusal-surface evaluation family; this page is the per-turn contract enforcement instance
- @concepts/mcp-security-posture.md — trust-boundary principle in parallel: the binding decision layer must not read untrusted input
- @concepts/agent-skill-injection.md — same injection-resistance logic (untrusted content must not reach the privileged component)
- @concepts/safety-harness-evolution.md — the withhold contract is a harness artifact that the measure→diagnose→fix loop can evolve (K268)

## Raw Concept

The question this page answers: how do you make an LLM reliably *refuse a capability it has* — withhold an answer it could trivially produce, to a user who can see it can — under adversarial pressure, without over-blocking legitimate use? Answer pattern: lift the decision out of the prompt into a **non-LLM policy core fed only trusted state**, enforce it per-turn with a **deterministic detector**, check risky replies with a **collusion-resistant LLM judge**, and calibrate with a **reason-capturing automated loop**.

## Narrative

### Refusal-under-knowledge vs classical refusal

Classical LLM safety refuses content the model should not produce (harmful instructions). Refusal-under-knowledge is the harder converse: the model *should* produce the content in general, but must withhold it for the user's own good — a frustrated student asking for the answer, a limited-capability assistant that must not complete a security-sensitive task. Naive metrics conflate distinct failures, and a capable model under pressure does not withhold reliably on a prompt alone.

### The contract pattern (transferable to any agent)

1. **Discretize the behavior into a typed ladder** — the eight-rung hint ladder (acknowledge → clarify → point to concept → leading question → verbal approach → worked example → pseudocode blanks → full solution). The ladder is the unit of decision, enforcement, and measurement. For other domains this is a permission/help ladder: what may be revealed, done, or emitted at each level.
2. **Compute the per-turn ceiling in a non-LLM policy core (P2)** — ordinary code, no model calls, no access to untrusted input, fed only trusted learner/agent state. This makes the binding property *injection-proof* (a prompt edit can never silently weaken it) and *exhaustively unit-testable* (500+ deterministic invariant tests).
3. **Deterministic detector outranks model judgment (P3)** — a code-reveal detector strips solution code independently of any LLM, with lenient/strict modes per contract; correctness comes from external deterministic signals (compile/run/test), not model assertion.
4. **Collusion-resistant judge on risky turns** — a small-model judge sees only the contract + draft + retrieved sources, never the raw untrusted input; returns allow/revise/block with a rule id and a one-sentence reason. Revision strongly preferred over blocking (P4).
5. **Calibrate with a reason-capturing automated loop** — scripted adversarial personas (answer-seeker, gate-evader, injector, earnest-but-stuck) driven through the live pipeline; a stronger auditor re-judges; each rejection's *reason* is recorded so failures are fixed by cause, not guessed at.

### The over-help ladder: a failure taxonomy

Violations of a withhold contract descend an ordered gross→subtle ladder, and each fix exposes the next: solution leaks under pressure → over-blocking honest help (ceiling too low) → fabricated citations (contract pressures the model to ground, it invents sources) → naming the exact bug in prose → over-grounding general facts as course claims. The lesson: **no single prompt edit produces reliable withholding**; only a reason-capturing measure→diagnose→fix loop walks the ladder to compliance. Also note the measurement-artifact trap (Rung 0): an auditor re-judging without the same retrieved sources reads every citation as unsupported.

### Authorized-use framing

This is a defensive harness pattern for agent runtimes, tool-permission ceilings, and safety-harness tuning — and for eval work on refusal surfaces. It is not a jailbreak aid. Applied to a pentest/SOC copilot, the same contract pattern enforces "assist, don't complete the sensitive action" per-turn, decided outside the model, with HITL before any prod harness mutation (K276).

## Snippets

> The most important property both injection-proof and unit-testable, so prompt edits could never silently weaken it. [Source: arXiv:2608.12292 p.6]

> The failures walked steadily down an over-help ladder, each rung subtler than the last, every one caught and named by the captured judge reason and fixed by cause until none remained. [Source: arXiv:2608.12292 p.5]

## Dead Ends

- Deterministic detection has known blind spots (split-fence, plain-prose, cross-language reveals) that are accepted by design; compensating layers (judge, execution path) plus "path of least resistance" is the goal, not leak-proofness.
- Over-blocking is the more harmful error than a leak (P4): if the guarded path is too frustrating, users route around it to unguarded tools, recreating the original harm.
