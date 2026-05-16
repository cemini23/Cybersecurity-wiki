---
title: "betterleaks — CEL-based secret scanner with BPE-tokenization false-positive reduction"
type: entity
category: tool
tags: [entity, tool, secrets-scanning, secrets-detection, pre-ip-sale-audit, dev-security, k44, conditional-go-phase-0-2026-05-14]
keywords: [betterleaks, cel-filtering, bpe-tokenization, gitleaks-alternative, secret-rotation, ip-sale-readiness, cemini-financial-suite, go-binary, postgres-dump-gap]
related:
  - "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
  - concepts/system-hardening.md
maturity: validated
created: 2026-05-14
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @concepts/system-hardening.md — secret-scanning as a dev/system-hardening control
## Raw Concept

A Go-based open-source secrets-scanning engine that outperforms legacy tools (gitleaks, trufflehog) on false-positive rate by combining CEL (Common Expression Language) filters with BPE (byte-pair encoding) tokenization to measure string rarity. **MIT license, claimed 934 stars, claimed last commit 2026-05-08, claimed 86.7% Go.** From K44 doc-level eval (OSINT-wiki ingest, May 14 2026).

**What prompted this page**: The K44 evaluation framed this as the **single most operationally critical** finding — flagged for *mandatory* execution as a pre-IP-sale codebase audit against the Cemini financial suite (`/opt/cemini`) and historical PostgreSQL dumps before the impending IP transfer. Verdict tier: Adopt (doc-level). Cybersec-wiki is the primary fit because secret-scanning is fundamentally a SOC / dev-security capability; OSINT-wiki cross-routes it for credential-exposure threat-actor profiling.

## Narrative

### Verdict snapshot (post-Phase-0, 2026-05-14)

| Dimension | Value | Status |
|-----------|-------|--------|
| Verdict | **Adopt** (doc-level) → **CONDITIONAL-GO** (Phase-0) | Phase-0 audit 2026-05-14 |
| License | MIT (Zachary Rice, 2026) | **VERIFIED** |
| Stars | 934 | **VERIFIED** |
| Last commit | 2026-05-12 (2d fresher than doc claim 2026-05-08) | **VERIFIED** |
| Contributors | 13 (multi-maintainer) | **VERIFIED** |
| Stack | Go (86.8%), Go Template (11.1%), CEL, re2 | **VERIFIED** |
| Star/fork ratio | 15.8 (healthy, no inflation) | **VERIFIED** |
| Primary fit | Cybersec-wiki | K44 eval |
| Cross-routes | Cemini-financial (pre-IP-sale audit) | K44 eval |
| Adoption priority | **Highest of K44** (pre-IP-sale critical) | this page |
| Load-bearing gap | No PostgreSQL dump-aware scanning (G7 FAIL) | Phase-0 audit |

### What makes betterleaks distinct from legacy secret scanners

The K44 eval's structural argument is that betterleaks reduces natural-language false-positives by:

