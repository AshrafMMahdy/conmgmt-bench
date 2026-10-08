# Tender watch — Hilma screening record (Kymenlaakso groundworks & municipal engineering)

**Run date:** 7 October 2026 · **Cadence:** every two weeks · **Buyer side:** we are the bidder
**Scope of this run:** open public works tenders in Finland fitting the firm's declared trade — **streets, water and sewer networks, cable trenches, foundations** — for municipalities and main contractors, based in **Kymenlaakso**.

---

## 1. Search method and its limits

| Step | Method | Result |
|---|---|---|
| Primary source | Hilma (hankintailmoitukset.fi) via the procurement-notice API, national + EU notices, deadline still open | Used |
| Cross-check | EU TED (Tenders Electronic Daily) filtered to Finland, CPV 45* (construction works) | Used |
| Geo filter | NUTS **FI1C4 / FI1C7** (Kymenlaakso), plus FI1C6 (Päijät-Häme) and FI1B1 (Uusimaa) as adjacent | Used |
| Trade filter | CPV 45000000, 45200000, 4521/4522/4523/4524 families, 45112* (earthworks), 45231300 (water/sewer) | Used |
| Buyer-name filter | Kymenlaakso, Kotka, Hamina, Kouvola, Haminan | Used |
| Free-text on Hilma | "vesihuolto*", "kadunrakennus*", "kunnallistekniikka*", "maanrakennus*", "katu-*" in the title | **0 hits** — the Finnish-language title search returned nothing useful in the window |

**Limits of this run — stated so the shortlist is read with the right confidence:**

- The window is the last 14 days of published notices. A tender published earlier but still open may not have surfaced.
- Hilma's own site was in a maintenance state during part of the run, and the portal hides the tender documents behind a registration; **no tender documents were retrieved for any candidate** (see §5).
- **Nothing in the window is a street/water/sewer urakka let by a Kymenlaakso municipality.** That is the headline finding of this run, and it is not an artefact of the filters — the regional notices that exist are demolition, forest work, property services, waste bins, health services and similar.
- **ASSUMPTION (flagged):** where the firm's maximum contract value, turnover, or operating radius is unknown, the likely role was read from the words of the notice rather than from company data, because no company data exists in the project.

---

## 2. Screening criteria — recorded BEFORE any notice was scored

| Id | Criterion | Weight | One-line rationale |
|---|---|---|---|
| C1 | Scope / trade match | 25 | The firm's declared trades are streets, water and sewer, cable trenches and foundations; anything else is a different business |
| C2 | Geographic / logistics fit | 12 | Crew and plant mobilisation and local incumbency decide margin; distance from Kymenlaakso is the penalty |
| C3 | Resource and plant fit | 12 | Whether the firm's crews and machines can actually execute it |
| C4 | Qualification and technical demands | 12 | The bar the notice sets (models, machine control, special techniques) |
| C5 | Realistic win feasibility as a small firm | 12 | Whether a small regional firm can win against the likely field; a tender you cannot win is not an opportunity |
| C6 | Contract value band and commercial fit | 8 | Whether the value sits in the firm's band — unknown for many notices |
| C7 | Buyer, role and relationship value | 7 | Municipality or main contractor, prime or subcontractor, and whether the buyer is worth building with |
| C8 | Contract-term and compliance risk | 12 | Carried and transferred risk, securities, interface risk |

Scoring is on a 1–5 scale per criterion, weighted; the result is a weighted average out of 5.00, **not** a percentage. Criteria were fixed before any notice was scored, and no weight was changed afterwards.

**Non-substantive records were excluded before scoring** — prior-information notices, market-dialogue invitations, requests for information and duplicate records are not biddable and were labelled, not analysed.

---

## 3. The shortlist — five notices

