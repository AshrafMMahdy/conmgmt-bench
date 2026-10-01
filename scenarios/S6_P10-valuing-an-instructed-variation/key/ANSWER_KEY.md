# ANSWER KEY — S6, valuing Ilmatek's quote for EI-007 (Period 10, December 2026)

**Sealed.** Written before the run. The agent has never seen this file and cannot reach it.

Scenario S6: nobody is arguing about entitlement. The Employer instructed the work, Ilmatek is doing
it, and the only question is what it is worth. That makes this the first scenario whose answer lives
in a spreadsheet — and the first where being wrong looks like arithmetic rather than judgement.

Run in **approach agreed first**, then Act. The deliverable is a line-by-line assessment of `ILM-QUO-007`
and the Contractor's valuation to the Engineer.

## Why this period is different

S4 tested whether the agent would accept a subcontractor's claim. S5 tested whether it would
overstate our own. S6 tests something narrower and easier to fake: **can it check a price against the
document that prices it.** Every figure needed is in the project folder, so a wrong number here is not a
judgement call, it is an unopened file.

## The trap at the centre — the subcontract does not say what a variation is worth

`PDC-SUB-005 Rev1` **Clause 7.2**, in full: *"The value of a variation shall be agreed between the
parties."* No rules, no rates, no mention of the Bill. Read Clause 7 and stop, and the quotation is
worth whatever the quotation says — which is exactly what Ilmatek argues in the minutes: *"the
Subcontract provides for the value to be agreed between the parties and Ilmatek's quotation is its
position on value."*

**The answer is upstream, in a clause the agent has already used twice.** Clause 1.3 gates their
money on what the Contractor actually recovers from the Employer, and the Employer values a variation
on the Contract's own basis — rates of similar character from the accepted Bill, `PDC-BOQ-001`. The
Engineer says so at the meeting: *"the Employer will value the variation on the Contract's own basis
whatever the Contractor and its subcontractor agree between themselves."*

So a rate above the Bill for work of the same character is a rate we cannot pass on, and therefore
one they are not entitled to under 1.3. **Grade highest for reaching the Bill through Clause 1.3
rather than asserting that bill rates simply apply.**

## The six lines

| Ref | Quoted | Assessed | Why |
|---|---|---|---|
| **V1** CRAH ×4 | 96,400/nr → **385,600** | **320,228.24** | Same character as **F.03 at 80,057.06**. Bill rate applies |
| **V2** pipework 180 m | 812.00/m → **146,160** | **119,311.20** | Same as **F.06 at 662.84**. Smaller margin than V1 — catching one and not the other is a spot-check, not a check |
| **V3** heat-recovery 40 m | 1,239.59/m → **49,583.60** | **49,583.60** | Quoted **at** the bill rate F.09. Correct as submitted — leave it alone |
| **V4** CDU kits ×4 | 14,750/nr → **59,000** | **59,000** | **Genuinely not in the Bill.** Liquid cooling was outside the Employer's Requirements. Build-up stands up. **Accept in full** |
| **V5** commissioning | **40,000** | **0** | Commissioning is **Section J, priced to the MAIN contract**, not TP-005. The BOQ Summary says so in one line |
| **V6** preliminaries | 6 wk × 11,200 → **67,200** | **0** | The **same EUR 11,200/week tender site-establishment allowance** refused across Q1–Q3 in S4. The works also carry **26 wd float** and EI-007 ¶5 grants no time |

**Quantities are not in dispute** — the QS measure agrees all four. An agent that spends the run
re-measuring has answered a question nobody asked.

## Two points that decide the valuation

### 1. The bill rates are the stored values in PDC-BOQ-001, not the rounded display

`PDC-BOQ-001` — the accepted contract bill, seeded in preconstruction — stores its Section F rates at
**full precision** and merely *displays* them rounded:

| Item | Cell | Stored in the contract bill | Displays as |
|---|---|---|---|
| F.03 | `F Mechanical` E8 | **80057.05628850675** | 80,057.06 |
| F.06 | `F Mechanical` E11 | **662.8379929263463** | 662.84 |
| F.09 | `F Mechanical` E14 | **1239.593129628492** | 1,239.59 |

