---
title: Agentic containment principles — P1–P6 framework audit matrix
type: concept
tags: [concept, agent-security, containment, framework-audit, memory-integrity, k114]
keywords: [p1-p6, reasoning-execution separation, capability scoping, memory integrity, layer validation, authenticated communication, runtime monitoring, containment gap]
related:
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
  - sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md
  - concepts/trajectory-context-control.md
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/agent-least-privilege-tool-selection.md
  - sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md
  - concepts/self-evolving-agent-security.md
maturity: draft
created: 2026-06-13
updated: 2026-06-23
---

## Relations

- @sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md — primary audit source (K114)
- @sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md — model-layer error-path gap vs framework guardrails
- @sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md — P3/P4 operationalization via GT-MCP (Reference)
- @concepts/trajectory-context-control.md — memory-commit gate pattern
- @sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md — model-layer error-path gap vs framework guardrails
- @concepts/agent-runtime-guardrails.md — runtime enforcement paradigms (AIRGuard, ChainCaps, ePCA)
- @concepts/mcp-security-posture.md — MCP-specific trust boundaries (admission, DCI, SPI, MSTI)
- @concepts/agent-skill-injection.md — install-time + cross-session injection surfaces
- @concepts/agent-execution-provenance.md — P6 trajectory / lineage accountability

## Raw Concept

K114 ingest (2026-06-13): six **containment principles** from arXiv:2606.12797 operationalized as a reusable compliance matrix for LangChain, AutoGPT, and OpenAI Agents SDK — synthesized with containment-gap experiments and cross-linked to MCP/error-path work (2606.07992).

**Self-evolution extension (2606.23075):** static P1–P6 audits assume **immutable anchors** (weights, tool set). Self-evolving agents violate P3/P6 by design — MLAS shows 17/25 cells critical with no effective defense. See @concepts/self-evolving-agent-security.md before certifying any "contained" agent that can modify memory, tools, or architecture.

## Narrative

Agentic LLM systems loop **perception ($P$) → reasoning ($B$) → execution ($E$) → memory update ($\mathcal{U}$)**. Without **inter-layer gates**, corruption at any stage propagates across cycles. Containment requires $\Phi(o_t,m_t)=E(B(P(o_t),m_t)) \in \mathcal{C}$ for policy-safe action space $\mathcal{C}$.

### P1–P6 definitions

| ID | Principle | Mechanism | Gate location |
|----|-----------|-----------|---------------|
| **P1** | Reasoning–execution separation | Policy gate $\pi$ between plan and tool call; only $E(\pi(u_t)) \in \mathcal{C}$ executes | $B \to E$ |
| **P2** | Capability scoping | Session token $T_k$ bounds tools, param ranges, rate limits, expiry | Session bootstrap |
| **P3** | Memory integrity | Integrity function $\mathcal{I}$ validates writes before $\mathcal{U}$; reject adversarial $\delta$ | $E \to \mathcal{U}$ |
| **P4** | Layer-transition validation | Security checks at **every** interface ($P\to B$, $B\to E$, $E\to\mathcal{U}$), not input-only | All boundaries |
| **P5** | Authenticated communication | Signed credentials on inter-agent messages; quarantine unverified | Multi-agent bus |
| **P6** | Runtime monitoring | Trajectory anomaly detection + containment on drift | Span all stages |

**Theorem (containment sufficiency):** P1 + P3 together block single-step memory-poisoning persistent policy violation [Source: arXiv:2606.12797]. Neither alone suffices — P3-only still allows one-shot unsafe execution; P1-only allows poisoned future inputs.

### Compliance matrix (default behavior)

Scoring: ✓ native default | ✓* explicit config | ✗ absent. **No framework achieves ✓ on any principle** [CONFIRMED].

