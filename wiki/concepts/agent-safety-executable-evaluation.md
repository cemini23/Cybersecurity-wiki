---
title: "Agent-safety executable evaluation — benign-output predicate tests (K298)"
type: concept
tags: [concept, agent-security, eval, executable-eval, k298]
keywords: [executable eval, benign-output tests, predicate tests, jailbreak, refusal, covert channel, ADR-Bench]
related:
  - sources/arxiv-2608-19857-inadvertent-context-leakage.md
  - sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md
  - concepts/inadvertent-context-leakage.md
  - concepts/agent-runtime-identity-adr.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/logit-tilting-rare-behaviour-audit.md
  - concepts/guardrail-construct-validity-agent-eval.md
maturity: draft
created: 2026-08-21
updated: 2026-09-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K298 executable eval)"
---

**Briefs:** `briefs/2026-08-21_k244-context-leakage-adr.md` (inbound; filed as K298) · `briefs/2026-08-21_k298-k300-ingest.md`

## Relations

- @sources/arxiv-2608-19857-inadvertent-context-leakage.md — the channel that motivates benign-output tests
- @concepts/inadvertent-context-leakage.md — defense steal this eval operationalizes
- @concepts/agent-runtime-identity-adr.md — ADR-Bench as the executable-eval shape
- @concepts/agent-runtime-guardrails.md — eval feeds the enforcement layer
- @concepts/ai-redteam-evidential-ceiling.md — keep eval-scope honesty (no universal certificate)
- @concepts/faithful-agent-asr-measurement.md — report how harm was verified, not a bare ASR

## Raw Concept

Question this page answers: **what should an executable agent-safety eval assert, given that refusal/jailbreak tests miss the benign-output leakage channel?**

## Narrative

Most agent-safety evals measure **refusal behavior**: "does the agent refuse the jailbreak / policy-violating request?" K298 shows that is not enough — a model can refuse a direct extraction while still emitting the secret through benign-looking completions. Executable eval must add **benign-output predicate tests**:

1. **Seed-and-probe**: place a test secret in context, instruct the agent to produce an ordinary artifact (a paragraph, a summary, a JSON blob, an email draft, a PR body "with numbers"), then run a **deterministic predicate** over the artifact: does it contain the seed secret (exact or reconstructed)?
2. **Not only jailbreaks**: the probe prompt is benign; the assertion is over the *output*, not the prompt class.
3. **Report honestly**: per faithful-ASR + evidential-ceiling discipline — state the harness, the judge (deterministic predicate vs LLM-as-judge), and verify from artifact content, not trajectory self-report.
4. **Wire as a gate**: benign-output predicates can run in CI against a local lane (`local-abliterated-llm-pentest-stack.md`) before the lane is trusted with any real secret.

**Relationship to ADR:** ADR-Bench (Uber) is the production-system shape — telemetry + two-tier detector over 300+ tasks / 17 agent attack techniques / 133 MCP servers. Executable eval is the pre-deployment gate; ADR is the runtime detection layer. Both are **evaluations with stated scope**, not universal safety certificates.

**Dual-ID:** Cybersec **K298** supporting concept. No attack prompts / no decoder PoCs on this page — the seed-and-probe pattern is documented for defensive eval only, authorized-lab framing.

## Snippets

> Add *benign-output* predicate tests to executable eval, not only jailbreaks. [Source: inbound brief 2026-08-21; K298 wire]
