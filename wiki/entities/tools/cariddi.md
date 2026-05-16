---
title: "cariddi — Go (gocolly) domain crawler + 102-vendor secret regex taxonomy (GPL-3.0)"
type: entity
category: tool
tags: [entity, tool, domain-crawler, secrets-hunting, endpoint-discovery, bug-bounty, k44, steal-from-patterns-only-phase-0-2026-05-14, gpl-3-poison-pill, no-headless-browser, robots-txt-ignored]
keywords: [cariddi, edoardottt, go-colly, 102-secret-regexes, gpl-3-clean-room-only, alternatives-trufflehog-gitleaks-katana-gospider, pure-http-not-js-rendered]
related:
  - concepts/bug-bounty.md
  - concepts/web-pentest-methodology.md
  - entities/tools/openalternative.md
  - "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
maturity: validated
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @concepts/bug-bounty.md — domain crawling for secret / endpoint discovery is a core bug-bounty recon activity
- @concepts/web-pentest-methodology.md — endpoint + parameter discovery feeds web-app testing
- @entities/tools/openalternative.md — OSS-directory for sourcing the MIT/Apache alternatives (katana, trufflehog, gospider) recommended over GPL-3.0 cariddi
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Go-based parallelized domain crawler (`gocolly/v2` wrapper, 2,649 LOC) for secrets / API-key / endpoint hunting. **GPL-3.0 verbatim with NO commercial dual-license**, 3,381 stars verified, 292 forks, 14 contributors, last push 2026-05-12. Notable IP: **102 named vendor secret regexes** in `pkg/scanner/secrets.go` (854 LOC). K44 verdict refined to **STEAL-FROM-PATTERNS-ONLY** with explicit clean-room re-implementation discipline.

## Narrative

### Phase-0 audit verdict (2026-05-14): STEAL-FROM-PATTERNS-ONLY

**GPL-3.0 isolation discipline applies**: never link, never embed, never derive — only clean-room re-implement algorithmic ideas in Python from spec. Even verbatim regex strings are treated as GPL expression (not idea) and must be re-derived from vendor docs.

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Clone succeeds | **PASS** | `edoardottt/cariddi` clean |
| G1 | License = GPL-3.0 verbatim | **PASS — POISON-PILL CONFIRMED** | GPL-3.0-or-later (35,149 bytes); no dual-license / commercial offer |
| G2 | Maturity | **PASS** | 3,381★, 292 forks, 14 contributors, created 2021-04-27, last push 2026-05-12 (2d ago) |
| G3 | Issue hygiene | **PASS** | 8 open issues / 3 open PRs — healthy single-maintainer cadence |
| G4 | Functionality matches K44 claim | **PASS** | "crawl urls and scan for endpoints, secrets, api keys, file extensions, tokens" |
| G5 | **Headless browser support** | **FAIL** | NO chromedp / playwright / rod — **pure HTTP via gocolly v2**. JS-rendered SPAs invisible. K44 implied JS-rendering — incorrect |
| G6 | Robots.txt respect | **FAIL** | `c.IgnoreRobotsTxt = true` hardcoded in `pkg/crawler/colly.go` — aggressive-by-default |
| G7 | Rate-limit + delay primitives | **PASS** | `Delay`, `Concurrency`, `Timeout`, `MaxDepth` first-class flags (colly RandomDelay) |
| G8 | Unique value vs nuclei | **PASS-CONDITIONAL** | nuclei = template-driven CVE/misconfig matching; cariddi = URL-discovery + 102 hardcoded secret regexes. Complementary, not duplicative |

### Clean-room re-implementable patterns (DO NOT COPY CODE)

1. **102-vendor secret-regex taxonomy** (Adafruit, Adobe, Airtable, Algolia, Alibaba, Anthropic, Asana, Atlassian, AWS-Access, AWS-Bedrock, AWS-Secret, AWS-MWS, SNS, Beamer, ...) — **DO NOT COPY REGEX STRINGS; re-derive each from vendor documentation** (regexes themselves are arguably copyrightable expression under GPL)
2. **Crawl-scope heuristic**: protocol-normalize → root-host extraction → same-domain restriction with `Intensive` opt-out — spec only
3. **Endpoint-parameter extraction** from URL query strings + categorization with "possible attacks" annotations — spec only
4. **Sensitive-extension filter list** — re-derive list, do NOT copy
5. **Delay / Concurrency / Timeout / MaxDepth primitive set** — generic crawler-pattern (not copyrightable interface)

### Concrete artifacts to NOT extract

- Any `.go` file under `pkg/scanner/`, `pkg/crawler/`, `internal/`
- Verbatim regex strings from `pkg/scanner/secrets.go` (treat as GPL expression, not idea)
- `Secret` / `Scan` / `Results` / `EndpointMatched` / `Parameter` struct layouts
- `pkg/crawler/colly.go` event-handler scaffold
- User-agent rotation list in `pkg/crawler/useragents.go`

### MIT / Apache-2.0 alternatives (recommended adoption path)

For actual runtime integration, prefer permissively-licensed equivalents:

- **trufflehog** (Apache-2.0, ~17k★) — secret detection, more mature, verified-secrets feature
- **gitleaks** (MIT, ~17k★) — secret-scan focus, more regex coverage
- **katana** (MIT, ProjectDiscovery) — crawler with headless mode (fills the G5 gap cariddi has)
- **gospider** (MIT, ~2.7k★) — closest functional twin to cariddi under permissive license

**Recommended posture**: document cariddi's secret-taxonomy + crawl-scope patterns as cybersec-wiki reference material; **adopt katana + trufflehog** for any actual runtime integration. Entity-page stance: "we documented the pattern; we did not adopt the code."

## Snippets

> "Cariddi is a highly parallelized domain crawler engineered to hunt for exposed secrets, API keys, and sensitive endpoints, featuring native proxy integration with BurpSuite. These capabilities align flawlessly with the offensive security and threat intelligence workflows defined in the Cybersec-wiki."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶289 — Phase-0 audit confirms the secrets-hunting positioning but flags two K44 gaps: NO headless browser support (pure HTTP via gocolly), and `c.IgnoreRobotsTxt=true` is hardcoded. The 102-vendor regex taxonomy is the real extraction value, but must be re-derived from vendor docs under GPL clean-room discipline.]
