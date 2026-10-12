#!/usr/bin/env python3
"""Writer for K418-K424 ingest (2026-10-12) + K288 NOMOS inbound pages.

No attack payloads in wiki. Slugs WITHOUT .md; every related ref ends with .md.
"""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-10-12"
NOTE = f"K418-K424 ingest / {DATE}"
NOMOS_NOTE = f"K288 inbound brief / {DATE}"


def w(rel, body):
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump(t):
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", t,
                  count=1, flags=re.M)


def add_related(rel, ref, note):
    """Add a reciprocal related: entry + Relations bullet to an existing page."""
    assert ref.endswith(".md"), ref
    p = WIKI / rel
    if not p.is_file():
        print("  skip (no page)", rel, "→", ref)
        return
    t = p.read_text(encoding="utf-8")
    if f"  - {ref}" not in t:
        t = t.replace("related:\n", f"related:\n  - {ref}\n", 1)
    if f"- @{ref}" not in t:
        if "## Relations\n\n" in t:
            t = t.replace("## Relations\n\n", f"## Relations\n\n- @{ref} — {note}\n", 1)
        else:
            t = t.rstrip() + f"\n\n## Relations\n\n- @{ref} — {note}\n"
    p.write_text(bump(t), encoding="utf-8")
    print("  patched", rel, "→", ref)


def src(slug, title, arxiv, kid, pdf, narrative, concept=None, extra=None,
        ood=False, wire=""):
    assert not slug.endswith(".md")
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra or [])]
    for r in rels:
        assert r.strip().endswith(".md"), r
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n"
    if concept:
        rel_sec += f"- @{concept}\n"
    if extra:
        rel_sec += "".join(f"- @{r}\n" for r in extra)
    if ood:
        tags = "source, ood"
        keywords = f"{arxiv}, ood"
    else:
        tags = "source, arxiv, agent-security"
        keywords = f"{arxiv}, {kid.lower()}"
    wire_line = wire or (
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)" if ood
        else f".cursor/rules/cemini-cybersec-agent-audit.mdc ({kid})")
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
| Read status | read |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"sources/{slug}.md", body)
    return slug


def concept(slug, title, kid, arxiv, narrative, related, wire, tags="agent-security"):
    assert not slug.endswith(".md")
    for r in related:
        assert r.endswith(".md"), r
    rels = "\n".join(f"  - {r}" for r in related)
    inl = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, {tags}, {kid.lower().replace('+', '-')}]
keywords: [{arxiv}, {kid}]
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

Question: **{title}** — operator steal from arXiv {arxiv}?

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"concepts/{slug}.md", body)
    return slug


