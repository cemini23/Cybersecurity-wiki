---
title: "OpenAnt — Detect→Attack two-stage LLM vuln-discovery"
type: entity
tags: [tool, llm-vuln-discovery, two-stage-pipeline, apache-2, offensive-security, knostic]
keywords: [openant, knostic, llm vulnerability discovery, detect attack two stage, apache-2.0]
related:
  - "@osint-wiki/entities/tools/openant.md"
  - "@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md"
  - concepts/llm-vulnerability-discovery.md
maturity: draft
created: 2026-05-12
updated: 2026-07-31
osint_eval_origin: doc2-url-10 (cross-routed from OSINT eval; cybersec primary)
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- `@osint-wiki/entities/tools/openant.md` — OSINT cross-route stub
- `@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md` — origin Gemini eval (URL 10)
- `@concepts/llm-vulnerability-discovery.md` — distilled methodology

## Raw Concept

- **Repo**: `github.com/knostic/OpenAnt`
- **License**: Apache-2.0
- **Tier**: Steal-from (primary methodology source)

## Narrative

Two-stage LLM vulnerability-discovery pipeline:
1. **Detect stage** — LLM scans target (code or running service) and identifies candidate vulnerable surfaces
2. **Attack stage** — LLM crafts and validates exploit attempts against detect-stage candidates

Apache-2.0 clean. Forms the methodological backbone for `@concepts/llm-vulnerability-discovery.md` together with IDAssist (binary RE angle).

### Phase-0 audit pending

Verify detect-stage prompt structure, attack-stage validation rigor, false-positive rate claims, supported target classes.
