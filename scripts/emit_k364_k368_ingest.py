#!/usr/bin/env python3
"""Writer for K364–K368 ingest (2026-09-24)."""
from __future__ import annotations

from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


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
) -> None:
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra_related or [])]
    rel_yaml = "\n".join(rels) if rels else "related: []"
    if rels:
        rel_yaml = "related:\n" + "\n".join(rels)
    rel_sec = ""
    if concept:
        rel_sec = f"\n## Relations\n\n- @{concept}\n"
    body = f"""---
title: "{title}"
type: source
tags: [source, {"ood" if ood else "arxiv, agent-security"}]
keywords: [{arxiv}, {kid.lower()}]
{rel_yaml}
maturity: draft
read_status: read
created: 2026-09-24
updated: 2026-09-24
phase_0_verdict: "REFERENCE 2026-09-24 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc ({kid})"
---
{rel_sec}
## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| arXiv | {arxiv} |
| Location | {EGRESS}/{pdf} |
| Retrieved | 2026-09-24 |
| Read status | read (abstract + triage) |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved 2026-09-24)]
"""
    w(f"sources/{slug}.md", body)


def concept(
    slug: str,
    title: str,
    kid: str,
    arxiv: str,
    source: str,
    narrative: str,
    related: list[str],
    wire: str,
) -> None:
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
created: 2026-09-24
updated: 2026-09-24
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

> Triage from arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved 2026-09-24)]
"""
    w(f"concepts/{slug}.md", body)


def main() -> int:
    src(
        "arxiv-2609-25294-controller-only-false-confirmation-rf-uav",
        "Controller-only false confirmation in passive RF UAV link detection",
        "2609.25294",
        "K364",
        "arxiv-2609.25294-controller-only-false-confirmation-in-passive-rf.pdf",
        "**K364** — passive RF counter-UAV classifiers can **false-confirm** a **controller-only** state (no linked aircraft) as if a full link were present. Steal: separate **ambient / controller-only / linked** eval cells; do not report accuracy against Wi-Fi clutter alone. **Authorized RF lab / owned spectrum only.**",
        "concepts/passive-rf-uav-controller-only-false-confirmation.md",
        ["concepts/through-wall-detection-sdr-pca.md"],
    )
    concept(
        "passive-rf-uav-controller-only-false-confirmation",
        "Passive RF UAV controller-only false confirmation",
        "K364",
        "2609.25294",
        "sources/arxiv-2609-25294-controller-only-false-confirmation-rf-uav.md",
        "Counter-UAV RF sensing must treat **controller-only emissions** as a distinct state — high background accuracy can hide **linked-vs-controller-only** confusion. Dual-band SDR measurement methodology steal for **owned-lab** detector eval; not unauthorized spectrum operations.",
        [
            "sources/arxiv-2609-25294-controller-only-false-confirmation-rf-uav.md",
            "concepts/through-wall-detection-sdr-pca.md",
            "concepts/wifi-har-privacy-perturbation-graw.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K364)",
    )

    src(
        "arxiv-2609-26079-ble-mac-randomization-reidentification",
        "Learning to Link — BLE re-identification under MAC randomization",
        "2609.26079",
        "K365",
        "arxiv-2609.26079-learning-to-link-automatic-re-identification-of.pdf",
        "**K365** — BLE **RPA/MAC randomization** does not eliminate re-identification from advertising metadata and structure; learned linkers beat hand rules. **Authorized wireless lab on owned devices only** — pairs Bluetooth NFT / pairing≠authorization (K305). **Runtime:** `scripts/k365_ble_reid_lab_precheck.py`.",
        "concepts/ble-mac-randomization-reidentification-lab.md",
        ["concepts/cross-lingual-safety-transfer-lrl.md"],
    )
    concept(
        "ble-mac-randomization-reidentification-lab",
        "BLE MAC randomization re-identification (lab)",
        "K365",
        "2609.26079",
        "sources/arxiv-2609-26079-ble-mac-randomization-reidentification.md",
        "Privacy advertising features still leak **stable linkability** under randomization. Defensive steal: test **service authorization** after pairing, not radio anonymity alone. Offensive eval framing is **owned-device lab only**; no LIVE third-party tracking.",
        [
            "sources/arxiv-2609-26079-ble-mac-randomization-reidentification.md",
            "concepts/wifi-rf-fingerprinting-open-set.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K365)",
    )

    src(
        "arxiv-2609-28322-learning-cost-reliable-inference",
        "Learning the cost of reliable inference",
        "2609.28322",
        "K366",
        "arxiv-2609.28322-learning-the-cost-of-reliable-inference.pdf",
        "**K366** — procurement/routing platforms can price **guaranteed quality tiers** via competitive provider routing instead of flat per-token pricing. Audit steal for **eval marketplaces and model routers**: report quality floor + cost jointly (pairs K354 certified availability). REFERENCE.",
        "concepts/reliable-inference-procurement-routing.md",
        ["concepts/certified-selective-prediction-guardrails.md"],
    )
    concept(
        "reliable-inference-procurement-routing",
        "Reliable inference procurement and routing",
        "K366",
        "2609.28322",
        "sources/arxiv-2609-28322-learning-cost-reliable-inference.md",
        "Fixed token pricing hides **quality–cost tradeoffs**. Platform routing with **competitive procurement** makes reliability a priced dimension — relevant when agents fan out to multiple model backends. Not a security boundary alone; pair measurement integrity (K277).",
        [
            "sources/arxiv-2609-28322-learning-cost-reliable-inference.md",
            "concepts/certified-selective-prediction-guardrails.md",
            "concepts/chain-of-self-questioning-selective-abstention.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K366)",
    )

    src(
        "arxiv-2609-28372-agentic-ai-surrogate-consumer-ood",
        "Shopping by algorithm — agentic AI as surrogate consumer (OOD)",
        "2609.28372",
        "OOD",
        "arxiv-2609.28372-shopping-by-algorithm-how-agentic-ai-deploys-hum.pdf",
        "Tool-Lab study of LLM **surrogate shoppers** and pricing heuristics — **marketing / consumer research**, not cyber-primary. **OOD stub**; route to SEO or gambling wiki if productized.",
        "",
        ood=True,
    )

    src(
        "arxiv-2609-28395-translation-finetune-forgetting-mt-instruction",
        "Fine-tuning LLMs for translation — general forgetting vs MT instruction",
        "2609.28395",
        "K368",
        "arxiv-2609.28395-fine-tuning-llms-for-translation-general-forgett.pdf",
        "**K368** — **general forgetting mitigation** metrics on broad benchmarks do **not** guarantee preservation of **MT-specific instruction following** after parallel-data fine-tune. Steal: any domain fine-tune is a **safety/capability event** — re-run task-specific eval (pairs K304 RIM). REFERENCE.",
        "concepts/translation-finetune-forgetting-mt-instruction-audit.md",
        ["concepts/cross-lingual-safety-transfer-lrl.md"],
    )
    concept(
        "translation-finetune-forgetting-mt-instruction-audit",
        "Translation fine-tune forgetting audit",
        "K368",
        "2609.28395",
        "sources/arxiv-2609-28395-translation-finetune-forgetting-mt-instruction.md",
        "Do not trust **general retention benchmarks** alone after MT fine-tuning. Report **MT-IF** (instruction-following under translation prompts) alongside generic retention. Applies to any specialized fine-tune path touching deployed agents.",
        [
            "sources/arxiv-2609-28395-translation-finetune-forgetting-mt-instruction.md",
            "concepts/cross-lingual-safety-transfer-lrl.md",
            "concepts/culturally-responsive-llm-benchmark-audit.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K368)",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
