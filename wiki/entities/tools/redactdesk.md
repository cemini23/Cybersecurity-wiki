---
title: "RedactDesk — PDF content-stream redaction (MIT)"
type: entity
tags: [tool, pdf-redaction, content-stream-mutation, mit, defensive-security, secure-doc-handling]
keywords: [redactdesk, pdf redaction, content stream mutation, mit, secure docs]
related:
  - "@osint-wiki/entities/tools/redactdesk.md"
  - "@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md"
  - entities/tools/karma.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
osint_eval_origin: doc2-url-18 (cross-routed; cybersec primary for secure-doc-handling)
---

## Relations

- `@osint-wiki/entities/tools/redactdesk.md` — OSINT cross-route
- `@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md` — origin eval (URL 18)
- `@entities/tools/karma.md` — license-broken alternative

## Raw Concept

- **License**: MIT
- **Tier**: Adopt-candidate / Steal-from (technique)

## Narrative

PDF redaction tool that performs **proper content-stream mutation** — actually removes redacted text from the PDF data stream rather than the common (broken) "draw a black rectangle over it" approach (which leaves the underlying text recoverable via text-extraction or selecting + copying).

### Why this matters for cybersec

Document forensics + secure-doc-handling pipelines need redactions that survive offline text-extraction tools. Most "redact" features in editors fail this test. RedactDesk is one of the few open-source tools that does it correctly.

### Phase-0 audit pending

Verify against actual extraction attacks (pdftotext, pdfminer, OCR roundtrip).