| Rank | Notice | Buyer | Deadline | One line on fit |
|---|---|---|---|---|
| 1 | **Säterinpuistontie välillä Leppävaarankatu – Turuntie** — notice **2026-057797** | Espoon kaupunki | **26.10.2026 12:00** | **Fits best on scope** — the notice's own words are "street and water-services construction works", the firm's two headline trades; but it is a ~150 km city contract of unknown value in the Helsinki region |
| 2 | **Niemen sataman pilaantuneen maaperän kunnostus** (Niemi harbour, contaminated-soil remediation) | Lahden kaupunki | **16.10.2026 07:00** | Excavation, haulage and replacement of contaminated soil — mass earthworks, but contaminated-soil work rather than street/water, and only 9 days to deadline |
| 3 | **Kaakkois-Suomen elinvoimakeskuksen siltojen ylläpitourakka 2027–2028 (optio 2029)** | KEHA-keskus / Kaakkois-Suomen elinvoimakeskus | **27.10.2026 13:00** | In the home region and a long contract (bridge maintenance, inspections, possibly culvert/pipe bridges with design) — but bridge repair specialism, and the incumbent field is large bridge contractors |
| 4 | **Purku-urakka – Valkealan entinen sairaala** (demolition, former Valkeala hospital) | Kouvolan kaupunki | **26.10.2026 10:00** | In the home municipality and a familiar kind of site work (~9,904 m² building plus yard structures and foundations) — but demolition, and the notice requires the bidder to have familiarised itself with the site at an event held **5.10.2026, already passed** |
| 5 | **KUTSU MARKKINAVUOROPUHELUUN – Sähkönjakeluverkon rakentaminen ja ylläpito 2028–2030** (distribution-network construction and maintenance) | Kymenlaakson Sähköverkko Oy | **20.10.2026 13:00** | **In-trade and in-region** — cable trench and distribution-network construction is the firm's declared trade — but it is a **market-dialogue notice, not a biddable tender**; it is the precursor to the real contract |

**Full screening scores (weighted average out of 5.00):**

| Rank | Notice | C1 (25) | C2 (12) | C3 (12) | C4 (12) | C5 (12) | C6 (8) | C7 (7) | C8 (12) | **Score** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Espoo 2026-057797 | 5 | 1 | 4 | 2 | 2 | 3 | 3 | 2 | **3.02** |
| 2 | Lahti 2026-058007 | 3 | 4 | 5 | 2 | 4 | 3 | 3 | 2 | **3.24** |
| 3 | KASELY 2026-057925 | 2 | 5 | 2 | 3 | 1 | 3 | 4 | 2 | **2.58** |
| 4 | Kouvola 2026-058095 | 2 | 5 | 3 | 2 | 3 | 3 | 5 | 2 | **2.89** |
| 5 | Kymenlaakson Sähköverkko 2026-057645 | — | — | — | — | — | — | — | — | **not scored — non-substantive (market dialogue, not a tender)** |

*(Each score is the criterion score on the 1–5 scale; the total is the weighted average out of 5.00. Recompute: Espoo 125+12+48+24+24+24+21+24 = 302/100 = 3.02; Lahti 75+48+60+24+48+24+21+24 = 324/100 = 3.24; KASELY 50+60+24+36+12+24+28+24 = 258/100 = 2.58; Kouvola 50+60+36+24+36+24+35+24 = 289/100 = 2.89.)*

**How to read this table honestly — and the one thing that must not be glossed over.** On the weighted metric **Lahti scores highest (3.24) and Espoo is second (3.02)**. Lahti takes the metric because mass excavation sits squarely inside the firm's plant capability, Lahti is the closer of the two, and earthworks is a less specialist field — while Espoo loses points on distance and on a technical bar that names machine control, information models and a railway underpass.

**Espoo is nevertheless the pick**, for the reason the firm's own rule names first: **fit**. On the trade-fit criterion — the heaviest criterion, and the one the rule speaks to — Espoo scores **5**, because the notice's scope is "street and water-services construction works", the firm's declared trade on both halves, whereas Lahti is contaminated-soil remediation, a different discipline with its own regulatory regime and its own plant and competence demands. Espoo also wins the second half of the rule, **deadline**: it closes 26.10.2026 with a question window to 19.10.2026, against Lahti's 16.10.2026 and 9 days.

So the weighted metric is a **screening aid**, and the fit-first rule is the **decision rule** — and the override is made in the open here rather than by bending the weights to fit the conclusion. Two caveats belong with it: the spread from 2.58 to 3.24 is narrow, so no candidate is a clear winner on this evidence; and if the firm's **operating radius** proves to be the binding constraint, the metric's preference for the closer Lahti job is the honest counter-argument — and it must be decided today, because Lahti closes in 9 days.

---

## 4. The pick, and why

**Selected: Espoo — Säterinpuistontie, Hilma notice 2026-057797.**

The reason is the one the firm's own rule names first: **fit**. This is the only open, biddable notice in the window whose scope statement is the firm's declared trade on both halves — the notice says the work comprises "katujen ja vesihuollon rakennustöitä", *street and water-services construction works*, and a substantial part of it is exactly what this firm does: street construction, water and sewer networks, foundations, in addition to cable-adjacent trenching.

It also wins on the second half of the rule, **deadline** — but only against the other scope candidate: Espoo closes **26.10.2026** with the question deadline on **19.10.2026**, giving 19 days and a real chance to ask questions, whereas the Lahden Niemi job closes **16.10.2026** with 9 days and no comparable question window.

