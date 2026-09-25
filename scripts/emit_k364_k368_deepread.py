#!/usr/bin/env python3
"""Deep-read updates for K364–K366, K368 (2026-09-25). Skips OOD 28372 (SEO wiki)."""
from __future__ import annotations

from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
DATE = "2026-09-25"


def patch(path: str, *, narrative: str, snippets: str, maturity: str | None = None, source: bool = False) -> None:
    p = WIKI / path
    t = p.read_text(encoding="utf-8")
    if source and "deep-read" not in t:
        t = t.replace("read_status: read", "read_status: deep-read", 1)
        t = t.replace("| Read status | read (abstract + triage) |", f"| Read status | deep-read ({DATE}) |", 1)
    if maturity and "maturity: draft" in t:
        t = t.replace("maturity: draft", f"maturity: {maturity}", 1)
    if "## Narrative\n\n" in t:
        start = t.index("## Narrative\n\n") + len("## Narrative\n\n")
        end = t.index("\n## Snippets", start)
        t = t[:start] + narrative + t[end:]
    if "## Snippets\n\n" in t:
        start = t.index("## Snippets\n\n") + len("## Snippets\n\n")
        end = len(t)
        if "\n## Dead Ends" in t:
            end = t.index("\n## Dead Ends", start)
        t = t[:start] + snippets + t[end:]
    p.write_text(t, encoding="utf-8")
    print("patched", path)


