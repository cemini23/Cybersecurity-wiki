---
title: "grex — regex generation from test cases for SOC/IR workflows"
type: entity
tags: [tool, regex, soc, ir, log-analysis, rust, apache-2.0, mcp-candidate]
keywords: [grex, pemistahl, regex generation, test cases, rust, python bindings, soc, incident response, malware beaconing, log parsing]
related:
  - concepts/incident-response.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-link-eval-41url-2026-05-18.md"
---

# grex — regex generation from test cases

## Relations

- @concepts/incident-response.md — rapid regex construction for novel log payloads
- @concepts/soc-operations.md — detection-engineering pattern extraction
- @concepts/threat-hunting.md — hypothesis-driven pattern generation

## Raw Concept

Routed from K53 OSINT-wiki tool eval (2026-05-18). CLI tool + Rust library generating optimized regular expressions from user-provided test cases. Adopt-tier, Apache-2.0, ~8,129 stars.

## Narrative

`pemistahl/grex` (Apache-2.0, ~8,129 stars) generates optimized regular expressions from user-provided test cases. Rust library with native Python bindings.

SOC/IR value: instantly build regex patterns for novel malware beaconing signatures or custom log payloads without manual regex crafting. Feed it example log lines and it produces a matching expression — useful when responding to novel threats where no existing Sigma/YARA rule matches.

K53 eval notes grex is a strong candidate for MCP-server wrapping, enabling Claude Code to generate regex on demand during incident response. License verified clean (Apache-2.0, GitHub API check 2026-05-18).
