---
title: The Containment Gap — agentic framework safety audit (arXiv 2606.12797)
type: source
tags: [source, arxiv, agent-security, framework-audit, memory-poisoning, public-facing-ai, k114]
keywords: [2606.12797, containment gap, langchain, autogpt, openai agents sdk, memory integrity, policy gate, p1-p6]
related:
  - concepts/agentic-containment-principles.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - concepts/agent-execution-provenance.md
maturity: draft
read_status: read
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/agentic-containment-principles.md — P1–P6 matrix + compliance synthesis
- @concepts/agent-runtime-guardrails.md — architectural vs model-layer enforcement
- @concepts/mcp-security-posture.md — SPI/memory poisoning overlaps P3
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — stored SPI empirical baseline
- @sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md — 247-paper lifecycle survey (compositional defense gap)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements |
| Authors | Md Jafrin Hossain, Mohammad Arif Hossain, Weiqi Liu, Nirwan Ansari |
| arXiv | 2606.12797 |
| Location | `research to be indexed/arxiv-2606.12797-the-containment-gap-how-deployed-agentic-ai-fram.pdf` |
| Retrieved | 2026-06-13 |
| Read status | **read** (methodology + matrix + experiments + interventions) |
| Verdict | **GO** — P1–P6 audit rubric portable to Cemini agent harness reviews |

## Narrative

Public-facing agentic systems (government benefits, healthcare triage, financial advising) compose perception → reasoning → execution → memory in a recursive loop. This paper asks whether **dominant frameworks provide architectural containment** — enforced boundaries between stages — independent of model alignment.

### Compositional pipeline

$$\Phi(o_t, m_t) = E(B(P(o_t), m_t))$$

Corruption at any stage propagates forward and into memory via $\mathcal{U}$. **Execution containment** requires $\Phi(o_t, m_t) \in \mathcal{C}$ for policy-safe action space $\mathcal{C}$.

### Framework audit (LangChain, AutoGPT, OpenAI Agents SDK)

Scoring: ✓ = native default; ✓* = requires explicit config; ✗ = absent. **Zero native ✓ on any P1–P6 principle** across all three frameworks [CONFIRMED]. Cohen's $\kappa = 0.81$ inter-rater reliability on 18 dyads.

| Pattern | Finding |
|---------|---------|
| Universal P3 failure | Memory integrity ✗ on **all three** — despite memory poisoning being top documented agent vuln class |
| Safety optional | Most controls are ✓* (opt-in callbacks/guardrails), not secure-by-default |
| Autonomy ↔ compliance | AutoGPT (5✗) < LangChain (2✗) < OpenAI SDK (1✗) — more autonomy, fewer native barriers |

Full matrix: @concepts/agentic-containment-principles.md.

### Empirical validation — LangChain welfare agent

**Scenario:** Synthetic benefits agent (250 claims, 5 regions); Qwen-2.5 3B via Ollama + Claude Haiku 4.5 + GPT-4o cross-backend.

| Attack | Without guard | With guard | Overhead |
|--------|---------------|------------|----------|
| Memory poison (corruption rate) | **1.000** | **0.000** | 0.016 ms |
| Tool bypass (path traversal / API / write) | **1.000** | **0.000** | 0.129 ms |

**Memory poisoning:** Single adversarial write at claim 11 ("Region B income <$30k → deny") → **100% corruption** on targeted post-poison decisions; mean accuracy **0.908 → 0.558**; Region B wrongful denial **88.9%**. Attack **generalizes** to Claude Haiku and GPT-4o (corruption 1.000) — alignment does not protect upstream memory.

**Complex five-factor policy:** Aggregate accuracy stays near baseline while Region B wrongful denials rise **3–3.5×** — targeted harm **concealed from standard monitoring** [CONFIRMED].

### Lightweight interventions (deterministic, no LLM)

1. **Memory integrity validator (P3)** — provenance + schema + demographic-targeting regex on `save_context`; reject external policy overrides
2. **Tool policy gate (P1/P2)** — deny-all allowlist, path canonicalization, rate limit

Both wrap LangChain abstractions; sub-millisecond overhead; backend-agnostic.

**Cemini relevance:** Audit lazy-tool / conductor / prod agent loops against P1–P6 before public-facing or high-privilege deployment. Memory writes to stash, wiki, and session files are P3 surfaces; prod brief staging is P1/P2 scope enforcement.

## Snippets

> "We do not observe native compliance in any of them. Memory integrity … is not observed in any of the three evaluated frameworks."
> — [Source: arXiv:2606.12797 abstract, retrieved 2026-06-13]

> "A single memory-poisoning write … increasing the wrongful denial rate for targeted applicants to 88.9%."
> — [Source: arXiv:2606.12797 abstract, retrieved 2026-06-13]

> "With both [P1 and P3] active, corruption drops from 1.000 to 0.000 across all backends."
> — [Source: arXiv:2606.12797 §2.3 Theorem 1, retrieved 2026-06-13]

## Dead Ends

- **Regex-only P3 validator** — paper acknowledges fragility vs semantic adversarial rewrites; LLM semantic validation trades latency + new failure modes.
- **LangChain-only empirical replication** — audit covers three frameworks but runtime attacks demonstrated on LangChain only; AutoGPT / OpenAI SDK replication future work.
