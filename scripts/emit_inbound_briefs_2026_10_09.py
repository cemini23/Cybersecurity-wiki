#!/usr/bin/env python3
"""Fill out pages for the inbound briefs of 2026-10-07..08. No attack payloads.

Sources: briefs/2026-10-07_k284-strata-local-inference.md,
         briefs/2026-10-08_k285-cyber-model-repair.md,
         briefs/2026-10-08_k285-rea-background-agents.md,
         briefs/2026-10-08_audio-visual-attack-forensics-from-image-gen.md

Slugs are passed WITHOUT .md; every related ref MUST end with .md.
"""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
DATE = "2026-10-09"


def w(rel, body):
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump(t):
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", t, count=1, flags=re.M)


def add_related(rel, ref, note):
    assert ref.endswith(".md"), ref
    p = WIKI / rel
    t = p.read_text(encoding="utf-8")
    if f"  - {ref}" not in t:
        t = t.replace("related:\n", f"related:\n  - {ref}\n", 1)
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n- @{ref} — {note}\n", 1)
    p.write_text(bump(t), encoding="utf-8")
    print("patched", rel, "→", ref)


def source(slug, title, ident, kind, location, narrative, related, read="read (routed brief)"):
    assert not slug.endswith(".md")
    for r in related:
        assert r.endswith(".md"), r
    rels = "\n".join(f"  - {r}" for r in related)
    inl = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title}"
type: source
tags: [source, routed]
keywords: [{ident}]
related:
{rels}
maturity: draft
read_status: {read}
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

{inl}

## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| Identifier | {ident} |
| Type | {kind} |
| Location | {location} |
| Retrieved | {DATE} |
| Read status | {read} |

## Narrative

{narrative}

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route ({DATE})]
"""
    w(f"sources/{slug}.md", body)


def concept(slug, title, kid, ident, narrative, related, wire, tags="agent-security"):
    assert not slug.endswith(".md")
    for r in related:
        assert r.endswith(".md"), r
    rels = "\n".join(f"  - {r}" for r in related)
    inl = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, {tags}, {kid.lower()}]
keywords: [{ident}, {kid}]
related:
{rels}
maturity: draft
created: {DATE}
updated: {DATE}
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{inl}

## Raw Concept

Question: **{title}** — operator steal from the inbound brief ({ident})?

## Narrative

{narrative}

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route ({DATE})]
"""
    w(f"concepts/{slug}.md", body)


def entity(slug, title, kid, ident, narrative, related, wire, verdict):
    assert not slug.endswith(".md")
    for r in related:
        assert r.endswith(".md"), r
    rels = "\n".join(f"  - {r}" for r in related)
    inl = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title}"
type: entity
tags: [entity, tool, {tags_for(title)}]
keywords: [{ident}, {kid}]
related:
{rels}
maturity: draft
created: {DATE}
updated: {DATE}
phase_0_verdict: "{verdict}"
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{inl}

## Raw Concept

{title} — evaluated from the inbound routed brief ({ident}).

## Narrative

{narrative}

## Snippets

