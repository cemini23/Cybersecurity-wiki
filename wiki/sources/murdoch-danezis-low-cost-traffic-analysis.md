---
title: Murdoch & Danezis — Low-Cost Traffic Analysis of Tor
type: source
tags: [source, academic, tor, traffic-analysis, anonymity]
keywords: [traffic confirmation, Murdoch, Danezis, autonomous system, timing analysis, 2005 IEEE S&P]
related:
  - concepts/metadata-traffic-analysis-anonymity.md
  - concepts/anonymity-networks.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — academic paper (PDF archived to egress-fi)"
wire_status: wont_wire
---

## Relations

- @concepts/metadata-traffic-analysis-anonymity.md — the single-AS traffic-confirmation result this concept is built on
- @concepts/anonymity-networks.md — Tor primer; this paper is the anonymity-breaking-attack layer

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Low-Cost Traffic Analysis of Tor |
| Authors | Steven J. Murdoch, George Danezis (University of Cambridge) |
| Venue | 2005 IEEE Symposium on Security and Privacy (Oakland, CA, USA) |
| URL | https://www.cl.cam.ac.uk/~sjm217/papers/oakland05torta.pdf |
| Retrieved | 2026-08-12 |
| Location | `research to be indexed/murdoch-danezis-low-cost-traffic-analysis.pdf` → archived to egress-fi cybersec/ |

## Narrative

Well-cited early result on Tor's susceptibility to **traffic confirmation** (the attacker who observes the network path rather than breaks cryptography). The paper argues that low-latency anonymity networks like Tor preserve enough timing/volume structure that an adversary observing a *small portion* of the network — even a single autonomous system (AS) that carries a user's traffic — can correlate flows entering and leaving the network and confirm who is talking to whom, at low cost. The paper also discusses countermeasures and design changes, including a "mixmaster"-style defense and an application of anonymity measures that reduce the effectiveness of such correlation. [TENTATIVE — abstract parsed from PDF page 1; figures/quantified results not extracted in this pass]

The network-size intuition is important for the wiki concept: adding more relays does not by itself defeat an AS-level observer, because the adversary watches the *links a user's traffic crosses*, not the whole network.

## Snippets

Page 1 (paraphrase, not verbatim — PDF text extraction garbled): the abstract frames Tor as the second-generation onion-routing anonymity network whose low latency, needed for interactive use like web browsing, is precisely what makes its traffic pattern correlatable by an observer, and proposes low-cost traffic-analysis attacks plus design countermeasures. Locator: p.1, `research to be indexed/murdoch-danezis-low-cost-traffic-analysis.pdf`.
