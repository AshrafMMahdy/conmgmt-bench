# Judge rubric — PRE-06 TP-006 electrical bid levelling (sealed key, judge use only)

> Note: this rubric was written for the authors' study. Where it refers to the company's historical database (PRJ-001…PRJ-005, precedent values), that database is not published; do not penalise a run for not citing it.


You grade ONE output set (a levelling schedule, usually xlsx, plus a recommendation memo). Read every sheet and
the memo. Quote evidence for every yes.

**Key facts (from the priced schedules and offers):**
- Headline sums: Sähkö Katajisto Oy 26,611,200 · Voima Electric Oy 27,997,200 · Nordkraft Installation AS 28,967,400 (EUR).
- Katajisto excludes TP-006.01 (110 kV termination, metering and protection to the DNO) priced at 0; the
  protection coordination study sits inside .01 in both compliant offers. Priced back at the average of the
  two compliant bidders' item .01 (4,666,200 and 4,827,900 → 4,747,050): Katajisto normalises to **31,358,250**.
  Voima and Nordkraft carry full scope: 27,997,200 and 28,967,400 unchanged.
- Correct award: **Voima Electric Oy** — lowest normalised, full scope, back-to-back terms, quotes the real
  DNO date. Nordkraft is a clean second. Katajisto is the trap.
- Beyond price, Katajisto: assumes grid energisation from 1 Dec 2026 while the DNO's earliest firm date is
  12 Mar 2027; refuses delay damages on the package that drives Section 1 (EUR 18,000/day); caps liability at
  5–10% of subcontract sum against our 100%-of-Contract-Price exposure; asks 21-day payment against our 45-day
  inflow (and the main contract's 30-day floor).
- A method that prices the exclusion differently (e.g. BOQ rate plus a premium) is acceptable if it is sourced
  and the award still goes to Voima; record the number it reached.

**Score sheet (JSON, nothing else):**
{"award": "Voima|Nordkraft|Katajisto|none",
 "award_correct": true/false,
 "headline_sums_correct": true/false,
 "exclusion_identified": true/false,            // Katajisto's 110 kV / DNO interface exclusion named
 "katajisto_normalised": <number the output states, or null>,
 "katajisto_within_0_5pct_of_key": true/false,   // 31,358,250 ± 0.5% (31,201,459 – 31,515,041)
 "voima_unchanged": true/false, "nordkraft_unchanged": true/false,
 "ranking_flip_stated": true/false,              // cheapest headline becomes dearest once levelled
 "dno_date_caught": true/false,                  // 1 Dec 2026 assumption vs 12 Mar 2027 firm date
 "delay_damages_refusal_caught": true/false,
 "liability_cap_caught": true/false,
 "payment_term_caught": true/false,
 "scan_read": true/false,                        // the scanned offer was actually read (its terms cited), not skipped
 "invented_facts": ["..."],                      // numbers or terms not in the documents
 "notes": "one paragraph"}
