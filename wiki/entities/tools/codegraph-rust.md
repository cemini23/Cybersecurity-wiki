---
title: "codegraph-rust — tree-sitter + vector hybrid code-graph"
type: entity
tags: [tool, code-graph, tree-sitter, rag-on-code, rust, mit, offensive-security, binary-re]
keywords: [codegraph-rust, tree-sitter, code rag, vector embeddings, mit, rust]
related:
  - "@osint-wiki/entities/tools/codegraph-rust.md"
  - "@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md"
  - concepts/llm-vulnerability-discovery.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
osint_eval_origin: doc1-url-5 (cross-routed; cybersec primary for RAG-on-code / binary RE)
---

## Relations

- `@osint-wiki/entities/tools/codegraph-rust.md` — OSINT cross-route
- `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` — origin eval (URL 5)
- `@concepts/llm-vulnerability-discovery.md` — methodology synthesis

## Raw Concept

- **License**: MIT
- **Tier**: Steal-from / Reference (architecture primitive)

## Narrative

Tree-sitter + vector embedding hybrid for code-graph construction in Rust. Cybersec use cases: source-code RAG for vuln-discovery (feed LLM the relevant subgraph instead of whole-file), decompiled binary cross-reference, dependency-call-graph anomaly detection.

### Methodology relevance

Forms the **structural-extraction stage** that any LLM vuln-discovery pipeline needs: tree-sitter parses syntactic structure, vector embeddings cluster semantic similarity. Pairs with OpenAnt (Detect→Attack) — codegraph-rust is the "what to inspect" primitive, OpenAnt is the "what to do once you're looking."