def main() -> int:
    patch(
        "sources/arxiv-2609-25294-controller-only-false-confirmation-rf-uav.md",
        source=True,
        maturity="validated",
        narrative="""**K364** — dual-band **USRP B210** passive RF study (GMU) on **DJI Phantom 3 4K, Hubsan H501S, DJI Mavic Mini** with explicit **ambient**, **controller-only**, and **linked** states (20 rounds; 2.4 + 5.8 GHz window grid). Detector trained on **linked + ambient only** hits **0.992** balanced linked-vs-ambient accuracy but **false-confirms 30/60** controller-only scans (**FCR_ctrl = 0.500**). Adding controller-only negatives with **confirm / reject / defer** under an **FCR constraint** cuts pooled **FCR_ctrl** from **0.350 → 0.050** but drops confirm-linked TPR **0.900 → 0.400** with **42.1% deferred**; platform mix matters (Hubsan/Mavic vs Phantom). **HIL** scan time **82.9 s → 28.9 s** for compact ranked scan.

Steal: always report **controller-only false confirmation** separately from linked-vs-background accuracy. **Authorized RF lab / owned spectrum only.**""",
        snippets="""> "An energy-feature detector trained only on linked and ambient scans reaches 0.992 balanced accuracy … but false-confirms 30 of 60 controller-only scans." [Source: arXiv 2609.25294 abstract]

> "For the pooled all-platform analysis, the constraint reduces observed FCR_ctrl from 0.350 to 0.050, while confirm-linked TPR decreases from 0.900 to 0.400 and 42.1% of scans are deferred." [Source: arXiv 2609.25294]""",
    )
    patch(
        "concepts/passive-rf-uav-controller-only-false-confirmation.md",
        maturity="validated",
        narrative="""Counter-UAV RF eval needs three cells: **ambient**, **controller-only** (powered RC, aircraft off), **linked**. High clutter/linked accuracy can **mask** controller-only false alarms — use **defer** when FCR constraints trade TPR for precision.""",
        snippets="""> Controller-only false confirmation: linked-UAV alarm with no aircraft present. [Source: arXiv 2609.25294; K364]""",
    )

    patch(
        "sources/arxiv-2609-26079-ble-mac-randomization-reidentification.md",
        source=True,
        maturity="validated",
        narrative="""**K365** — ML **linking** of BLE **RPA** epochs from **Extended Advertising** plaintext fields (KAUST/Politecnico). **14** target devices in pools of hundreds; with **two** observed RPA epochs, a **decision tree** reaches **~98.6% recall**, **<2%** packet-level FPR, **0.38%** false device IDs after MAC aggregation. Field note: only **~1/3** of observed devices in their traces actually use RPA **15 years** after introduction.

Defensive steal: **pairing ≠ authorization**; MAC randomization ≠ unlinkability. **Runtime:** `k365_ble_reid_lab_precheck.py`. **Owned devices only.**""",
        snippets="""> "Even when trained on only two observed RPA epochs, a simple decision tree can recover almost all advertisements from the target (98.6% recall), with a packet-level FPR below 2%." [Source: arXiv 2609.26079 abstract]

> "Only 1/3 of observed devices do not even support [RPA]." [Source: arXiv 2609.26079]""",
    )
    patch(
        "concepts/ble-mac-randomization-reidentification-lab.md",
        maturity="validated",
        narrative="""Automated feature learning lowers expertise for **advertising-channel re-id** under RPA — test **service-layer authorization** and rotation policies on owned devices, not anonymity claims alone.""",
        snippets="""> ML shifts re-id from manual signatures to scalable feature learning on EA packets. [Source: arXiv 2609.26079; K365]""",
    )

    patch(
        "sources/arxiv-2609-28322-learning-cost-reliable-inference.md",
        source=True,
        maturity="validated",
        narrative="""**K366** (MPI-SWS) — **procurement platform** for LLM routing: **reverse second-price auction** with truthful cost bids; platform learns provider quality and routes to the **cheapest qualified** provider for a user’s quality threshold. Experiments (Llama/Qwen on math + QA benches): winner **pricing margin 10–71%** vs fixed per-token markets — quality tier and task shape matter.

Audit steal for **OpenRouter / routing marketplaces**: report **quality floor + $/task**, not flat token price alone (pairs K354). REFERENCE economics; not a security boundary.""",
        snippets="""> "The pricing margin of the most cost-competitive provider varies significantly—from 10% to 71%—depending on the task and quality threshold." [Source: arXiv 2609.28322 abstract]""",
    )
    patch(
        "concepts/reliable-inference-procurement-routing.md",
        maturity="validated",
        narrative="""When agents or eval harnesses fan out to multiple model backends, treat **reliability tier** as a priced auction outcome — fixed token lists hide **10–71%**-class spreads in the paper’s simulaton.""",
        snippets="""> Reverse second-price routing to qualified lowest-cost provider. [Source: arXiv 2609.28322; K366]""",
    )

    patch(
        "sources/arxiv-2609-28395-translation-finetune-forgetting-mt-instruction.md",
        source=True,
        maturity="validated",
        narrative="""**K368** (AppTek/RWTH) — MT parallel-data **SFT** improves COMET (e.g. Amharic→En **45.6 → 71.5**) but risks **MT-IF** (formality, gender, length controls). **General forgetting mitigations** screened on Llama 3.2 1B then 3.1 8B (AR-EN, ES-EN): **EWC** best preserves **general benchmarks** (ES-EN avg general **−1.7** vs **−11.0** for plain SFT) yet **still drops formality/gender control** vs SFT; only **data mixing with control-task examples** retains controls — **does not generalize to unseen prompts** for the same control.

Steal: after **any domain fine-tune** on deployed agents, re-run **task-specific instruction eval**, not general retention alone (pairs K304 RIM).""",
        snippets="""> "Elastic Weight Consolidation preserves general capabilities best … yet its scores for formality and grammatical gender control remain close to standard fine-tuning. Only data mixing with control-task examples preserves these controls." [Source: arXiv 2609.28395 abstract]""",
    )
    patch(
        "concepts/translation-finetune-forgetting-mt-instruction-audit.md",
        maturity="validated",
        narrative="""**MT-IF** (instruction-conditioned translation) is a separate axis from **General** benchmark retention after parallel-data FT. EWC is not a free lunch for controlled MT behavior.""",
        snippets="""> General forgetting mitigation ≠ MT-specific instruction following. [Source: arXiv 2609.28395; K368]""",
    )

    log = WIKI / "log.md"
    lt = log.read_text(encoding="utf-8")
    entry = f"""## [{DATE}] deep-read | K364–K366, K368 (Grok-aligned)

- Deep-read **2609.25294, 26079, 28322, 28395**; sources + concepts → **validated**.
- **Deferred (Grok + route):** K373 product logger, K371 bench clone, K369 NeuroSploit replication, K370 RF hardware, duplicate K373 friend one-pager.
- **friend brief:** n/a.

"""
    if "deep-read | K364–K366" not in lt:
        log.write_text(entry + lt, encoding="utf-8")
        print("log ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