**The trade-off, stated plainly:** Espoo is **150 km from base**, in the Helsinki metropolitan area, and the surrounding scheme is of the order of **13 M€** (web-sourced context, not the notice). For a small Kymenlaakso firm that means two things: mobilisation cost and local competition on the one hand, and a contract that may simply be too large to prime on the other. **Geography is the price of the fit, and it is a real price.**

**Runner-up gap:** by the weighted metric the runner-up is not behind — it is **ahead**: Lahti 3.24 against Espoo's 3.02, with Kouvola third at 2.89 and KASELY fourth at 2.58. The selection therefore rests on the fit-first rule argued in §3 and above, **not** on the decimal. Neither alternative is a clean substitute: **Lahti** is contaminated-soil remediation, not the declared street/water trade, and closes in **9 days**; **Kouvola** is demolition with a site-familiarisation event that has **already passed** on 5.10.2026, which is a practical bar to bidding it at all.

**The single most valuable action in this run is not a bid.** The one directly on-trade, in-region opportunity is **Kymenlaakson Sähköverkko Oy's market dialogue** for distribution-network construction and maintenance 2028–2030, open to join until **20.10.2026**. It is cable trench and network construction — the declared trade — in the home region, it is free, and engaging it shapes the specification of a 2028–2030 contract before it is tendered. **Recommendation: join that dialogue regardless of what is decided about Espoo.**

---

## 5. Document access — the constraint on every candidate

For **every** candidate in this run, the actual tender documents sit behind the buyer's Cloudia/Tarjouspalvelu supplier portal, which requires registration and log-in. The Espoo notice is the instructive case: its own notice record says document access is **not restricted** (TED BT-14 = "Ei"), yet the portal page states that viewing all the information requires registering and logging in.

**Consequence:** the tarjouspyyntö, bill of quantities, contract terms, award criteria and suitability requirements were **not retrieved for any candidate**, and were therefore not analysed. No attempt was made to work around the registration — no account was created and the buyer was not contacted, per instruction. **Everything downstream of the notice in this run is built on the notice alone, with "not stated" where the notice is silent.**

---

## 6. Full retrieved set — with substantive / non-substantive labels

**Retrieved and de-duplicated: 31 distinct records. Substantive open works notices: 15. Non-substantive (prior-information, market dialogue, request for information, or duplicate): 16. On-trade biddable street/water/sewer works let by a Kymenlaakso municipality: 0.**

