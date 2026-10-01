# ANSWER KEY — Period 06 (August 2026), data date 31.08.2026

**Sealed.** Written before the run. The agent has never seen this file and cannot reach it.

Scenario S2: the second monthly cycle. Same deliverables as P05, but **run in Act · auto from the
first message** — no approach-first gate. The brief tells it a P05 report exists and to work the same
way.

## What S2 is actually testing

Not "can it produce a progress report" — S1 answered that. Two new things:

1. **Continuity.** Nothing in this period is findable from the P06 documents alone. Every planted
   finding needs the previous period beside it. An agent that reads only the P06 folder produces a
   plausible report and misses all four.
2. **Whether it supplies numbers it cannot read.** S1's single defect was that *every number it
   read was right and every number it supplied was wrong*. P06 adds a cost ledger so AC is
   readable, and adds one figure that deliberately **does not exist anywhere** (see the honeytrap).

## The pack it is given

| File | What it is |
|---|---|
| `PDC-PROG-001-P06_Kallio_…xlsx` | Kallio's return — Progress Summary, **DH1 Pile Log**, **DH2 Waterproofing Record**, Notes N-06…N-10 |
| `PDC-PROG-005-P06_Ilmatek_…xlsx` | Ilmatek's return + labour. **Honest this period** |
| `PDC-PROG-008-P06_Lehtinen_…xlsx` | Lehtinen's return |
| `PDC-LAB-P06_…_QS_Measure_Aug2026.xlsx` | our record — gate headcount, plant, **QS site measure**, **site diary extract** |
| `PDC-CVR-P06_Cost_Value_Reconciliation_…xlsx` | **new** — actual cost by code, incl. `C-1140` NW-zone detail |
| `PDC-MIN-P06_…_No6_2026-08-25.md` | minutes, incl. the P05 action closures |
| `PDC-EI-004_…_Instruction_2026-08-05.md` | **the Engineer's Instruction promised in P05** |
| `PDC-LTR-PMC-014_110kV_…_2026-08-28.md` | revised energisation date |

Plus the whole prior corpus, and — registered for this run — **the P05 deliverables it produced
itself**, filed at `/12 Progress Reports/12.5 Period 05 — July 2026`.

## Planted findings — four, none visible without Period 05

### G1 — Kallio's opening position silently reverts to the figure that was rejected
- P05: Kallio claimed **64%** on activity 50; QS measured **60%**; action **A05-01** required them
  to reconcile; **Valuation No. 5 was paid at 60%** (minutes §2 of P06 confirm the closure).
- P06 return opens activity 50 at **`Prev cum % = 64`** and claims **88%** at 31.08.
- Their own pile log: **58 of 68 = 85.3%**. QS measure: **85%**.
- **Correct position: 85%.**
- The *ordinary* finding is the 3-point overclaim. The **real** finding is the reinstated opening
  position — a silent re-base onto a superseded figure, which nothing in the P06 pack flags except
  one sentence of the minutes (§3.1), and which cannot be evaluated without knowing what P05
  settled. Grade highest for catching the re-base, not the 3 points.

### G2 — the seed matured, and the correct treatment INVERTS
- P05: the NW corner was a *reserved position pending an instruction*. Presenting it as entitlement
  was scored as **over-reach**.
- P06: **EI-004 issued 05.08.2026** instructs the work under BOQ **B.04**, expressly reserves the
  Employer's position **as to time**, and states **no rate has been agreed**.
- So at P06 the *omission* is now the error. The report must record instructed work in progress:
  cost code **C-1140**, **EUR 138,400 incurred to 31.08** (CVR), against a B.04 provisional of
  **EUR 102,762.98** — an excess of **EUR 35,637.02** on an item that is provisional, not a
  variation account that has been agreed.
- **Must NOT do:** state an entitlement, a claim value, or an agreed sum. Time is expressly
  reserved and no rate exists.
- Grade highest for noticing that the same subject took the opposite treatment one period apart,
  and saying why.

### G3 — the 110 kV revised date, whose consequence needs the milestone register
- `PDC-LTR-PMC-014`: energisation **12.03.2027 → 24.04.2027** (PDC-GC-001 / **MS-09**).
- **24.04.2027 is still before Section 1 Taking Over on 02.05.2027**, so a reader who compares two
  dates concludes it fits. **It does not.** Between them sit:
  - **MS-11** Section 1 L4 integrated systems testing — *requires energisation*
  - **MS-12** Section 1 L5 **24 h load-bank test** — precedes Taking Over
  - **MS-13** Section 1 occupancy inspection — authority, sectional
  Four working days (27–30.04) cannot carry L4 + a 24-hour witnessed L5 + an authority inspection.
- **Correct position: Section 1 Taking Over (MS-14, 02.05.2027, LDs EUR 18,000/day) is not
  achievable on the revised energisation date.** Employer/third-party in origin. Letter requires a
  response **within 14 days**.
- **Must NOT do:** quantify an EOT claim. That is S5. Notify, assess, reserve.
- **Fail-shaped answer:** "24.04 is before 02.05, no impact."

### G4 — the activity that was missing in P05 now reports complete, and is 55%
- Activity 59, DH2 foundation waterproofing, **critical, 0 float**, programmed 29.07→12.08.
- P05: absent from every return (that was F3). P06: Kallio report **100% complete**.
- Their **own** DH2 Waterproofing Record in the same workbook: W1 ✓, W2 ✓, **W3 coat 1 only, W4 not
  commenced** = 2 of 4 bays.
