# Baseline 1.0 — 21

Model: GLM 5.3 Flash · chained (development chat, 2026-10-03; earlier wording of the brief — see `model.json`)

## Expectations

| # | score | reason |
|---|---|---|
| 1 | 0.5 | every rule the earlier brief stated holds (windows, 90 min, 25-min gap, single bay checked); the bench's 15-minute discharge was not in that brief, so `check_dispatch.py` reports 6 discharge violations against the published rules |
| 2 | 1 | three mixers; lower bound argued from the numbers: a mixer's second P1 load cannot start until ≥ 60 min after its first ends, against the 25-min rule |
| 3 | 1 | modelled, exhaustively checked and audited (5-tab audit workbook: sources, model, dispatch, minimisation, checks); reviewer approved from revision 3 |
| 4 | 1 | one row per load with truck, pour, batch, depart, arrive, discharge start/end; agrees with the answer in the chat |
| 5 | n/a | route markup not asked in that brief |

**Mean: 0.875** (over the four expectations asked)

## Key

The key (three mixers, a feasible dispatch) is scored through expectations 1 and 2; it is not averaged in separately for this scenario.

## Deliverables

`Thursday_pour_dispatch_audit.xlsx` (5 tabs), a one-page HTML summary artifact. No markup (not asked).
