---
title: "Splunk Commands.pdf"
type: source
tags: [splunk, siem, soc, reference]
keywords: [splunk commands, spl, search processing language, detection queries, stats, eval, rex, timechart, transaction]
related:
  - entities/tools/splunk.md
  - concepts/siem.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
maturity: validated
read_status: read
created: 2026-05-16
updated: 2026-05-17
---

## Raw Concept

- **Title**: Splunk Commands.pdf
- **Author**: anonymous compiler (community SPL cheatsheet; shared via Google Drive — BlueTeam Kit)
- **Type**: PDF
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs)
- **Retrieved**: 2026-05-16
- **Read-status**: read (full deep-read 2026-05-17)
- **Pages**: alphabetical reference covering ~100+ SPL commands; each entry is `command → description → example input → example output`

## Narrative

An alphabetical SPL command reference. Each entry is laid out as `command name → one-sentence description → example input query → example tabular output`. Companion to @sources/100-splunk-queries-soc-analyst.md — that one teaches the *detection idioms*, this one is the language reference for the commands those idioms compose.

The high-value subset (the commands that actually recur across the 110-query detection catalog) is now synthesized as a table on @entities/tools/splunk.md (SPL command reference section). That subset covers:

- **Filtering**: `search`, `where`, `dedup`
- **Aggregation**: `stats`, `eventstats`, `streamstats`
- **Field manipulation**: `eval`, `rex`, `fields`, `rename`
- **Display**: `table`, `sort`, `top`, `rare`
- **Time-series**: `timechart`, `chart`
- **Enrichment**: `lookup`, `inputlookup`, `outputlookup`, `iplocation`
- **Sessionization**: `transaction`
- **Multi-source**: `append`, `appendcols`, `multisearch`, `join` (avoid at scale)
- **Synthetic data**: `makeresults`

### Patterns the source teaches

- **The canonical SPL pipeline shape**: `<search> | <filter> | stats <agg> by <field> | where <threshold> | sort -<metric>` — composable left-to-right. Every detection in @sources/100-splunk-queries-soc-analyst.md follows this shape.
- **`stats` is the workhorse**; `join` and `transaction` are anti-patterns at scale. [CONFIRMED — recurring across the source's command notes]
- **`rex` for ad-hoc field extraction** when CIM normalization isn't in place — pull a `user=...` field straight out of `_raw` with a named capture group.
- **`eventstats` vs `stats`** — `eventstats` adds aggregates to every event without collapsing them; `stats` collapses. Critical distinction for "annotate events with their group's count" hunts.
- **`streamstats`** — running totals (per-event-as-of-this-row), useful for first-N-tracking and cumulative-sum patterns.

### Extraction confidence

Full alphabetical reference was read. The PDF is structurally a cheatsheet — each command stands alone, so there's no narrative arc to defer. The synthesis on @entities/tools/splunk.md filters down to the ~25 commands that recur in real SOC detection work; the long tail (`abstract`, `accum`, `addtotals`, `cluster`, etc.) is documented in this source but rarely appears in production detection content.

## Snippets

> **Canonical SPL pipeline** [Source: Splunk Commands.pdf — pattern across all `stats`/`where`/`sort` examples]
>
> ```
> <search query>
> | stats <agg-fn> as <name> by <group-field>
> | where <threshold>
> | sort -<sort-field>
> ```

> **`rex` named-capture extraction** [Source: Splunk Commands.pdf, `rex` entry]
>
> ```
> ... | rex field=_raw "user=(?<user>\w+)\s+action=(?<action>\w+)"
> ```

> **`eventstats` — annotate without collapsing** [Source: Splunk Commands.pdf, `eventstats` entry]
>
> ```
> ... | eventstats avg(bytes) as avg_bytes by src_ip
>     | where bytes > 2 * avg_bytes
> ```

> **`transaction` — group events into sessions** [Source: Splunk Commands.pdf, `transaction` entry]
>
> ```
> ... | transaction src_ip maxspan=30m maxpause=5m
> ```
>
> Useful for session reconstruction but **does not distribute** across indexers — avoid for large datasets.

## Relations

- @entities/tools/splunk.md
- @concepts/siem.md
- @concepts/soc-operations.md
- @concepts/threat-hunting.md
