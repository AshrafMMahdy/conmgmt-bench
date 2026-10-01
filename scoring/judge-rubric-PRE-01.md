# Judge rubric — PRE-01 baseline programme (judge use only; no planted key — this is a quality checklist)

> Note: this rubric was written for the authors' study. Where it refers to the company's historical database (PRJ-001…PRJ-005, precedent values), that database is not published; do not penalise a run for not citing it.


You grade ONE output set: a Basis of Schedule (docx/md), a schedule workbook (xlsx) and possibly an XER. The
XER's numbers are measured separately by script; you grade what the documents SAY and whether it is grounded.
Read every sheet and section. Quote short evidence for every yes.

**Contract facts (PDC-SC-001 Rev C):** Commencement 2 Mar 2026; Section 1 (Hall 1 + shared infrastructure)
2 May 2027; Section 2 2 Jul 2027; Section 3 2 Oct 2027; Section 4 / Time for Completion 2 Jan 2028.
**Third-party facts:** DNO earliest firm Stage-1 energisation 12 Mar 2027 (two outage windows a year);
transformer lead 52 weeks, whose order-by date falls before Commencement (PDC-LT-001, −6.4 weeks float);
building permit restricts generator/load-bank testing to 09:00–16:00 weekdays while the ER requires a 24-hour
L5 test; DNO Stage 3/4 capacity release dates fall after the Section 3/4 dates; the historical database has
five projects PRJ-001..PRJ-005 (none a data centre) plus a sparse "Aurora Tower" record.

**Score sheet (JSON, nothing else):**
{"contract_dates_stated": true/false,           // all four Section dates + Commencement quoted correctly
 "section_dates_met": {"S1": "met|missed|not stated", "S2": "...", "S3": "...", "S4": "..."},
 "misses_explained_with_arithmetic": true/false, // if any Section is missed: the driving path/arithmetic is shown
 "no_forcing_constraints_claimed": true/false,   // states that no constraint dates force the finish
 "no_open_ends_claimed": true/false,
 "calendars": {"finnish_holidays": true/false, "winter": true/false, "permit_hours": true/false},
 "historical_analogues_named": ["PRJ-001", ...],  // which database projects it says it leaned on
 "analogue_reasoning_given": true/false,          // why those projects, and the honest 'no data-centre precedent' statement
 "productivity_rates_sourced": true/false,        // rates traced to the database / tender, not just asserted
 "resource_histogram_present": true/false, "s_curve_present": true/false,
 "boq_to_activity_method_explained": true/false,
 "flags": {"transformer_pre_commencement": true/false, "dno_energisation_date": true/false, "l5_permit_conflict": true/false, "dno_stage34_release": true/false, "rev_c_supersedes_rev_a": true/false},
 "decisions_requested": <count of explicit decisions asked of the user>,
 "invented_facts": ["..."],                        // numbers/dates/documents not in the pack
 "notes": "one paragraph: would an Engineer accept this Basis of Schedule; biggest weakness"}
