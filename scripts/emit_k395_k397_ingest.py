#!/usr/bin/env python3
"""Writer for K395-K397 ingest (2026-10-06). No attack payloads in wiki."""
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
    print("patched related", rel, "→", ref)


def src(slug, title, arxiv, kid, pdf, narrative, concept, extra=None, wire=""):
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra or [])]
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else "\n## Relations\n\n"
    if extra:
        rel_sec += "".join(f"- @{r}\n" for r in extra)
    wire_line = wire or f".cursor/rules/cemini-cybersec-agent-audit.mdc ({kid})"
    body = f"""---
title: "{title}"
type: source
tags: [source, arxiv, agent-security]
keywords: [{arxiv}, {kid.lower()}]
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
    # ---------------- K395: authorship attribution ------------------------
    src(
        "arxiv-2610-03531-authorship-attribution-zero-shot-representations",
        "Author representation strategies for zero-shot authorship attribution",
        "2610.03531",
        "K395",
        "arxiv-2610.03531-author-representation-strategies-for-zero-shot-a.pdf",
        "**K395** — authorship attribution (stylometry) asks who wrote a text, from style alone. In the "
        "**zero-shot** setting — no task-specific training, just candidate labels — it largely fails: a "
        "label-only prompt scores at chance and **degrades as candidates grow** (df3 30.0/43.3/30.0% for "
        "Mixtral/Gemma/Qwen, down to df15 **3.3/8.0/7.3%**). The paper's finding is that what matters is the "
        "**author representation**, not the prompt: representative writing samples reach **43.3%**, "
        "LLM-generated style descriptions **33.3%** (much more compact), and a **two-stage LISA style-embedding** "
        "framework **56.6%** (candidate-space reduction k=2 + embedding-dimension selection N=35, P+A) "
        "against a 36.6% single-stage baseline. Two operator steasl: **model choice dominates prompt "
        "choice** (max prompt spread 16.6 pp vs max model spread 36.6 pp), and LLMs show **selection bias** "
        "— with 15 candidates, predictions collapse onto a few authors while others get almost none. "
        "Attribution framing only: useful for OSINT / threat-actor writing attribution, and for knowing "
        "when a stylometric claim is not supportable. No repo. **No de-anonymisation recipes in wiki.**",
        "concepts/authorship-attribution-author-representation.md",
        ["concepts/osint-for-cybersecurity.md", "concepts/threat-hunting.md",
         "concepts/linguistic-illegibility-llm-security.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K395)",
    )
    concept_page(
        "authorship-attribution-author-representation",
        "Authorship attribution needs an author representation",
        "K395",
        "2610.03531",
        "Asking an LLM 'who wrote this, from these names?' is near-chance and gets worse as the candidate "
        "list grows. What moves the number is the **representation of each candidate author**: writing "
        "samples, an LLM-written style description, or a style embedding. Style embeddings with a "
        "**two-stage** reduce-then-select step scored best (56.6%). Carry two cautions: **model choice "
        "matters more than prompt wording** (36.6 pp vs 16.6 pp spread), and models concentrate "
        "predictions on a few candidates as the task hardens — a confident label from a flat-looking "
        "distribution can still be selection bias, not evidence. Use for OSINT attribution support, not "
        "as a forensic conclusion.",
        [
            "sources/arxiv-2610-03531-authorship-attribution-zero-shot-representations.md",
            "concepts/osint-for-cybersecurity.md",
            "concepts/threat-hunting.md",
            "concepts/linguistic-illegibility-llm-security.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K395)",
    )

    # ---------------- K396: TPRS ------------------------------------------
    src(
        "arxiv-2610-03585-threat-preserving-representation-sensitivity",
        "Threat-preserving representation sensitivity in agent-security benchmarks",
        "2610.03585",
        "K396",
        "arxiv-2610.03585-threat-preserving-representation-sensitivity-in.pdf",
        "**K396 — the strongest finding of the batch.** An agent-security ASR is routinely read as a "
        "property of the agent. It is not: it is a property of the **agent plus the agent-visible "
        "representation**. **Threat-preserving representation sensitivity (TPRS)** holds the task, harmful "
        "action, policy, ground truth, environment, and evaluation criteria fixed and changes only how the "
        "threat is *presented*: **ΔT(B,m) = ASR(T(B),m) − ASR(B,m)**. Across **28,904 agent runs** on three "
        "benchmarks the score moves in both directions. On **ASB**, renaming attacker tools to "
        "threat-**neutral** names **raises** committed ASR by **11.67 pp** (36.67%→48.34%) on GPT-5-mini and "
        "**13.21 pp** (20.85%→34.06%) on Haiku 4.5. On **MCPTox**, introducing threat-related names "
        "**lowers** ASR by **11.00 pp** / **4.11 pp**. On AgentDojo the effect is near zero. The shift is "
        "**not explainable by threat vocabulary alone** — a neutral name matched on token count, length, "
        "and casing reproduced **8.54 of 11.00** points. The sharpest reading: when the **attacker** picks "
        "the tool name (as on ASB), the benchmark's own naming choice is an unintentional defence, and the "
        "reported ASR **understates** what the attacker can get by 11.67–13.21 pp. Operator steal: **stop "
        "treating one ASR as a robustness certificate** — report sensitivity across a controlled set of "
        "threat-preserving representations, state when an attack counts as success, and measure benign "
        "utility under the same transformations. Pairs K388 (breaking level) and K321 (construct validity). "
        "**No attack payloads in wiki.**",
        "concepts/threat-preserving-representation-sensitivity.md",
        ["concepts/guardrail-construct-validity-agent-eval.md",
         "concepts/benchmark-shortcut-attack-pyramid-audit.md",
         "concepts/faithful-agent-asr-measurement.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K396)",
    )
    concept_page(
        "threat-preserving-representation-sensitivity",
        "Threat-preserving representation sensitivity (TPRS)",
        "K396",
        "2610.03585",
        "Before quoting an ASR, ask what it is a property *of*. **TPRS** changes only the agent-visible "
        "representation of a threat — tool names, descriptions — while the task, harmful action, policy, "
        "ground truth, environment, and criteria stay fixed, and measures how far the score moves. It moved "
        "**11.67–13.21 pp** on ASB and **11.00 pp** on MCPTox across 28,904 runs; on ASB the movement is "
        "**upward**, because the original threat-flavoured names were acting as a defence the benchmark did "
        "not intend. Practical rules: **report sensitivity, not a single number**; say explicitly when an "
        "attack counts as success (native vs committed ASR differ in both value and sensitivity); and "
        "measure **utility** under the same transformations, since representation can move that too. Pairs "
        "the K388 breaking-level rule — both ask whether a score certifies the capability it claims.",
        [
            "sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md",
            "concepts/guardrail-construct-validity-agent-eval.md",
            "concepts/benchmark-shortcut-attack-pyramid-audit.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K396)",
    )

    # ---------------- K397: FrugalEvo -------------------------------------
    src(
        "arxiv-2610-03675-frugalevo-cost-aware-program-evolution",
        "FrugalEvo: towards cost-aware LLM-guided program evolution",
        "2610.03675",
        "K397",
        "arxiv-2610.03675-frugalevo-towards-cost-aware-llm-guided-program.pdf",
        "**K397** — LLM-guided evolutionary search (AlphaEvolve-style) is usually scored as gain per "
        "*iteration*. This argues for **gain per unit cost** instead, and introduces **BA-AUC** (Budget-Aware "
        "Area Under the Curve): the area under the best-so-far score curve plotted against **cumulative LLM "
        "cost**, up to a budget. The framework splits the loop — a **strong, expensive LLM explores** "
        "strategies while a **cheap LLM implements and refines** the code — and the harness and prompts are "
        "built to **maximise prefix sharing** across evolution steps for cache reuse. Over 10 math and "
        "systems optimisation tasks it matches or beats OpenEvolve / ShinkaEvolve / AdaEvolve / EvoX on "
        "final quality and BA-AUC, at **$1.68** (Terra + Luna) and **$0.55** (GLM-5.3 + Flash) against "
        "roughly **$50** for multi-agent baselines (CORAL, SwarmResearch). Operator steal: **budget the "
        "loop, not the iteration count**, and split strategist from implementer. Tangential to security — "
        "it is a harness-cost pattern, useful for the wiki's cost thread (K376 FragToken, K366 inference "
        "procurement), not a security technique. Repo `github.com/chchenhui/frugalevo` **Apache-2.0** but "
        "**305 MB** — REFERENCE, no clone.",
        "concepts/budget-aware-agentic-search-cost.md",
        ["concepts/fragtoken-inference-cost-amplification-lab.md",
         "concepts/reliable-inference-procurement-routing.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K397)",
    )
    concept_page(
        "budget-aware-agentic-search-cost",
        "Budget-aware agentic search cost",
        "K397",
        "2610.03675",
        "Score an agentic search loop by **gain per unit cost**, not gain per iteration. **BA-AUC** is the "
        "area under the best-so-far score curve against cumulative model spend, so a method that is slower "
        "but cheaper can win. Two design moves travel: **split the roles** — an expensive model proposes "
        "strategies, a cheap one implements them — and **shape the harness for cache reuse**, maximising "
        "shared prefixes across steps. Reported at **$0.55–$1.68** against ~**$50** for multi-agent "
        "baselines. Applies to budgeted red-team or evolve loops: cap the spend, then compare. Pairs the "
        "inference-cost threads at K376 / K366.",
        [
            "sources/arxiv-2610-03675-frugalevo-cost-aware-program-evolution.md",
            "concepts/fragtoken-inference-cost-amplification-lab.md",
            "concepts/reliable-inference-procurement-routing.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K397)",
    )

    # ---------------- backlinks into existing pages -----------------------
    for concept_ref, new_ref, note in (
        ("concepts/guardrail-construct-validity-agent-eval.md", "concepts/threat-preserving-representation-sensitivity.md",
         "K396 TPRS — representation moves the score while the security problem is fixed"),
        ("concepts/benchmark-shortcut-attack-pyramid-audit.md", "concepts/threat-preserving-representation-sensitivity.md",
         "K396 TPRS — the sibling rule: report sensitivity, not a single score"),
        ("concepts/faithful-agent-asr-measurement.md", "concepts/threat-preserving-representation-sensitivity.md",
         "K396 TPRS — ASR is a property of agent + representation"),
        ("concepts/fragtoken-inference-cost-amplification-lab.md", "concepts/budget-aware-agentic-search-cost.md",
         "K397 BA-AUC — budget the loop, not the iteration"),
        ("concepts/reliable-inference-procurement-routing.md", "concepts/budget-aware-agentic-search-cost.md",
         "K397 cost-aware agentic search"),
        ("concepts/osint-for-cybersecurity.md", "concepts/authorship-attribution-author-representation.md",
         "K395 authorship attribution needs an author representation"),
        ("concepts/threat-hunting.md", "concepts/authorship-attribution-author-representation.md",
         "K395 stylometric attribution support"),
    ):
        add_related(concept_ref, new_ref, note)

    for source_ref, concept_refs in {
        "sources/arxiv-2610-03531-authorship-attribution-zero-shot-representations.md": (
            "concepts/osint-for-cybersecurity.md", "concepts/threat-hunting.md",
            "concepts/linguistic-illegibility-llm-security.md"),
        "sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md": (
            "concepts/guardrail-construct-validity-agent-eval.md",
            "concepts/benchmark-shortcut-attack-pyramid-audit.md",
            "concepts/faithful-agent-asr-measurement.md"),
        "sources/arxiv-2610-03675-frugalevo-cost-aware-program-evolution.md": (
            "concepts/fragtoken-inference-cost-amplification-lab.md",
            "concepts/reliable-inference-procurement-routing.md"),
    }.items():
        for cr in concept_refs:
            add_related(cr, source_ref, "K395-K397 ingest source page")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
