#!/usr/bin/env python3
"""Writer for K403-K407 ingest (2026-10-07). No attack payloads in wiki.

Conventions that have bitten this script before:
  - concept_page(slug, ...) takes a slug WITHOUT a .md extension.
  - every entry in a `related`/`extra` list MUST carry its .md extension.
"""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-10-07"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump_updated(text: str) -> str:
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", text, count=1, flags=re.M)


def add_related(rel: str, ref: str, note: str) -> None:
    assert ref.endswith(".md"), f"related ref needs .md: {ref}"
    p = WIKI / rel
    t = p.read_text(encoding="utf-8")
    if f"  - {ref}" not in t:
        t = t.replace("related:\n", f"related:\n  - {ref}\n", 1)
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n- @{ref} — {note}\n", 1)
    t = bump_updated(t)
    p.write_text(t, encoding="utf-8")
    print("patched", rel, "→", ref)


def src(slug, title, arxiv, kid, pdf, narrative, concept, extra=None, ood=False, wire=""):
    assert not slug.endswith(".md"), slug
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra or [])]
    for r in rels:
        assert r.strip().startswith("- ") and r.strip().endswith(".md"), r
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else "\n## Relations\n\n"
    if extra:
        rel_sec += "".join(f"- @{r}\n" for r in extra)
    tags = "source, ood" if ood else "source, arxiv, agent-security"
    keywords = f"{arxiv}, ood" if ood else f"{arxiv}, {kid.lower()}"
    wire_line = wire or (
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)" if ood
        else f".cursor/rules/cemini-cybersec-lab-redteam.mdc ({kid})")
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