| Hilma notice | Buyer | Deadline (UTC) | CPV | NUTS | Substantive? | Label |
|---|---|---|---|---|---|---|
| 2026-057797 | Espoon kaupunki | 2026-10-26 | 45200000 | FI1B1 | **Yes** | open works notice — **SELECTED** |
| 2026-058007 | Lahden kaupunki | 2026-10-16 | 45112340 | FI1C6 | **Yes** | open works notice — shortlist 2 |
| 2026-058222 | Lahden kaupunki | 2026-10-16 | 45112340 | FI1C6 | **No** | **duplicate record** of 2026-058007 (same object, same deadline) |
| 2026-057925 | KEHA-keskus / Kaakkois-Suomen elinvoimakeskus | 2026-10-27 | 45200000 | FI1C7 | **Yes** | open works notice — shortlist 3 |
| 2026-058095 | Kouvolan kaupunki | 2026-10-26 | 45000000 | FI1C7 | **Yes** | open works notice — shortlist 4 |
| 2026-057645 | Kymenlaakson Sähköverkko Oy | 2026-10-20 | 45230000 | FI1C7 | **No** | **market-dialogue / prior-information notice (e1) — not a tender**; shortlist 5 as a future opportunity |
| 2026-057571 | Helsingin kaupunki | 2026-10-15 | 45200000 | FI1B1 | **Yes** | open works notice (underpass) — out of area, not shortlisted |
| 2026-057574 | Helsingin kaupunki | 2026-10-12 | 45200000 | FI1B1 | **Yes** | open works notice (street) — out of area |
| 2026-058825 | Lapuan Jätevesi Oy | 2026-10-21 | 45252100, 45112000, 45231300 | FI199 | **Yes** | open works notice (wastewater) — distant |
| 2026-057827 | Metsähallitus | 2026-10-22 | 45240000, 45111000, 45233200 | FI1D8 | **Yes** | open works notice, €65,000 — distant, small |
| 2026-058407 | Rajavartiolaitos | 2026-11-16 | 45220000, 45110000 | FI1D8 | **Yes** | open works notice — security-classified annexes, distant |
| 2026-056887 | Väylävirasto | 2026-10-16 | 45234100 | FI | **Yes** | open framework (rail area) — €2 M, not the trade |
| 2026-058003 | Vantaan Energia Oy | 2026-10-12 | 45231112, 44162000, 45262400 | FI1B1 | **Yes** | open works notice (process piping) — not the trade |
| 2026-058638 | Tuusulan kunta | 2026-10-13 | 45112720 | FI1B1 | **Yes** | open works notice (park civil works) — out of area |
| 2026-058392 | Varkauden kaupunki | 2026-10-29 | 45233252, 45233253 | FI1DB | **Yes** | open works notice (paving) — €2.5 M, distant |
| 2026-058752 | Stara, Helsingin kaupunki | 2026-10-29 | 45233222 | FI1B1 | **Yes** | open works notice (paving) — €450,000 |
| 2026-057450 | Kuusan Nuorisoseura r.y. | 2026-10-09 | 45000000 | FI198 | **Yes** | open works notice — €280,000, distant |
| 2026-057861 | Karkkilan kaupunki | 2026-10-09 | 90610000, 90620000 | FI1B1 | **Yes** | open works notice (machine services / winter maintenance) — €60,000 |
| 2026-057724 | Sodankylän kunta | 2026-10-12 | 45000000, 45232000 | FI1D7 | **Yes** | open works notice (street lighting) — €60,000, very distant |
| 2026-056516 | Kouvolan kaupunki | 2026-10-13 | 77200000 | FI1C7 | **No** | **out of trade** — forestry work |
| 2026-058399 | Kouvolan kaupunki | 2026-10-16 | 70100000 | FI1C7 | **No** | **out of trade** — property-development services |
| 2026-057117 | Kymenlaakson Jäte Oy | 2026-10-16 | 34928480 | FI1C7 | **No** | **out of trade** — waste-bin supplies |
| 2026-058653 | Kymenlaakson liitto | 2026-10-21 | 75000000 | FI1C7 | **No** | **out of trade** — financial administration services |
| 2026-058346 | Kymenlaakson hyvinvointialue | 2026-10-23 | 85130000 | FI1C7 | **No** | **out of trade** — health services; market dialogue |
| 2026-057179 | Kymenlaakson hyvinvointialue | 2026-10-19 | 79634000 | FI1C7 | **No** | **out of trade** — training services |
| 2026-058611 | Mäntsälän kunta | 2026-11-10 | 45000000, 45200000 | FI1B1 | **No** | **prior-information / market-dialogue notice — not a tender** |
| 2026-058017 | Nakkilan seurakunta | 2026-10-07 | 45000000 | FI196 | **No** | **prior-information notice (ennakkoilmoitus) — not a tender** |
| 2026-058018 | Nakkilan seurakunta | 2026-10-07 | 45000000 | FI196 | **No** | **prior-information notice (ennakkoilmoitus) — not a tender** |
| 2026-058662 | Vaasan kaupunki | 2026-10-31 | 45000000 | FI19A | **No** | **market-dialogue invitation — not a tender** |
| 2026-058383 | Vaasan kaupunki, Talotoimi | 2026-10-13 | 45000000 | FI19A | **No** | **market-dialogue invitation — not a tender** |

**Note on identification:** no notice is listed here with an invented identifier. Each row carries the buyer's own Hilma notice number and, where it was read, the notice's Hilma/Sähköinen id and portal link. Where a record could not be read back by its bare numeric id (the Lahti record resolves instead to an unrelated legacy notice), the row is carried on its notice number alone and that read failure is stated rather than worked around.

---

## 7. Assumptions used in this run (recorded, not hidden)

1. **No company data exists in the project.** No profile, capability statement, rate file, HSE data, financial data or prior run output was found — the working directory and the saved-output list were both empty, and the organisation memory and knowledge wiki returned nothing on this firm. Every company-side judgement in this run is therefore an assumption, and §5 of the tender brief lists the missing facts.
2. **The firm is small.** Read from the user's own description ("small groundworks and municipal-engineering subcontractor"); no headcount, turnover or plant-list data was available.
3. **Operating radius is unknown.** The Espoo-versus-region tension is handled by flagging it as the decision the firm must make, not by assuming an answer.
4. **Likely role.** Where a notice's scale exceeds a small firm's capacity, the realistic role is stated as subcontractor rather than assumed away.
5. **Value for Espoo.** The ~13 M€ figure is **web-sourced context and not from the notice**, and is labelled as such wherever it appears.

---

## 8. Carry-forward to the next run

- Re-check the five shortlisted notices for corrigenda and for the Kymenlaakson Sähköverkko dialogue.
- Hunt specifically for **Kymenlaakso municipal street and water/sewer urakat** — none appeared in this window; if none appears next window either, the recommendation is to build the relationship through the utility market dialogue rather than chase out-of-region city contracts.
- **Fix the standing gap:** obtain the company profile, capability statement, reference list, financials and HSE data, so the next run can screen on facts instead of assumptions. Without it, the same 20 missing-input rows will repeat every fortnight.
