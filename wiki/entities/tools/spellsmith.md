---
title: SpellSmith — MCP security-aware tool description defense (Reference)
type: entity
tags: [entity, tool, mcp, taint-style, defense, reference]
keywords: [spellsmith, tongji, description enhancement, invocation reflection, 2607.07461]
related:
  - sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md
  - concepts/mcp-taint-style-vulnerabilities.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/agent-data-injection-attacks.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-09
updated: 2026-07-09
phase_0_verdict: "Reference 2026-07-09 — no public repo at ingest; adopt description-augmentation + reflection pattern in prod-mcp proxy; not drop-in product"
---

**Briefs:** `briefs/2026-07-09_spellsmith-mcp-taint-mitigation-handoff.md`

## Relations

- @sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md — paper provenance
- @concepts/mcp-taint-style-vulnerabilities.md — vulnerability landscape synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Name | SpellSmith |
| Authors | Tongji University (Shi et al.) |
| arXiv | 2607.07461 |
| Repo | None public at ingest 2026-07-09 |

## Narrative

### Phase-0 audit verdict (2026-07-09): Reference

| # | Gate | Status |
|---|------|--------|
| G0 | Public artifact | **FAIL** — no canonical repo |
| G1 | Domain fit | **PASS** — MCP taint mitigation via metadata |
| G2 | Overlap | **PARTIAL** — complements DefenseClaw scan + HCP invariants; does not replace code fixes |
| G3 | prod-mcp fit | **CONDITIONAL** — implement as allowlist-proxy description rewriter + pre-invoke reflection hook |

### Three modules

1. **Risk identification** — capability → CWE taint profile
2. **Description enhancement** — embed invocation policy in MCP `description`
3. **Invocation reflection** — second LLM turn before `tools/call`

Paper benchmark: **792** attack prompts; baseline **63.89%** case ASR → SpellSmith **0.13%**.

### Cemini adoption posture

- **GO** — T3 description templates on prod-mcp allowlisted tools; reflection gate on shell/network/file MCPs
- **NO-GO** — treat augmented descriptions as sole defense without server-side validation

## Snippets

> "Embedding text-based mitigations into the MCP tool's Description property."
[Source: arxiv-2607.07461 §1 — paraphrase anchor]
