---
title: "claude-code-ultimate-guide — 28-CVE catalog + 655 malicious-skill-pattern DB"
type: entity
tags: [tool, claude-code-reference, cve-catalog, malicious-skill-detection, cc-by-sa, defensive-security]
keywords: [claude-code-ultimate-guide, FlorianBruniaux, 28 cve catalog, 655 malicious skill patterns, cc-by-sa-4.0]
related:
  - "@osint-wiki/entities/tools/claude-code-ultimate-guide.md"
  - "@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md"
  - concepts/llm-pentest-automation.md
  - entities/tools/nvidia-skillspector.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - entities/tools/ecc.md
maturity: draft
created: 2026-05-12
updated: 2026-07-31
osint_eval_origin: doc1-url-17 (cross-routed; substantive cybersec content)
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- `@osint-wiki/entities/tools/claude-code-ultimate-guide.md` — OSINT cross-route (workflow angle)
- `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` — origin eval (URL 17)
- `@ccc-wiki/entities/tools/claude-code-ultimate-guide.md` — CCC-side meta-wiki entry; the 28-CVE catalog + 655 malicious-skill patterns inform CCC's Phase-0 skill audit workflow
- @concepts/llm-pentest-automation.md — malicious-skill detection is an LLM-agent security surface of this discipline
- @entities/tools/nvidia-skillspector.md — dynamic skill scanner vs this page's static 655-pattern DB
## Raw Concept

- **Repo**: `github.com/FlorianBruniaux/claude-code-ultimate-guide`
- **License**: CC-BY-SA-4.0 (Share-Alike — copy ideas not files)
- **Tier**: Steal-from / Study

## Narrative

24,000-line Claude Code reference guide. Substantial cybersec content embedded:

- **28-CVE catalog** specific to AI coding assistants
- **655 malicious-skill-pattern detection rules** — pre-built signatures for catching skill-injection / supply-chain compromise in skill libraries

### Cybersec utility

These two databases together form a defensive baseline for any organization deploying agentic coding tools at scale. Use them to vet third-party Claude Code skills before installation; treat as a "skill-malware" signature library.

### Licence caveat

CC-BY-SA-4.0 Share-Alike on docs means: extracting CVE/pattern identifiers + categorical understanding is fair use; copying full database files verbatim into our own wiki triggers SA copyleft.
