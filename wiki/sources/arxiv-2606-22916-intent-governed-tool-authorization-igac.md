---
title: IGAC — intent-governed tool authorization for AI agents (arXiv 2606.22916)
type: source
tags: [source, arxiv, agent-security, authorization, igac, mcp, least-privilege]
keywords: [2606.22916, igac, intent certificate, openport, manifest filtering, tool authorization]
related:
  - concepts/intent-governed-tool-authorization.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/chaincaps.md
  - entities/tools/airguard.md
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
phase_0_verdict: "Reference 2026-06-24 — IGAC mapped onto Accentrust OpenPort substrate; no standalone IGAC OSS repo; steal intent-certificate + manifest-narrowing pattern for prod-mcp"
---

## Relations

- @concepts/intent-governed-tool-authorization.md — IGAC invariant + OpenPort mapping

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Intent-Governed Tool Authorization for AI Agents |
| Authors | Genliang Zhu (Accentrust / Georgia Tech), Chu Wang (Accentrust / UIUC) |
| arXiv | 2606.22916 |
| Substrate | OpenPort (authorization-dependent discovery) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.22916-intent-governed-tool-authorization-for-ai-agents.pdf` |
| Retrieved | 2026-06-24 |
| Read status | **read** (abstract, IGAC components, OpenPort pilot, high-risk allow stats) |

## Narrative

Static OAuth/API scopes answer "can this credential call this tool?" — insufficient for agents. A read+export integration may be credential-valid yet **unjustified** when the user asked only for a bounded summary.

**Intent-Governed Access Control (IGAC)** treats user **expressed intent** as a monotone, auditable policy attribute:

| Component | Role |
|-----------|------|
| **Intent certificates** | Session-scoped authority ceiling derived from user request |
| **Policy narrowing** | Intent may only **reduce** static integration authority |
| **Intent-aware manifest filtering** | Hide tools/actions outside current intent from planner |
| **Intent–tool–payload consistency checks** | Reject calls whose args exceed certified intent |

**Central invariant:** user intent may only **reduce** authority granted by static integration credentials — never expand.

### Pilot finding

On a constrained high-risk subset, static OpenPort still emitted immediate allow for **85.71%** of high-risk requests — IGAC layering needed for defense-in-depth.

Complements attested MCP admission (2605.24248) and AIRGuard runtime narrowing — IGAC sits at **server-side authorization** before tool metadata reaches the planner.

`[TENTATIVE]` — OpenPort pilot; general MCP mapping not lab-validated in this wiki.

## Snippets

> "A tool call can be authorized by static credentials and still be unjustified by the user's current request."

> "The central invariant is that user intent may only reduce the authority granted by static integration credentials."

[Source: arxiv-2606.22916-intent-governed-tool-authorization-for-ai-agents.pdf]
