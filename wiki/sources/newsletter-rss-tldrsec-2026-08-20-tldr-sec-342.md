---
title: "tl;dr sec #342 — Figma's Agentic Detection, Agent Identity, Uber's Agent-(E)DR (2026-08-20)"
type: source
tags: [source, newsletter, tldrsec, agent-identity, adr, k298]
keywords: [tldr sec 342, ADR, agent telemetry, SPIFFE, SVID, act=agent, OAuth token exchange, Cloudflare, Trust Ratchet, ADR-Bench]
related:
  - concepts/agent-runtime-identity-adr.md
  - concepts/inadvertent-context-leakage.md
  - concepts/agent-safety-executable-evaluation.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
phase_0_verdict: "REFERENCE 2026-08-21 — newsletter source page; no code, no payloads. Steal: ADR telemetry shape + SPIFFE act=agent identity + Cloudflare task-scoped access."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K298 ADR/identity)"
---

## Relations

- @concepts/agent-runtime-identity-adr.md — primary synthesis (ADR telemetry + SPIFFE `act=agent`)
- @concepts/inadvertent-context-leakage.md — the detector answer to the benign-output channel
- @concepts/agent-safety-executable-evaluation.md — ADR-Bench shape → executable eval

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [tl;dr sec] #342 — Figma's Agentic Detection, Agent Identity, Uber's Agent-(E)DR |
| Author | tl;dr sec newsletter (Daniel Miessler) |
| URL | https://tldrsec.com/p/tldr-sec-342 (retrieved 2026-08-21) |
| Location | newsletter RSS — no raw PDF; egress archive n/a |
| Retrieved | 2026-08-21 |
| Read status | read (via inbound brief + published summary) |

## Narrative

Supporting source for **K298** (agent runtime identity + ADR telemetry). Three steal items:

1. **Uber `uber/ADR` (Agent Detection & Response)** — a production security system for enterprise AI agents: an observability sensor captures agent telemetry (prompts, MCP activity, reasoning traces, tool calls, execution context) feeding a **two-tier detector** for unsafe behavior (credential exposure, prompt injection, data exfiltration, policy-violating tool use); benchmarked with **ADR-Bench** across 300+ tasks, 17 agent attack techniques, and 133 MCP servers. [TENTATIVE] single newsletter summary; verify against Uber's own repo before citing numbers in an engagement.
2. **Agent identity (SPIFFE)** — a trusted local app acts as the trust anchor, verifying the agent's OS code-signing identity and minting **short-lived SPIFFE JWT-SVIDs** backed by a device key in Secure Enclave/TPM; OAuth 2.0 Token Exchange issues delegated tokens carrying **`sub` (human) and `act` (agent) claims**; emerging OAuth Transaction Tokens bind intent per call. No long-lived credentials on disk.
3. **Cloudflare task-scoped access** — Identity Broker for short-lived sender-constrained credentials, a **Task-Scoped Access Engine** for per-request least privilege, a Mediation Layer controlling harness tool calls + network egress, a **Trust Ratchet** that irreversibly removes capabilities when protected events occur, an Agent Activity Log for enforcement evidence, and a Grant Review Loop proposing template changes from observed behavior.

Also in the issue (context only, no ingest): Figma's agentic detection, OpenAI defender-window commentary, CosmosEscape (Wiz, patched — architectural migration), Chainguard install-script scanning. No payloads / no attack kits.

**Phase-0:** REFERENCE / no clone. Dual-ID: Cybersec **K298** supporting source; do not confuse with Uber ADR repo license — verify before any code adoption (none planned; methodology steal only).

## Snippets

> The system pairs an observability sensor that captures agent telemetry (prompts, MCP activity, reasoning traces, tool calls, execution context) with a two-tier detector … benchmarked with ADR-Bench across 300+ tasks covering 17 agent attack techniques and 133 MCP servers. [Source: tldrsec.com/p/tldr-sec-342 (retrieved 2026-08-21)]

> OAuth 2.0 Token Exchange for delegated tokens carrying sub (human) and act (agent) claims … short-lived SPIFFE JWT-SVIDs backed by a device key in the Secure Enclave or TPM. [Source: tldrsec.com/p/tldr-sec-342 (retrieved 2026-08-21)]