> Verified from the routed brief, not a first-hand repo audit. [Source: `briefs/` inbound route ({DATE})]
"""
    w(f"entities/tools/{slug}.md", body)


def tags_for(title):
    return "agent-security"


def main() -> int:
    # ---------- Strata (tool) ---------------------------------------------
    entity("strata", "Strata (local 125B-MoE inference engine)", "K284",
        "github.com/Niko1221/Strata",
        "**MIT, 16,491 stars, active (verified 2026-10-07).** A **125B-parameter MoE** model runs on "
        "consumer hardware and is exposed as a **localhost OpenAI/Anthropic-compatible endpoint**. That "
        "removes the usual trade-off for the private and air-gapped lanes: frontier-grade local reasoning "
        "with **zero token cost** and no data leaving the host.\n\n"
        "**Why it matters for this wiki.** Two lanes gain at once. The **local abliterated lab / cyber "
        "analysis** lane gets strong local reasoning without a cloud call. **Atto air-gapped "
        "Latin/genealogical parsing** gets the privacy-perimeter path that never touches a cloud model. "
        "Because the endpoint is OpenAI/Anthropic-shaped, **existing agent code points at it with no code "
        "change** — which is the whole attraction.\n\n"
        "**Constraints, and they are real.** The **first load locks 35-55 GB of system RAM** and needs a "
        "fast **NVMe SSD** for n-gram table paging. It competes for RAM/VRAM with any other local "
        "workload. Check the host fits before planning around it. **Human-gated; no install performed.**",
        ["concepts/local-abliterated-llm-pentest-stack.md",
         "concepts/reliable-inference-procurement-routing.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K284)",
        verdict="CONDITIONAL-GO K284 — MIT, active, high-star; local only. Verify the host has 35-55GB RAM and NVMe before adopting. No clone this batch.")

    # ---------- PatchBench + SLDR -----------------------------------------
    source("arxiv-2610-10276-patchbench-local-suppression-vs-repair",
        "PatchBench: activation patching, local suppression vs selective repair",
        "arXiv 2610.10276", "arXiv paper (routed by OSINT K285)",
        "not held locally — routed brief only",
        "**A global metric can hide a large local regression.** Activation patching 'repairs' a jailbreak "
        "refusal; PatchBench asks whether that is a **selective repair** or **broad local suppression**. It "
        "generates **29 neighbours per failure** (paraphrase, translation, punctuation, spelling; benign "
        "structural/lexical) and measures two axes: **HNCS** (harmful-neighbour correction) and **BNPS** "
        "(benign-neighbour preservation).\n\n"
        "**Findings.** AST-style patching gains HNCS but **loses large BNPS** — Qwen-3B **+3.1 HNCS over "
        "AlphaSteer yet −27.4 BNPS**; Gemma-4B **58.3 lower BNPS**. And the headline: **MMLU can be flat "
        "while local regression is severe** — CAST on Llama-8B shows **MMLU −0.07** but **BNPS −26.3**. "
        "Operator steal: **audit the change set, not the metric.** A repair that passes an aggregate "
        "benchmark can still have broken a neighbourhood you never measured. Pairs K396 (report "
        "sensitivity) and K405 (a change invisible on the quality metric).",
        ["concepts/local-suppression-vs-repair.md",
         "concepts/threat-preserving-representation-sensitivity.md",
         "concepts/speculative-decoding-safety-asymmetry.md"],
        read="read (routed brief)")
    source("arxiv-2610-10345-sldr-signed-layer-safety-repair",
        "SLDR: repairing malicious fine-tunes by touching two layers",
        "arXiv 2610.10345", "arXiv paper (routed by OSINT K285)",
        "not held locally — routed brief only",
        "**Layer safety sensitivity is signed.** Malicious fine-tuning — a rented poisoned LoRA — strips "
        "refusal, and SLDR's finding is that the layers which matter have a **direction**. So it repairs "
        "only the **two extreme-sensitivity layers** with a LoRA recovery adapter, and **routes only "
        "malicious queries** through the repair (cosine-based malicious score, tau = 0).\n\n"
        "**Result:** average **Harmful Score 11.54 → 0.08** with finetune accuracy **92.39 → 92.32**, "
        "near-lossless, beating BDS / Panacea / Lisa / Antidote / STAR-DSS. Works across Llama-3.1, "
        "Llama-3, Qwen-2.5, Mistral. Operator steal: a repair does not have to be global — **find the "
        "signed layers and route only the traffic that needs repair.** Pairs K410 (constrained-action "
        "remediation) and the K285 PatchBench finding that breadth of repair is what causes collateral "
        "damage.",
        ["concepts/local-suppression-vs-repair.md",
         "concepts/speculative-decoding-safety-asymmetry.md"],
        read="read (routed brief)")
    concept("local-suppression-vs-repair",
        "Local suppression is not repair", "K285-a", "arXiv 2610.10276 / 2610.10345",
        "When a model refusal is 'fixed' by activation patching, two very different things may have "
        "happened: the harmful behaviour was **selectively repaired**, or a broad neighbourhood was "
        "**suppressed** — which also damages benign behaviour that happened to sit nearby.\n\n"
        "Measure it **locally**, not globally: generate neighbours of the failure and score **harmful-"
        "neighbour correction** against **benign-neighbour preservation**. PatchBench's numbers show why a "
        "global benchmark is not enough — **MMLU moved −0.07 while BNPS fell 26.3**. The constructive "
        "counterpart is SLDR: safety sensitivity across layers is **signed**, so repair the extreme layers "
        "and **route only the affected traffic**, giving Harmful Score **11.54 → 0.08** at near-zero "
        "accuracy cost. Rule: **a repair claim needs a neighbourhood test, and the narrowest repair is "
        "usually the right one.**",
        ["sources/arxiv-2610-10276-patchbench-local-suppression-vs-repair.md",
         "sources/arxiv-2610-10345-sldr-signed-layer-safety-repair.md",
         "concepts/threat-preserving-representation-sensitivity.md",
         "concepts/speculative-decoding-safety-asymmetry.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K285-a)")

    # ---------- rea + background-agents (tools) ---------------------------
    entity("rea", "rea — agent-first reverse-engineering toolkit and MCP server", "K285-b",
        "github.com/morluto/rea",
        "**MIT, 19,363 stars.** 'Reverse engineer anything with agents, from app behaviour down to native "
        "binaries.' An **agent-first reverse-engineering toolkit and MCP server** that bridges Claude / "
        "Cursor into **Hopper disassembly and execution tracing**.\n\n"
        "**Why it is notable here.** This was a **Pass in K283** and is an **Extract here** — a "
        "re-evaluation, because the technique it names (MCP-mediated decompilation) is now mature enough "
        "to be routine. **Hard gate:** it needs a **local Hopper Disassembler** and must stay inside a "
        "**whitehat authorized scope**. The pattern is filed; **no PoC, no exploit steps, no payloads.**",
        ["concepts/local-abliterated-llm-pentest-stack.md",
         "concepts/llm-vulnerability-discovery.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K285-b)",
        verdict="EXTRACT K285 — MIT, high-star, technique mature. Requires local Hopper + authorized scope. No clone this batch.")
    entity("background-agents", "background-agents — sandboxed background coding agents", "K285-c",
        "github.com/ColeMurray/background-agents",
        "**MIT, 3,345 stars.** An open-source **background agents** coding system: **sandboxed "
        "`spawn-child` delegation** plus **managed skills**. Already an Extract in K283 for GuruWatcher; "
        "recorded here for the **local lab**.\n\n"
        "**Play:** a **background binary-auditing agent** that runs in an isolated container without "
        "blocking the operator. **Constraint:** needs a container runtime (Modal / Daytona / Docker) and "
        "enforces a **single-tenant** organizational boundary — keep it inside the lab. Pairs the "
        "K421 containment line: delegation is only safe when the child is sandboxed and bounded.",
        ["concepts/agentic-containment-principles.md",
         "concepts/model-is-not-a-security-boundary-kubernetes-agents.md",
         "concepts/coding-agent-supply-chain-install-gap.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K285-c)",
        verdict="EXTRACT K285 — MIT, sandboxed delegation. Needs a container runtime; single-tenant only. No clone this batch.")

    # ---------- STCA + LipDA ----------------------------------------------
    source("arxiv-2610-08331-stca-av-vlm-adversarial-attack",
        "STCA: transferable spatial-temporal adversarial attack on autonomous-driving VLMs",
        "arXiv 2610.08331", "arXiv paper (routed from image-gen 2026-10-08)",
        "not held locally — routed brief only",
        "**A black-box transferable attack on vision-language models in a safety-critical perception "
        "stack.** The perturbation is visually mild — **SSIM falls only 0.93 → 0.82** — and beats PGD and "
        "FGSM baselines. Attack success rises sharply:\n\n"
        "| Target | BDD100K ASR | nuScenes ASR |\n|---|---|---|\n"
        "| Video-LLaVA | 32.6% → **71%** | 57.6% → 83% |\n"
        "| Qwen2.5-VL | 45% → **84.2%** | 64.7% → 96.5% |\n"
        "| Dolphin | 46.9% → 46.2% | 37.6% → 47.1% |\n\n"
        "**The most actionable defensive finding is in that last row:** the **domain-tuned Dolphin** "
        "model is markedly **more robust** than the general-purpose VLMs. Operator steal: **domain tuning "
        "bought adversarial robustness here; a general VLM in a safety-critical loop did not.** No "
        "GitHub, no repo, no weights, no dataset; uses public BDD100K and nuScenes; **no licence "
        "stated**. Authorized robustness lab only. **No perturbation recipes or attack code in wiki.**",
        ["concepts/vlm-perception-adversarial-robustness.md",
         "concepts/adversarial-region-estimation-vs-single-example.md"],
        read="read (routed brief)")
    source("arxiv-2610-08417-lipda-lipsync-forgery-attribution",
        "LipDA: lipsync forgery detection and source attribution",
        "arXiv 2610.08417", "arXiv paper (routed from image-gen 2026-10-08)",
        "not held locally — routed brief only",
        "**Exploit the biological coupling between lip motion and head pose** — a coupling lipsync "
        "generators break. Real mouths move pose-consistently; generated ones do not. Detection aligns a "
        "**lip-ROI ResNet encoder** with a **6-DoF head-pose landmark encoder** via margin contrastive "
        "loss; attribution adds audio-visual cross-attention plus a temporal CNN/Bi-LSTM over keypoints to "
        "capture per-generator fingerprints.\n\n"
        "**Detection AUC:** LipSync-A **99.42**, AVLips **99.82**, TalkHeadBench **97.50** — about 8 "
        "points over SpeechForensics. **Attribution: 97.5% accuracy / 93.9 F1**, over 12 points above "
        "TALL; generalises to unseen generators (Sonic 87.8, KDTalker 84.6, OmniSync 95.5) and Celeb-DF "
        "92.76. Ships **LipSync-A**: 15 generators, 7 architectures, 16,000 labelled forged videos. Code "
        "at `github.com/AnsonShe/LipDA` — **no licence stated**; ~270 samples come from commercial APIs, "
        "so **verify terms before use**.\n\n"
        "**Two caveats worth carrying.** Attribution leans on **generator leakage** — high numbers mean "
        "fingerprints are distinctive, not that forgeries are detectable in the wild; and the generator "
        "set is fixed, so the **84-95% generalisation figures are the honest bound.**",
        ["concepts/lipsync-forgery-detection-attribution.md",
         "concepts/armor-plusplus-agentic-deepfake-detector-attacks.md"],
        read="read (routed brief)")
    concept("vlm-perception-adversarial-robustness",
        "Adversarial robustness of VLM perception", "K-av1", "arXiv 2610.08331",
        "A vision-language model in a **safety-critical perception loop** is an adversarial target, and a "
        "**black-box transferable** perturbation does not have to look dramatic. On two autonomous-driving "
        "datasets the attack lifted ASR from **32.6% to 71%** (Video-LLaVA) and **45% to 84.2%** "
        "(Qwen2.5-VL) while **SSIM only fell 0.93 to 0.82** — a change a human reviewer would wave "
        "through.\n\n"
        "The actionable half is the failure to generalise in the other direction: a **domain-tuned** model "
        "(Dolphin) barely moved (46.9% → 46.2%), while the general VLMs collapsed. So **domain tuning "
        "bought adversarial robustness here** — worth weighing against the usual assumption that a bigger "
        "general model is the safer one. For any VLM sitting in a control or triage path, ask what it was "
        "tuned on and test transfer, not just accuracy. Pairs K403's region-estimation rule: measure the "
        "failure surface, not one example.",
        ["sources/arxiv-2610-08331-stca-av-vlm-adversarial-attack.md",
         "concepts/adversarial-region-estimation-vs-single-example.md",
         "concepts/llm-adversarial-fuzzing.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K-av1)")
    concept("lipsync-forgery-detection-attribution",
        "Lipsync forgery detection and attribution", "K-av2", "arXiv 2610.08417",
        "Lipsync generators break a coupling real faces keep: **the mouth moves in a way the head pose "
        "predicts.** Aligning a lip encoder against a **6-DoF head-pose encoder** turns that broken "
        "coupling into a detector — **AUC 99.42 / 99.82 / 97.50** across three benchmarks, roughly 8 "
        "points over the prior method — and per-generator fingerprints push **attribution to 97.5% / "
        "93.9 F1**.\n\n"
        "Read those numbers honestly. **Attribution measures generator leakage, not field detectability** "
        "— the fingerprints are distinctive because the generators are stylistically distinct. And the "
        "generator set is fixed, so on a generator it has never seen, accuracy falls to **84-95%**; that "
        "is the bound to quote, not 97.5%. Pairs the K413 image-generator red-team benchmark and the "
        "deepfake-detector-attack line.",
        ["sources/arxiv-2610-08417-lipda-lipsync-forgery-attribution.md",
         "concepts/armor-plusplus-agentic-deepfake-detector-attacks.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K-av2)",
        tags="deepfake-detection")

    # ---------- backlinks --------------------------------------------------
    for rel, ref, note in (
        ("concepts/local-abliterated-llm-pentest-stack.md", "entities/tools/strata.md",
         "K284 Strata: local 125B MoE with a localhost API"),
        ("concepts/local-abliterated-llm-pentest-stack.md", "entities/tools/rea.md",
         "K285-b agent-first RE toolkit + MCP"),
        ("concepts/llm-vulnerability-discovery.md", "entities/tools/rea.md",
         "K285-b MCP-mediated decompilation for binary analysis"),
        ("concepts/agentic-containment-principles.md", "entities/tools/background-agents.md",
         "K285-c sandboxed spawn-child delegation"),
        ("concepts/model-is-not-a-security-boundary-kubernetes-agents.md", "entities/tools/background-agents.md",
         "K285-c delegation is safe only when the child is sandboxed"),
        ("concepts/coding-agent-supply-chain-install-gap.md", "entities/tools/background-agents.md",
         "K285-c managed skills + spawn-child delegation"),
        ("concepts/reliable-inference-procurement-routing.md", "entities/tools/strata.md",
         "K284 local inference removes per-token cost on private lanes"),
        ("concepts/threat-preserving-representation-sensitivity.md",
         "concepts/local-suppression-vs-repair.md",
         "K285-a a change visible only in a neighbourhood"),
        ("concepts/speculative-decoding-safety-asymmetry.md",
         "concepts/local-suppression-vs-repair.md",
         "K285-a aggregate metrics hide local regressions"),
        ("concepts/speculative-decoding-safety-asymmetry.md",
         "sources/arxiv-2610-10276-patchbench-local-suppression-vs-repair.md",
         "K285-a MMLU flat while BNPS -26.3"),
        ("concepts/speculative-decoding-safety-asymmetry.md",
         "sources/arxiv-2610-10345-sldr-signed-layer-safety-repair.md",
         "K285-a signed layer sensitivity, narrow repair"),
        ("concepts/armor-plusplus-agentic-deepfake-detector-attacks.md",
         "concepts/lipsync-forgery-detection-attribution.md",
         "K-av2 lip-pose coupling detector"),
        ("concepts/armor-plusplus-agentic-deepfake-detector-attacks.md",
         "sources/arxiv-2610-08417-lipda-lipsync-forgery-attribution.md",
         "K-av2 LipDA detection + attribution"),
    ):
        add_related(rel, ref, note)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
