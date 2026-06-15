---
title: Trajectory context control — GT-MCP multi-agent context governance
type: concept
tags: [concept, agent-security, mcp, prompt-injection, multi-agent, context-poisoning, trajectory-control]
keywords: [gt-mcp, causal graph, contextual drift, cci, agr, cds, self-healing, stackelberg, closed-loop]
related:
  - sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agentic-containment-principles.md
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - concepts/agent-execution-provenance.md
maturity: draft
created: 2026-06-15
updated: 2026-06-15
---

## Relations

- @sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md — primary source (GT-MCP)
- @concepts/mcp-security-posture.md — K100 trust-boundary layers; trajectory control sits above them
- @concepts/agent-runtime-guardrails.md — side-effect authorization vs context-state authorization
- @concepts/agentic-containment-principles.md — P3 memory integrity + P4 layer-transition validation
- @concepts/context-fractured-decomposition-attacks.md — artifact-mediated drift across instances; GT-MCP addresses in-session trajectory steering
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — stored SPI; GT-MCP rollback/quarantine as complementary control

## Raw Concept

Daily digest ingest (2026-06-15): arXiv:2606.10322 — **trajectory context control** treats multi-turn LLM context as a **controlled dynamical state** rather than an append-only log. GT-MCP is the reference architecture; portable pattern applies to any MCP/agent harness with persistent memory.

## Narrative

Persistent-context agents (RAG, tools, multi-agent buses) fail when **locally plausible adversarial fragments accumulate** across turns — direct/indirect injection, poisoned retrieval, tool outputs, dormant triggers, trajectory steering, agreement mimicry. Single-turn filters and passive MCP routing do not regulate **which accepted outputs become memory** [CONFIRMED].

### Problem framing

| View | Limitation |
|------|------------|
| Jailbreak / refusal testing | Ignores state after "safe" intermediate turns |
| Instruction isolation (Spotlighting, StruQ) | Boundary enforcement without trajectory regulation |
| MCP as transport | Routes context; does not stabilize evolution |
| Majority voting | Amplifies shared errors; 9.6% ISR in GT-MCP eval |

**Trajectory-control objective:** keep validated context $c_t$ on a **reasoning manifold** represented by causal graph $G_t$; block unsupported merges before they condition turn $t+1$.

### GT-MCP control loop (portable pattern)

```
Untrusted inflows (RAG, tools, user) → observed context c̃_t (provenance-tagged)
  → 3 heterogeneous agents → candidate claims S_i
  → per-candidate: CCI_i, AGR_i, CDS_i (tentative update)
  → select argmax T_i = α·CCI + β·AGR − γ·CDS
  → if CDS_selected > δ_c: self-heal (quarantine + rollback depth d*)
  → else merge selected output into validated c_{t+1}
  → audit record R_t (all candidates, scores, recovery metadata)
```

**Key invariant:** only the **trust-selected** output updates persistent validated context — not every agent response, not every tool return.

### Trust signals (operational definitions)

| Signal | Measures | Ablation impact (ISR) |
|--------|----------|------------------------|
| **CCI** | Structural support of extracted claims in $G_t$ | No-CCI → **3.8%** |
| **AGR** | Cross-agent semantic agreement | No-AGR → **2.9%** |
| **CDS** | Drift if candidate were merged | No-CDS → **4.5%** (largest) |
| **Self-heal** | Rollback + quarantine on high CDS | No-Heal → **1.6%** |

Full pipeline: **0.0% ISR**, 99.6% stable turns, recovery in 0.4% of turns [Source: arxiv-2606.10322 Table XXVIII/XXX].

### Layer placement in Cemini / prod-mcp stack [TENTATIVE]

| K100 layer | Trajectory control relationship |
|------------|--------------------------------|
| Admission (allowlist) | Upstream — blocks bad servers before context assembly |
| DCI / semantic honesty | Upstream — description↔code before tool trust |
| SPI / persistence | Adjacent — GT-MCP quarantine targets same persistent channels |
| Error-path (VATS) | Adjacent — error responses are untrusted inflows in `c̃_t` |
| **Trajectory (GT-MCP class)** | **Downstream of generation, upstream of memory commit** — gates $U(c_t, \hat{y}_t)$ |

Maps to **P3 + P4** in @concepts/agentic-containment-principles.md: validate writes before $\mathcal{U}$; check every $P \to B \to E \to \mathcal{U}$ transition.

### Phase-0 posture

**Reference** until GT-MCP reference implementation + LICENSE publish. Pattern is adoptable in harness design (multi-model probe + drift gate + checkpoint store) without importing paper code.

## Snippets

> "Robust LLM interaction requires active governance of reasoning trajectories rather than passive acceptance of context updates."
> — [Source: arxiv-2606.10322 §I, retrieved 2026-06-15]

> "Trust, therefore, reflects whether a candidate is structurally grounded, semantically compatible with peer agents, and safe to integrate into a persistent context."
> — [Source: arxiv-2606.10322 §V-B, retrieved 2026-06-15]

## Dead Ends

- **Trust score without candidate-specific CDS** — shared drift term does not affect selection ranking; ablation shows 4.5% ISR.
- **Full context reset on anomaly** — GT-MCP uses bounded subgraph rollback (max depth 2, max quarantine 4 fragments) to preserve validated memory.
- **Single dominant model** — DeepSeek-R1 stabilizer role shows value of heterogeneous agents under controller mediation, not static ranking.