def concept_page(slug, title, kid, arxiv, narrative, related, wire):
    assert not slug.endswith(".md"), slug
    for r in related:
        assert r.endswith(".md"), r
    rel_yaml = "\n".join(f"  - {r}" for r in related)
    rel_inline = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, agent-security, {kid.lower()}]
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
    # ---------------- K403 ATLAS-AL ---------------------------------------
    src("arxiv-2610-07323-atlas-al-adversarial-region-active-learning",
        "ATLAS-AL: adaptive trust-region for latent adversarial searches via active learning",
        "2610.07323", "K403",
        "arxiv-2610.07323-atlas-al-adaptive-trust-region-for-latent-advers.pdf",
        "**K403** — most black-box attacks optimise for **one** successful adversarial example. This argues "
        "the useful object is a **representative adversarial SET** — an estimate of the whole failure "
        "**region**, which tells you *where and how* a system fails and supports **continuous auditing** as "
        "robustness drifts. ATLAS casts attack generation as **active learning level-set estimation**, "
        "combining **calibrated approximations** of the target with a **local-global sampling** "
        "architecture: the model samples where it is uncertain rather than uniformly, so fewer queries land "
        "in regions already known well. On toy problems it recovers more of the adversarial region under a "
        "**limited query budget** than prior work, and on standard and adversarially-trained MNIST / CIFAR / "
        "ImageNet it produces better representative attacks than **NES, SignHunter, BayesOpt**. Operator "
        "steal: **audit coverage, not a single failure** — and note that adversarial training is a target "
        "condition here, not an assumed defence. Pairs K396 (report sensitivity, not one number) and K388 "
        "(breaking level): all three replace a point score with a claim about a region. Lab only, owned or "
        "procured models. **No attack code or perturbation recipes in wiki.**",
        "concepts/adversarial-region-estimation-vs-single-example.md",
        ["concepts/threat-preserving-representation-sensitivity.md",
         "concepts/benchmark-shortcut-attack-pyramid-audit.md",
         "concepts/guardrail-construct-validity-agent-eval.md",
         "concepts/llm-adversarial-fuzzing.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K403)")
    concept_page("adversarial-region-estimation-vs-single-example",
        "Estimate the adversarial region, not one example", "K403", "2610.07323",
        "A single adversarial example proves a model *can* fail. It does not tell you **where it fails**, "
        "which is what an audit needs. Treat attack generation as **level-set estimation**: model the "
        "failure region, then sample inside it to build a **representative set**. Make the search "
        "**active** — spend queries where the estimate is uncertain, not uniformly — because query budget "
        "is the binding constraint on a black box. Report **region coverage under a query budget**, and "
        "re-run it over time: the point of a region estimate is that it is comparable across releases. "
        "Same shape as the K396 sensitivity and K388 breaking-level rules.",
        ["sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md",
         "concepts/threat-preserving-representation-sensitivity.md",
         "concepts/benchmark-shortcut-attack-pyramid-audit.md",
         "concepts/guardrail-construct-validity-agent-eval.md",
         "concepts/llm-adversarial-fuzzing.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K403)")

    # ---------------- K404 PQC BLE pairing --------------------------------
    src("arxiv-2610-07870-post-quantum-ble-pairing-nfc-oob-implant",
        "Plug-and-play quantum-resistant BLE pairing for medical implants via NFC out-of-band",
        "2610.07870", "K404",
        "arxiv-2610.07870-plug-and-play-quantum-resistant-ble-pairing-for.pdf",
        "**K404** — BLE pairing is the cryptographic foundation for implant communication, but the "
        "MITM-resistant association models (**Numeric Comparison**, **Passkey Entry**) need a UI that an "
        "implantable medical device does not have. **NFC out-of-band** pairing is the usual workaround; the "
        "problem is that existing NFC-OOB schemes only *authenticate* a **classical** BLE key exchange "
        "(quantum-vulnerable), and the NFC channel itself is eavesdroppable and open to active injection "
        "under a stronger threat model. The proposal runs a **post-quantum KEM (Kyber / FireSABER) entirely "
        "over the NFC channel**, so **no shared secret is transmitted over NFC** at all, long-range RF "
        "exposure during pairing drops, the **BLE stack is unchanged**, and it inherently resists "
        "**RF battery-depletion** attacks. On an IMD-class testbed the overhead is **under 0.57% for "
        "Kyber-1024 and 0.56% for FireSABER**. Operator steal: **harvest-now-decrypt-later applies to "
        "pairing**, not just transport — an OOB channel that authenticates a classical exchange is a "
        "temporary fix; and a very short-range channel is a **threat-model** control, not just a convenience. "
        "Authorized device lab only. **No pairing bypass or key-recovery recipes in wiki.**",
        "concepts/post-quantum-oob-pairing-medical-implants.md",
        ["concepts/wireless-pentest.md",
         "concepts/ble-mac-randomization-reidentification-lab.md",
         "concepts/ble-backscatter-polarization-shift-identification-lab.md",
         "concepts/mobile-app-attestation.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K404)")
    concept_page("post-quantum-oob-pairing-medical-implants",
        "Post-quantum out-of-band pairing for implants", "K404", "2610.07870",
        "Devices without a screen cannot use MITM-resistant BLE association, so pairing leans on an "
        "**out-of-band** channel — usually NFC. Two things follow. First, **harvest-now-decrypt-later "
        "reaches pairing**: if the OOB channel merely *authenticates* a classical key exchange, the session "
        "is recorded today and broken later. Run the **post-quantum KEM on the OOB channel itself** so no "
        "shared secret crosses it. Second, **proximity is a threat-model control** — a very short-range "
        "channel shrinks the set of attackers who can inject — but it does not replace authentication, "
        "because the channel is still eavesdroppable. Cost is small: under 0.57% overhead, no BLE stack "
        "change. Authorized device lab only.",
        ["sources/arxiv-2610-07870-post-quantum-ble-pairing-nfc-oob-implant.md",
         "concepts/wireless-pentest.md",
         "concepts/ble-mac-randomization-reidentification-lab.md",
         "concepts/ble-backscatter-polarization-shift-identification-lab.md",
         "concepts/mobile-app-attestation.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K404)")

    # ---------------- K405 secure speculative decoding --------------------
    src("arxiv-2610-08678-secure-speculative-decoding",
        "Secure speculative decoding for large language models",
        "2610.08678", "K405",
        "arxiv-2610.08678-secure-speculative-decoding-for-large-language-m.pdf",
        "**K405 — an inference optimisation that silently weakens safety.** Speculative decoding speeds a "
        "**target** model by letting a smaller **draft** model propose tokens the target then verifies. "
        "Prior work studied only the efficiency–utility trade-off. This is the first systematic look at the "
        "**security** implications, and it finds a sharp **security–utility asymmetry**: swapping in a "
        "weaker draft model raises **attack success rates for jailbreak and prompt injection** substantially "
        "while barely moving utility — so the cost of the weakness is invisible on a quality benchmark. The "
        "mechanism is the **early tokens** the draft model generates, which the target's ordinary acceptance "
        "check waves through. **SecureSD** applies a **stricter verification criterion to draft-model tokens "
        "at early decoding positions**, cutting jailbreak and prompt-injection ASR by **up to 92.4%** while "
        "keeping **99.8%** of the decoding speedup and utility within **98.4%** of existing methods. "
        "Operator steal: **treat any inference-time optimisation as a safety-relevant change** — a draft "
        "model is part of the trusted computing base once it can put tokens in the output stream. Pairs the "
        "inference-cost thread (K376) and the IPI thread. Lab only, owned or procured models. **No jailbreak "
        "payloads or decoding exploits in wiki.**",
        "concepts/speculative-decoding-safety-asymmetry.md",
        ["concepts/fragtoken-inference-cost-amplification-lab.md",
         "concepts/reliable-inference-procurement-routing.md",
         "concepts/prompt-injection-detector-calibration.md",
         "concepts/crescendo-multi-turn-jailbreak.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K405)")
    concept_page("speculative-decoding-safety-asymmetry",
        "Speculative decoding safety asymmetry", "K405", "2610.08678",
        "Speculative decoding lets a **small draft model** write tokens that a **large target model** "
        "verifies. The verification check is tuned for *distributional* agreement, not for safety — so a "
        "weak draft model can push jailbreak and prompt-injection content through early decoding positions "
        "while a utility benchmark shows almost nothing. That asymmetry is the finding: **the safety cost "
        "does not appear on the metric you are watching.** The defence is to tighten verification for "
        "draft-model tokens **at early positions** specifically (up to **92.4%** ASR reduction at **99.8%** "
        "of the speedup). Operator rule: an optimisation that adds a model to the token path **adds a model "
        "to the trusted computing base** — re-run the safety eval, not just the quality eval.",
        ["sources/arxiv-2610-08678-secure-speculative-decoding.md",
         "concepts/fragtoken-inference-cost-amplification-lab.md",
         "concepts/reliable-inference-procurement-routing.md",
         "concepts/prompt-injection-detector-calibration.md",
         "concepts/crescendo-multi-turn-jailbreak.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K405)")

    # ---------------- K406 BARE-AI ----------------------------------------
    src("arxiv-2610-08739-bare-ai-bit-flip-resilience",
        "BARE-AI: bit-flip attack resilience in AI hardware through built-in performance monitors",
        "2610.08739", "K406",
        "arxiv-2610.08739-bare-ai-bit-flip-attack-resilience-in-ai-hardwar.pdf",
        "**K406** — a **bit-flip attack** perturbs a few memory locations and degrades DNN accuracy sharply; "
        "existing defences carry heavy hardware cost, need retraining, or miss *targeted* flips. BARE-AI "
        "detects, localises, and mitigates at **runtime**. It adds **AI Performance Counters (APCs)** — "
        "lightweight monitors in the accelerator datapath that capture per-layer activation statistics "
        "(**sparsity, entropy, kurtosis, spectral shift**) — and feeds them to **PULSE**, a compact "
        "offline-trained ensemble realised on-chip as a small neural engine. For recovery it introduces an "
        "**Activation Shift Index (ASI)** for layer-level fault localisation and a **z-score statistical "
        "repair** that resets anomalous weights toward clean layer statistics. Across CNNs, ViTs and LLMs "
        "under random / targeted / adaptive / magnitude-based BFAs: **up to 98%** detection on vision "
        "models, **74–95%** on language models; near-clean accuracy restored for CNNs and ViTs, partial for "
        "LLMs. Cost is **< 3% energy, < 4% area, ~10% latency** (a configurable operating point takes "
        "latency to ~6%), and the overhead stays bounded as the tolerated flip count grows. Operator steal: "
        "**activation statistics are a cheap, model-agnostic tripwire for weight corruption**, and a "
        "monitor beats a retrain when the fault is physical. Pairs K402 — both are hardware-layer integrity "
        "stories that a software-only argument misses. Authorized hardware lab only. **No fault-injection "
        "recipes in wiki.**",
        "concepts/dnn-bit-flip-detection-runtime-monitors.md",
        ["concepts/hardware-membership-inference-microarchitecture.md",
         "concepts/tpm-attest-linux-integrity-attestation.md",
         "concepts/mobile-app-attestation.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K406)")
    concept_page("dnn-bit-flip-detection-runtime-monitors",
        "Runtime detection of bit-flip corruption in DNNs", "K406", "2610.08739",
        "A few flipped bits in model memory can gut accuracy, and the flips need not be random — targeted "
        "and adaptive attacks defeat simple checks. The practical defence is a **runtime monitor**, not a "
        "retrain: instrument the accelerator with lightweight counters over **per-layer activation "
        "statistics** (sparsity, entropy, kurtosis, spectral shift) and detect deviation from the clean "
        "profile. Detection is only half — you also need **localisation** (which layer) and **repair** "
        "(nudge anomalous weights back toward clean statistics). Reported at **up to 98%** detection on "
        "vision models and **74–95%** on LLMs, for **< 3% energy / < 4% area / ~10% latency**. The "
        "operator rule: a software-only integrity argument misses the memory system — pairs K402, where the "
        "same lesson arrives from the privacy side.",
        ["sources/arxiv-2610-08739-bare-ai-bit-flip-resilience.md",
         "concepts/hardware-membership-inference-microarchitecture.md",
         "concepts/tpm-attest-linux-integrity-attestation.md",
         "concepts/mobile-app-attestation.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K406)")

    # ---------------- K407 IdeaAnchor (OOD) -------------------------------
    src("arxiv-2610-08781-ideaanchor-research-ideation-ood",
        "IdeaAnchor: teaching LLMs to turn literature into research ideas (OOD)",
        "2610.08781", "K407",
        "arxiv-2610.08781-ideaanchor-teaching-llms-to-turn-literature-into.pdf",
        "**K407 — OOD for security.** IdeaAnchor trains LLMs to perform **literature-grounded research "
        "ideation**: it mines structured specifications from published papers that encode each input paper's "
        "**functional role**, its **relationships** to the others, and **target synthesis criteria**, then "
        "uses those as privileged signals for demonstration, self-distillation, and RL training, with "
        "retrieval added at generation time. **Security relevance: none** — no attacker, defender, or "
        "protected asset; this is an academic-research-assistant capability. Routed as an OOD stub. Cyber "
        "keeps the pointer only.",
        "", ood=True,
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)")

    # ---------------- backlinks -------------------------------------------
    for concept_ref, new_ref, note in (
        ("concepts/threat-preserving-representation-sensitivity.md",
         "concepts/adversarial-region-estimation-vs-single-example.md",
         "K403 estimate the failure region, not one example"),
        ("concepts/benchmark-shortcut-attack-pyramid-audit.md",
         "concepts/adversarial-region-estimation-vs-single-example.md",
         "K403 region coverage under a query budget"),
        ("concepts/guardrail-construct-validity-agent-eval.md",
         "concepts/adversarial-region-estimation-vs-single-example.md",
         "K403 active-learning level-set estimation for robustness audit"),
        ("concepts/llm-adversarial-fuzzing.md",
         "concepts/adversarial-region-estimation-vs-single-example.md",
         "K403 adaptive search over failure regions"),
        ("concepts/wireless-pentest.md",
         "concepts/post-quantum-oob-pairing-medical-implants.md",
         "K404 post-quantum OOB pairing for implant-class devices"),
        ("concepts/ble-mac-randomization-reidentification-lab.md",
         "concepts/post-quantum-oob-pairing-medical-implants.md",
         "K404 pairing is the cryptographic foundation BLE privacy builds on"),
        ("concepts/ble-backscatter-polarization-shift-identification-lab.md",
         "concepts/post-quantum-oob-pairing-medical-implants.md",
         "K404 NFC out-of-band pairing for implant-class devices"),
        ("concepts/fragtoken-inference-cost-amplification-lab.md",
         "concepts/speculative-decoding-safety-asymmetry.md",
         "K405 an inference optimisation that weakens safety"),
        ("concepts/reliable-inference-procurement-routing.md",
         "concepts/speculative-decoding-safety-asymmetry.md",
         "K405 draft model enters the token path and the TCB"),
        ("concepts/prompt-injection-detector-calibration.md",
         "concepts/speculative-decoding-safety-asymmetry.md",
         "K405 draft-model tokens raise injection ASR"),
        ("concepts/crescendo-multi-turn-jailbreak.md",
         "concepts/speculative-decoding-safety-asymmetry.md",
         "K405 jailbreak ASR rises with a weak draft model"),
        ("concepts/hardware-membership-inference-microarchitecture.md",
         "concepts/dnn-bit-flip-detection-runtime-monitors.md",
         "K406 hardware-layer integrity: activation statistics as a tripwire"),
        ("concepts/tpm-attest-linux-integrity-attestation.md",
         "concepts/dnn-bit-flip-detection-runtime-monitors.md",
         "K406 runtime detection of weight corruption"),
        ("concepts/mobile-app-attestation.md",
         "concepts/dnn-bit-flip-detection-runtime-monitors.md",
         "K406 physical-fault integrity monitoring"),
    ):
        add_related(concept_ref, new_ref, note)

    for source_ref, concept_refs in {
        "sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md": (
            "concepts/threat-preserving-representation-sensitivity.md",
            "concepts/benchmark-shortcut-attack-pyramid-audit.md",
            "concepts/guardrail-construct-validity-agent-eval.md",
            "concepts/llm-adversarial-fuzzing.md"),
        "sources/arxiv-2610-07870-post-quantum-ble-pairing-nfc-oob-implant.md": (
            "concepts/wireless-pentest.md",
            "concepts/ble-mac-randomization-reidentification-lab.md",
            "concepts/ble-backscatter-polarization-shift-identification-lab.md",
            "concepts/mobile-app-attestation.md"),
        "sources/arxiv-2610-08678-secure-speculative-decoding.md": (
            "concepts/fragtoken-inference-cost-amplification-lab.md",
            "concepts/reliable-inference-procurement-routing.md",
            "concepts/prompt-injection-detector-calibration.md",
            "concepts/crescendo-multi-turn-jailbreak.md"),
        "sources/arxiv-2610-08739-bare-ai-bit-flip-resilience.md": (
            "concepts/hardware-membership-inference-microarchitecture.md",
            "concepts/tpm-attest-linux-integrity-attestation.md",
            "concepts/mobile-app-attestation.md"),
    }.items():
        for cr in concept_refs:
            add_related(cr, source_ref, "K403-K407 ingest source page")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
