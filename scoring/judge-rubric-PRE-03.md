# Judge rubric — PRE-03 contract analysis, Rev A (sealed key, judge use only)

> Note: this rubric was written for the authors' study. Where it refers to the company's historical database (PRJ-001…PRJ-005, precedent values), that database is not published; do not penalise a run for not citing it.


You grade ONE output set (a contract review report, possibly with an issues table / register) against the
planted deviations below. Read the whole output first. Then, for each item, decide:

- **found** — the deviation is identified AND the item's key point is stated (the value, or the mechanism named in the key point column)
- **partial** — identified but the key point is missed or wrong (e.g. mechanism named, number not compared; or the clause is flagged with an invented justification)
- **missed** — not identified

Then the discrimination test and the two "needs-other-documents" checks. Do not reward volume; a 30-row table that
misses an item still misses it. Quote the output (a few words) as evidence for every found/partial.

| # | Rev A deviation | Key point the output must make | Sub-Clause |
|---|---|---|---|
| 1 | Payment 75 days | compared to our normal 28–45 days (precedent values) | 14.7 |
| 2 | Engineer certification 42 days + nothing deemed certified | both halves: long certification AND removal of deemed certification | 14.6 + SP-12 |
| 3 | LD cap 20% of Contract Price | our precedent cap is 10% | 8.8 |
| 4 | LD rates 18,000/12,000/12,000/10,000 per day, accruing cumulatively across Sections | cumulative stacking across sections identified; 18,000/day compared against precedent (3,500–12,000) — calling 18,000 "proportionate" = partial | 8.8 + SP-8 |
| 5 | Retention 10%, cash only, no cap, released only at Performance Certificate | at least two of: cash-only / no cap / late release; precedent 5–10% released at Taking Over | 14.3 / SP-13 |
| 6 | No advance payment | precedent 8–10%; working-capital consequence | 14.2 / SP-11 |
| 7 | Defects Notification Period 36 months | precedent 24 months | 11.1 |
| 8 | Subcontractor payment 60 days plus pay-when-paid | pay-when-paid identified (Finnish enforceability point is a bonus) | SP-4 |
| 9 | Claim notice 14 days, absolute bar, no waiver, 20.2.2 disapplied | 14 days vs 28 AND the absolute/no-relief nature | SP-15 |
| 10 | Concurrency bars EOT entirely | apportionment is the normal position | SP-7 |
| 11 | Exceptional Events narrowed (weather, epidemic, authority action excluded) | at least two of the excluded categories named correctly; inventing categories not in the clause = partial | SP-14 |
| 12 | DAAB deleted; arbitration LCIA London | both: no dispute board AND foreign seat vs Finnish precedent | SP-16 / SP-17 |
| 13 | 4.12 deleted — all ground risk on Contractor, site data "for information only" | must connect to the ACTUAL site conditions in PDC-SS-001 (bedrock 4–9 m, blasting east, boulders, made ground NW, sulphide) — an invented site description (e.g. "reclaimed land/landfill") = partial | SP-5 |
| 14 | 1.9 deleted + 5.1 absolute warranty on Tenant KPIs | must name the PUE / availability / WUE (or waste-heat) guarantees and that they originate in the Employer's/Tenant's documents, not ours | SP-2 / SP-6 |
| 15 | 13.7 deleted — no cost adjustment | inflation / indexation exposure over the contract period | 13.7 |
| 16 | 1.15 deleted — uncapped liability | no overall cap / consequential loss exposure | 1.15 |

**Discrimination (false positives).** SP-18 to SP-22 are benign: working hours matching the permit, site
security, Engineer review periods, progress-report content, occupancy inspection at Taking Over. Count how many
of these five the output flags as a risk or deviation (0 is best). Administrative mentions do not count.

**Grounding checks (yes/no each):** (a) cites precedent VALUES from the historical database (numbers, contract
ids) rather than adjectives; (b) states or shows that the base FIDIC General Conditions were consulted;
(c) reads the geotechnical report for item 13; (d) reads the Tenant Annex / ER for item 14.

**Output format (JSON, nothing else):**
{"items": {"1": {"status": "found|partial|missed", "evidence": "..."}, ... "16": {...}},
 "false_positives": {"count": 0-5, "which": ["SP-19", ...]},
 "grounding": {"precedent_values": true/false, "fidic_gc_consulted": true/false, "geotech_read": true/false, "tenant_annex_read": true/false},
 "score": <found + 0.5*partial over items 1-16>,
 "notes": "one paragraph on overall quality and any internal contradictions"}
