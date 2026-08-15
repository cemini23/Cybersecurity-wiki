---
title: InterSAGE — trust-native Internet of Agents identity and capability protocol
type: concept
tags: [concept, multi-agent, identity, ioai, mcp]
keywords: [InterSAGE, Agent Identity Card, AIC, capability attenuation, DID, IoA]
related:
  - sources/arxiv-2608-13030-intersage.md
  - concepts/internet-of-agentic-ai-ioai.md
  - concepts/mcp-security-posture.md
  - concepts/agentic-containment-principles.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/intersage-trust-native-ioa-protocol.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc (CCC K278 dual-ID — not Cybersec ATOBench)"
---

## Relations

- @sources/arxiv-2608-13030-intersage.md — positioning paper
- @concepts/internet-of-agentic-ai-ioai.md — IoAI threat model; InterSAGE is an identity/capability layer
- @concepts/mcp-security-posture.md — capability ads must be provenance-checked, not trusted as grant

## Raw Concept

How do federated agents prove *who* they are and *what* they may do without collapsing identity into a single spoofable handle?

## Narrative

**Agent Identity Card (AIC):** four independently signed dimensions — developer, code package, operator, deployment context. One compromised dimension cannot impersonate the rest. **Capability-aware discovery:** skill/tool advertisements are DID-bound Verifiable Credentials; verify issuer, subject binding, permission alignment, freshness before interaction. **Monotonic capability attenuation** — least privilege is a signed structural invariant; app policy stays independent. Dual-ID: CCC K278 ≠ Cybersec K278 ATOBench. No product install. [Source: arXiv:2608.13030]
