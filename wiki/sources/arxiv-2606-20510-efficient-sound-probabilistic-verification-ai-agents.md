---
title: Efficient and Sound Probabilistic Verification for AI Agents (arXiv 2606.20510)
type: source
tags: [source, arxiv, agent-security, guardrail, formal-methods, datalog, probabilistic-verification, dro]
keywords: [2606.20510, probabilistic datalog, distributionally robust optimization, praline, souffle, pii detector, taint tracking, reference monitor]
related:
  - concepts/agent-probabilistic-datalog-verification.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/ai-for-cybersecurity.md
  - concepts/neuro-symbolic-auditable-reasoning.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - entities/tools/airguard.md
maturity: draft
read_status: read
created: 2026-06-21
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-21 — Google DeepMind paper; no public artifact URL in PDF; Praline prior art (OOPSLA2 2025 doi:10.1145/3763058) also Reference until artifact located"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @concepts/agent-probabilistic-datalog-verification.md — synthesized DRO + probabilistic Datalog framework
- @concepts/agent-runtime-guardrails.md — extends deterministic guardrail stack with noisy-classifier semantics
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — deterministic ePCA complement (SMT vs probabilistic bounds)
- @entities/tools/airguard.md — runtime authority layer paired with probabilistic predicate evaluation

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Efficient and Sound Probabilistic Verification for AI Agents |
| Authors | Alaia Solko-Breslin, Pramod Kaushik Mudrakarta, Mihai Christodorescu, Somesh Jha, Krishnamurthy Dvijotham |
| Affiliations | Google DeepMind, Google, UPenn, UW–Madison |
| arXiv | 2606.20510v1 [cs.CR] |
| Prior art | Praline — Wang et al., *Probabilistic inference for datalog with correlated inputs*, OOPSLA2 2025 (doi:10.1145/3763058) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.20510-2606-20510v1-efficient-and-sound-probabilistic-v.pdf` |
| Retrieved | 2026-06-21 |
| Read status | **read** (abstract, intro, problem formulation, eval setup, conclusion) |

## Narrative

Google DeepMind paper bridging **deterministic Datalog reference monitors** (Palumbo et al. 2602.16708; Wang et al. 2026 AgentSpec) and **noisy upstream classifiers** — PII detectors, declassifiers, redaction tools that fail with non-zero probability per invocation.

### Problem

Deterministic monitors treat predicates as Boolean. Real agents face **probabilistic predicates**: a PII scanner may miss sensitive content; a redactor may fail. Naïve thresholding (block if P(PII) > τ) creates a brittle security–utility trade-off. Prior probabilistic Datalog work (JudgeD, Praline) can compute exact optima but solver overhead is too high for complex agent trajectories at runtime.

### Approach

1. **Distributionally robust optimization (DRO)** — sound **upper bound** on policy-violation probability without unsafe independence assumptions across correlated predicates (e.g., files in same directory → correlated PII detector outputs).
2. **Probabilistic Datalog** — policies expressed as Datalog rules over taint/information-flow semantics; derivation graphs extracted via **Praline-instrumented Soufflé**.
3. **SDP relaxation** — polynomial-time second-order moment tracking when exact LP (Equation 1) is infeasible on large derivation graphs; still sound (conservative bound).

### Taint semantics (terminal agents)

| Transition | Semantics |
|------------|-----------|
| Propagate | taint flows unchanged |
| Merge | taint = OR of inputs |
| Declassify | taint AND redaction_failure |
| CreateClean | false |
| CreateTainted | true |

Applied to **Intercode-NL2Bash** and **ATBench** — bound worst-case probability of sensitive-file leak during data-sharing bash actions.

### Benchmarks

| Benchmark | Role |
|-----------|------|
| Intercode-NL2Bash | Terminal agent taint tracking |
| ATBench | Tool-calling agent taint |
| Praline side-channel tasks | Compiler register-allocation info-flow (6 tasks, Wang et al. 2019) |

**RQ findings (paper):** (1) optimal security–utility trade-off vs prior art at fixed security levels; (2) strict independence assumptions **underestimate** risk when predicates are positively correlated; (3) SDP relaxation matches Praline security on classical policies with higher average latency.

### Cybersecurity relevance

- **Prod MCP / lazy-tool:** upstream content classifiers (secrets scanners, PII regex, VT labels) are probabilistic — deterministic allow/block on point estimates ignores correlated failure modes across related files/API responses.
- **Complements ePCA (2605.29251):** ePCA gives deterministic UNSAT deadlocks under crisp predicates; this paper covers the **ambiguous classifier** layer operators actually deploy.
- **Complements AIRGuard / ChainCaps:** those enforce authority and composition; this paper addresses **policy evaluation under noisy environment predicates** at intercept time.
- **Red team:** test correlated false negatives (same directory batch, sibling MCP tool responses) — independence-assuming monitors may under-bound leak probability.

`[TENTATIVE]` — no public reproduction artifact; latency numbers and benchmark configs not lab-validated in this wiki.

## Snippets

> "In many practical applications of AI agents, there is a need to enforce security policies in the face of ambiguity, leading to probabilistic predicates or state transitions (for example, a declassifier or Personally Identifiable Information (PII) detector that has some failure probability on each invocation)."

> "We address this by introducing a sound and efficient framework for such verification based on distributionally robust optimization, computing sound upper bounds on the probability of policy violation regardless of possible correlations between predicates."

> "Assuming independence can systematically overestimate risks when probabilistic predicates are known to be strictly positively correlated, and the overestimation increases as correlations increase."

[Source: arxiv-2606.20510-efficient-sound-probabilistic-verification-ai-agents.pdf]
