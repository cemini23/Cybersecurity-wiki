---
name: codepoisonrag-lab-precheck
description: >-
  K323 advisory checklist before RACG/code-gen knowledge-poisoning lab eval.
  Use when operator says CodePoisonRAG / K323 / RACG poisoning precheck.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# CodePoisonRAG — K323 advisory checklist

Canon: `@wiki/concepts/codepoisonrag-racg-knowledge-poisoning.md` (arXiv **2609.02774**). Helper: `scripts/k323_codepoisonrag_precheck.py`. **Authorized lab only** — no poison bodies in wiki.

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k323_codepoisonrag_precheck.py checklist
python3 scripts/k323_codepoisonrag_precheck.py selftest
```

Report **Top-k retrieval**, **corpus ratio**, **ASR with/without defense**. Pair `@wiki/concepts/committee-certified-rag-provenance.md`.

## NEVER

- No LIVE third-party vector ingest without authorization.
- No CWE injection templates or poison artifact bodies in wiki/briefs.
