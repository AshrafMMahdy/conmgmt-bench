# Polaris DC-1 — Aviapolis Data Campus, Phase 1

**Synthetic demonstration project. Not a real project, company, site or contract.** Every document in this folder was authored for this evaluation; names of companies and people are fictional.

## Identity

| Item | Value |
|---|---|
| Project | Polaris DC-1 — Aviapolis Data Campus, Phase 1 |
| Location | Aviapolis, Vantaa, Finland (plot ref 92-52-7-2, fictional) |
| Employer | Polaris Digital Infrastructure Oy — Finnish SPV of an international digital-infrastructure fund |
| Contractor ("us") | NordBuild Oy — general contractor, design and build |
| Engineer | Norvia Consulting Oy (the FIDIC "Engineer") |
| Anchor tenant | Unnamed hyperscaler under NDA — drives the SLA, the phasing and the delay-damages exposure |
| Contract form | FIDIC Yellow Book 2017 General Conditions, amended by Particular Conditions; Finnish governing law |
| Document prefix | `PDC-` |

The Employer's fund uses FIDIC as its house form worldwide; the site, the law and the subcontract market are Finnish (subcontracts on YSE 1998). That mismatch is deliberate and is part of what the scenarios test.

## Facility

| Item | Value |
|---|---|
| IT load | 10 MW — four 2.5 MW data halls |
| White space | ~1,250 m² per hall (~5,000 m² total); GFA ~14,500 m² |
| Form | Single storey + services mezzanine; steel frame, precast wall panels, slab-on-grade |
| Resilience | Tier III equivalent — concurrently maintainable, N+1 |
| Design PUE | ≤ 1.25 annualised |
| Cooling | Indirect adiabatic / free-cooling led, CRAH + chilled water, dry-cooler yard |
| Power | 110/20 kV primary substation, 8 × 2.5 MVA standby generators, UPS + battery rooms per hall |
| Heat recovery | Waste heat to the Vantaa district-heating network |
| Ground | Glacial till over bedrock at 4–9 m; blasting required in the eastern third |

## Commercial and programme baseline

| Item | Value |
|---|---|
| Contract price | EUR 92,400,000 lump sum, design and build |
| Time for Completion | 22 months from the Commencement Date (2 March 2026) |
| Sectional completion | Hall 1 — month 14 · Hall 2 — month 16 · Hall 3 — month 19 · Hall 4 — month 22 |

## Tender packages (eight, three offers each)

| # | Package |
|---|---|
| TP-001 | Earthworks, blasting, piling and substructure |
| TP-002 | Structural steel and precast concrete |
| TP-003 | Envelope — cladding, roofing, louvres |
| TP-004 | Architectural finishes and data-hall containment |
| TP-005 | Mechanical — chillers, dry coolers, CRAH, pipework |
| TP-006 | Electrical — HV/MV switchgear, transformers, UPS, generators, busway |
| TP-007 | ELV, BMS/DCIM, fire detection and suppression |
| TP-008 | External works, security, fibre entry |

## Folder

`01`–`09` is the tender-stage pack the agent receives on day one. Documents that arrive later (subcontract revisions, each month's progress returns, instructions, claims, letters) sit in the scenario that introduces them (`scenarios/<id>/inputs/`) and are added to the project when that scenario starts.

Many documents are deliberately imperfect scans (`_SCANNED`): the agent has to read them as a person would.