1. **CEL-based filtering**: rules expressed in Common Expression Language (Google's policy language). Provides composable, declarative filtering with less false-positive noise than regex-only engines.
2. **BPE tokenization for string rarity**: instead of regex-matching against known secret formats, scores string rarity probabilistically. High-entropy random strings (likely secrets) score differently from low-entropy English (likely false positives).
3. **re2 regex engine**: Go's RE2 implementation is linear-time, eliminating ReDoS attack surface that has historically plagued regex-heavy secret scanners.

### Why this is the most operationally critical K44 candidate

The Cemini IP-sale posture (per `@osint-wiki/concepts/cemini-license-posture.md`) treats codebase IP hygiene as gating for the upcoming financial suite transfer. **Hardcoded credentials, leftover API keys, or DB passwords in `/opt/cemini` or its historical PostgreSQL dumps would directly impair the IP sale**. betterleaks's claimed false-positive-rate improvement makes it the candidate-of-choice for the exhaustive pre-sale audit.

The K44 eval explicitly directs:

> "Critically, we must Adopt this tool immediately to recursively scan the /opt/cemini algorithmic trading stack and historical PostgreSQL databases, ensuring that absolutely no hardcoded credentials or API keys breach the perimeter prior to our impending financial suite IP sale."

### Phase-0 audit verdict (2026-05-14)

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | Canonical `betterleaks/betterleaks` resolved; no naming conflicts |
| G1 | Star + maturity | **PASS** | 934★ verified, 13 contributors, last commit 2026-05-12, 100d old, 15.8 star/fork ratio (healthy) |
| G2 | License | **PASS** | MIT verified verbatim (Zachary Rice, 2026) |
| G3 | Codebase orientation | **PASS** | Well-organized: `cmd/` + `detect/` + `celenv/` + `sources/` + `config/` + `report/`. README accurately describes CEL + BPE-tokenization (no eval-doc hallucination). Originally forked from gitleaks lineage; backing from Aikido Security |
| G4 | CEL ruleset coverage | **CONDITIONAL** | 276 built-in rules. Cemini-relevant coverage: ✓ Polymarket (3 rules: api-key/secret/passphrase + private-key), ✓ AWS (AKIA), ✓ JWT (2 rules), ✓ SSH private keys, ✓ generic high-entropy via `entropy()` CEL fn. **Missing**: PostgreSQL connection strings, Binance HMAC, Hetzner tokens — custom rules required |
| G5 | Output format | **PASS** | JSON, CSV, SARIF, JUnit, HTML. Stable JSON schema with findings array + redaction support |
| G6 | CI/CD integration | **PASS** | `.pre-commit-hooks.yaml` (3 variants: golang, docker_image, system) + Dockerfile (Alpine multi-stage) + GHA workflows. No published Marketplace action (minor) |
| G7 | **PostgreSQL dump scanning** | **FAIL** | **No specialized `.sql`/`.dump` handler.** `betterleaks dir dump.sql` treats as raw text → (a) FP-prone on SQL comments/string literals, (b) potential perf issues on multi-GB dumps, (c) no SQL-credential context awareness (CREATE USER, `IDENTIFIED BY`, stored procs). **Critical gap for Cemini IP-sale use case** |

**Verdict: CONDITIONAL-GO** — Production-grade tool, but PostgreSQL dump scanning gap blocks straightforward Phase A execution.

### Updated adoption plan (post-Phase-0)

**CONDITIONAL-GO conditions** (must complete before Phase A live scan):

1. **Write custom Cemini CEL ruleset** (`cemini-postgres.toml`) extending base config:
   - `CREATE USER|ROLE ... WITH PASSWORD ...`
   - `host=...: password=...` (libpq/JDBC connection strings, including in SQL comments)
   - Binance HMAC patterns
   - Hetzner cloud API token patterns
   - Exclude-list patterns: `PASSWORD_HASH`, `PLACEHOLDER`, schema version strings, sample/example dummy secrets

2. **Test on sanitized sample** — Run against first 100 MB of an anonymized Cemini PostgreSQL dump to:
   - Verify FP-rate is acceptable on SQL comments and stored procs
   - Confirm perf on multi-GB inputs (split if needed)
   - Empirically validate the K44-claimed "superior FP-rate vs gitleaks" — the source repo ships NO quantitative benchmark; this must be measured

3. **Two-stage scan for `.sql` dumps**:
   - Stage 1: betterleaks for known formats (API keys, JWT, SSH, high-entropy)
   - Stage 2: Custom SQL parser for database-specific contexts (CREATE USER, GRANT, stored procs) — separate tool needed if FP-rate is too high

**Phase A (pre-IP-sale exhaustive scan) — gated on CONDITIONAL-GO conditions clearing**:

- Week 1: Pre-commit hook deployment on `/opt/cemini` repo (low-risk, immediate value)
- Week 2: Live filesystem + git-history scan via `betterleaks git --log-opts=...`
- Week 3: PostgreSQL dump scans (with custom rules from item 1 above)
- Week 4: Final IP-transfer secrets report + remediation guidance

**Phase B (CI/CD)**: deploy `.pre-commit-hooks.yaml` (system variant for portability) + GHA workflow on every PR. Block on high-confidence findings.

**Phase C (sister-wikis)**: extend to image-gen-wiki, seo-wiki etc. (lower priority).

### Critical findings from Phase-0

1. **K44 doc accuracy is high** — claimed stars/license/stack all verified within ±1%. Worth noting because the K43-failure pattern (doc-level vs Phase-0 mismatch) didn't recur here. The eval-source LLM didn't hallucinate the project.
2. **The "superior FP-rate" claim is unbenchmarked** — the K44 eval asserts this, but the repo itself ships NO quantitative comparison vs gitleaks/trufflehog. The CEL-based filtering and BPE-tokenization features are real, but empirical validation must come from our own scan.
3. **PostgreSQL dump scanning is the load-bearing gap** — for non-database codebases this tool is straight-Adopt. For the Cemini use-case (which is explicitly historical PostgreSQL dumps), it's CONDITIONAL.
4. **No naming conflicts / sock-puppet risk** — repo is legitimately maintained by gitleaks lineage maintainers (Zachary Rice) with Aikido Security backing. Multi-maintainer reduces bus-factor risk.

### Adoption plan (post-Phase-0 GO)

If Phase-0 clears:

1. **Phase A — pre-IP-sale exhaustive scan** (highest priority): full recursive scan of `/opt/cemini` source tree + historical Git history (`betterleaks git --depth=full`) + all PostgreSQL dump files in cold storage. Triage findings; rotate any discovered credentials with audit-trail.
2. **Phase B — continuous integration**: pre-commit hook + GitHub Actions check on every PR. Block merges with new high-confidence findings.
3. **Phase C — sister-wiki scanning**: extend to image-gen-wiki, seo-wiki, etc. (lower priority).

### Why "Adopt" not "Steal-from"

The K44 eval directly Adopts despite Cemini's general posture of preferring Steal-from for security tools (to avoid binary dependencies in the shipped product). The justification: betterleaks is an **operational scan tool**, not an embedded library — it runs against the codebase as a separate process, with no static or dynamic linkage into the shipped Cemini suite. MIT license + non-embedded usage = clean IP-sale story.

## Snippets

> "Betterleaks is a formidable, highly portable secrets scanning engine that significantly outperforms legacy tools by employing CEL-based filtering and BPE tokenization to measure string rarity, drastically cutting natural language false positives."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶205]

