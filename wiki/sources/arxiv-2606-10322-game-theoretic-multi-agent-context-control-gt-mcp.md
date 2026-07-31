---
title: GT-MCP — game-theoretic multi-agent context control (arXiv 2606.10322)
type: source
tags: [source, arxiv, agent-security, mcp, prompt-injection, multi-agent, trajectory-control]
keywords: [2606.10322, gt-mcp, context poisoning, causal graph, drift monitoring, stackelberg, self-healing]
related:
  - concepts/trajectory-context-control.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agentic-containment-principles.md
  - concepts/context-fractured-decomposition-attacks.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/internet-of-agentic-ai-ioai.md
  - concepts/crescendo-multi-turn-jailbreak.md
maturity: draft
read_status: read
created: 2026-06-15
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-17 — re-audit: no public GT-MCP repo on GitHub; architectural pattern only until implementation + LICENSE ships [NEEDS VERIFICATION 2026-06-17]"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @concepts/trajectory-context-control.md — synthesized concept (GT-MCP control layer)
- @concepts/agent-runtime-guardrails.md — trajectory-level guard vs single-turn filters
- @concepts/mcp-security-posture.md — extends K100 layer model with context-evolution control
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — cross-session SPI; GT-MCP targets multi-turn trajectory steering

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs |
| Authors | Saeid Jamshidi, Amin Nikanjam, Arghavan Moradi Dakhel, Kawser Wazed Nafi, Foutse Khomh |
| Affiliation | SWAT Lab, Polytechnique Montréal (+ Huawei Montreal, work done at Poly) |
| arXiv | 2606.10322 |
| Location | `raw-sources/arxiv-2606.10322-game-theoretic-multi-agent-context-control-gt-mcp.pdf` |
| Retrieved | 2026-06-15 |
| Read status | **read** (abstract + GT-MCP architecture + eval tables; threat model + ablations skimmed) |
| Phase-0 | **Reference** — paper-only; no GitHub/LICENSE artifact found |

## Narrative

Reframes **prompt injection and context poisoning** in persistent-context / tool-integrated LLM systems as a **trajectory-control problem**: each accepted output updates state that conditions future generations. Standard MCP is a **passive routing layer** — it does not stabilize how context evolves across turns [CONFIRMED].

**GT-MCP** (Game-Theoretic Secure Model Context Protocol) adds a **controller-driven closed loop** over three heterogeneous LLM agents. Selection uses a trust score combining **causal consistency (CCI)**, **cross-agent agreement (AGR)**, and **candidate-specific contextual drift (CDS)** — not majority voting on fluency alone.

### Control primitives

| Component | Role |
|-----------|------|
| Causal context graph $G_t$ | Validated claims + support relations; low-support nodes quarantined |
| Trust selection | $\hat{i}_t = \arg\max_i T_i(t)$ where $T_i = \alpha CCI_i + \beta AGR_i - \gamma CDS_i$ |
| Self-healing | Rollback to checkpoint when $CDS_{\hat{i}_t}(t) > \delta_c$; shallowest depth minimizing structural risk + info loss |
| Controller packet | `pkt_t = ⟨q_t, c_t, r_t, P_t, τ_t, Ω_t⟩` — provenance-separated validated vs untrusted inflows |

Only the **selected** candidate may update validated context $c_t$ through merge operator $U(\cdot)$.

### Threat model + eval schedule

500 turns/run, 10 seeds, 3 agents (GPT-5.3, Llama-3.1-70B, DeepSeek-R1). **328 benign / 172 adversarial** turns across six families: direct injection, retrieval poisoning, tool-output injection, dormant trigger, trajectory steering, agreement mimicry.

### Headline results [CONFIRMED]

| Metric | Full GT-MCP | Best baseline (RAG defense) | Single-agent |
|--------|-------------|-------------------------------|--------------|
| Controller ISR | **0.0%** | 5.8% | 17.8% |
| Mean drift | **0.11** | 3.77 | 8.91 |
| Mean utility | **−0.19** | −1.41 | −3.84 |
| Stable turns | **99.6%** | 90.2% | 71.6% |
| Recovery trigger | **0.4%** | — | — |
| Latency/token | 1.63×10⁻³ s | 1.05×10⁻³ s | 7.9×10⁻⁴ s |

Ablation: removing **No-CDS** worst (ISR 4.5%, mean CDS 2.07); **No-Heal** still 1.6% ISR. Two high-drift events (PromptInject-style + PoisonedRAG-style) both recovered — zero persistent memory corruption.

### Defender mapping

Complements K100 MCP layers (admission, DCI, SPI, MSTI, error-path) with a **trajectory layer**: regulate **whether** tool/retrieval/agent outputs become persistent memory, not just whether they pass a single-turn filter. Aligns with P3/P4 containment (memory integrity + layer-transition validation) from 2606.12797.

## Snippets

> "Although the Model Context Protocol (MCP) standardizes context exchange and tool invocation, it serves as a passive routing layer and does not enforce stability in context evolution."
> — [Source: arxiv-2606.10322 abstract, retrieved 2026-06-15]

> "GT-MCP treats contextual reasoning as a disturbed dynamical process whose state must remain close to a validated reasoning manifold."
> — [Source: arxiv-2606.10322 §I, retrieved 2026-06-15]

> "Full GT-MCP achieves zero observed controller-level injection success, the lowest mean drift, and the highest stable-turn percentage."
> — [Source: arxiv-2606.10322 Table XXX, retrieved 2026-06-15]

## Dead Ends

- **Majority voting alone** — 9.6% ISR; agreement mimicry still steers shared unsupported assumptions.
- **Prompt filtering / RAG sanitization only** — reduce immediate injection but do not govern post-acceptance context updates (5.8% / 7.4% ISR respectively).
- **Adopting GT-MCP code today** — no public implementation in paper; Reference until artifact + LICENSE audit.
