#!/usr/bin/env python3
"""Writer for K392-K394 ingest (2026-10-03). No attack payloads in wiki."""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-10-03"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump_updated(text: str) -> str:
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", text, count=1, flags=re.M)


def add_related(rel: str, ref: str, note: str) -> None:
    p = WIKI / rel
    t = p.read_text(encoding="utf-8")
    yaml_line = f"  - {ref}"
    if yaml_line not in t:
        t = t.replace("related:\n", f"related:\n{yaml_line}\n", 1)
    body_line = f"- @{ref} — {note}"
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n{body_line}\n", 1)
    t = bump_updated(t)
    p.write_text(t, encoding="utf-8")
    print("patched related", rel, "→", ref)


def src(
    slug: str,
    title: str,
    arxiv: str,
    kid: str,
    pdf: str,
    narrative: str,
    concept: str,
    extra_related: list[str] | None = None,
    ood: bool = False,
    wire: str = "",
) -> None:
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra_related or [])]
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else "\n## Relations\n\n"
    if extra_related:
        rel_sec += "".join(f"- @{r}\n" for r in extra_related)
    tags = "source, ood" if ood else "source, arxiv, wireless-security"
    keywords = f"{arxiv}, ood" if ood else f"{arxiv}, {kid.lower()}"
    wire_line = wire or (
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)"
        if ood
        else f".cursor/rules/cemini-cybersec-lab-redteam.mdc ({kid})"
    )
    body = f"""---
title: "{title}"
type: source
tags: [{tags}]
keywords: [{keywords}]
{rel_yaml}
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — no attack payloads in wiki."
wire_status: policy_wired
wire_target: "{wire_line}"
---

## Relations
{rel_sec}
## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| arXiv | {arxiv} |
| Location | {EGRESS}/{pdf} |
| Retrieved | {DATE} |
| Read status | read (deep-read) |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"sources/{slug}.md", body)


def concept_page(
    slug: str,
    title: str,
    kid: str,
    arxiv: str,
    narrative: str,
    related: list[str],
    wire: str,
) -> None:
    rel_yaml = "\n".join(f"  - {r}" for r in related)
    rel_inline = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, wireless-security, {kid.lower()}]
keywords: [{arxiv}, {kid}]
related:
{rel_yaml}
maturity: draft
created: {DATE}
updated: {DATE}
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{rel_inline}

## Raw Concept

Question: **{title}** — operator steal from arXiv {arxiv}?

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"concepts/{slug}.md", body)


def main() -> int:
    # ---------------- K392 ------------------------------------------------
    src(
        "arxiv-2609-31519-wpa3-sae-asymmetric-pe-tickets",
        "Fast and secure simultaneous authentication of equals for WPA3",
        "2609.31519",
        "K392",
        "arxiv-2609.31519-fast-and-secure-simultaneous-authentication-of-e.pdf",
        "**K392** — WPA3-SAE fixed the WPA2 offline-dictionary weakness but **introduced a DoS surface**: "
        "the hunting-and-pecking loop that derives the Password Element (PE) is expensive, and an attacker "
        "can force the AP to run it repeatedly (Dragonblood-class CPU exhaustion). Three changes make the "
        "cost asymmetric: **RIIE** moves the iterative discovery to the *client* so the AP does a one-step "
        "derivation; a **slow-path KDF** (PBKDF2/Argon2, variable cost) puts the deliberate delay on the "
        "supplicant rather than the AP; and **SFTR** adds stateless **session tickets** (Kerberos / TLS 1.3 "
        "style, STEK-encapsulated, sequential TID, IPsec-style anti-replay window) so known devices skip PE "
        "derivation entirely. Measured on hostapd 2.10 + wpa_supplicant 2.10 with OpenSSL, N=100: standard "
        "SAE **2284 µs** (σ=521.8) → proposed initial auth **72.5 µs** (σ=11.0, **−96.8%**) → ticket "
        "fast-path **21 µs** (σ=4.9, ~**99%**). Operator steal: the load-bearing idea is **which side pays** "
        "— a cost the client must pay is cheap to demand; a cost the AP must pay is a DoS lever. Also note "
        "the honest trade: moving iteration to the client is what keeps offline-dictionary resistance, so "
        "the slow-path KDF is not optional. PBKDF2 was run at only 10 iterations for functional validation "
        "and is stated to scale. Wireless lab only — the paper's goal is availability, not a bypass.",
        "concepts/wpa3-sae-dos-cost-asymmetry.md",
        [
            "concepts/wireless-pentest.md",
            "concepts/network-security.md",
        ],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K392)",
    )
    concept_page(
        "wpa3-sae-dos-cost-asymmetry",
        "WPA3 SAE cost asymmetry — DoS hardening",
        "K392",
        "2609.31519",
        "SAE is deliberately expensive, which is both its strength and its availability weakness. The "
        "design rule to reuse: **put the expensive, unbounded work on the side that can afford to be "
        "exhausted, and make the other side's work fixed.** Here the client does the iteration and the AP "
        "does a single derivation; a variable-cost KDF adds a tunable delay on the supplicant (PBKDF2 / "
        "Argon2 with real iteration counts — 10 is a prototype value); stateless tickets let known devices "
        "skip the exchange. Two cautions: the slow path is what preserves offline-dictionary resistance, so "
        "shortening it is a security change, not a performance tweak; and ticket state/replay handling is "
        "the new surface. Assess an AP's SAE posture by **measuring per-authentication AP CPU cost under "
        "repeated failed attempts**, not by reading the cipher suite.",
        [
            "sources/arxiv-2609-31519-wpa3-sae-asymmetric-pe-tickets.md",
            "concepts/wireless-pentest.md",
            "concepts/network-security.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K392)",
    )

    # ---------------- K393 ------------------------------------------------
    src(
        "arxiv-2610-01580-pld-eap-teap-wifi-authentication",
        "Protocol integration of physical layer deception into EAP-TEAP Wi-Fi authentication",
        "2610.01580",
        "K393",
        "arxiv-2610.01580-protocol-integration-of-physical-layer-deception.pdf",
        "**K393** — credential-based EAP authenticates *whoever holds the credential*, so a cloned or "
        "exfiltrated credential makes an adversary indistinguishable at the credential layer. This adds "
        "**Physical Layer Deception (PLD)** as a second factor derived from the channel: each round exposes "
        "a deceptive primary object (`m = p ⊕ k`, fresh nonzero key) over the TEAP/TLS tunnel while a "
        "key-bearing **recovery object** travels separately over IEEE 802.11 Category-127 action frames, "
        "where a favourably-placed receiver recovers the true value more reliably than a remote one. "
        "Authentication-specific twist: a batch of L≤3 rounds with **exactly A active positions, A≥1**, no "
        "activation flag, and all rounds must verify — because an all-inactive attempt would leak every "
        "true challenge and never exercise the recovery path. Implemented end to end in **hostap 2.12** "
        "(server + hostapd + wpa_supplicant) under mac80211_hwsim; **1593 attempts** across four campaigns. "
        "The AP relays and never decrypts TEAP, so it never sees the plaintext primary object. Results: "
        "ordinary TEAP 30/30 accepted; full recovery L=3, A=1 and A=3 both 30/30; degraded recovery "
        "(r=.95, A=1) 29/30; the **naive credential-bearing attacker is rejected in all 30 attempts**. "
        "Trade-off is analytic: **PFA = r_E^A**, **PFR = 1 − r_B^A**, with a 2000 ms recovery deadline. "
        "Operator steal: a second factor can live in the **channel**, not in another secret — but the "
        "binding needs a recovery channel the attacker cannot co-locate with. Wireless/enterprise lab only.",
        "concepts/physical-layer-deception-enterprise-wifi-auth.md",
        [
            "concepts/wireless-pentest.md",
            "concepts/wifi-rf-fingerprinting-open-set.md",
            "concepts/network-security.md",
        ],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K393)",
    )
    concept_page(
        "physical-layer-deception-enterprise-wifi-auth",
        "Physical layer deception as a second auth factor",
        "K393",
        "2610.01580",
        "A credential is a bearer token: whoever holds it authenticates. A **channel-derived** second "
        "factor asks instead whether the claimant is *where* it claims — evidence a remote party cannot "
        "easily reproduce. The mechanism here is **deception, not measurement**: the server puts a "
        "deliberately wrong value on the primary path and a key on a secondary path, so only a "
        "well-positioned receiver recovers the truth. Design constraints worth keeping: at least one round "
        "must be active (all-inactive leaks the truth), no activation flag is transmitted (its presence "
        "would be the signal), and **all** rounds gate the result. Costs are explicit — a false-accept "
        "probability **r_E^A** traded against a false-reject **1 − r_B^A** — so it is only deployable where "
        "that trade is chosen deliberately. Pairs channel-fingerprint approaches; it does not replace them.",
        [
            "sources/arxiv-2610-01580-pld-eap-teap-wifi-authentication.md",
            "concepts/wireless-pentest.md",
            "concepts/wifi-rf-fingerprinting-open-set.md",
            "concepts/network-security.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K393)",
    )

    # ---------------- K394 (OOD: computational art) -----------------------
    src(
        "arxiv-2610-02045-form-and-void-agent-ood",
        "Form and Void: entangled composition through an autonomous AI agent (OOD)",
        "2610.02045",
        "K394",
        "arxiv-2610.02045-form-and-void-entangled-composition-through-an-a.pdf",
        "**K394 — OOD for security.** A multimodal agent (FaV-A) that generates **positive–negative space** "
        "art: it plans a base object from an abstract topic, analyses the base image's shape and spatial "
        "structure to find candidate negative-space semantics, then writes mask-free composition "
        "instructions for a final synthesis pass. Staged pipeline (plan → parse/anchor → synthesise), no "
        "masks or layout templates; tokens/deliberation were meant to include an agentic workaround for "
        "mask-free photo editing and the in-context workaround that keeps multi-subject editing "
        "identity-aligned. User study N=50 on 5-point Likert: full FaV-A topic adherence 4.65 ± 0.35 vs "
        "3.45–4.15 for ablations, and the largest gaps on Gestalt quality (4.58 ± 0.40 vs 1.60–2.15). "
        "**Security relevance: none** — no attacker, defender, or protected asset; users are designers and "
        "computational-art researchers. Routed to **image-gen** (text-to-image agent technique). Cyber "
        "keeps this stub only.",
        "",
        ood=True,
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)",
    )

    # ---------------- cross-links into existing pages ---------------------
    _backlinks = {
        "sources/arxiv-2609-31519-wpa3-sae-asymmetric-pe-tickets.md": (
            "concepts/wireless-pentest.md",
            "concepts/network-security.md",
        ),
        "sources/arxiv-2610-01580-pld-eap-teap-wifi-authentication.md": (
            "concepts/wireless-pentest.md",
            "concepts/wifi-rf-fingerprinting-open-set.md",
            "concepts/network-security.md",
        ),
    }
    for source_ref, concept_refs in _backlinks.items():
        for concept_ref in concept_refs:
            add_related(concept_ref, source_ref, "K392-K393 wireless ingest source")

    for concept_ref, new_ref in (
        ("concepts/wireless-pentest.md", "concepts/wpa3-sae-dos-cost-asymmetry.md"),
        ("concepts/wireless-pentest.md", "concepts/physical-layer-deception-enterprise-wifi-auth.md"),
        ("concepts/network-security.md", "concepts/wpa3-sae-dos-cost-asymmetry.md"),
        ("concepts/network-security.md", "concepts/physical-layer-deception-enterprise-wifi-auth.md"),
        ("concepts/wifi-rf-fingerprinting-open-set.md", "concepts/physical-layer-deception-enterprise-wifi-auth.md"),
    ):
        add_related(concept_ref, new_ref, "K392-K393 wireless cross-link")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