## Dead Ends

- **Doc-level metrics were claims** — Phase-0 G1 confirmed them. Stars (934 ✓), commit date (2026-05-12 vs claimed 2026-05-08, 2d fresh ✓), MIT license ✓, Go stack ✓. K44 eval was accurate for this tool, unlike the K43 failures (bukosabino/ta + tradingview-mcp).
- **The K44 eval's "significantly outperforms gitleaks/trufflehog" claim remains unbenchmarked** — the source repo ships no quantitative comparison data. Empirical FP-rate validation must come from our own scan against a known-clean + known-secrets Cemini corpus before declaring superiority.
- **PostgreSQL dump scanning is the load-bearing failure mode (G7)** — no specialized `.sql`/`.dump` handler. Raw-text scan is FP-prone on SQL comments and stored procs. The Cemini use-case specifically requires historical PostgreSQL dump audit; custom CEL rules + a two-stage scan workflow are required before Phase A can execute.
- **No published GitHub Marketplace action** — Docker integration is strong, but Marketplace action would simplify GHA wiring. Minor.
- **Treating CEL filtering as a silver bullet** — CEL improves rule expressiveness vs regex-only allowlists, but rule quality still dominates outcomes. Custom rules for Cemini-specific patterns (Polymarket beyond the 3 shipped, Binance, Hetzner, postgres) are non-optional, not a "nice-to-have."
