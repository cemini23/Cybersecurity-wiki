---
title: Internet of Agentic AI (IoAI) — federated agent ecosystems
type: concept
tags: [concept, agentic-ai, multi-agent, ioai, interoperability, threat-model, mcp]
keywords: [ioai, internet of agentic ai, agent naming service, a2a, controlled emergence, table 4]
related:
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/agentic-containment-principles.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/trajectory-context-control.md
  - concepts/llm-code-review-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - entities/tools/sevra-bench.md
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - sources/arxiv-2608-13030-intersage.md
  - concepts/intersage-trust-native-ioa-protocol.md
maturity: draft
created: 2026-06-17
updated: 2026-08-15
---

## Relations

- @sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md — primary vision source (2606.12835)
- @concepts/mcp-security-posture.md — MCP as IoAI interoperability primitive; K100 admission stack
- @concepts/agentic-containment-principles.md — P1–P6 local containment matrix
- @concepts/trajectory-context-control.md — GT-MCP drift gate for inter-agent context merge

## Raw Concept

Ingest 2026-06-17: arXiv:2606.12835 frames **IoAI** as Internet-scale ecosystems of heterogeneous LLM agents — discovery, negotiation, tool use, workflow execution — with **controlled emergence** as the central engineering problem. Synthesized for mapping IoAI Table 4 threats to existing wiki controls.

## Narrative

**IoAI** extends bounded multi-agent frameworks (CrewAI, AutoGen, LangGraph) to **open, cross-organizational** agent networks. Intelligence is collective: agents specialize (planner, executor, verifier), communicate over shared substrates (HTTP, pub/sub, **MCP**, A2A), and form temporary coalitions. Unlike traditional distributed systems, nodes **reason, delegate, and revise plans** — amplifying both capability and failure propagation.

### Architecture layers (portable mental model)

```
Discovery (ANS / registries / gossip)
  → Identity + trust (DID, VC, PKI, attestation)
    → Messaging (sync RPC, pub/sub, P2P)
      → Agent protocols (MCP, A2A, ANP, ACP)
        → Workflow orchestration + resource management
          → Governance + incentive compatibility
```

**Cemini operator note:** prod-mcp + lazy-tool implements a **closed IoAI cell** (single operator, deny-by-default tool admission) — not public federation, but the same threat classes apply at LAN/laptop scale.

### IoAI Table 4 → wiki control mapping

| IoAI threat (Table 4) | Local control (this wiki) | Gap |
|----------------------|---------------------------|-----|
| Sybil / rogue agents | @concepts/mcp-security-posture.md admission + skill_audit | No federated ANS |
| Impersonation / credential theft | P5 authenticated communication (@concepts/agentic-containment-principles.md) | Human-centric OAuth assumed |
| MITM / tampering / replay | TLS + signed tool manifests [TENTATIVE] | Inter-agent bus unsigned today |
| Prompt injection | SPI, VATS, runtime guardrails | Cross-agent context merge |
| Tool/API compromise | DCI, WebMCP MSTI, SkillSpector | Supply-chain depth |
| Workflow poisoning | GT-MCP trajectory gate; SEVRA merge-gate eval | Multi-org workflow bus |
| Cascading failures | Checkpoint rollback (GT-MCP pattern); containment P4 | Federation blast radius |
| Supply-chain / data poisoning | skill_audit, preingest_check, defending-code harness | Model/dataset provenance |
| Reputation / incentive gaming | — | **Open gap** — no wiki control yet |

### Controlled emergence

Useful collective behavior from local agent rules **without** sacrificing predictability. Operationalized locally as:

1. **Deny-by-default** tool/skill admission (K100)
2. **Memory-commit gates** before persistent context merge (GT-MCP pattern)
3. **Human GO** on write tools and brief distribution (P1 partial)
4. **Eval harnesses** (SEVRA, SeClaw) before granting autonomous approve/execute authority

### Research anchors cited in paper

DARPA MATHBAC (formal agent communication), NIST AI RMF GenAI profile, OWASP LLM Top 10, MCP spec 2025-11-25 [TENTATIVE — not independently verified 2026-06-17].

## Snippets

[Source: arxiv-2606.12835 §3]

> IoAI seeks to transform isolated agents and bounded multi-agent systems into a globally interconnected ecosystem in which autonomous agents identify collaborators, exchange information, negotiate responsibilities, share resources, and collectively execute workflows through standardized communication and trust mechanisms.

## Dead Ends

- **Premature open agent marketplace** without ANS + incentive-compatible reputation — Sybil and collusion rows in Table 4 become practical immediately.
- **Single-framework orchestration as IoAI** — LangGraph alone is a bounded MAS, not Internet-scale federation.
