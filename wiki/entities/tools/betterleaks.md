---
title: "betterleaks — CEL-based secret scanner with BPE-tokenization false-positive reduction"
type: entity
category: tool
tags: [entity, tool, secrets-scanning, secrets-detection, pre-ip-sale-audit, dev-security, k44, adopt-doc-level-pending-phase-0]
keywords: [betterleaks, cel-filtering, bpe-tokenization, gitleaks-alternative, secret-rotation, ip-sale-readiness, cemini-financial-suite, go-binary]
related:
  - "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
maturity: adopt-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Go-based open-source secrets-scanning engine that outperforms legacy tools (gitleaks, trufflehog) on false-positive rate by combining CEL (Common Expression Language) filters with BPE (byte-pair encoding) tokenization to measure string rarity. **MIT license, claimed 934 stars, claimed last commit 2026-05-08, claimed 86.7% Go.** From K44 doc-level eval (OSINT-wiki ingest, May 14 2026).

**What prompted this page**: The K44 evaluation framed this as the **single most operationally critical** finding — flagged for *mandatory* execution as a pre-IP-sale codebase audit against the Cemini financial suite (`/opt/cemini`) and historical PostgreSQL dumps before the impending IP transfer. Verdict tier: Adopt (doc-level). Cybersec-wiki is the primary fit because secret-scanning is fundamentally a SOC / dev-security capability; OSINT-wiki cross-routes it for credential-exposure threat-actor profiling.

## Narrative

### Verdict snapshot (doc-level, K44)

| Dimension | Value | Source |
|-----------|-------|--------|
| Verdict | **Adopt** (doc-level) | K44 eval |
| License | MIT | K44 eval (UNVERIFIED at source level) |
| Stars | 934 | K44 eval (UNVERIFIED) |
| Last commit | 2026-05-08 | K44 eval (UNVERIFIED) |
| Stack | Go (86.7%), Go Template, CEL, re2 | K44 eval |
| Primary fit | Cybersec-wiki | K44 eval |
| Cross-routes | Cemini-financial (pre-IP-sale audit) | K44 eval |
| Adoption priority | **Highest of K44** (pre-IP-sale critical) | this page |

### What makes betterleaks distinct from legacy secret scanners

The K44 eval's structural argument is that betterleaks reduces natural-language false-positives by:

1. **CEL-based filtering**: rules expressed in Common Expression Language (Google's policy language). Provides composable, declarative filtering with less false-positive noise than regex-only engines.
2. **BPE tokenization for string rarity**: instead of regex-matching against known secret formats, scores string rarity probabilistically. High-entropy random strings (likely secrets) score differently from low-entropy English (likely false positives).
3. **re2 regex engine**: Go's RE2 implementation is linear-time, eliminating ReDoS attack surface that has historically plagued regex-heavy secret scanners.

### Why this is the most operationally critical K44 candidate

The Cemini IP-sale posture (per `@osint-wiki/concepts/cemini-license-posture.md`) treats codebase IP hygiene as gating for the upcoming financial suite transfer. **Hardcoded credentials, leftover API keys, or DB passwords in `/opt/cemini` or its historical PostgreSQL dumps would directly impair the IP sale**. betterleaks's claimed false-positive-rate improvement makes it the candidate-of-choice for the exhaustive pre-sale audit.

The K44 eval explicitly directs:

> "Critically, we must Adopt this tool immediately to recursively scan the /opt/cemini algorithmic trading stack and historical PostgreSQL databases, ensuring that absolutely no hardcoded credentials or API keys breach the perimeter prior to our impending financial suite IP sale."

### Phase-0 audit gates (must clear before adoption)

| # | Gate | Method | Block |
|---|------|--------|-------|
| G1 | **Star + maturity verification** | `gh api repos/betterleaks/betterleaks` — confirm 934 stars, 2026-05-08 last commit, contributor count >1 | If single-maintainer or last commit >180d stale, downgrade to Defer |
| G2 | **License verification** | `gh api repos/.../license` + read LICENSE file | If not actually MIT, escalate to Reject |
| G3 | **False-positive rate validation** | Run against a known-clean corpus + a synthetic secrets-injected corpus; compare FP-rate to gitleaks baseline | If FP-rate not materially better than gitleaks, no decisive advantage — Defer in favor of mature gitleaks |
| G4 | **CEL ruleset coverage** | Audit shipped rules: do they cover the Cemini stack's actual secret formats (Polymarket CLOB API keys, Binance signed-request HMAC, PostgreSQL connection strings, AWS/Hetzner cloud creds)? | If gaps, custom-rule writing burden estimated before adopt |
| G5 | **Output format compatibility** | Confirm JSON output schema for ingestion into Cemini's existing security dashboards | Non-portable output ⇒ wrapper required |
| G6 | **CI/CD integration pattern** | Confirm pre-commit hook + GitHub Actions integration; pre-existing patterns in Cemini's CI | If integration burden >1 day, schedule explicitly |

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

- **Doc-level metrics are claims.** Stars (934), commit date (2026-05-08) are from a single eval document with LLM-synthesis markers — apply K43 doc-level vs Phase-0 skepticism. Gate G1 covers verification.
- **The K44 eval does not benchmark betterleaks against gitleaks or trufflehog quantitatively.** The "significantly outperforms" claim is unsupported in the source. Gate G3 must produce real numbers before Adopt is finalized.
- **No mention of historical-data scan modes.** PostgreSQL dump scanning, S3 bucket scanning, Hetzner storage-bucket scanning all need verification of supported input formats.
