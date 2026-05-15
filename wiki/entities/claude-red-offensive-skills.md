---
title: Claude-Red — Offensive Security Skills Library for Claude Code
type: entity
tags: []
keywords: []
related: []
maturity: draft
created: 2026-05-15
updated: 2026-05-15
cross-wiki-source: @osint-wiki/entities/tools/claude-red-offensive-skills.md
---

# Claude-Red — Offensive Security Skills Library for Claude Code

## Relations

- @osint-wiki/entities/tools/claude-red-offensive-skills.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/entities/tools/claude-red-offensive-skills.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

## Raw Concept
Routed from OSINT wiki K46 ingest (v4 multi-wiki link evaluation, 2026-05-15). Tier: Adopt. License: MIT (clean).

URL: https://github.com/SnailSploit/Claude-Red
Stars: 1.3k | Last commit: 2026-03-08 | Open issues: 0
Stack: Python / Shell / Markdown

## Narrative
Claude-Red is a curated offensive security skills library mapping 16 web application methodologies directly into the SKILL.md paradigm used by Claude Code. Each skill loads on conversational trigger — only the relevant methodology is loaded when invoked. Covers: offensive-sqli, offensive-ssrf, offensive-xss, offensive-xxe, offensive-idor, offensive-csrf, offensive-rce, offensive-lfi, offensive-ssti, offensive-cors, offensive-jwt, offensive-file-upload, offensive-command-injection, and more.

V.2 release with structured phases: reconnaissance, vulnerability discovery, exploitation, reporting. Phase 3 splits wireless into 802.11 and WPA3 sub-modules.

Key architectural pattern: sparse git checkout for modular installation — only clone the attack vector skills you need, no context-window bloat from unused skills.

## Cross-reference
@osint-wiki/entities/tools/claude-red-offensive-skills.md — OSINT tool entity page with cross-wiki routing annotations.
