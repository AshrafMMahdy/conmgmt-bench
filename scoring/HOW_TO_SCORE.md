# How to score a run

Two scores per scenario, reported side by side. Never one number.

## 1. Expectations (every scenario)

`scenarios/<id>/expectations.md` lists 3–6 outcome rules. Score each **0** (not met), **0.5** (partly), **1** (met), with a one-line reason quoting the output. Scenario score = sum / count.

## 2. Key (16 scenarios)

`scenarios/<id>/key/ANSWER_KEY.md` lists planted or expected items. For each: **found** (identified and the key point stated), **partial** (identified, key point missed or wrong), **missed**. Report the three counts. A finding not in the key counts only after it is verified against the source documents — then it counts as a found with a note.


## 3. Deliverables

Say what files were produced and whether they open. A deliverable that is asked for and not produced is a 0 on the expectation that names it; a run that silently substitutes (a folder of images for a deck) scores lower than one that says "no deck".

## 4. Chained vs one-shot

Say which. Chained runs may use earlier deliverables; one-shot runs are scored on the same expectations without allowance.

## 5. Judge rubrics

`judge-rubric-PRE-01/03/06.md` are structured rubrics usable by a human or an LLM judge; they produce a JSON score sheet. Use them if you want the finer grain; the expectations score is still the one that goes on the leaderboard.

## 6. The sheet

Fill `results-template.csv` (one row per scenario) and open a pull request to `leaderboard.md`. Attach the outputs.
