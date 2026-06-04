---
title: "defenseclaw — enterprise AI security governance (Cisco AI Defense)"
type: entity
tags: [tool, ai-security, governance, defensive, agentic-ai, runtime, apache-2.0]
keywords: [defenseclaw, cisco ai defense, agentic ai security, capability scanning, runtime traffic inspection, mcp scanner, audit trails, splunk, otlp]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/responsible-disclosure.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/agentredguard.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - sources/arxiv-2606-02240-agentredbench.md
  - entities/tools/llm-defense-lattice.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
maturity: draft
created: 2026-05-21
updated: 2026-06-04
cross-wiki-source: @osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md
---

# defenseclaw — enterprise AI security governance

## Relations

- @concepts/ai-for-cybersecurity.md — secures agentic AI runtimes in enterprise deployments
- @concepts/llm-adversarial-fuzzing.md — complements FuzzyAI by providing the defensive-detection layer
- @concepts/llm-pentest-automation.md — governance for LLM-driven security tooling
- @concepts/responsible-disclosure.md — audit-trail requirements for authorized testing
- @entities/tools/nvidia-skillspector.md — skill/MCP supply-chain scanner complementing runtime governance
- @entities/tools/airguard.md — open-source runtime authority guard (MIT)
- @entities/tools/chaincaps.md — MCP composition IFC reference
- @concepts/agent-runtime-guardrails.md — guardrail taxonomy synthesizing enterprise + OSS patterns
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — formal ePCA guardrail research complement

## Raw Concept

Routed from K42 OSINT-wiki tool eval (2026-05-15). Cisco AI Defense's open-source AI security governance platform. Adopt-tier, Apache-2.0, 654 stars.

## Narrative

`cisco-ai-defense/defenseclaw` (Apache-2.0, 654 stars) provides enterprise security governance for agentic AI runtimes. Capability scanning, runtime traffic inspection, audit trails, MCP/skill scanners, and OTLP + Splunk observability.

Primary cybersec fit: blue-team governance layer for any organization deploying LLM-driven security tooling (pentest agents, SOC copilots, threat-intel summarizers). Complements FuzzyAI by supplying the defensive-detection layer that FuzzyAI (offense-only) lacks.

Key capabilities:
- **Capability scanning** — enumerates what an AI agent can do at runtime
- **Runtime traffic inspection** — monitors LLM API calls for prompt-injection attempts
- **MCP/skill scanners** — audits connected MCP servers and skills for over-permissioning
- **Audit trails** — OTLP + Splunk observability for compliance and incident response
