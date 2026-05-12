# GitHub Repo Eval Prompt — Phase-0 Audit

A reusable prompt template for evaluating a list of GitHub repositories before adopting any of them into this workspace. Adapted from the Phase-0 audit pattern in `CLAUDE.md`.

> **Template note**: Replace `{{TOOL_CATEGORIES}}` and `{{FAILURE_MODES}}` (sections §3 and §4 below) with categories and failure modes specific to this wiki's domain. See the comment blocks for examples. The rest of the prompt is domain-agnostic.

## How to use

1. Paste the list of GitHub URLs at the bottom of the prompt (one per line) under `## Repos to audit`
2. Send the whole thing to Claude (in this workspace, claude.ai, or Claude Desktop)
3. Claude runs the audit per repo and returns structured output
4. For GO / CONDITIONAL-GO repos: save the draft entity page section to `wiki/entities/tools/<slug>.md` (or whichever entity subfolder fits)
5. NO-GO repos still get logged — paste the verdict block into `wiki/log.md` so future-you doesn't re-evaluate the same dud six months later

## The prompt (copy from here down)

---

You are auditing a list of GitHub repositories for adoption into a {{DOMAIN_NAME}} workspace. The workspace is a knowledge hub for **{{OPERATOR_PROFILE}}**. Assume the operator {{OPERATOR_CONSTRAINTS}} — anything proposed must respect those constraints, or it gets routed to "research-only, do not adopt."

For EACH repo in the list, run a Phase-0 audit (~5 min per repo) and produce a structured report.

### Tools to use (preferred order)

1. `mcp__exa__get_code_context_exa` — primary tool. Pulls README, file structure, recent commits, key files.
2. `mcp__exa__crawling_exa` — fallback for the LICENSE file or specific docs pages if `get_code_context_exa` is incomplete.
3. `mcp__brave-search__brave_web_search` — for community signal: search "<repo name> review", "<repo name> issues", "<repo name> Reddit". Borderline verdicts only — skip for clear GO or NO-GO.
4. `mcp__playwright__browser_navigate` — only if the repo's docs require interactive walkthrough or there's a hosted demo; rare at Phase 0.

### Audit checklist (run for every repo)

**1. License**
- What is the SPDX identifier? (MIT / Apache-2.0 / GPL-2.0 / GPL-3.0 / AGPL-3.0 / BSD / proprietary / unknown)
- **Red flag — AGPL on a hosted service**: triggers source-disclosure obligations if used server-side. For local laptop use, AGPL is usually fine.
- **Red flag — proprietary or unknown**: assume "all rights reserved" by default; cannot legally redistribute or fork.
- **Red flag — license drift / poison-pill licenses**: BUSL, Commons-Clause, PolyForm-NC. Note the specific clause.

**2. Maturity**
- Star count
- Last commit date (red flag: >12 months stale, *unless* the repo is feature-complete and stable — note this distinction)
- Open vs closed issue ratio (red flag: many open issues with no maintainer responses)
- Maintainer activity (recent comments in issues / PRs)

**3. Domain fit** — does this repo fit one of these slots:

{{TOOL_CATEGORIES}}

<!--
Replace {{TOOL_CATEGORIES}} with a bulleted list of tool categories relevant to
this domain. Each bullet is one slot a candidate repo could fill. End the list
with this universal fallback:

- **Doesn't fit** → NO-GO (note category and skip remaining audit steps)

Example shape from a sister wiki:

- **Local-pack rank tracker** — grid-based or zip-based local rank tracking
- **Schema markup generator** — JSON-LD generation for LocalBusiness, Service, Review
- **Review-management tool** — aggregation across platforms, response drafting
- **Adjacent / multi-purpose** — useful but not directly in scope
- **Doesn't fit** → NO-GO
-->

**4. Failure mode for class** (run the matching one based on §3)

{{FAILURE_MODES}}

<!--
Replace {{FAILURE_MODES}} with one bullet per §3 category, listing the most-
likely failure mode for that tool class. The point of this section is to know
in advance what would make each category of tool dangerous or worthless.

Example shape from a sister wiki:

