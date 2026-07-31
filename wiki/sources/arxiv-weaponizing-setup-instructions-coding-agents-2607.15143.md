---
title: Weaponizing setup instructions against AI coding agents (arXiv 2607.15143)
type: source
tags: [source, arxiv, supply-chain, coding-agent, llm, install-gap]
keywords: [2607.15143, install gap, typosquat, separator confusion, registry redirect, pre-install gate, claude code, cursor]
related:
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/npm-supply-chain-defense.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/llm-code-review-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/coding-agent-install-gap-and-preinstall-gate.md"
  - "@ccc-wiki/sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md"
maturity: draft
read_status: read
created: 2026-07-17
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-18 — no public attack harness; claimed github.com/cardwizard/Sentinel 404; ADOPT pre-install gate pattern (CCC K179)"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-18_coding-agent-install-gap-handoff.md`, `briefs/2026-07-18_k179-coding-agent-preinstall-gate-cybersec-prod.md`

## Relations

- @concepts/coding-agent-supply-chain-install-gap.md — cybersec synthesis
- @ccc-wiki/concepts/coding-agent-install-gap-and-preinstall-gate.md — CCC harness steal (K179)
- @concepts/npm-supply-chain-defense.md — classical npm cooldown complements agent pre-install gate

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents |
| Authors | Aadesh Bagmar, Pushkar Saraf |
| arXiv | 2607.15143 |
| Code | Claimed Sentinel — **404** as of 2026-07-18 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.15143-weaponizing-setup-instructions-coding-agents.pdf` (+ CCC copy) |
| Retrieved | 2026-07-18 (deepen; stub 2026-07-17) |
| Read status | **read** (19 pp; attack classes + harness×model) |

## Narrative

### Install gap

No authenticity check between packages named in README/requirements/Makefile and code that runs at `pip`/`npm`/`cargo` install time. AI coding agents remove the human glance that used to catch odd registries.

### Key results [CONFIRMED from paper]

| Finding | Implication |
|---------|-------------|
| Same model catches attack on one harness, installs on another | Security = **harness×model**, not model alone |
| Blatant typosquats caught; separator-confusion (`azurecore` vs `azure-core`) slips | Name heuristics insufficient |
| Registry/source redirection missed almost everywhere (pip/npm/Cargo) | Source blind spot is primary |
| Security prompts help only the named dimension | Prompt-only ≠ gate |
| Deterministic pre-install check (name/source/version) closes most of the gap | Prefer allowlist/pin/registry host gate |

Five attack classes across twelve scenarios on Claude Code / Cursor / Copilot / Codex, grounded in documented incidents (incl. torchtriton-class shadowing).

### Phase-0 (2026-07-18)

| Gate | Status |
|------|--------|
| Public code | **FAIL** — Sentinel 404 |
| Domain fit | Core coding-agent / TipDrop / CCC |
| Verdict | **REFERENCE** empirics; **ADOPT** pre-install gate (pairs Prebind K151); **NO-GO** install |

## Snippets

> "install-time security rests on the harness-model combination, not the model alone"
[Source: arxiv-2607.15143 abstract]

> "a deterministic pre-install check that verifies names, sources, and versions before any code runs closes most of it"
[Source: arxiv-2607.15143 abstract]
