#!/usr/bin/env python3
"""Writer for K398-K402 ingest (2026-10-06). No attack payloads in wiki.

Slugs are passed WITHOUT a .md extension: concept_page()/src() append it.
"""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-10-06"


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
    if f"  - {ref}" not in t:
        t = t.replace("related:\n", f"related:\n  - {ref}\n", 1)
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n- @{ref} — {note}\n", 1)
    t = bump_updated(t)
    p.write_text(t, encoding="utf-8")
    print("patched", rel, "→", ref)


def src(slug, title, arxiv, kid, pdf, narrative, concept, extra=None, ood=False, wire=""):
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra or [])]
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
    # ---------------- K398 Penumbra ---------------------------------------
    src("arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search",
        "Penumbra: sample-efficient adversarial search for regulatory obligations",
        "2610.04693", "K398",
        "arxiv-2610.04693-penumbra-sample-efficient-adversarial-search-for.pdf",
        "**K398** — agents now sit under **binding professional obligations** (portfolio analysis, clinical "
        "triage) that a violation leaves **no lexical signature** for: whether an omission is material "
        "depends on what the response *left out*. Probing that boundary is expensive — every probe costs a "
        "generation plus two adjudications — so the binding constraint is **sample efficiency, not volume**. "
        "PENUMBRA walks from a **verified anchor** under an **expanding edit budget**, scoring each edit with "
        "a **three-level committee** (clear / guarded / borderline); it keeps widening while the verdict "
        "class is unchanged, so **minimality is enforced rather than filtered for** — the first class change "
        "*is* the boundary. It then emits the **adjacent pair** straddling that change: one compliant and one "
        "violating response differing by a handful of words. Coverage is the **defeat surface** — distinct "
        "(obligation × defeat mode) cells carrying a certified pair. Numbers: adaptive allocation reaches "
        "uniform allocation's **full-budget coverage on 59% of candidates**; at equal records it covers "
        "**1.43×** the defeat modes of naive enumeration; on a financial-advisory constitution it returns "
        "**144 pairs over 60 obligations** and a clinical-triage constitution **49 pairs over 18**. The "
        "committee is **frozen** (adapting either side does not repair drift). Operator steal: an obligation "
        "boundary is best tested with **adjacent pairs**, not a single judged response — and it is the pair "
        "that shows where the obligation's own terms stop deciding. Pairs K396 (representation sensitivity) "
        "and K321 (construct validity). **No policy text or probe payloads in wiki.**",
        "concepts/compliance-boundary-adjacent-pair-search.md",
        ["concepts/threat-preserving-representation-sensitivity.md",
         "concepts/guardrail-construct-validity-agent-eval.md",
         "concepts/responsible-disclosure.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K398)")
    concept_page("compliance-boundary-adjacent-pair-search",
        "Compliance boundary testing by adjacent pairs", "K398", "2610.04693",
        "A regulatory obligation is decided by **what a response omits**, so it leaves no keyword to grep "
        "for. Test it by walking from a verified-compliant anchor under a growing edit budget and stopping "
        "at the **first verdict change** — that gives two adjacent responses straddling the boundary, "
        "differing by a few words. Minimality is then a property of the search, not a filter applied after "
        "it. Score coverage as **distinct (obligation × defeat mode) cells** holding a certified pair, not "
        "as a count of probes. Freeze the judging committee: if it adapts with the search, the boundary "
        "moves with it. Complements K396 — both replace a single judged score with a controlled comparison.",
        ["sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md",
         "concepts/threat-preserving-representation-sensitivity.md",
         "concepts/guardrail-construct-validity-agent-eval.md",
         "concepts/responsible-disclosure.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K398)")

    # ---------------- K399 Red-TTT ----------------------------------------
    src("arxiv-2610-05282-red-ttt-test-time-training-jailbreak",
        "Red-TTT: test-time training for automated jailbreaking",
        "2610.05282", "K399",
        "arxiv-2610.05282-red-ttt-test-time-training-for-automated-jailbre.pdf",
        "**K399** — automated red-teaming either draws more samples at test time (search, rewriting, tree "
        "expansion) or trains a stronger attacker offline with RL. Both share one limit: **once an attack on "
        "a specific behaviour begins, the attacker's weights are frozen**, so anything learned about that "
        "behaviour stays in context instead of the model. Red-TTT updates the **attacker at test time** on "
        "the behaviour in front of it, and adapts the training objective to red-teaming — where success is "
        "judged by the **single best sample, not the average**. It needs only sampling access to the victim "
        "and drops into existing pipelines unchanged. HarmBench, four victim models: ASR **72.4%** vs "
        "**55.9%** for a budget-matched Best-of-N at 120 samples, improving in **every** configuration and "
        "gaining **+9.0 to +23.0** over frozen controls; on HarmBench standard-200 against Llama-3-8B it "
        "reaches **77.0%** against CodeChameleon **44.5%**, X-Teaming **21.5%**, AutoDAN-Turbo **27.0%**. "
        "Repo `github.com/SaFo-Lab/Red-TTT`. Operator steal: a **fixed-policy** attacker is a ceiling, and "
        "the right objective for red-teaming is best-of-N, not mean quality. Lab only; owned or procured "
        "models. **No jailbreak prompts or attack code in wiki.**",
        "concepts/test-time-training-redteam-attacker.md",
        ["concepts/llm-adversarial-fuzzing.md",
         "concepts/crescendo-multi-turn-jailbreak.md",
         "concepts/piminer-agentic-prompt-injection-redteam.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K399)")
    concept_page("test-time-training-redteam-attacker",
        "Test-time training for a red-team attacker", "K399", "2610.05282",
        "A red-team attacker with frozen weights cannot accumulate anything about the behaviour it is "
        "attacking — every signal stays in the prompt. Letting it **train at test time** on the current "
        "behaviour beats a budget-matched search baseline (**72.4% vs 55.9%** ASR at 120 samples), needs "
        "only sampling access to the victim, and needs no pipeline change. The second, quieter steal is the "
        "**objective**: red-teaming success is the *single best* sample, not the average, so a training "
        "objective borrowed from alignment work is the wrong shape. Authorised lab only, owned or procured "
        "models; no attack code or jailbreak bodies in the wiki.",
        ["sources/arxiv-2610-05282-red-ttt-test-time-training-jailbreak.md",
         "concepts/llm-adversarial-fuzzing.md",
         "concepts/crescendo-multi-turn-jailbreak.md",
         "concepts/piminer-agentic-prompt-injection-redteam.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K399)")

    # ---------------- K400 Mosaic attacks ---------------------------------
    src("arxiv-2610-05346-mosaic-attacks-sequential-fragment-defense",
        "Reflections and fragments: securing LLMs against sequential mosaic attacks",
        "2610.05346", "K400",
        "arxiv-2610.05346-reflections-and-fragments-securing-llms-against.pdf",
        "**K400 — the strongest theory result of the batch.** A **mosaic attack** is a multi-turn sequence "
        "whose individual fragments are innocuous in isolation and assemble into a harmful payload. The "
        "paper formalises mosaic defence as a finite extensive-form game with imperfect information and "
        "proves the result that matters operationally: **no fixed bounded window of recent prompts is "
        "sufficient in general** — safety-relevant information may sit arbitrarily far back. It then "
        "introduces a **watchman**, an online state mechanism carrying that information forward, and shows "
        "that under explicit assumptions it gives **zero-failure defence with positive benign helpfulness**, "
        "and under stronger conditions is optimal among zero-failure defenders. The cost is priced too: an "
        "exact watchman can need **exponentially many states**, and exact maliciousness detection "
        "**exponentially many queries** in an unstructured black-box model — though the construction behind "
        "the state bound is *efficiently learnable from labelled examples*, while certifying worst-case "
        "safety needs far more under restricted access. Also: **self-play equilibrium alone does not "
        "certify usefulness**, motivating a constrained formulation that maximises worst-case benign "
        "helpfulness among zero-failure defenders. Empirically, role-specific attacker/defender **LoRA "
        "adapters** over frozen LLMs trained by multi-turn self-play strengthen **both** roles, including "
        "against unseen objectives. Operator steal: **a bounded-window or per-turn session guard is not a "
        "defence** — this is the formal companion to K312's non-decaying loop state. Pairs K312, Crescendo, "
        "AMT-X. **No attack fragments or payloads in wiki.**",
        "concepts/mosaic-attack-bounded-window-insufficiency.md",
        ["concepts/non-decaying-loop-safety-state.md",
         "concepts/crescendo-multi-turn-jailbreak.md",
         "concepts/amt-x-phase-structured-multi-turn-red-teaming.md",
         "concepts/linguistic-illegibility-llm-security.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K400)")
    concept_page("mosaic-attack-bounded-window-insufficiency",
        "Mosaic attacks defeat bounded-window defenses", "K400", "2610.05346",
        "The operator rule: **a defence that looks at only the last N turns is not a defence.** For mosaic "
        "attacks — each fragment benign alone, harmful assembled — the paper proves no fixed bounded window "
        "suffices, because the safety-relevant fragment can be arbitrarily far back. What is required is an "
        "**online state mechanism** (a watchman) that carries the distinction forward. Price it honestly: an "
        "exact watchman can need exponentially many states, and detecting completeness can need "
        "exponentially many black-box queries — but that construction is learnable from labelled examples, "
        "so a learned watchman is the practical route. Do not treat **self-play equilibrium** as proof of "
        "usefulness; it says nothing about worst-case benign helpfulness. This is the theory under K312's "
        "non-decaying loop state.",
        ["sources/arxiv-2610-05346-mosaic-attacks-sequential-fragment-defense.md",
         "concepts/non-decaying-loop-safety-state.md",
         "concepts/crescendo-multi-turn-jailbreak.md",
         "concepts/amt-x-phase-structured-multi-turn-red-teaming.md",
         "concepts/linguistic-illegibility-llm-security.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K400)")

    # ---------------- K401 Contextual Reader (OOD) ------------------------
    src("arxiv-2610-06844-contextual-reader-diffusion-transformers-ood",
        "Learning to read the contextual tokens in diffusion transformers (OOD)",
        "2610.06844", "K401",
        "arxiv-2610.06844-learning-to-read-the-contextual-tokens-in-diffus.pdf",
        "**K401 — OOD for security.** A framework for reading **contextual tokens** in Multimodal Diffusion "
        "Transformers: a lightweight bottleneck network maps intermediate contextual tokens to "
        "interpretations, showing they carry a global representation of the emerging scene — "
        "generation-specific semantics appear surprisingly early in denoising, with fine detail becoming "
        "readable over time, and the information stays decodable even with an **empty prompt**. Readings "
        "that are more legible correlate with higher human-preference scores, and a **Contextual Alignment** "
        "training technique reinforces that information to improve quality and coverage. **Security "
        "relevance: none** — it is generation interpretability and a training technique, with no attacker, "
        "defender, or protected asset. Routed to **image-gen**; cyber keeps this stub.",
        "", ood=True,
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)")

    # ---------------- K402 TransScope -------------------------------------
    src("arxiv-2610-06848-transcope-hardware-membership-inference",
        "TransScope: what the software hides about LLM training data, the hardware reveals at scale",
        "2610.06848", "K402",
        "arxiv-2610.06848-transcope-what-the-software-hides-about-llm-trai.pdf",
        "**K402 — a privacy result that removes an assumption people rely on.** Membership is the root "
        "privacy primitive, and prior work found no hardware-based out-of-distribution detection against "
        "**constant-time, static** black-box models with masked confidence. This is the first **cycle-level** "
        "examination of how LLMs and ViTs interact with microarchitecture, including integrated accelerators, "
        "and the answer is that **training data does change the execution footprint** even with no "
        "input-dependent branch, no dynamic optimisation, and no early exit. The mechanism is specific and "
        "worth carrying: **tokenisation performed during training alters the locality of vocabulary-token "
        "fetches at inference**, which changes page-table access patterns and **TLB** behaviour in a "
        "data-dependent way, so microarchitectural state varies with whether the input was in-distribution. "
        "TLBs and on-core accelerators are the components that reveal or amplify it. Numbers: **AUC 0.9** "
        "against a best-previously-reported **0.6** (PETAL), and OOD-detection accuracy **98%** at **1.5% "
        "FPR**. Operator steal: **constant-time software does not imply a constant hardware footprint** — "
        "when you argue that a model reveals nothing about its training data, the argument has to cover the "
        "memory system, not just the code path. Pairs the privacy-exposure thread (K347). **No attack "
        "tooling in wiki.**",
        "concepts/hardware-membership-inference-microarchitecture.md",
        ["concepts/asleval-privacy-exposure-displacement.md",
         "concepts/hardware-id-masking-opsec.md",
         "concepts/tpm-attest-linux-integrity-attestation.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K402)")
    concept_page("hardware-membership-inference-microarchitecture",
        "Hardware membership inference through microarchitecture", "K402", "2610.06848",
        "\"The model is constant-time and returns masked confidence, so it leaks nothing\" is a **software** "
        "claim. This work shows the **hardware** still leaks: tokenisation performed at training time shifts "
        "the locality of vocabulary fetches at inference, which perturbs page-table access and the **TLB** in "
        "a way that depends on whether the input was in the training distribution. Reported at **0.9 AUC** "
        "and **98% accuracy at 1.5% FPR**, against 0.6 AUC for the best previously reported method. The "
        "operator consequence: a privacy or anti-extraction argument must cover the **memory system and any "
        "on-core accelerators**, not only the code path — and that surface is visible to a co-tenant or a "
        "host measuring cycles. Pairs the K347 privacy-exposure-displacement thread.",
        ["sources/arxiv-2610-06848-transcope-hardware-membership-inference.md",
         "concepts/asleval-privacy-exposure-displacement.md",
         "concepts/hardware-id-masking-opsec.md",
         "concepts/tpm-attest-linux-integrity-attestation.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K402)")

    # ---------------- backlinks -------------------------------------------
    for concept_ref, new_ref, note in (
        ("concepts/non-decaying-loop-safety-state.md", "concepts/mosaic-attack-bounded-window-insufficiency.md",
         "K400 formal companion: no fixed bounded window suffices"),
        ("concepts/crescendo-multi-turn-jailbreak.md", "concepts/mosaic-attack-bounded-window-insufficiency.md",
         "K400 mosaic attacks: fragments benign alone, harmful assembled"),
        ("concepts/amt-x-phase-structured-multi-turn-red-teaming.md", "concepts/mosaic-attack-bounded-window-insufficiency.md",
         "K400 bounded-window insufficiency"),
        ("concepts/llm-adversarial-fuzzing.md", "concepts/test-time-training-redteam-attacker.md",
         "K399 test-time training for the attacker"),
        ("concepts/piminer-agentic-prompt-injection-redteam.md", "concepts/test-time-training-redteam-attacker.md",
         "K399 attacker weights are not frozen at test time"),
        ("concepts/guardrail-construct-validity-agent-eval.md", "concepts/compliance-boundary-adjacent-pair-search.md",
         "K398 adjacent-pair compliance boundary testing"),
        ("concepts/threat-preserving-representation-sensitivity.md", "concepts/compliance-boundary-adjacent-pair-search.md",
         "K398 replace one judged score with a controlled pair"),
        ("concepts/asleval-privacy-exposure-displacement.md", "concepts/hardware-membership-inference-microarchitecture.md",
         "K402 hardware membership inference defeats constant-time software"),
    ):
        add_related(concept_ref, new_ref, note)

    for source_ref, concept_refs in {
        "sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md": (
            "concepts/threat-preserving-representation-sensitivity.md",
            "concepts/guardrail-construct-validity-agent-eval.md", "concepts/responsible-disclosure.md"),
        "sources/arxiv-2610-05282-red-ttt-test-time-training-jailbreak.md": (
            "concepts/llm-adversarial-fuzzing.md", "concepts/crescendo-multi-turn-jailbreak.md",
            "concepts/piminer-agentic-prompt-injection-redteam.md"),
        "sources/arxiv-2610-05346-mosaic-attacks-sequential-fragment-defense.md": (
            "concepts/non-decaying-loop-safety-state.md", "concepts/crescendo-multi-turn-jailbreak.md",
            "concepts/amt-x-phase-structured-multi-turn-red-teaming.md",
            "concepts/linguistic-illegibility-llm-security.md"),
        "sources/arxiv-2610-06848-transcope-hardware-membership-inference.md": (
            "concepts/asleval-privacy-exposure-displacement.md", "concepts/hardware-id-masking-opsec.md",
            "concepts/tpm-attest-linux-integrity-attestation.md"),
    }.items():
        for cr in concept_refs:
            add_related(cr, source_ref, "K398-K402 ingest source page")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
