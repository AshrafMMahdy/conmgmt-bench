# Key — bid evaluation (shared by PRE-05 and PRE-06; TP-006 rows and the beyond-price findings apply here)

## 7. BID EVALUATION — EXPECTED FINDINGS (TP-001 to TP-008)

Subcontracts are on **YSE 1998** while the main contract is FIDIC-based, so every offer carries back-to-back gaps a GC must close. Exclusions point at risks seeded elsewhere in the project (BH-12 sulphide, north-west made ground, archaeology, blasting vibration limits, the 12.03.2027 grid date, the Oct-Apr district-heating window).

**The core test: in 5 of the 8 packages the apparent-lowest bidder is NOT lowest once its exclusions are priced back in. In the other 3 it still is** — so a blanket 'lowest bid is a trap' heuristic fails. The agent has to actually normalise.

| Package | Bidder | Headline (EUR) | Normalised (EUR) | Verdict |
|---|---|---|---|---|
| TP-001 | Kallio Maanrakennus Oy | 5,853,540 | 6,547,540 | apparent low |
| TP-001 | Pohjola Infra Oy | 6,370,980 | 6,466,980 | **lowest normalised** |
| TP-001 | Uudenmaan Louhinta Oy | 6,856,080 | 6,856,080 | - |
| TP-002 | Terästyö Vantaa Oy | 8,470,770 | 8,872,770 | apparent low / **lowest normalised** |
| TP-002 | Nordisk Stål & Element AB | 8,953,560 | 8,953,560 | - |
| TP-002 | Rakennus Virtanen Oy | 9,436,350 | 9,436,350 | - |
| TP-003 | Nordic Facade Systems Oy | 5,294,520 | 5,600,520 | apparent low / **lowest normalised** |
| TP-003 | Salo Julkisivu Oy | 5,627,160 | 5,627,160 | - |
| TP-003 | Baltic Envelope Group | 5,532,912 | 5,777,912 | - |
| TP-004 | Sisustus Aalto Oy | 4,504,500 | 4,652,500 | apparent low / **lowest normalised** |
| TP-004 | Interia Rakentajat Oy | 4,666,200 | 4,666,200 | - |
| TP-004 | Vantaan Sisätyö Oy | 4,827,900 | 4,827,900 | - |
| TP-005 | Kylmä-Nordic Oy | 20,623,680 | **28,641,851** † | apparent low |
| TP-005 | Ilmatek LVI Oy | 22,286,880 | 22,286,880 | **lowest normalised** |
| TP-005 | Scandinavian Cooling Partners AB | 23,683,968 | 23,683,968 | - |
| TP-006 | Sähkö Katajisto Oy | 26,611,200 | **31,358,250** † | apparent low |
| TP-006 | Voima Electric Oy | 27,997,200 | 27,997,200 | **lowest normalised** |
| TP-006 | Nordkraft Installation AS | 28,967,400 | 28,967,400 | - |
| TP-007 | Turva ICT Oy | 4,650,030 | 6,335,030 | apparent low |
| TP-007 | Fintronic Systems Oy | 5,183,640 | 5,183,640 | **lowest normalised** |
| TP-007 | Baltic Safety & Controls UAB | 5,056,590 | 5,266,590 | - |
| TP-008 | Maanrakennus Lehtinen Oy | 3,585,120 | 3,770,120 | apparent low |
| TP-008 | Infra Yhtiöt Oy | 3,714,480 | 3,714,480 | **lowest normalised** |
| TP-008 | Vantaa Ympäristörakenne Oy | 3,825,360 | 3,825,360 | - |

Ranking flips on normalisation in: **TP-001, TP-005, TP-006, TP-007, TP-008**. It does not flip in TP-002, TP-003, TP-004.

† **Corrected 2026-08-01, derived from the priced schedules rather than authored.** TP-005 and
TP-006 are the only two packages shipping `.xlsx` priced schedules, so their normalised figures can
be computed instead of asserted — and when a live run levelled TP-006 it produced €31,358,250 and
the key said €28,256,200. The agent was right and the key was wrong.

The correct method, which is what the schedules support: each excluded line is priced back at the
average of what the compliant bidders charge for that same item.

- **TP-006** — Sähkö Katajisto excludes `TP-006.01` (110 kV termination, metering and protection to
  the DNO) at 0. Voima prices it 4,666,200, Nordkraft 4,827,900 → add back **4,747,050**.
  26,611,200 + 4,747,050 = **31,358,250**. The protection coordination study sits inside TP-006.01
  in both compliant offers, so it is not a separate add.
- **TP-005** — Kylmä-Nordic excludes **three** items (`TP-005.04`, `.06`, `.08`), not one. Peers
  price each at 2,591,498 / 2,753,950 → add back 2,672,724 each, **8,018,171** total.
  20,623,680 + 8,018,171 = **28,641,851**.

Both verdicts are unchanged — Ilmatek and Voima remain lowest normalised — but the *margins* in the
original table were far too small, and a grader using them would have marked a correct answer wrong.

**The other six packages have no priced schedules**, so their normalised column is narrative-authored
and has NOT been verified the same way. Treat those figures as indicative of direction only: trust
the verdict column, not the euro amount, and re-derive from the offer documents before failing an
agent on a number.

### Beyond price — findings that should change the award recommendation

Lowest normalised price is still not automatically the right award. The clearest examples:

- **TP-003** Nordic Facade Systems is lowest normalised, but offers a 10-year **materials-only** warranty against the 25-year envelope life in the ER, does not warrant the louvre acoustic performance (we owe 45 dB(A) at the boundary), refuses delay damages and wants 21-day payment against our 45-day inflow.
- **TP-005** Kylma-Nordic excludes the heat-recovery plant, water treatment and L5 support, models only 7,900 free-cooling hours against the 8,300 required, and offers **no PUE/WUE performance guarantee** — while we carry an absolute 1.25 PUE guarantee.
- **TP-006** Sahko Katajisto excludes the 110 kV termination and the protection study, assumes energisation from 1 December 2026 when the DNO's earliest firm date is **12 March 2027**, and refuses delay damages on the package that drives Section 1 (EUR 18,000/day).
- **TP-007** Turva ICT prices sprinklers throughout including white space, contradicting the ER, and excludes the data-hall suppression system and the fire-engineering approval support.
- **TP-004** Sisustus Aalto excludes containment blanking as 'Tenant supply', which contradicts ER section 1.3 — blanking is the Contractor's.

### Recurring back-to-back gaps to close

| Gap | Bidders | Main contract position |
|---|---|---|
| Liability capped at 5-10% of subcontract sum | Kallio, Nordic Facade, Kylma-Nordic, Sahko Katajisto, Turva ICT | Our liability is capped at the Contract Price, with no matching cap in our favour |
| Delay damages not accepted | Kallio, Nordic Facade, Sahko Katajisto | We carry EUR 18,000/day on Section 1 |
| Payment at 21 days | Kallio, Nordic Facade, Kylma-Nordic, Sahko Katajisto, Turva ICT | We are paid at 45 days — a working-capital gap |
| Defects period 12 months | Sisustus Aalto, Turva ICT | 24 months |
| Unfranchised steel indexation | Terasto Vantaa | 13.7 pays only above a 2% cumulative movement |

### Deliberately clean signals

Ilmatek (TP-005) and Voima Electric (TP-006) are priced slightly above the apparent low but carry full scope, warrant performance, accept back-to-back terms, match our 45-day payment and correctly reference the 12.03.2027 grid date and the heating-season window. A good evaluation recommends them and says why.
