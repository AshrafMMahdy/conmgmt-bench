# ConMgmt-Bench

An open evaluation set for AI agents in construction project management — from tender to claim. Version 1.0.

Twenty scenarios from one synthetic project (Polaris DC-1, a data-campus design-and-build in Finland), covering the work a general contractor's planning, commercial and claims teams actually do: baseline programme, productivity rates, contract analysis across three revisions, bid levelling and award, subcontract gap analysis, programme compliance, drawings, site logistics, a board pack, three month-ends of progress reporting, two claims argued in opposite directions, a variation valuation and a determination response.

Each scenario is a prompt a construction professional would actually send, the documents they would have at that moment, outcome expectations, an answer key where one was written before the run, and **our own outputs as baseline 1.0** — what an acceptable answer looks like, not a ceiling.

- `project/` — the tender-stage document set (contract, drawings, specifications, bill, offers, permits, surveys). Many are deliberate scans.
- `scenarios/` — one folder per scenario: `prompt.md`, `expectations.md`, `key/`, `inputs/` (documents that arrive for that scenario), `baseline-1.0/` (model, outputs, grading). `chain.json` gives the order and dependencies; `_BASELINE_NOTE.md` the caveats.
- `scoring/` — how to score, judge rubrics where they exist, the results template, the leaderboard.
- `tools/` — programme metrics for PRE-01 and a results-sheet builder.

## Running it

Chained is the default: follow `scenarios/chain.json`, add each scenario's `inputs/` to the project before starting it, keep earlier deliverables in the project. One-shot variants (`prompt-oneshot.md`) exist for the tasks the baseline ran as conversations. One run per scenario is enough; say which model, which date, chained or one-shot.

What you need that is not here: the FIDIC Yellow Book 2017 General Conditions (copyright; see `project/01 Contract and Commercial/_NOT_SHIPPED_FIDIC_Yellow_Book_2017.md`).

## Scoring

Per scenario: each expectation 0 / 0.5 / 1, and each key item found / partial / missed. Report both; do not collapse them into one number. `scoring/HOW_TO_SCORE.md` has the detail and `scoring/results-template.csv` the sheet. Send results as a pull request to `scoring/leaderboard.md` with the outputs attached (https://github.com/AshrafMMahdy/conmgmt-bench).

## Sponsored runs

If you want a model or an agent run against the full set and graded by the authors, see `sponsored-runs.md`.

## Licence

Project documents, prompts, keys and baseline outputs: CC BY 4.0 (`LICENSE-DATA.md`). Scripts: MIT (`LICENSE-CODE.md`). The project, companies, people and figures are fictional.
