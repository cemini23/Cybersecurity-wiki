---
title: SafeClawBench — staged agent security endpoints (CCC K121 route)
type: concept
tags: [concept, safeclawbench, agent-security, cross-wiki]
keywords: [2606.18356, semantic-core, sandbox-harm, openclaw]
related:
  - ccc-wiki/sources/arxiv-safeclawbench-staged-agent-security-2606.18356.md
  - ccc-wiki/concepts/safeclawbench-staged-security-endpoints.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/defenseclaw.md
maturity: draft
created: 2026-06-21
updated: 2026-06-21
---

## Relations

- `@ccc-wiki/sources/arxiv-safeclawbench-staged-agent-security-2606.18356.md` — arXiv source
- `@ccc-wiki/concepts/safeclawbench-staged-security-endpoints.md` — CCC pointer page
- `@concepts/seclaw-agent-security-evaluation.md` — SeClaw trajectory eval peer
- `@entities/tools/defenseclaw.md` — runtime admission/scanner patterns

## Raw Concept

Cross-wiki stub from CCC K121 ingest — SafeClawBench staged security benchmark for tool-using agents.

## Narrative

arXiv **2606.18356** — **600** adversarial tasks; **three reported endpoints**:

1. Semantic Core (attack text compliance)
2. Harm evidence (audit-visible artifacts)
3. Sandbox observed harm (executable effects)

Dataset: `huggingface.co/datasets/sairights/safeclawbench`.

**Cybersec operator actions:**

- Run endpoint ladder separately — never collapse to single ASR
- Pair with defenseclaw scanners + Tier-2 sandbox for sandbox endpoint
- Compare against SeClaw trajectory scoring where overlap exists

**Verdict:** **REFERENCE** eval harness — ingest dataset license/terms before automated runs.

## Snippets

> "291 of 347 observed sandbox harms occur in rows that pass the semantic check."

> — [Source: @ccc-wiki/sources/arxiv-safeclawbench-staged-agent-security-2606.18356.md]
