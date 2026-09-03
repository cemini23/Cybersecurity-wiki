---
title: "Committee-certified RAG provenance — ranking as an integrity boundary (K299)"
type: concept
tags: [concept, rag, provenance, integrity, k299, defensive]
keywords: [RAG provenance, corpus tamper, ranking replay, hash commitment, committee scoring, ZK, MPC, schema-valid not authenticated]
related:
  - sources/arxiv-2608-20097-trustrag-committee-rag.md
  - concepts/mcp-security-posture.md
  - concepts/agent-execution-provenance.md
  - concepts/agent-data-injection-attacks.md
  - concepts/planner-state-integrity-embodied-agents.md
  - concepts/codepoisonrag-racg-knowledge-poisoning.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K299 RAG integrity boundary)"
---

**Briefs:** `briefs/2026-08-21_k298-k300-ingest.md`

## Relations

- @sources/arxiv-2608-20097-trustrag-committee-rag.md
- @concepts/mcp-security-posture.md — tool-return / retrieved data as untrusted input
- @concepts/agent-execution-provenance.md — replayable ranking = provenance for answers
- @concepts/agent-data-injection-attacks.md — the adversary: tampered corpus / poisoned chunks
- @concepts/planner-state-integrity-embodied-agents.md — schema-valid ≠ true (ESTI, same lesson)
- @concepts/ai-for-cybersecurity.md — RAG is core infra for security knowledge layers

## Raw Concept

Question this page answers: **when can we trust what a RAG system retrieved, and what does "trust" mean operationally for an agent's evidence?**

## Narrative

**RAG ranking/provenance is an integrity boundary.** A centralized RAG stack presents an opaque surface: who curated the corpus, who re-ranked the results, was a chunk tampered with between ingestion and retrieval? Schema-valid retrieved chunks (well-formed, plausible-looking) are **not authenticated** — this is the same lesson as ESTI planner-state integrity (`planner-state-integrity-embodied-agents.md`): conformance to a field's shape is not evidence of semantic truth.

**TrustRAG's answer (K299, 2608.20097):** make the *ranking* replayable and the *corpus* tamper-evident without centralizing authority:
- **Hash commitments** on document content + embeddings — silent alteration or dropping becomes detectable.
- **Committee ZK certification + MPC (MP-SPDZ) aggregation** — credibility scores combine distributed expert input without leaking individual preferences or enabling strategic manipulation; any client can verify the aggregate.
- **Deterministic replay** — the protocol binds per-chain outputs via hash commitments and exposes enough metadata that a client can re-run and check the final ranking.

### Operator steal (defensive, no blockchain required)

1. **Treat retrieved chunks as untrusted input** (pairs ADI / MCP tool-return policy) — schema-valid ≠ authenticated.
2. **Pin provenance metadata**: for any RAG you build or audit (runbooks, threat-intel layer, SOC knowledge), record corpus version + retrieval params + ranking inputs so an answer can be re-derived.
3. **Corpus integrity**: hash/commit the ingestion set; detect silent edits or drops; log who could re-rank and when.
4. **Verifiable aggregation**: if you use multiple "judge"/scoring inputs (credibility, freshness, source weight), keep the aggregation auditable and replayable rather than an opaque platform output.
5. Full ZK/MPC/blockchain machinery is **overkill for a laptop wiki** — the *pattern* (replayability + tamper-evidence) is the steal; the crypto stack is context for high-stakes enterprise deployments.

**Name collision:** this is the Fudan committee TrustRAG (2608.20097), **not** Zhou/HuichiZhou TrustRAG (2501.00879) and not gomate-community/TrustRAG. Do not adopt those repos as this paper's artifact.

**Phase-0:** REFERENCE / no clone. [TENTATIVE] single paper; protocol unverified independently.

## Snippets

> …no document or score can be silently altered or dropped, and every ranking can be independently replayed and checked. [Source: arXiv 2608.20097 abstract]

> Schema-valid retrieved chunks are not authenticated without committee/hash replay. [Source: K299 wire 2026-08-21]
