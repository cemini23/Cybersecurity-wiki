---
title: "Agent runtime identity + ADR telemetry (K298)"
type: concept
tags: [concept, agent-security, identity, adr, spiife, telemetry, k298]
keywords: [agent identity, ADR, agent detection and response, SPIFFE, JWT-SVID, act=agent, OAuth token exchange, trust ratchet, task-scoped access]
related:
  - sources/arxiv-2608-19857-inadvertent-context-leakage.md
  - sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md
  - sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md
  - concepts/inadvertent-context-leakage.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/agent-execution-provenance.md
  - concepts/mcp-security-posture.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc + mcp-tool-control.mdc (K298 ADR/identity)"
---

**Briefs:** `briefs/2026-08-21_k244-context-leakage-adr.md` (inbound; filed as K298) · `briefs/2026-08-21_k298-k300-ingest.md`

## Relations

- @sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md — ADR telemetry + SPIFFE `act=agent` + Cloudflare task-scoped access
- @sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md — SOC foundations (asset-ID map, gather-not-decide)
- @concepts/inadvertent-context-leakage.md — the channel this layer detects and constrains
- @concepts/agent-runtime-guardrails.md — enforcement paradigms this wires into
- @concepts/agent-least-privilege-tool-selection.md — least-privilege tool grants pair with task-scoped access
- @concepts/agent-execution-provenance.md — telemetry → evidence provenance
- @concepts/mcp-security-posture.md — MCP tool calls are a primary telemetry + grant surface

## Raw Concept

Two questions: **how do we know which agent (or human) performed an action, and how do we detect agent misbehavior at runtime?** Synthesized from tl;dr sec #342 (Uber ADR, SPIFFE agent identity, Cloudflare task-scoped access) + SecPro #248 (SOC foundations), routed with K298.

## Narrative

**ADR (Agent Detection & Response) is the agentic analog of EDR.** An observability sensor captures agent telemetry — prompts, MCP activity, reasoning traces, tool calls, execution context — and a **two-tier detector** flags unsafe behavior: credential exposure, prompt injection, data exfiltration, policy-violating tool use. The Uber ADR-Bench shape (300+ tasks, 17 agent attack techniques, 133 MCP servers) is the eval template. [TENTATIVE] newsletter-sourced; verify repo claims before quoting in an engagement.

**Identity: `sub=human` / `act=agent`.** A trusted local app verifies the agent's OS code-signing identity and mints **short-lived SPIFFE JWT-SVIDs** backed by a device key in Secure Enclave/TPM — no standing long-lived credential on disk. OAuth 2.0 Token Exchange carries **`sub` (human) + `act` (agent)** claims; per-call intent binding via Transaction Tokens. This gives auditors a durable "who/what acted" answer and lets grants be **task-scoped** (per-request least privilege), with a **Trust Ratchet** that irreversibly removes capabilities when a protected event fires, plus an activity log and a grant-review loop.

**Why it matters for K298 (inadvertent leakage):** you cannot detect or attribute a benign-output covert channel without (a) telemetry over what the model *emitted* (not just what it was told) and (b) an identity layer that says which agent/human held which grant. Detection complements the *prevention* steal (never return secrets to the model).

**SOC foundations (SecPro #248):** telemetry is only as good as the data under it — one asset-ID map, normalized timestamps/metadata, agent least privilege, RAG over runbooks, and **automate gather, not decide** (decisions stay human/approval-bound).

**Phase-0:** REFERENCE / no clone (newsletter methodology). No ADR product install without a Phase-0 audit of the actual repo.

## Snippets

> OAuth 2.0 Token Exchange for delegated tokens carrying sub (human) and act (agent) claims … short-lived SPIFFE JWT-SVIDs backed by a device key in the Secure Enclave or TPM. [Source: tldrsec.com/p/tldr-sec-342 (retrieved 2026-08-21)]

> A useful rule is to automate information gathering before decision-making. [Source: secpro.substack.com/p/248 (retrieved 2026-08-21)]
