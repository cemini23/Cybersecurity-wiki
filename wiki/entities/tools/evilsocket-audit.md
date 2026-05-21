---
title: "evilsocket/audit — 8-stage vulnerability discovery agent (Glasswing pattern)"
type: entity
tags: [tool, vulnerability-discovery, llm-agent, claude-code, glasswing-pattern, static-analysis, mit, adopt]
keywords: [evilsocket, audit, glasswing pattern, vulnerability discovery, claude code agent sdk, reachability gating, adversarial verification, false-positive filter, nginx cve]
related:
  - concepts/llm-vulnerability-discovery.md
  - concepts/ai-for-cybersecurity.md
  - concepts/exploit-development.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/analyzing-github-projects-agentic-infra-2026-05-21.md"
---

# evilsocket/audit — 8-stage vulnerability discovery agent

## Relations

- @concepts/llm-vulnerability-discovery.md — extends the Detect→Attack pipeline with Glasswing architecture
- @concepts/ai-for-cybersecurity.md — production-ready LLM-driven security tooling
- @concepts/exploit-development.md — produces verified exploit PoCs (e.g., Nginx CVE-2026-42945)
- @concepts/llm-pentest-automation.md — architectural reference for agent-based vulnerability discovery

## Raw Concept

Routed from K56 OSINT-wiki ingest (2026-05-21). 8-stage vulnerability-discovery agent driven by Claude Code Agent SDK. MIT, 388 stars. Implements Cloudflare's Project Glasswing pattern.

## Narrative

`evilsocket/audit` (MIT, 388 stars) is an 8-stage vulnerability-discovery agent driven by Claude Code Agent SDK (Claude Pro/Max subscription, no API key). Architecture follows Cloudflare's **Project Glasswing pattern**:

| Mechanism | Purpose |
|---|---|
| Many narrow agents | Multiple tightly-scoped agents investigate specific code paths in parallel |
| Deliberate disagreement | Secondary agent (different model/temperature) attempts to disprove first agent's findings → adversarial verification → false-positive filter |
| Explicit reachability gating | System must cryptographically/logically prove attacker-controlled input traverses to vulnerable sink. Without proof, discarded. |
| Feedback loops | Confirmed bugs seed subsequent hunts for identical patterns elsewhere |

Public demonstration: PoC for Nginx CVE-2026-42945 (bypassed ASLR on vanilla Ubuntu via LFI/file-read primitive). Zero open issues — stable, focused codebase. The Glasswing pattern (many narrow agents + deliberate disagreement + reachability gating + feedback loops) is the highest-value architectural primitive for LLM-driven vulnerability discovery.