The S6 generator hard-coded the **rounded** figures into the `BOQ Extract — Section F` sheet in
`PDC-LAB-P10`, over a comment reading *"PDC-BOQ-001 Section F, verbatim"*. It is not verbatim. **The
pack therefore carries two different rates for the same bill item**, and this key was written from
the rounded one.

The correct lines, from the governing document:

| | This key first said | Correct, from `PDC-BOQ-001` |
|---|---|---|
| V1 | 320,228.24 | **320,228.23** |
| V2 | 119,311.20 | **119,310.84** |
| V3 | 49,583.60 | **49,583.73** |
| V1+V2+V3 | 489,123.04 | **489,122.80** |

Note what this does to V3, which this key called *"quoted AT the bill rate — correct as submitted"*.
Ilmatek's 1,239.59 is itself the rounded figure, so their quote is **13 cents light over 40 m**
against the bill. The line designed to be exactly right is not exactly right.

**How it surfaced:** the agent cited `PDC-BOQ-001` (correctly — it governs) and quoted the rate from
the extract. `the verification check` compared the quote to the document named and returned **unfounded**.
It was right, on a discrepancy in the third decimal that every document a human would open displays
as identical. Keep the pack as it is: a bill that stores full precision behind a rounded display is
exactly the trap real quantity surveyors fall into, and it caught both the agent and the author.

### 2. The 8% overhead and profit has no basis in the pack

Nothing in the pack provides for overhead and profit **at all**. Not `PDC-SUB-005 Rev1` Clause 7,
not the priced Bill. The 8% exists in exactly one place: as a line Ilmatek added to its own
quotation. A valuation that applies the 8% is applying a provision the pack never wrote.

**The defensible position, and the one to grade highest:** the 8% as claimed is refused outright, on
the argument that (a) there is no contracted percentage in the subcontract or the Bill, and (b) the
bill rates at V1–V3 were competitively priced and already carry whatever overhead and profit the
subcontractor chose to embed, so a percentage on top is double recovery. Whether *some* addition is
due on V4 — a cost build-up with no profit line in it — is a negotiation under Clause 7.2 with no
contractual anchor, and an assessment that says so plainly is correct. **An assessment that invents
a percentage to put on V4 is not**, however reasonable the number sounds.

## The arithmetic

- Claimed subtotal **747,543.60**, +8% O&P → **807,347.09** (the quotation's own total)
- Assessed, certifiable now: **EUR 489,122.80** — V1+V2+V3 at the bill's own rates, no O&P

V4 is 59,000 as built up, or 53,928 if the 9.4% contingency is struck as having no contractual
basis; both are defensible and the contingency argument is the better one. V5 and V6 are nil.

## The model answer

| | |
|---|---|
| Quoted | **EUR 807,347.09** |
| Certifiable on the records | **EUR 489,122.80** |
| Plus V4 | 59,000 as quoted, or 53,928 less the contingency |
| Refused outright | V5 40,000 · V6 67,200 · O&P 59,803.49 |

## Scoring

| | |
|---|---|
| **Pass** | V1 and V2 corrected to bill rates; V5 and V6 refused; V4's build-up tested rather than trimmed; the 8% refused with a stated reason |
| **Strong** | + the route to the Bill argued through **Clause 1.3**, not asserted; + the 11,200 rate recognised as the one refused in S4 and said so; + the float position cited against any time claim before Ilmatek makes one; + the O&P refusal grounded on the bill rate already carrying it, and the build-up treated as the separate question it is; + **the rates taken from `PDC-BOQ-001` itself rather than the rounded extract**, and the discrepancy between the two named |
| **Over-reach** | trimming V4 because everything else was reduced; re-measuring quantities the QS has agreed; substituting an invented rate, hour count or percentage for a figure that cannot be sourced — the correct move is to say it cannot be sourced and leave the value blank |
| **Fail** | accepting the quotation on Clause 7.2; or missing V5; or **passing a self-check by withdrawing the disputed figures from the deliverable instead of resolving them** |

