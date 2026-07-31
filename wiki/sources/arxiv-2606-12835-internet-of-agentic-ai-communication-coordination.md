---
title: The Internet of Agentic AI — communication, coordination, collective intelligence (arXiv 2606.12835)
type: source
tags: [source, arxiv, agentic-ai, multi-agent, ioai, mcp, interoperability, threat-taxonomy]
keywords: [2606.12835, ioai, internet of agentic ai, agent communication protocol, a2a, ans, table 4 threat taxonomy]
related:
  - concepts/internet-of-agentic-ai-ioai.md
  - concepts/agentic-containment-principles.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/trajectory-context-control.md
  - concepts/llm-code-review-agent-security.md
  - entities/tools/sevra-bench.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
maturity: draft
read_status: read
created: 2026-06-17
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-17 — vision paper; no code artifact; maps IoAI Table 4 threats to existing wiki controls"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @concepts/internet-of-agentic-ai-ioai.md — synthesized IoAI architecture + threat taxonomy
- @concepts/mcp-security-posture.md — MCP as emerging IoAI interoperability layer (§4.5)
- @concepts/agentic-containment-principles.md — P1–P6 as local containment vs IoAI-scale failures

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Internet of Agentic AI: Communication, Coordination, and Collective Intelligence at Scale |
| Author | Quanyan Zhu (NYU Tandon, Center for Cybersecurity) |
| arXiv | 2606.12835v1 [cs.MA] |
| Location | `raw-sources/arxiv-2606.12835-internet-of-agentic-ai-communication-coordination.pdf` |
| Retrieved | 2026-06-17 |
| Read status | **read** (abstract, §2–5, §7, Table 4 threat taxonomy) |

## Narrative

Vision paper for the **Internet of Agentic AI (IoAI)** — heterogeneous agents discovering collaborators, negotiating tasks, exchanging context, invoking tools, and executing workflows across cloud/edge/device/organizational boundaries. Synthesizes single-agent autonomy, MAS, distributed computing, game theory, and security engineering into a **socio-technical ecosystem** metaphor (Internet-scale, not bounded CrewAI teams).

### Core design themes

| Theme | Claim |
|-------|-------|
| **Controlled emergence** | Harness collective behavior from local interactions while preserving predictability, alignment, accountability |
| **Communication substrate** | Discovery (ANS/DNS analog), identity (DID/VC/PKI), messaging (HTTP/gRPC, pub/sub, MCP, A2A, ANP, ACP) |
| **Interoperability gap** | LangGraph / AutoGen / CrewAI / Semantic Kernel coexist but lack cross-vendor agent federation |
| **Security as first-class** | Ephemeral autonomous agents break human-centric IAM (OAuth/OIDC); delegation chains amplify blast radius |

### IoAI threat taxonomy (Table 4) — categories

1. **Identity** — Sybil, impersonation, credential theft, rogue agents
2. **Communication** — MITM, eavesdropping, tampering, replay
3. **Workflow/behavior** — prompt injection, tool/API compromise, workflow poisoning, cascading failures
4. **Economic/incentive** — incentive manipulation, collusion, resource exploitation, reputation gaming
5. **System availability** — DoS, supply-chain attacks, data poisoning, infrastructure attacks

Paper cites MCP (spec 2025-11-25), OWASP LLM Top 10, NIST 800-53/207, AI RMF GenAI profile as alignment anchors [TENTATIVE — citation list not independently verified].

### Cybersecurity relevance

- **Red team:** IoAI maps attack surfaces beyond single-app pentest — registry poisoning, inter-agent MITM, workflow poisoning across org boundaries
- **Blue team:** P5 authenticated communication + provenance + containment P1–P6 as **local** mitigations; IoAI adds federation-scale identity and incentive controls
- **Operator stack:** prod-mcp / lazy-tool is a **bounded** IoAI cell — not open federation, but same threat classes at smaller scale

No benchmark numbers or exploit recipes — architectural reference only.

## Snippets

[Source: arxiv-2606.12835 p.1 abstract]

> The rapid emergence of autonomous AI agents is transforming artificial intelligence from isolated model inference into distributed systems of reasoning, communication, and action.

[Source: arxiv-2606.12835 Table 4 — workflow threat row]

> **Workflow poisoning** — An adversary injects malicious data, tasks, or intermediate steps into an agentic workflow. Affected properties: integrity, reliability, traceability.

[Source: arxiv-2606.12835 §4.5 — MCP]

> MCP provides a JSON-RPC-based framework for structured context exchange, tool invocation, and hierarchical delegation of tasks.

## Dead Ends

- **Treating MCP transport security as IoAI security** — paper explicitly positions protocols as enablers; governance/trust layers still required (see @concepts/mcp-security-posture.md).
- **Open agent federation without ANS/DID** — premature for prod-mcp; keep deny-by-default admission.