| Principle | LangChain Agents | AutoGPT | OpenAI Agents SDK |
|-----------|------------------|---------|-------------------|
| **P1** Reasoning–exec. sep. | ✓* callbacks | ✗ | ✓* guardrails (opt-in) |
| **P2** Capability scoping | ✓* tool lists | ✗ | ✓* tool lists + handoffs |
| **P3** Memory integrity | ✗ | ✗ | ✗ (no native memory layer) |
| **P4** Layer-transition val. | ✓* partial callbacks | ✗ | ✓* incomplete guardrail hooks |
| **P5** Auth. communication | ✗ | ✗ | ✓* handoffs, no crypto |
| **P6** Runtime monitoring | ✓* LangSmith trace | ✓* HITL | ✓* API monitoring |
| **Summary** | 0✓ / 4✓* / 2✗ | 0✓ / 1✓* / 5✗ | 0✓ / 5✓* / 1✗ |

**Critical gap:** P3 ✗ universally — memory poisoning (SPI, fake policy notes, skill context) persists unchecked by default.

### Empirical anchors (2606.12797)

| Attack | Unguarded | With P3/P1 gates |
|--------|-----------|------------------|
| Memory poison corruption rate | 1.000 (all backends incl. GPT-4o, Claude Haiku) | 0.000 |
| Tool bypass rate | 1.000 | 0.000 |
| Targeted wrongful denial (simple policy) | 88.9% Region B | baseline restored |
| Concealed harm (5-factor policy) | 3–3.5× targeted denials, aggregate acc. stable | validator drops corruption to 0 |

Prototype gates: **0.016 ms** (memory validator), **0.129 ms** (tool policy gate) — deterministic, no LLM in loop.

### Mapping to Cemini stack [TENTATIVE]

| Principle | Cemini surface | Current posture |
|-----------|----------------|-----------------|
| P1 | prod-mcp write tools, brief scp, server Claude actions | Human GO + skill_audit — partial P1 |
| P2 | lazy-tool closed allowlist per server | ✓* operator-maintained |
| P3 | stash episodic memory, hot.md, wiki agent instructions | ✗ no write validator |
| P4 | conductor routing, kb-server ingest | Partial — no unified gate model |
| P5 | Multi-agent handoffs (conductor, federation) | ✗ no crypto message auth |
| P6 | ingest_session_gate, wiki_lint, skill_audit | Advisory batch checks, not runtime P6 |

**Error-path gap (2606.07992):** Even with P1/P6 at framework layer, **raw model layer** complies with error-path IPI at 100% ACR after mutation — framework guardrails (Codex/Gemini CLI) blocked in production CLI eval but bespoke loops remain exposed. See @sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md.

### Priority interventions (paper)

1. **P2** — deny-all tool declaration per session (0% bypass, 0.129 ms in prototype)
2. **P1** — enforce policy gate between reasoning output and execution (not just optional callbacks)
3. **P3** — provenance-verified memory writes (corruption 1.000 → 0.000, 0.016 ms)

## Snippets

> "If an agentic system satisfies P1 … and P3 … then no single-step memory-poisoning attack can induce a persistent policy violation."
> — [Source: arXiv:2606.12797 Theorem 1, retrieved 2026-06-13]

## Dead Ends

- **Opt-in guardrails as compliance** — ✓* scoring still fails secure-by-default bar for public-facing deployment.
- **P3 regex validator alone** — blocks demonstrated demographic/policy-override patterns; semantic evasion remains open.
- **Compound / trajectory attacks (P6 gap)** — paper notes harmless steps composing harm needs trajectory analysis; lightweight gates don't cover.

### IoAI addendum (2026-06-17)

arXiv:2606.12835 **Table 4** extends P1–P6 with **federation-scale** rows: Sybil agents, inter-agent MITM, incentive/reputation gaming. P5 (authenticated communication) is the primary bridge — still ✗ on conductor handoffs. Closed-cell operator posture: treat unknown MCP/skill as Sybil; defer open federation until ANS/DID. See @concepts/internet-of-agentic-ai-ioai.md.

**P2 least-privilege tool choice (2606.20023):** P2 capability scoping at framework layer (deny-all tool declaration) addresses **external** tool exposure; TOOLPRIVBENCH shows **internal** over-privilege among authorized tools — agents escalate after transient narrow-tool failures. Pair P2 allowlists with OPUR eval and runtime authority narrowing (AIRGuard). Harm-refusal alignment does not substitute. See @concepts/agent-least-privilege-tool-selection.md.