def main() -> int:
    # ================= K418 aerial RAN testbed / PWS =====================
    s = src("arxiv-2610-05007-aerial-5g-gnb-arm-testbed",
            "Toward lightweight aerial 5G gNBs: a reproducible OAI testbed on commodity ARM",
            "2610.05007", "K418",
            "arxiv-2610.05007-toward-lightweight-aerial-5g-gnbs-reproducible-o.pdf",
            "**K418 — a reproducible open-source RAN testbed, and a public-warning channel on it.** For a "
            "battery-powered UAV base station every gram and watt spent on RAN compute competes with flight "
            "time, so the design keeps the **5G Core and central unit (CU) on the ground** and flies only "
            "the backhaul endpoint, **distributed unit (DU)**, and radio over the **3GPP F1 split**. The "
            "measured question: can **commodity ARM** boards run a real **OpenAirInterface (OAI) 5G DU**? "
            "With **Raspberry Pi 5** and **Jetson Orin Nano** as DUs, a **USRP B210**, and a commercial "
            "handset, Jetson preserves **88.4%** of x86 split-DU Ethernet DL throughput and **87.5-89.0%** "
            "across three bearers; **5G/WireGuard** keeps **76.4-77.1%** of each host's wired DL rate. The "
            "integrated payload weighs **657.4 g** and draws ~**28 W** under sustained traffic.\n\n"
            "A controlled link-adaptation intervention moves split DL from **23.4 to 99.4 Mb/s** as the "
            "dominant MCS moves **3 to 26** — the collapse was scheduling/timing, not the platform. The "
            "security-relevant artifact is a **PWS-over-F1 patch**: it carries the **Write-Replace Warning** "
            "procedure from the ground CU to the remote DU so **SIB8** is scheduled to handsets, giving an "
            "area-wide **Public Warning System** emergency broadcast. Repos "
            "`github.com/promaaa/oai-cu-du-lab` and `github.com/promaaa/jetson-kernel-sctp`; licence not "
            "stated. Operator steal: a **reproducible ARM RAN testbed** lowers the bar to exercise the "
            "wireless/emergency-broadcast surface in an authorized lab, and a **PWS channel is a "
            "high-integrity target** — it is meant to be believed by every handset in range. Authorized "
            "lab only. **No exploit steps in wiki.**",
            "concepts/aerial-ran-testbed-pws-broadcast.md",
            ["concepts/wireless-pentest.md", "concepts/network-security.md"],
            wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K418)")
    concept("aerial-ran-testbed-pws-broadcast",
            "A PWS emergency broadcast is a high-integrity target", "K418", "2610.05007",
            "A **Public Warning System** broadcast (the `Write-Replace Warning` / **SIB8** path) is "
            "designed so that every compatible handset in range **believes and acts on it** without "
            "challenge. That is exactly what makes it a high-value target: the integrity of the "
            "warning — not its confidentiality — is the whole security property, and a spoofed or "
            "suppressed alert has physical-world consequences.\n\n"
            "K418 matters here because it makes the surface **reproducible on commodity hardware**: the "
            "OAI **CU/DU F1 split** runs a real 5G DU on **Raspberry Pi 5 / Jetson Orin Nano** with a "
            "USRP B210, and the paper **releases the PWS-over-F1 patch** that carries the warning from the "
            "ground CU to the airborne DU. For a defender the operator rule is simple: **treat the warning "
            "channel as an authenticated control plane, not as broadcast content.** For a laboratory the "
            "value is a low-cost way to exercise emergency-broadcast integrity in a Faraday cage — "
            "authorized RF lab only.",
            ["sources/arxiv-2610-05007-aerial-5g-gnb-arm-testbed.md",
             "concepts/wireless-pentest.md",
             "concepts/network-security.md"],
            ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K418)")
    for r in ["concepts/wireless-pentest.md", "concepts/network-security.md"]:
        add_related(r, "sources/arxiv-2610-05007-aerial-5g-gnb-arm-testbed.md", NOTE)
        add_related(r, "concepts/aerial-ran-testbed-pws-broadcast.md", NOTE)

    # ================= K419 holistic RFFI ================================
    src("arxiv-2610-05979-holistic-rffi-vector-quantization",
        "From identification to discovery: holistic RF fingerprinting via learning-aided quantization",
        "2610.05979", "K419",
        "arxiv-2610.05979-from-identification-to-discovery-holistic-rf-fin.pdf",
        "**K419 — one expandable representation for identify, reject, and discover.** Radio-frequency "
        "fingerprint identification (RFFI) authenticates a transmitter from hardware impairments in the "
        "analog waveform, but existing pipelines treat the three tasks as separate components: **closed-set "
        "identification** (name a registered device), **open-set recognition** (OSR — reject an unknown "
        "one), and **novel-class discovery** (NCD — organise rejected signals into new identities). The "
        "paper unifies them by casting RFFI as **vector quantization in a learned latent space**: "
        "registered devices are **labeled codewords**, closed-set is codeword assignment, OSR is an "
        "uncertainty from **codebook geometry**, and NCD reuses the **continuous** open-set score to "
        "cluster rejected samples into new devices.\n\n"
        "Numbers (LoRa and Wi-Fi datasets): closed-set accuracy **97.9%** at ten devices; with **five "
        "unseen devices** it correctly associates **81.8%** of held-out samples to their new identities "
        "(vs **80.4%** for GCD and **18.6%** for OpenNCD); with **seven rogue transmitters** new-device "
        "accuracy **90.3%** (vs 78.7% / 40.0%); total accuracy after registration **91.1-92.6%**. It is "
        "cheap — **~5 MFLOPs/frame**, **>99.9%** in the convolutional feature extractor. Repo "
        "`github.com/omer-hazan/RFFI-with-GCD-via-VQVAE`; licence not stated.\n\n"
        "The design lesson is the coupling: **binarising the OSR decision early destroys the information "
        "NCD needs.** Operator steal: an unauthorized-transmitter detector should keep the **continuous "
        "novelty score**, and a single codebook lets a system detect unknowns *and* name them as new "
        "devices without retraining. Authorized RF lab only.",
        "concepts/holistic-rffi-open-world-discovery.md",
        ["concepts/horffi-high-openness-rffi.md",
         "concepts/wifi-rf-fingerprinting-open-set.md",
         "concepts/rf-fingerprint-probe-point-benchmark.md",
         "concepts/rf-fingerprint-temperature-drift.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K419)")
    concept("holistic-rffi-open-world-discovery",
            "Keep the open-set score; it is the discovery signal", "K419", "2610.05979",
            "Device identification from RF fingerprints is usually three pipelines bolted together: "
            "classify a registered device, reject an unknown one, then cluster the rejects. K419 shows "
            "the three are one problem and that **the coupling is the point** — the **uncertainty the "
            "open-set stage produces is the signal that makes discovery work**, so collapsing it to a "
            "binary reject/fail decision before clustering throws away exactly what is needed.\n\n"
            "One **learned codebook** carries all three: codewords name registered devices, codebook "
            "**geometry** gives the open-set score, and expansion of the codebook registers a newly "
            "discovered transmitter. Measured on LoRa and Wi-Fi: **97.9%** closed-set at ten devices, "
            "**81.8%** new-device accuracy with five unseen devices, **90.3%** with seven rogue "
            "transmitters. Operator rule for a rogue-device or unauthorized-transmitter detector: "
            "**preserve the continuous novelty score and design for expansion** — an unknown device "
            "should become a named one without a retrain. Pairs K326 (open-set Wi-Fi CSI) and K245 "
            "(high-openness RFFI). Authorized RF lab only.",
            ["sources/arxiv-2610-05979-holistic-rffi-vector-quantization.md",
             "concepts/horffi-high-openness-rffi.md",
             "concepts/wifi-rf-fingerprinting-open-set.md",
             "concepts/rf-fingerprint-probe-point-benchmark.md",
             "concepts/rf-fingerprint-temperature-drift.md"],
            ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K419)")
    for r in ["concepts/horffi-high-openness-rffi.md",
              "concepts/wifi-rf-fingerprinting-open-set.md",
              "concepts/rf-fingerprint-probe-point-benchmark.md",
              "concepts/rf-fingerprint-temperature-drift.md"]:
        add_related(r, "sources/arxiv-2610-05979-holistic-rffi-vector-quantization.md", NOTE)
        add_related(r, "concepts/holistic-rffi-open-world-discovery.md", NOTE)

    # ================= K420 OOD: sustainable cloud-fog-edge ==============
    src("arxiv-2610-13307-sustainable-cloud-fog-edge-smart-buildings",
        "Sustainable cloud-fog-edge systems for smart buildings under memory constraints",
        "2610.13307", "K420",
        "arxiv-2610-13307-sustainable-cloud-fog-edge-systems-for-smart-bui.pdf",
        "**K420 — OOD (sustainability / embedded ML).** An architecture and algorithmic study for "
        "**privacy-preserving, low-power learning inside smart buildings**: an Arduino sensor chain "
        "(Uno R4 WiFi / BME280), a lightweight **KOptim** SLA orchestrator interoperable with FIWARE, and "
        "a **Generalized Hebbian Algorithm (GHA) PCA** adapted to run on microcontrollers under a memory "
        "constraint, using buffered sorting that preserves extreme samples. It roughly matches "
        "full-memory PCA quality at **O(W log W)** sorting cost and includes a **critical review of "
        "fog-node security vulnerabilities and power overhead**. Repo "
        "`github.com/madou-sow/OnlineML_ESP32`; licence not stated. **Not security-primary** — no attack "
        "or defense technique for this wiki's lanes; retained as a stub for the edge/IoT footprint. "
        "Routing: no target wiki; leave as OOD stub.",
        None, ood=True,
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)")

    # ================= K421 PHY info hiding ==============================
    src("arxiv-2610-13367-secrets-in-preamble-phy-wifi",
        "Secrets in preamble: practical and robust PHY information hiding for Wi-Fi",
        "2610.13367", "K421",
        "arxiv-2610.13367-secrets-in-preamble-practical-and-robust-phy-inf.pdf",
        "**K421 — a covert channel below the MAC, and its defensive dual.** Physical-layer information "
        "hiding embeds secrets inside PHY waveforms without breaking the primary link, enabling **covert "
        "communication, PHY steganography, and watermarking**. Prior Wi-Fi schemes were limited by low "
        "**steganographic capacity** and poor **robustness** to environmental change. This work hides the "
        "secret in the **legacy short training field (L-STF)** of the Wi-Fi preamble and **preserves the "
        "L-STF autocorrelation structure**, so **packet detection and coarse frequency-offset "
        "compensation** — which a receiver depends on — are not disturbed. A pair of **neural networks** "
        "learns the embedding and extraction rules.\n\n"
        "Measured on a hardware prototype (**USRP B210**) in indoor *and* outdoor conditions, it reliably "
        "embeds **46 secret bits per Wi-Fi packet** across diverse channels, with the design explicitly "
        "targeting robustness against interference (tested at 1% and 10% of received signal power) and "
        "channel variation; secret-bit-error rate is the training loss, with BCH coding discussed as "
        "recovery. No code release (MATLAB/Simulink + SDR). Operator steal, two-sided: a **46-bit "
        "per-packet PHY covert channel survives real channels**, which is both an **exfil path invisible "
        "to upper-layer inspection** and a **watermark for transmitter authentication**. Authorized RF "
        "lab only. **No embedding recipes or code in wiki.**",
        "concepts/phy-layer-covert-channel-wifi-preamble.md",
        ["concepts/inference-time-covert-agentic-communication.md",
         "concepts/physical-layer-deception-enterprise-wifi-auth.md",
         "concepts/spectral-whitening-wireless-protocol-id.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K421)")
    concept("phy-layer-covert-channel-wifi-preamble",
            "A covert channel and a watermark are the same mechanism", "K421", "2610.13367",
            "Hiding data in the Wi-Fi **preamble** is the cleanest statement of a PHY covert channel: the "
            "secret rides inside a field the receiver must already process, and the design goal is "
            "**indistinguishability** — here, preserving the **L-STF autocorrelation** so that packet "
            "detection and coarse frequency-offset compensation behave exactly as they would without the "
            "secret. That invisibility is precisely what makes the same mechanism usable for two opposite "
            "purposes: **covert exfiltration** by an adversary, and **watermarking for transmitter "
            "authentication** by a defender.\n\n"
            "The K421 prototype embeds **46 secret bits per packet** on commodity SDR hardware, indoors "
            "and outdoors, and trains for robustness to interference — so the capacity and reliability "
            "bar for a practical PHY channel is now low. Two operator rules follow. First, **upper-layer "
            "inspection cannot see a preamble channel** — encryption of payload and metadata does not "
            "cover it; physical-layer monitoring or watermark verification does. Second, when you want "
            "transmitter authentication, a robust PHY watermark is a candidate primitive. Pairs K393 "
            "(channel-derived Wi-Fi auth) and the covert-communication line (K359). Authorized RF lab "
            "only; no embedding recipes in wiki.",
            ["sources/arxiv-2610-13367-secrets-in-preamble-phy-wifi.md",
             "concepts/inference-time-covert-agentic-communication.md",
             "concepts/physical-layer-deception-enterprise-wifi-auth.md",
             "concepts/spectral-whitening-wireless-protocol-id.md"],
            ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K421)")
    for r in ["concepts/inference-time-covert-agentic-communication.md",
              "concepts/physical-layer-deception-enterprise-wifi-auth.md",
              "concepts/spectral-whitening-wireless-protocol-id.md"]:
        add_related(r, "sources/arxiv-2610-13367-secrets-in-preamble-phy-wifi.md", NOTE)
        add_related(r, "concepts/phy-layer-covert-channel-wifi-preamble.md", NOTE)

    # ================= K422 QTestBench ==================================
    src("arxiv-2610-13811-qtestbench-llm-quantum-code-tests",
        "QTestBench: a test framework for evaluating LLM-generated quantum code",
        "2610.13811", "K422",
        "arxiv-2610.13811-qtestbench-a-test-framework-for-evaluating-llm-g.pdf",
        "**K422 — a generated test that passes is not a test that discriminates.** LLMs now write the "
        "unit tests that guard code, but a suite that **accepts incorrect code is worse than no test at "
        "all** — and on quantum software, where outputs are probabilistic, tolerances matter, and "
        "correctness is defined by **domain-specific checkers**, a well-formed test can still disagree "
        "with the benchmark's own verdict. **QTestBench** prompts models to produce syntactic, semantic, "
        "and behavioral tests, injects candidate solutions at runtime, and scores each test **against an "
        "independent benchmark checker — never against the tests themselves.**\n\n"
        "Over five LLMs, eight **PennyLane QHack** challenges and ten **Qiskit HumanEval** tasks: "
        "generated suites **almost always execute**, but **discrimination lags** — best test quality "
        "**0.71** on QHack and **0.34** on Qiskit HumanEval, so **executability alone overstates "
        "quality**. Two failure modes are named: **too weak** (checks only that the entry point exists, "
        "passes a wrong solution) and **too strict** (a 1e-4 tolerance fails a correct implementation). "
        "**Oracle-verified synthetic mutants** stabilise bug-detection estimates when natural faulty "
        "solutions are scarce — on three of ten Qiskit tasks there are **none**. Repo "
        "`github.com/eBrain4Everyone/QTestBench`; licence not stated. Operator steal: **score generated "
        "tests against an independent oracle, measure accept-correct AND reject-incorrect, and use "
        "synthetic mutants when negatives are rare.** Pairs K300 and K413.",
        "concepts/llm-generated-test-discrimination.md",
        ["concepts/llm-generated-dependency-breaking-tests.md",
         "concepts/code-monitor-red-teaming-public-tests.md",
         "concepts/llm-vuln-repair-metrics-audit.md",
         "concepts/verification-generation-gap.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K422)")
    concept("llm-generated-test-discrimination",
            "A passing generated test is not a discriminating test", "K422", "2610.13811",
            "An LLM-written test suite that runs and passes tells you almost nothing: the question is "
            "whether it **separates a correct implementation from a faulty one**. QTestBench makes that "
            "the metric — inject candidate solutions, compare each test's verdict to an **independent "
            "oracle's** label, and never treat the generated tests as ground truth. The gap is large: "
            "suites **almost always execute**, yet the best model reaches test quality **0.71** on one "
            "benchmark and **0.34** on another, so **executability overstates quality**.\n\n"
            "Two concrete failure modes to check for: a **too-weak** test that only verifies the entry "
            "point and so passes a wrong solution, and a **too-strict** test whose tolerance (e.g. 1e-4) "
            "fails a correct one. When natural faulty solutions are rare — true for three of ten Qiskit "
            "tasks — **oracle-verified synthetic mutants** restore a stable bug-detection estimate. "
            "Operator rule: for any agent that writes its own tests, **score the tests against an "
            "external oracle and report accept-correct and reject-incorrect separately**. Pairs K300 "
            "(dependency-breaking tests) and K413 (the verification-generation gap).",
            ["sources/arxiv-2610-13811-qtestbench-llm-quantum-code-tests.md",
             "concepts/llm-generated-dependency-breaking-tests.md",
             "concepts/code-monitor-red-teaming-public-tests.md",
             "concepts/llm-vuln-repair-metrics-audit.md",
             "concepts/verification-generation-gap.md"],
            ".cursor/rules/cemini-cybersec-agent-audit.mdc (K422)")
    for r in ["concepts/llm-generated-dependency-breaking-tests.md",
              "concepts/code-monitor-red-teaming-public-tests.md",
              "concepts/llm-vuln-repair-metrics-audit.md",
              "concepts/verification-generation-gap.md"]:
        add_related(r, "sources/arxiv-2610-13811-qtestbench-llm-quantum-code-tests.md", NOTE)
        add_related(r, "concepts/llm-generated-test-discrimination.md", NOTE)

    # ================= K423 X-AgentRed ==================================
    src("arxiv-2610-13886-x-agentred-cross-service-redteam",
        "X-AgentRed: red-teaming personal agents in evolving multi-service ecosystems",
        "2610.13886", "K423",
        "arxiv-2610.13886-x-agentred-red-teaming-personal-agents-in-evolvi.pdf",
        "**K423 — the harm is in the composition, not the call.** Personal agents connect to many "
        "services through tools, and when their **effects accumulate and interact across services**, a "
        "benign user request can produce a harmful outcome. Discovering those **cross-service paths** is "
        "hard because generation is biased toward tool combinations seen in training. **X-AgentRed** is a "
        "**self-evolving** red-teaming framework: it analyses each tool's **effects, potential harms, and "
        "execution preconditions** and builds a **directed graph** in which one tool's effects satisfy "
        "another's preconditions; it samples **recipes** from the graph, instantiates them as realistic "
        "scenarios, and uses **execution feedback** to diversify blocked paths by **tool substitution** "
        "and by **refining the preconditions** at failed steps.\n\n"
        "Across **four frontier agentic models** it reaches **1.77x** the harmful-path rate of the "
        "**STAC** baseline and explores a more diverse tool set — **2.99x tool coverage** on average. "
        "Meta Research; **no public release** — this is attack tooling, **never clone**. Operator steal: "
        "the attack surface is the **graph of tool effects and preconditions**, not prompt-space "
        "patterns; a **feedback-driven, self-evolving** search finds novel cross-service chains that "
        "one-shot generation misses. Defend by bounding **combinations** — effect-aware, least-privilege "
        "tool gating — not by filtering each call. **No attack recipes or trajectories in wiki.**",
        "concepts/cross-service-agent-compositional-harm.md",
        ["concepts/layer-paradigm-agent-red-teaming.md",
         "concepts/black-box-agentic-redteam-taxonomy.md",
         "concepts/agentxploit-repository-runtime-red-teaming.md",
         "concepts/task-conditioned-excess-authority.md",
         "concepts/intent-governed-tool-authorization.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K423)")
    concept("cross-service-agent-compositional-harm",
            "Harm emerges from the composition of benign tool calls", "K423", "2610.13886",
            "A personal agent invokes individually-benign tools across services, and their **effects "
            "accumulate and interact** — information, permissions, and state propagate — so a benign "
            "request can end in a harmful outcome. That makes the unit of risk the **combination**, not "
            "the call, and it means a per-call filter is looking in the wrong place.\n\n"
            "X-AgentRed operationalises the search over combinations: build a **directed graph of tool "
            "effects and preconditions** (one tool's effect can enable another), sample recipes, "
            "instantiate scenarios, and **self-improve from execution feedback** by substituting tools "
            "and refining preconditions at blocked steps. It achieves **1.77x** the harmful-path rate and "
            "**2.99x** tool coverage of a strong baseline across four frontier models. `github.com/"
            "CHATS-lab/ToolShield` and `github.com/ZJU-LLM-Safety/TRACE` are cited **prior work**, not a "
            "release of this system.\n\n"
            "The operator consequence: **defend the composition.** Effect-aware, least-privilege tool "
            "gating — what a *sequence* of authenticated calls may collectively do — is the lever, not "
            "prompt filtering of single messages. Pairs K327 (black-box agentic red-team taxonomy), K375 "
            "(AgentXploit repo-to-runtime), and the intent-governed tool authorization line. Defensive "
            "lab only; no attack recipes in wiki.",
            ["sources/arxiv-2610-13886-x-agentred-cross-service-redteam.md",
             "concepts/layer-paradigm-agent-red-teaming.md",
             "concepts/black-box-agentic-redteam-taxonomy.md",
             "concepts/agentxploit-repository-runtime-red-teaming.md",
             "concepts/task-conditioned-excess-authority.md",
             "concepts/intent-governed-tool-authorization.md"],
            ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K423)")
    for r in ["concepts/layer-paradigm-agent-red-teaming.md",
              "concepts/black-box-agentic-redteam-taxonomy.md",
              "concepts/agentxploit-repository-runtime-red-teaming.md",
              "concepts/task-conditioned-excess-authority.md",
              "concepts/intent-governed-tool-authorization.md"]:
        add_related(r, "sources/arxiv-2610-13886-x-agentred-cross-service-redteam.md", NOTE)
        add_related(r, "concepts/cross-service-agent-compositional-harm.md", NOTE)

    # ================= K424 task context / component roles ===============
    src("arxiv-2610-13895-task-context-component-roles",
        "Task context shapes component roles in language models",
        "2610.13895", "K424",
        "arxiv-2610-13895-task-context-shapes-component-roles-in-language.pdf",
        "**K424 — a shared attention head is not a fixed feature; its role is task-conditional.** Circuit "
        "analysis shows LLMs **reuse the same attention heads across tasks**, but identifying a shared "
        "head does not explain what it does differently in each. This work compares **identical graph "
        "facts** across tasks and measures two things per component: **influence** (how an intervention on "
        "a head changes later layers) and **importance** (the effect on the answer). Task changes "
        "**redistribute influence** across five open-weight models (four families, 1.5-14B).\n\n"
        "The concrete demonstration: in **Gemma-2-9B** and **Qwen3-14B**, a single **activation edit** "
        "switches **which fact the model reads** while the written instruction stays fixed — the same "
        "heads then respond to different facts and influence later components differently. The authors "
        "build two **linear response maps** (before and after the edit), and for a **separate factual "
        "intervention** the condition-matched map reduces **mean squared prediction error by 53.6%** in "
        "Gemma and **5.0%** in Qwen against the average of the two maps. No code release.\n\n"
        "Operator steal for the security/interpretability lane: **a head's role is a function of task "
        "context**, so an interpretability finding does not transfer as a fixed label, and any steering "
        "or intervention meant to change one behaviour while preserving others must be **re-validated "
        "per task**. Pairs K318 (multi-token SAE readout), K349 (Deep Noir steering), K383 (CounterSteer).",
        "concepts/task-dependent-component-roles.md",
        ["concepts/late-attention-entity-token-copying-interpretability.md",
         "concepts/deep-noir-steering-discovery-chronometry.md",
         "concepts/countersteer-activation-steering-ipi-defense.md",
         "concepts/probe-internal-recognition-sandbagging-audit.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K424)")
    concept("task-dependent-component-roles",
            "A component's role is a function of task context", "K424", "2610.13895",
            "Mechanistic interpretability often treats a discovered circuit as a fixed label: 'this head "
            "does X'. K424 shows the label is **task-conditional**. Hold the input facts identical and "
            "change only the task, and **influence redistributes** — the same attention heads respond to "
            "**different facts** and change later computation **differently**. In Gemma-2-9B and "
            "Qwen3-14B a single **activation edit** flips **which fact the model reads** while the written "
            "instruction is unchanged, and a **condition-specific linear response map** predicts a later "
            "head's response far better than the average of the two maps — **53.6%** lower MSE in Gemma, "
            "**5.0%** in Qwen.\n\n"
            "The operator rule matters for safety interventions: **an interpretability result does not "
            "transfer across tasks as a static fact**, so a steering edit or activation clamp validated "
            "on one behaviour must be **re-validated for the behaviour you intend to preserve**. This is "
            "the mechanistic counterpart to the wiki's measurement-integrity line — a component-level "
            "claim is only as strong as the task surface it was measured on. Pairs K318, K349, K383, K337.",
            ["sources/arxiv-2610-13895-task-context-component-roles.md",
             "concepts/late-attention-entity-token-copying-interpretability.md",
             "concepts/deep-noir-steering-discovery-chronometry.md",
             "concepts/countersteer-activation-steering-ipi-defense.md",
             "concepts/probe-internal-recognition-sandbagging-audit.md"],
            ".cursor/rules/cemini-cybersec-agent-audit.mdc (K424)")
    for r in ["concepts/late-attention-entity-token-copying-interpretability.md",
              "concepts/deep-noir-steering-discovery-chronometry.md",
              "concepts/countersteer-activation-steering-ipi-defense.md",
              "concepts/probe-internal-recognition-sandbagging-audit.md"]:
        add_related(r, "sources/arxiv-2610-13895-task-context-component-roles.md", NOTE)
        add_related(r, "concepts/task-dependent-component-roles.md", NOTE)

    # ================= K288 inbound NOMOS ===============================
    src("arxiv-2610-11030-nomos-compiled-policy-tool-gate",
        "NOMOS: compiling a written agent policy into a deterministic runtime tool-call gate",
        "2610.11030", "K288",
        "arxiv-2610.11030-nomos-compiled-policy-to-tool-gate.pdf",
        "**K288 (inbound, OSINT brief) — compile the policy, gate the call.** NOMOS turns a **written "
        "agent policy** into a **deterministic, LLM-free runtime tool-call gate**, and it is the "
        "strongest published counter-argument to prompt-level guardrails. Four passes: **PARSE → "
        "EXTRACT** (the only LLM pass; N=5 majority vote) **→ RESOLVE** (deterministic static checks: "
        "self-blocking reachability, argument-signature consistency, domain satisfiability, state "
        "contradictions, write-scope correctness) **→ MATERIALIZE**. The runtime gate evaluates each "
        "proposed tool call against **facts taken only from real tool results and user turns** "
        "(structural fact provenance) and returns allow/block in **microseconds with zero LLM**.\n\n"
        "Results: violations among state-changing calls **66.3% → 2.6%** (airline) and **30.8% → 6.9%** "
        "(retail) — **26x** and **4.5x**; **AgentDojo banking ASR 0.0%** (288 pairs) against **46.5% "
        "undefended** (a tool filter alone leaves 11.8%); **Pass^5 / Pass^1 0.51 → 0.67**, so the policy "
        "does not break the agent. A prompt-level PolicyGuard reimplementation costs **+74% wall-clock "
        "and 347 LLM calls** against **3 us/call and zero**. It reproduces on **Llama-3.3-70B** "
        "(86.9% → 7.1%) and the compiler runs **on-premise** on gemma-4-26B.\n\n"
        "**The caution that matters:** RESOLVE **repairs 37% and rejects 13%** of extracted rules — the "
        "generated policy is wrong **about a third of the time**, so policy extraction must be "
        "**statically verified, never trusted**. Operator steal: **an LLM-written policy is an input to "
        "a checker, not a control.** Artifact DOI `10.5281/zenodo.22123419`; **implementation "
        "proprietary, not released.** **No PoC or exploit steps.**",
        "concepts/nomos-compiled-policy-enforcement.md",
        ["concepts/intent-governed-tool-authorization.md",
         "concepts/mcp-execution-control-invariants.md",
         "concepts/agent-runtime-guardrails.md",
         "concepts/mcp-security-posture.md"],
        wire=".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K288 inbound)")
    concept("nomos-compiled-policy-enforcement",
            "Compile the policy once; enforce it in code", "K288", "2610.11030",
            "Prompt-level guardrails ask the model to police itself. NOMOS takes the opposite path: "
            "**compile a written policy into a deterministic runtime gate** so enforcement is code, not "
            "an LLM judgement. The LLM appears in exactly one pass — **EXTRACT**, with an N=5 majority "
            "vote — and the **RESOLVE** pass then verifies the extracted rules **statically**; the "
            "runtime evaluates each proposed tool call against facts drawn from real tool results and "
            "user turns and allows or blocks in **microseconds with zero LLM**.\n\n"
            "The measured effect is large: state-changing violations fall **66.3% → 2.6%** and **30.8% → "
            "6.9%** (**26x / 4.5x**), AgentDojo banking **ASR 0.0%** against 46.5% undefended, and "
            "**Pass^5 0.51 → 0.67** — the gate does not break the agent. The cost is negligible where it "
            "matters: **3 us/call and zero LLM calls** against a prompt-level baseline's **+74% "
            "wall-clock and 347 calls**.\n\n"
            "The load-bearing caveat is the reason to pair it with a static checker: **RESOLVE repairs "
            "37% and rejects 13% of extracted rules**, so **the generated policy is wrong about a third "
            "of the time.** Operator rule: **treat an LLM-written policy as an input to a checker, never "
            "as the control itself** — extract with a model, verify statically, enforce deterministically. "
            "Pairs K249/intent-governed tool authorization (IGAC) and the MCP execution-control "
            "invariants line. Artifact DOI `10.5281/zenodo.22123419`; implementation proprietary.",
            ["sources/arxiv-2610-11030-nomos-compiled-policy-tool-gate.md",
             "concepts/intent-governed-tool-authorization.md",
             "concepts/mcp-execution-control-invariants.md",
             "concepts/agent-runtime-guardrails.md",
             "concepts/mcp-security-posture.md"],
            ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K288 inbound)")
    for r in ["concepts/intent-governed-tool-authorization.md",
              "concepts/mcp-execution-control-invariants.md",
              "concepts/agent-runtime-guardrails.md",
              "concepts/mcp-security-posture.md"]:
        add_related(r, "sources/arxiv-2610-11030-nomos-compiled-policy-tool-gate.md", NOMOS_NOTE)
        add_related(r, "concepts/nomos-compiled-policy-enforcement.md", NOMOS_NOTE)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
