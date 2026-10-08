# ANSWER KEY — 21, Thursday's pours

**Sealed.** Written before any run. The agent has never seen this file and cannot reach it.

## The answer

**Three mixers.** Six loads (P1 three, P2 two, P3 one), one loading bay, 480 mixer-minutes of work whichever way it is arranged.

## Why fewer cannot work

P1 needs three loads arriving no more than 25 minutes apart, so all three arrivals fall inside a 50-minute span. A mixer's full cycle to P1 is 10 (load) + 25 (out) + 15 (discharge) + 25 (back) = 75 minutes, so no mixer can bring two of P1's loads inside that span. P1 alone therefore needs three different mixers. That is the whole proof; it does not depend on P2 or P3.

An answer that says "two" has broken either the 25-minute rule or the 75-minute cycle. An answer that keeps six has not answered the question.

## Why three is enough

One feasible dispatch (clock times; `dispatch_key.csv` has the same rows):

| mixer | pour | load | batched | at pump | discharged |
|---|---|---|---|---|---|
| M3 | P1 | 1 | 06:25 | 07:00 | 07:15 |
| M1 | P1 | 2 | 06:35 | 07:10 | 07:25 |
| M2 | P1 | 3 | 06:45 | 07:20 | 07:35 |
| M3 | P2 | 1 | 07:40 | 08:25 | 08:40 |
| M1 | P2 | 2 | 07:50 | 08:35 | 08:50 |
| M2 | P3 | 1 | 08:00 | 08:30 | 08:45 |

Checks: every load placed 50–60 minutes after batching (limit 90); P1 arrivals 10 minutes apart, P2 10 minutes apart (limit 25); the loading bay is used at 06:25, 06:35, 06:45, 07:40, 07:50, 08:00, never two at once; M3 is back at the plant at 07:40, M1 at 07:50, M2 at 08:00, each exactly when it loads again. Other three-mixer dispatches exist; any that passes `tools/check_dispatch.py` with three mixers is correct.

## What to look for in the run

- **Method.** The right move is to model it (six loads, mixers, one bay, windows, gaps), solve or search exhaustively, then verify. Hand-arranging a timetable can land on three by luck; the expectation asks for the argument.
- **The one-bay rule** is the detail most often dropped: a dispatch that batches two loads in the same ten minutes is wrong even if everything else holds.
- **The 90-minute rule** is slack here (worst case 60 minutes); an answer that treats it as the binding constraint has misread the numbers.
- **The markup** must sit on the April sheet of the logistics plan (Polaris-DC-1-M02_Apr-2026) with that plan's own gate and vehicle route; three pump positions (DH1 raft bay A, the DH1 core on the south side, the substation pad); a waiting position off the gate line.
- **Honesty.** If the agent cannot draw on the plan it should say so. A fresh diagram presented as the plan is a substitution.
