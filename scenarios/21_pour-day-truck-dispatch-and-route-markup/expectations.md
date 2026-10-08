# Expectations — 21

Outcome rules a good answer meets. Score each 0 / 0.5 / 1; see `scoring/HOW_TO_SCORE.md`.

1. The dispatch respects every stated rule — pump windows, placement within 90 minutes of batching, at most 25 minutes between arrivals on the same pour, one loading bay, a mixer on one trip at a time. Check it mechanically: `python tools/check_dispatch.py <workbook or csv>`.
2. The mixer count is the minimum (the key says how many) and the answer shows why fewer cannot work — an argument from the numbers, not "I tried and could not".
3. The problem is treated as what it is: modelled and solved (an exact solver, a search, or an exhaustive check that is shown), not hand-arranged. The run says what method it used.
4. The workbook has the columns asked for, one row per load, with clock times a plant dispatcher can act on, and it agrees with the answer in the chat.
5. The route markup is drawn on the April sheet of the site logistics plan in the project — gate, vehicle route, the three pump positions, a waiting position — on one page. If the plan could not be marked up, the answer says so instead of substituting a sketch on a blank page.
