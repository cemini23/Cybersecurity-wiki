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
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/metaverse-security.md
- @concepts/web-pentest-methodology.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/lazarus.md
- @sources/blockchain-and-smart-contract-testing-security.md
- @sources/smart-contract-security-overview-pt-1.md


## Raw Concept

Two corpus PDFs anchor.

## Narrative

Smart-contract security focuses on bytecode (typically EVM — Solidity / Vyper) deployed to public chains. Standard bug classes: reentrancy (DAO 2016), integer overflow/underflow (pre-Solidity 0.8 era), front-running / MEV, oracle manipulation, access-control mistakes (missing onlyOwner), upgradability proxy bugs, signature malleability. Tools: Slither, Mythril, Echidna (fuzzing), Foundry (test framework). Audit firms: OpenZeppelin, Trail of Bits, ConsenSys Diligence. DeFi-specific risks add: liquidity-pool drain via flash loans, governance-token capture.
