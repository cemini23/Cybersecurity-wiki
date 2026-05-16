---
title: Blockchain + Smart Contract Security
type: concept
tags: [blockchain, smart-contract, web3]
keywords: [blockchain, smart contract, solidity, evm, defi]
related:
  - concepts/metaverse-security.md
  - concepts/web-pentest-methodology.md
  - entities/people/joas-a-santos.md
  - entities/threat-actors/lazarus.md
  - sources/blockchain-and-smart-contract-testing-security.md
  - sources/smart-contract-security-overview-pt-1.md
  - "@osint-wiki/entities/tools/polymarket-insider-tracker.md"
maturity: draft
created: 2026-05-12
updated: 2026-05-16
---

## Relations

- @concepts/metaverse-security.md
- @concepts/web-pentest-methodology.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/lazarus.md
- @sources/blockchain-and-smart-contract-testing-security.md
- @sources/smart-contract-security-overview-pt-1.md
- @osint-wiki/entities/tools/polymarket-insider-tracker.md — cross-wiki: Polymarket surveillance engine whose funding-chain analysis traces wallet capital back to centralized-exchange hot wallets

## Raw Concept

Two corpus PDFs anchor.

## Narrative

Smart-contract security focuses on bytecode (typically EVM — Solidity / Vyper) deployed to public chains. Standard bug classes: reentrancy (DAO 2016), integer overflow/underflow (pre-Solidity 0.8 era), front-running / MEV, oracle manipulation, access-control mistakes (missing onlyOwner), upgradability proxy bugs, signature malleability. Tools: Slither, Mythril, Echidna (fuzzing), Foundry (test framework). Audit firms: OpenZeppelin, Trail of Bits, ConsenSys Diligence. DeFi-specific risks add: liquidity-pool drain via flash loans, governance-token capture.

**On-chain financial profiling.** For threat-actor financial profiling, on-chain funding-chain analysis can de-anonymize the capital behind a wallet. @osint-wiki/entities/tools/polymarket-insider-tracker.md is a Polymarket surveillance engine whose funding-chain analysis traces wallet capital back to centralized-exchange hot wallets like Binance — a useful technique for attributing the off-ramp side of crypto-financed adversary activity (MIT, https://github.com/pselamy/polymarket-insider-tracker).