- **Local-pack rank tracker**: scrape-vs-API method (scraping is fragile)? grid coverage density? data freshness vs claim?
- **Schema generators**: spec drift — deprecated properties? validates in Google Rich Results Test?
- **Review-management tools**: enables review gating (policy violation)? generates fake reviews? cross-platform or single?
-->

**5. Wiki coverage check** — if the workspace already has any `wiki/entities/tools/*.md` pages, scan them for parallel implementations or prior NO-GO rejections of the same tool. (Skip if `wiki/entities/tools/` is empty — early in the wiki's life this section is unused.)

### Output format (per repo)

```
=== <repo-owner>/<repo-name> ===
URL: https://github.com/<owner>/<repo>
License: <SPDX or "unknown">
Last commit: <YYYY-MM-DD>
Stars: <N> | Open issues: <N>
Domain fit: <category from §3, or "doesn't fit">

Failure-mode-for-class check:
- <bullet 1>
- <bullet 2>
- <bullet 3 if relevant>

Operator-fit (runnability):
- <one bullet — what does the operator need to run this? install Python / Node / Docker? GUI or CLI? hosted demo? Verdict: "operator-runnable" | "needs-engineer-help" | "research-only">

Wiki coverage: <"no parallel" | "duplicates @path" | "prior NO-GO @path">

Verdict: GO | CONDITIONAL-GO | NO-GO

Reasoning (1-3 sentences): <...>

--- DRAFT ENTITY PAGE (only if GO or CONDITIONAL-GO) ---
File: wiki/entities/tools/<slug>.md

---
title: <Tool Name>
type: entity
tags: [tooling, <category-tag>]
keywords: [<3-5 fine-grained search terms>]
related: [<any wiki page that should backlink — leave empty if none>]
maturity: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## Raw Concept
Sourced from Phase-0 GitHub audit on <YYYY-MM-DD>. Repo: https://github.com/<owner>/<repo> @ <commit-sha>.

## Narrative
<2-4 sentence summary: what it does + key strengths + key risks + verdict reasoning + operator-runnability note>

## Snippets
[Source: github.com/<owner>/<repo> — README]
> <key README quote, if useful>
```

### Important rules

- **Be skeptical of README claims**: READMEs are marketing. Verify against issue threads + commit activity before accepting any feature claim as real.
- **Flag single-source claims**: if a feature is only in the README and not corroborated externally, mark `[NEEDS VERIFICATION YYYY-MM-DD]` in the Narrative.
- **Do not adopt parallel implementations**: if Repo B does what Repo A already does (and A is in the wiki), only one goes GO. Justify which.
- **License-unknown defaults to NO-GO**: unless the maintainer can be contacted to clarify within reasonable time.
- **Hard NO-GO triggers** (skip rest of audit, mark NO-GO with single-line reason): {{HARD_NOGO_TRIGGERS}}

<!--
Replace {{HARD_NOGO_TRIGGERS}} with domain-specific dealbreakers — things that
violate platform policies, expose the operator to bans, or are otherwise
clearly out-of-scope regardless of other merits. Examples from sister wikis:

- Repo enables review gating (Google policy violation)
- Repo automates a platform via dashboard scripting (suspension risk)
- Repo generates fake content (reviews, citations, engagement)
- Repo's stated purpose is a blackhat tactic that risks platform manual action
-->

- **Cost discipline**: max 2 Exa calls per repo (one `get_code_context_exa`, optional one `crawling_exa` for LICENSE). For lists >10 repos, skip the Brave community-signal step on rounds 2+ unless the verdict is borderline.
- **Order of report**: list all GO repos first, then CONDITIONAL-GO, then NO-GO. Sort within each tier by domain fit + operator-runnability + maturity.

### When all repos are processed, end with a summary block

```
=== Summary ===
Total: <N>
GO: <count> — list of names
CONDITIONAL-GO: <count> — list (with the conditions)
NO-GO: <count> — list (with one-line reason each)
Hard NO-GOs (policy violations): <count> — list with the trigger
Most interesting finding: <one-sentence note>
Operator-runnable subset: <count> of GO/CONDITIONAL-GO
```

---

## Repos to audit

(Paste GitHub URLs below, one per line — example format:)

```
https://github.com/example/foo
https://github.com/example/bar
```