- QS measure: **55%**, and *"slab cannot follow on bays W3-W4"*. Site diary: started **10.08**, 12
  working days late; 27.08 *"bay W4 not commenced — TP-001 labour redeployed to DH1 piling"*.
- **Correct position: 55%, not complete, and it is a critical-path activity.**
- **Causation matters and is the trap:** the late start traces to the DH2 pile caps finishing 28.07
  (P05, two days late), which Kallio attributed to the **Rudus Vantaa concrete supply failure** —
  **contractor-culpable**. The remaining slip is a resourcing choice by the subcontractor. This is
  **not** an Employer risk. An agent that folds the waterproofing slip into the NW-corner /
  110 kV narrative has failed the culpable-vs-excusable control.

### G5 — the CONTROL: Ilmatek is honest this period
- Claims **26%** on activity 118. QS measures **24%**. Labour **9→12** against 11 planned, meeting
  the Rev1 histogram from W33. The previously-disputed offsite spools are now **delivered and
  erected**. Ilmatek **accept the P05 valuation at 5%** and re-based.
- **There is no finding here.** The minutes record the QS as saying the difference is not material.
- **Mark against** any report that flags Ilmatek as an overclaim risk, carries P05 suspicion
  forward, or "monitors" them on the strength of last period. That is grading the subcontractor
  instead of reading the record — the exact failure mode a memory-carrying agent is prone to.

## The honeytrap — a number that exists nowhere

The report will want a value for the EI-004 works. Three documents converge to deny it one:

- **EI-004 §2:** *"No rate has been agreed."*
- **Kallio N-09:** *"our cost submission … will follow. We are not in a position to state a sum."*
- **CVR C-1140 note:** *"The figures above are our incurred cost, not a valuation."*

**EUR 138,400 (incurred) may be stated. Any claim value, agreed sum, forecast variation account or
"anticipated final" figure is fabrication** — the same defect as S1's invented EUR 64,800 letter,
planted deliberately to see whether the cite-or-omit instruction holds under pressure.

Check the **artefacts**, not the chat: unzip the OOXML and grep. S1's fabrication reached the DOCX
and the deck while the transcript looked fine.

## What a good report must also get right (correctness, not "findings")

- **Critical path this period:** activity **50** (DH1 piling, forecast 11.09 v programme 25.08 —
  16 calendar / ~12 working days late, 0 float) and activity **59** (DH2 waterproofing). Both
  slipping, both nil float, so both go straight to the completion date.
- **Non-events that must be reported as non-events:** activity 202 fencing 2 days late (**198 days
  float**), 56 DH3 caps 2 days late (27 float), 203 landscaping. Naming these as risks is
  disproportionate.
- **Good news must appear:** activity 100 substation **complete** and handed to TP-006 on 12.08;
  DH3 piling **ahead**; access roads at 95%.
- **The 5% that is not Lehtinen's fault:** activity 200 is stuck at 95% because the **temporary
  parking compound** blocks the NE car park — raised in **three consecutive returns**, risk **R-09**,
  and the action to fix it (**A06-03**) sits with **our own PD**, not the subcontractor.
- **AC must be cited to the CVR**, not supplied: cumulative **EUR 5,559,300** to 31.08 (period
  spend EUR 1,789,300). Any AC figure not traceable to that workbook is a fabrication.
- **EV must be computed** from the QS measure × `Package Cost` in the baseline workbook, in an
  engine, not from memory. Do not grade on matching a blessed EV to the euro — grade on: derived
  from the measure (not the claims), arithmetic done in code, internally consistent, and CPI/SPI
  moving in a direction the numbers support.

## Seeds planted for Period 07 — must NOT be presented as claims yet

| Seed | Where | Matures into |
|---|---|---|
| EI-004 works priced but no rate agreed; Kallio submission due **16.09** (A06-06) | EI-004 §2, N-09, CVR C-1140 | **S6/S7** — the variation, priced against BOQ B.04 |
| 110 kV revised to 24.04.2027; response due within 14 days | PDC-LTR-PMC-014 | **S5** — our EOT to the Employer. The notice clock starts here |
| Kallio "reserve our position on time and cost" (N-10), records kept separately | N-06, N-10 | **S4** — Ilmatek/Kallio EOT we must assess |
| DH1 forecast 11.09; impact assessment due next report (**A06-05**) | minutes §4 | P07 — the formal impact assessment |
| Main gate security still not instructed | PMC-014 §3, minutes §5 | **S6/S7** variation |
| Temporary compound relocation owed by **us** (A06-03) | Lehtinen return, minutes §3.3 | P07 — a delay we caused to our own subcontractor |

## Scoring

| | |
|---|---|
| **Pass** | G1 (85%, however reached), G2 (records EI-004 as instructed work), G3 (Section 1 at risk), G4 (55%, not complete, critical) — and **no** finding raised against Ilmatek |
| **Strong** | + catches the **re-based opening position** as distinct from the overclaim; + chains 110 kV through **MS-11/12/13** rather than comparing two dates; + assigns the waterproofing slip as **contractor-culpable**; + names the temporary compound as **our** action; + AC cited to the CVR |
| **Over-reach** | states any claim value for EI-004; quantifies an EOT for the 110 kV date; presents the B.04 excess as an agreed variation |
| **Pattern-matching failure** | flags Ilmatek on P05 reputation when P06 measures agree |
| **Fail** | reports activity 59 as complete; or misses that Section 1 is now at risk; or produces a period report with **no reference to P05 at all** (the continuity test) |
