---
title: "Teaching an LLM tutor to withhold the answer — supervisor architecture + evidence-driven Socratic tuning (arXiv 2608.12292)"
type: source
tags: [source, arxiv, llm-security, guardrail, refusal, harness, agent-audit, llm-eval]
keywords: [2608.12292, refusal-under-knowledge, withhold contract, supervisor architecture, hint ladder, policy core, deterministic detector, LLM judge, over-help ladder, Socratic tutoring, prompt injection]
related:
  - concepts/refusal-under-knowledge-withhold-contract.md
  - concepts/agent-runtime-guardrails.md
  - concepts/concept2scenario-refusal-suppression.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
maturity: draft
read_status: read
created: 2026-08-13
updated: 2026-08-13
phase_0_verdict: "REFERENCE 2026-08-13 — deployed system, no public code URL. Harness-steal pattern: machine-checkable per-turn withhold/refuse-capability contract. K276 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K276)"
---

**Briefs:** `briefs/2026-08-13_k276-tutor-withhold-contract.md`

## Relations

- @concepts/refusal-under-knowledge-withhold-contract.md
- @concepts/agent-runtime-guardrails.md — withholding *is* a runtime-guardrail instance; enforcement lives outside the generating model
- @concepts/concept2scenario-refusal-suppression.md — refusal-surface evaluation family; this is the per-turn-contract enforcement instance
- @concepts/mcp-security-posture.md — trust boundary: the binding decision layer never reads untrusted input (parallel to MCP admission)
- @concepts/agent-skill-injection.md — same injection-resistance principle (untrusted input must not reach the privileged decision component)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior |
| Author | Yusuf Pisan (University of Washington Bothell) |
| arXiv | 2608.12292 (cs.CY, v1 12 Aug 2026) |
| Code | None public at retrieval (2026-08-13); deployed system at UW Bothell, no repo URL |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.12292-teaching-a-large-language-model-tutor-to-withhol.pdf` |
| Retrieved | 2026-08-13 |
| Read status | read (7 pp, full text extracted) |

## Narrative

The paper reports a deployed LLM tutor that enforces **answer-withholding as a per-turn, machine-checkable contract** — the core of its product value, not a safety wrapper. Background evidence: Bastani et al. RCT (~1000 secondary students) found an unguarded chatbot raised practice scores but lowered later tool-removed exam scores; a Socratically guarded version kept the practice gain and removed the loss. The tutor must therefore perform **refusal-under-knowledge**: it knows the answer, the student sees that it knows, the student is frustrated and asks directly — and the system must still withhold while staying warm and genuinely helpful.

**Supervisor architecture (six principles):**
- P1 withhold-by-default; help follows an **eight-rung hint ladder** (H0 acknowledge → H7 full solution), an explicit typed object that is the unit of decision/enforcement/measurement.
- P2 **decide without reading student text**: a non-LLM policy core, fed only trusted learner state, computes the per-turn contract (help ceiling, goals in scope, exam lockdown, grounding requirement, judge escalation). Injection-proof and exhaustively unit-testable.
- P3 **deterministic signals outrank model judgments**: a deterministic code-reveal detector strips solution code independently of any LLM; code correctness comes from compile/run/test, never model assertion.
- P4 prefer **revising a reply over refusing it** — over-blocking is a measured failure (students route around friction back to unguarded chatbots).
- P5 one writer for learner state (auditable, typed transitions).
- P6 make everything observable (per-turn logs of contract, verdicts, help level, latency, cost).

A small pre-classifier maps the student message to an intent enum (framed as data, never instruction); a strategist proposes one instructional move; a small-model **judge** checks risky drafts against the contract (collusion-resistant: sees only contract + draft + retrieved sources, never the raw student message), returning allow/revise/block with a rule id and one-sentence reason at temperature zero.

**Calibration method (no human subjects):** four acceptance gates — G1 no solution reveals, G2 no over-blocking of honest help (earnest revise rate ≤5%), G3 hint-ceiling compliance ≥95% under adversarial pressure, G4 exam integrity. Offline adversarial simulation with four scripted personas (earnest-but-stuck, answer-seeker, gate-evader, injector), then a live billed loop against a throwaway database with a printed cost ledger (hard assertion it refuses to start without the throwaway-db check).

**The over-help ladder** (measure → diagnose → fix): first run showed 43% earnest revise rate + 54% reported ceiling compliance — half was a *measurement artifact* (auditor re-judged without the retrieved sources the live judge saw). Descending the ladder: Rung 1 code-under-pressure (lenient detector missed partial code), Rung 2 over-blocking honest debugging (ceiling set too low — fixed with a constructive-code floor), Rung 3 fabricated citations (contract pressured the actor to cite; fixed: cite only retrieved sources) + code-adjacent mislabeling, Rung 4 naming-the-bug-in-prose and over-grounding general facts. Final state: 0% earnest revise rate (G2), 100% hint-ceiling compliance (G3), zero rung breaches, cost well under a dollar per loop.

**Cyber relevance:** this is the harness-steal pattern for any agent that must *refuse a capability it has*. The recipe — put the irreversible decision in code (non-LLM policy core on trusted state), enforce per-turn with a deterministic detector, calibrate with a reason-capturing automated loop, and treat violations as an ordered gross→subtle ladder — transfers directly to agent-runtime guardrails, tool-permission ceilings, and safety-harness tuning.

## Snippets

> A useful LLM tutor must, by default and under pressure, decline to produce the solution it could trivially produce while still helping the student make progress... Classical refusal in LLM safety is refusal of content the model should not produce. A tutor instead faces what we call refusal-under-knowledge. [Source: arXiv:2608.12292 p.1]

> The single most stabilizing choice was P2: computing the help ceiling in a non-LLM policy core fed only trusted state made the most important property both injection-proof and unit-testable, so prompt edits could never silently weaken it. [Source: arXiv:2608.12292 p.6]

> We offer the measure, diagnose, and fix loop as a reusable recipe for any LLM agent that must refuse a capability it has. [Source: arXiv:2608.12292 abstract]

## Dead Ends

- Not a learning-outcomes result: the decisive test (delayed, tool-removed assessment, controlled) is future work pending a pilot cohort + human-subjects approval. The four gates pass on ~two dozen scripted turns run a handful of times.
- The detector misses split-fence, plain-prose, and cross-language reveals **by design**; the goal is making the guarded path the path of least resistance, not leak-proofness.
- LLM judge + auditor inherit LLM-as-judge reliability limits (position/verbosity/self-preference biases); mitigation is the rubric, deterministic detector, escalation, and planned human-rater calibration.
