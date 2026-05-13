---
title: "IDAssist — IDA-Pro LLM plugin for binary RE"
type: entity
tags: [tool, ida-pro, reverse-engineering, llm-plugin, binary-re, malware-analysis, mit]
keywords: [idassist, ida pro, reverse engineering, llm-driven re, binary analysis, mit]
related:
  - "@osint-wiki/entities/tools/idassist.md"
  - "@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md"
  - concepts/llm-vulnerability-discovery.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
osint_eval_origin: doc2-url-12 (cross-routed from OSINT eval as cybersec-primary)
---

## Relations

- `@osint-wiki/entities/tools/idassist.md` — OSINT cross-route stub
- `@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md` — origin Gemini eval (URL 12)
- `@concepts/llm-vulnerability-discovery.md` — methodology synthesis

## Raw Concept

- **License**: MIT
- **Tier**: Adopt-candidate (cybersec wiki primary fit)
- **Origin**: Cross-routed from OSINT wiki Gemini eval as cybersec-primary

## Narrative

IDA Pro plugin that wires LLMs into the IDA disassembler for assisted binary reverse engineering. Use cases: malware analysis, vuln research, decompiler-output annotation, function-purpose inference. MIT license clean — adopt-candidate for any RE workflow.

### Phase-0 audit pending

Verify: star count, last-commit recency, IDA Pro version compat, supported LLM backends (OpenAI / local / Anthropic). File full evaluation after Phase-0 lands.
