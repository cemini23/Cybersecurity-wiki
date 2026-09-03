---
title: "Safety harness evolution — trajectory-driven safe-boundary learning for LLM agents"
type: concept
tags: [methodology, agent-security, harness-evolution, guardrail, self-evolving]
keywords: [safety harness, harness evolution, SHE, artifact decomposition, attribution-guided, safety-utility selection, Rule Bank, Safety Memory]
related:
  - sources/arxiv-2608-09885-she-safety-harness-evolution.md
  - entities/tools/she-safety-harness-evolution.md
  - concepts/agent-runtime-guardrails.md
  - concepts/harnessopt-bench.md
  - concepts/self-evolving-agent-security.md
  - concepts/safeevolve-harness-policy-co-evolution.md
  - concepts/ai-for-cybersecurity.md
  - concepts/blast-radius-reversible-context-eviction.md
  - sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md
  - concepts/decoding-level-taboo-diagnostic.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/refusal-under-knowledge-withhold-contract.md
  - sources/arxiv-2608-12851-skill-misevolution.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608-12977-self-evolving-security.md
  - concepts/self-evolving-runtime-defense.md
  - sources/arxiv-2608-16465-jailbreakskill.md
  - concepts/evolving-attack-skill-libraries.md
maturity: draft
created: 2026-08-11
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc (K268)"
---

# Safety harness evolution — trajectory-driven safe-boundary learning for LLM agents

## Relations

- @sources/arxiv-2608-09885-she-safety-harness-evolution.md
- @entities/tools/she-safety-harness-evolution.md
- @concepts/agent-runtime-guardrails.md — harness evolution *is* a runtime-guardrail lifecycle; pairs static enforcement with adaptive boundaries
- @concepts/harnessopt-bench.md — harness optimization is measurable (HarnessOpt-Bench); SHE is the safety-flavored instance
- @concepts/self-evolving-agent-security.md — self-evolution must be bounded (validity check + safety-utility selection), else attacks embed across cycles
- @concepts/ai-for-cybersecurity.md — agent-security operationally relevant for pentest/SOC copilots
- @concepts/blast-radius-reversible-context-eviction.md — layering: what may be *replaced* in context (gate/verification) vs which harness artifact *learns* a new boundary
- @sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md — taboo-guided alignment as an active robustness regularizer for evolved harnesses
- @concepts/decoding-level-taboo-diagnostic.md — decoding-time robustness diagnostic pairs with harness evolution to keep safety boundaries learned, not hard-coded
- @concepts/faithful-agent-asr-measurement.md — harness-dependent ASR makes harness-evolution gains measurable only under a stated measuring tuple (K271)

- @concepts/refusal-under-knowledge-withhold-contract.md
## Raw Concept

Agent safety depends on the harness as much as the weights. Existing mechanisms (rules, runtime guardrails) are static after deployment; failures visible in trajectories cannot feed back into the safety boundary. This page captures the SHE pattern (2608.09885): make the harness an evolvable set of functionally decoupled artifacts and let trajectory failures drive bounded, validated refinements.

## Narrative

### Why harness-level safety

For long-horizon, tool-using agents, risk arises from **execution steps** performed by harness components (context construction, memory retrieval, tool authority, response filtering), not just model outputs. Static guardrails (LlamaFirewall, SafeHarness) specify boundaries but do not learn from rollout failures — leaving a gap between *safety diagnosis* and *safety improvement*.

### The SHE recipe (four artifacts + attribution loop)

1. **Decouple the harness into artifacts with explicit safety responsibilities** — System Prompt (behavioral contract), Rule Bank (structured rules + interventions), Safety Memory (unresolved-failure experience), Tool Policy (tool authority + enforcement). Coupled functions obscure responsibility attribution and make localized evolution dangerous.
2. **Diagnose trajectories along three axes** — harm domain (privacy/financial/physical/cyber/availability/misinfo), attack surface (user/context/tool-output/tool-spec/memory), failure mode (unsafe compliance, tainted-context compliance, unauthorized tool use, unsafe side effect, over-refusal).
3. **Route to the smallest responsible artifact** — a failure spanning one responsibility gets a localized edit; this avoids interfering with unrelated components.
4. **Bounded edits + validity check** — each edit specifies target artifact, scope, operation, learned content, evidence. `ValidEdit` rejects reward-hacking or evaluator-specific shortcuts and capability-removal-only "gains".
5. **Safety–utility selection with rejection feedback** — a candidate replaces the best harness only if `S↑ ∧ U≥`, otherwise it is stored in `Frej` so later rounds avoid repeating the mistake.

### Evidence and limits

- Agent-SafetyBench: ASR 8.6%→5.5%, Clean UBR 25.7%→19.8%, UA 33.5%→47.6%; vs static SafeHarness, 3.1× lower ASR.
- Held-out AgentHarm transfer: Harm Score 19.8%→9.8%, Harm Refusal 78.4%→86.4%; cross-model transfer without re-evolution.
- Component-replacement ablation shows each learned artifact contributes; evolution-model ablation shows the loop works across GPT-5.5 / DeepSeek-V3.2 / GLM-5.2.
- The evolved boundary example (app acquisition) shows SHE learns *recommendation-vs-execution* distinctions rather than broad refusals.

### HITL / live-harness constraints (operational)

- **No unbounded self-modification of a LIVE/production harness** — evolution must run in a lab/offline loop with safety–utility selection and rollback (pairs HarnessOpt/K252 self-evolving + K253 Argus verification gates).
- Treat the validity check as the guardrail *on the evolution itself*: it exists precisely to stop the loop from reward-hacking its own evaluator.
- Attribution quality is bounded by the diagnosis/judge model; audit the judge before trusting evolved artifacts.

## Snippets

> The safety of LLM agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. [Source: arXiv:2608.09885 abstract]

> SHE uses a structured safety diagnosis to attribute the failure and route it to the most relevant harness artifacts for bounded local refinement. Candidate refinements are retained only after validity checking and best-harness selection. [Source: arXiv:2608.09885 p.2]

## Dead Ends

- Treating the harness as a single monolithic prompt makes attribution impossible — SHE's functional decoupling is the load-bearing design choice.
- Naive "evolve against a single ASR number" encourages reward hacking; the joint safety–utility + validity check is what separates SHE from a benchmark-chaser.
