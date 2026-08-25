---
title: "TrustRAG — Blockchain-Enhanced RAG via Committee-Based Credibility Scoring (arXiv 2608.20097)"
type: source
tags: [source, arxiv, rag, provenance, blockchain, k299]
keywords: [2608.20097, TrustRAG, committee scoring, zero-knowledge, MPC, MP-SPDZ, hash commitment, RAG provenance, corpus integrity]
related:
  - concepts/committee-certified-rag-provenance.md
  - concepts/agent-data-injection-attacks.md
  - concepts/agent-execution-provenance.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
phase_0_verdict: "REFERENCE 2026-08-21 — no public SPDX repo at hunt for THIS paper (Fudan committee ZK/MPC TrustRAG). Re-hunt 2026-08-25: still none. Name collision: HuichiZhou/TrustRAG (2501.00879) + gomate-community/TrustRAG are NOT this artifact; no clone. No MP-SPDZ / blockchain stack clone as this paper's code."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K299 RAG integrity boundary)"
---

**Briefs:** `briefs/2026-08-21_k298-k300-ingest.md`

## Relations

- @concepts/committee-certified-rag-provenance.md — primary synthesis (RAG provenance / corpus integrity)
- @concepts/agent-data-injection-attacks.md — retrieval/chunk injection is the adversary this guards
- @concepts/agent-execution-provenance.md — replayable ranking as evidence provenance

## Raw Concept

| Field | Value |
|-------|-------|
| Title | TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring |
| Authors | Baixiang Liu, Haotian Che, Yuan Li (Fudan University) |
| arXiv | 2608.20097 (cs.CR / cs.AI, 13 pp) |
| Code | none public with SPDX at retrieval (2026-08-21 hunt) — see Narrative for name collisions |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.20097-trustrag-blockchain-enhanced-rag-via-committee-b.pdf` |
| Retrieved | 2026-08-21 |
| Read status | read (abstract + intro + method sections) |

## Narrative

TrustRAG attacks the **centralized-RAG opacity problem**: retrieval pipelines, indexing, and ranking heuristics are controlled by a small number of providers/platform teams, so a client cannot verify where a document came from, whether it was tampered with, or whether the ranking is honest. The design:

1. **Immutable registration** — documents are registered with content + embedding hashes as provenance anchors (no silent alteration or dropping).
2. **Committee ZK certification** — a committee of domain experts certifies documents via a zero-knowledge protocol; membership, uniqueness, and score correctness are enforced without disclosing individual votes (no leaking evaluator preferences / no strategic manipulation).
3. **MPC aggregation** — hidden score components are split into Shamir secret shares and combined by committee nodes via an **MP-SPDZ-based** secure aggregation interface → chain-local tallies and credibility values, without revealing individual votes or blinding factors.
4. **Hash commitments + replayable ranking** — rather than a recursive global proof, per-chain outputs are bound through hash commitments and the metadata is sufficient to **deterministically replay** the final ranking — every ranking can be independently replayed and checked.

Target domains: healthcare, finance, logistics/traffic, legal case law — where a wrong or manipulated document directly leads to bad decisions.

**Name collision (important):** multiple unrelated "TrustRAG" artifacts exist — `HuichiZhou/TrustRAG` (Zhou et al., 2501.00879, AAAI-2026-workshop) and `gomate-community/TrustRAG` are **not** this paper's artifact. **Do not clone them** as this source. The Fudan committee paper has no public SPDX at hunt → **REFERENCE, no clone**.

**Phase-0:** REFERENCE. Dual-ID: **Cybersec K299** (this paper) ≠ any other wiki's TrustRAG reference.

## Snippets

> Before a document is used, it is certified by a committee of domain experts through a zero-knowledge protocol, and the committee's hidden scores are combined via secure multi-party computation into a trust score that any client can verify. [Source: arXiv 2608.20097 abstract]

> …no document or score can be silently altered or dropped, and every ranking can be independently replayed and checked. [Source: arXiv 2608.20097 abstract]
