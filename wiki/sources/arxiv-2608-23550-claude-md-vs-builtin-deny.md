---
title: "When 'Do Not' Is Not deny — Security Rules in CLAUDE.md vs. Built-In Controls (arXiv 2608.23550)"
type: source
tags: [source, arxiv, agent-security, usable-security, claude-md, deny, k303]
keywords: [2608.23550, CLAUDE.md, deny, permission rule, sandbox, write-only channel, security rules, built-in controls, AGENTS.md]
related:
  - concepts/nl-security-rules-vs-builtin-deny.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
phase_0_verdict: "REFERENCE 2026-08-25 — study/analysis artifacts released per paper (no code repo to clone). Policy steal: prefer built-in deny/hooks over prose-only security rules; do not put secrets in NL rules only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc + mcp-tool-control.mdc (K303)"
---

## Relations

- @concepts/nl-security-rules-vs-builtin-deny.md — primary steal (NL rules ≠ enforcement)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When "Do Not" Is Not deny: Security Rules in CLAUDE.md vs. Built-In Controls |
| Authors | Ting Yan |
| arXiv | 2608.23550 (11 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.23550-when-do-not-is-not-deny-security-rules-in-claude.pdf` |
| Retrieved | 2026-08-25 |
| Read status | read (abstract + method + results + appendices) |
| Public code | analysis artifacts + control reference released per paper; no tool repo to clone (hunt 2026-08-25) |

## Narrative

**CLAUDE.md is a write-only channel**: a developer writes a natural-language security rule ("never write secrets to logs") and gets **no feedback** on whether anything will enforce it. Claude Code's `deny` (permission rules, sandbox, modes) is a built-in control that blocks an action *before* the agent can take it. Both can express the same goal but control the agent differently — and they share the same plain-text form, so a developer cannot tell which kind of rule they wrote.

**Measurement (481 public CLAUDE.md files, retrieved 2026-08-14 via GitHub code search; 647 examined, 481 included):**
- An LLM classifier (Claude Sonnet 5, frozen prompt) matched extracted candidate security rules against a **frozen control reference** of Claude Code's documented built-in controls; two security practitioners independently validated a stratified 180-segment sample, blind to the classifier and to each other.
- **Only ~4–16% of retrieved security rules have a matching built-in control**; under the strictest matching standard the estimate is **4.4% (95% CI 2.6–6.7%)**.
- Extraction recall (whole-file audit, 50 files, 95 in-scope segments): **66.3%** — reported rates apply to the rules the method captured.
- Built-in controls counted: allow/ask/deny rules; tool/command/path/domain patterns; permission modes; filesystem + network sandboxing; managed restrictions. **Hooks are not built-in controls** (PreToolUse needs developer code; prompt/agent hooks decide by model judgment).
- Exploratory secondary split of the 870 security rules: 144 (16.6%) matching built-in control; 446 (51.3%) writable as custom deterministic checks; 181 (20.8%) model-mediated (need open-ended judgment); 99 (11.4%) missing enforcement-time context.

**Prior evidence cited:** shipped command denylists are 69.0–98.6% fragile; removing one declared-scope sentence raises an agent's out-of-scope action rate from 0.0% to 17.1%.

**Why filed (K303, primary wire):** directly governs how *this workspace* writes security policy for agents — CLAUDE.md prose and `.cursor/rules` text are documentation/steering, **not** enforcement; deterministic controls (PreToolUse deny, sandbox, permission rules) are the enforcement layer. No tool clone. [Source: arXiv 2608.23550 PDF]

## Snippets

> CLAUDE.md is a write-only channel. A developer writes a security rule but gets no feedback on whether a control will enforce it. [Source: arxiv-2608.23550-claude-md-vs-builtin-deny PDF, abstract]

> Under the strictest standard the estimate was 4.4% (95% CI: 2.6–6.7%) … our extraction method captured 66.3% of eligible security rules. [Source: arxiv-2608.23550-claude-md-vs-builtin-deny PDF, abstract]

> "Never run npm publish" can be matched by a deny permission rule and checked before the command runs; "never put customer secrets in logs" needs the model to decide what counts as a secret and whether an output is a log. [Source: arxiv-2608.23550-claude-md-vs-builtin-deny PDF, §1]
