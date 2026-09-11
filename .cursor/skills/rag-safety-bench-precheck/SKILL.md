---
name: rag-safety-bench-precheck
description: >-
  K328 RAG-Safety-Bench eval checklist before retrieval-conditioned safety
  claims. Pairs K323 CodePoisonRAG upstream poisoning boundary. Operator-invoked.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
---

# RAG-Safety-Bench precheck (K328)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k328_rag_safety_bench_precheck.py checklist
```

Canon: `wiki/concepts/rag-safety-bench-evaluation.md` (arXiv **2609.11758**).

Separate base-model refusal from retrieval-conditioned outcomes. Do not treat one scalar as a fleet safety certificate.

Pair with: K323 CodePoisonRAG, K299 committee RAG provenance.
