---
name: pii-redact
description: >-
  Strip PII before any LLM sees Atto vault / citizenship docs. Use before ingest,
  exhibit drafts, or external model calls on civil records. Transkribus remains sole HTR.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# PII redact (Atto)

Canon: `@wiki/entities/tools/pii-redaction.md` · `@wiki/entities/tools/openai-privacy-filter.md` · `osint-invariants.mdc`.

## Procedure

1. Magika sniff blob type before LLM (`.local/adopts/magika` patterns).
2. Strip SSN/CF/passport/vitals using privacy-filter / openredaction / pii-redaction REFERENCE clones.
3. Human-gate: no auto-approve identity; no raw PII in git fixtures.

## NEVER

- No living-person vitals in wiki or briefs committed to git.
- No free-tier model calls on unstripped civil docs.
- Transkribus remains sole product HTR — this skill is not OCR.
