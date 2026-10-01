# Polaris DC-1 — Productivity Rates Basis
## Computed from NordBuild Historical Database
### Date: 1 August 2026 — For Baseline Programme Submission

---

## 1. METHODOLOGY

Every construction-activity duration in the Polaris DC-1 baseline programme is derived from a productivity rate computed from NordBuild's own historical project data. The formula is:

```
Productivity = BOQ Quantity / (Number of Crews × Members per Crew × Duration in Working Days × 8 hours)
```

This yields a rate expressed in units per man-hour. The Polaris duration is then:

```
Duration = Polaris BOQ Quantity / (Productivity × Crew Size × 8 hours/day)
```

Where the Polaris BOQ quantity is taken from PDC-BOQ-001. An activity with a measurable BOQ quantity (m³, m², lm, nr) uses this quantity-driven method. An activity with no measurable quantity (design, approvals, commissioning tests, procurement, management) uses the historical analog duration directly, adjusted for project scale.

Margin added: a uniform +10% contingency on all quantity-derived durations to account for Finnish winter working (Dec–Mar), learning-curve for data-centre first-build, and the faster tempo of the 22-month programme. This 10% is embedded in every computed duration and flagged in Section 3 below.

---

## 2. HISTORICAL DATABASE — PROJECTS LEANED ON

Data sourced from NordBuild's five-project historical database (ev_1, 990 analogs):

| Project | Type | Location | Planned | Actual | Relevance |
|---------|------|----------|---------|--------|-----------|
| PRJ-001 | Commercial Office | Helsinki | 427 wd | 446 wd | Closest geography; similar ground (bedrock, piling). Primary analog source. |
| PRJ-002 | Commercial Office | Stockholm | 349 wd | 361 wd | Faster programme on PT flat slab — used for best-practice rates. |
| PRJ-003 | Residential | Oslo | 397 wd | 458 wd | Granitic bedrock piling; module-construction experience |
| PRJ-004 | Mixed-Use | Helsinki | 427 wd | 450 wd | Large steel frame — best analog for Polaris steel structure |
| PRJ-005 | Mixed-Use | Stockholm | 540 wd | 586 wd | Basement + complex MEP — used for plant-space rates |

**PRJ-001 is the primary analog** due to Helsinki geography, comparable scale, and data-centre-compatible steel-concrete hybrid structure. PRJ-004 provides the large-scale steel erection rates. PRJ-002 provides the best-practice/target rates where faster delivery was achieved.

---

## 3. COMPUTED PRODUCTIVITY RATES — BY TRADE

### 3.1 SITE PREPARATION & EARTHWORKS

| Activity | Analog | Rate (per man-hr) | Rate (per crew-day¹) | Source |
|----------|--------|-------------------|---------------------|--------|
| Bulk Earthworks & Rough Grading | PRJ-001 | 1.953 m³/man-hr | 125 m³/day (8-man crew) | hist-prj-001-act-132 |
| Basement/Deep Excavation & Shoring | PRJ-001 | 1.562 m³/man-hr | 100 m³/day (8-man crew) | hist-prj-001-act-137 |
| Rock Excavation/Blasting | PRJ-001 | 1.250 m³/man-hr | 80 m³/day (8-man crew) | hist-prj-001-act-137 (adjusted -20% for blasting) |

¹ Crew-day = one 8-man crew working 8 hours. Two-crew gang = 2× this rate.

**Polaris quantities (from BOQ Section A):**
- Site strip & bulk cut: ~12,000 m³ → 48 days with 2-crew gang (250 m³/day) → **53 days** (+10% margin)
- Rock excavation (blasting): ~4,500 m³ → 28 days with 2-crew gang (160 m³/day) → **31 days** (+10% margin)
- Trench excavation for services: ~2,000 m³ → 10 days with 1-crew (100 m³/day) → **11 days** (+10%)

**Winter note:** Bulk earthworks scheduled May–Oct 2026; rock excavation timed outside Dec–Mar freeze window where possible. 10% margin covers spring thaw rework.

### 3.2 PILING & FOUNDATIONS

| Activity | Analog | Rate (per man-hr) | Per crew-day¹ | Source |
|----------|--------|-------------------|---------------|--------|
| Rock-socketed bored piles | PRJ-001 | 0.0347 piles/man-hr | 1.67 piles/rig-day | hist-prj-001-act-134 |
| Pile testing & inspection | PRJ-001 | — | 5 days (LS) | hist-prj-001-act-135 |
| RC Pile caps | PRJ-001 | 0.625 m³/man-hr | 40 m³/day (8-man crew) | hist-prj-001-act-140 |
| Foundation/Ground slab | PRJ-001 | 0.469 m³/man-hr | 30 m³/day (8-man crew) | hist-prj-001-act-141 |
| Waterproofing & tanking | PRJ-001 | 3.125 m²/man-hr | 25 m²/day per man | hist-prj-001-act-139 |

¹ Rig-day = 1 piling rig with 6-man crew (driller + assistants + supervisor + crane).

**Polaris quantities:**
- Piles: ~160 nr (estimated from 4 DH buildings × ~40 piles each) → 48 days with 2 rigs (1.67 × 2 = 3.33/day) → **53 days** (+10%)
- Pile caps: ~960 m³ RC → 12 days with 2-crew gang (80 m³/day) → **13 days** (+10%)
- Ground slabs (4 halls): ~2,400 m³ RC → 40 days with 2-crew gang (60 m³/day) → **44 days** (+10%)
- Waterproofing: ~1,000 m² → 10 days with 1×4 crew (25 m²/man-day × 4 = 100 m²/day) → **11 days** (+10%)

### 3.3 STRUCTURAL FRAME

| Activity | Analog | Rate (per man-hr) | Per crew-day | Source |
|----------|--------|-------------------|--------------|--------|
| RC structural frame (columns, beams, walls) | PRJ-001 | 0.208 m³/man-hr | 10 m³/day (12-man crew) | hist-prj-001-act-145 |
| Precast plank/deck installation | PRJ-001 | 1.389 m²/man-hr | 66.7 m²/day (6-man crew) | hist-prj-001-act-146 |
| Structural steel fabrication | PRJ-004 | — | 35 days (LS, 12-man shop) | hist-prj-004-act-82 |
| Ground floor steel erection | PRJ-004 | — | 8 days per hall (2×8 crew) | hist-prj-004-act-148 |
| Upper floor steel erection | PRJ-004 | — | 40 days per hall (2×10 crew) | hist-prj-004-act-149 |

**Polaris specifics:** Data centre is predominantly steel-frame with precast plank floors. Each hall ~1,500 m² footprint × 2 storeys. Steel fabrication lead time: 35 days shop + delivery. Erection: 8 days GF + 40 days upper per hall. With 2 halls proceeding in staggered parallel (S1 halls first, S2/S3 halls staggered 4 weeks behind), total steel erection: ~96 days critical window.

### 3.4 BUILDING ENVELOPE

| Activity | Analog | Rate (per man-hr) | Per crew-day | Source |
|----------|--------|-------------------|--------------|--------|
| External wall insulation system | PRJ-001 | 3.646 m²/man-hr | 175 m²/day (6-man crew) | hist-prj-001-act-150 |
| Cladding/louvre installation | PRJ-004 | — | 15 days/hall (LS) | hist-prj-004-act-155 |
| Roof waterproofing | PRJ-001 | 4.688 m²/man-hr | 150 m²/day (4-man crew) | hist-prj-001-act-153 |
| Roof insulation & finishing | PRJ-001 | 7.500 m²/man-hr | 240 m²/day (4-man crew) | hist-prj-001-act-154 |

**Polaris quantities:**
- Wall insulation + cladding: ~9,000 m² total (4 DH halls + admin/NOC) → 52 days with 1×6 crew → **57 days** (+10%)
- Roof waterproofing: ~6,000 m² → 40 days with 1×4 crew → **44 days** (+10%)

### 3.5 MECHANICAL & HVAC

| Activity | Analog | Rate (per man-hr) | Per crew-day | Source |
|----------|--------|-------------------|--------------|--------|
| Riser piping (heating/cooling) | PRJ-001 | 0.3125 lm/man-hr | 15 lm/day (6-man crew) | hist-prj-001-act-168 |
| HVAC ductwork | PRJ-001 | 0.781 m²-duct/man-hr | 37.5 m²/day (8-man crew) | hist-prj-001-act-169 |
| Chiller/CRAH installation | PRJ-001 | — | 5 days/unit (4-man crew) | hist-prj-001-act-170 |
| Pipework pre-fabrication | PRJ-004 | — | 12 days (LS) | hist-prj-004-act-172 |

**Polaris specifics:** Data centre cooling is a high-quantity activity. BOQ shows ~1,200 lm of cooling pipework (risers + distribution) and ~480 CRAH fan-wall units. Using the riser pipe rate: 1,200 lm ÷ (15 lm/day × 2 gangs) = 40 days → **44 days** (+10%). CRAH installation: 480 units ÷ 8 units/day (2 crews × 4/day each) = 60 days → **66 days** (+10%).

### 3.6 ELECTRICAL

| Activity | Analog | Duration | Crew | Source |
|----------|--------|----------|------|--------|
| Cable trays & containment — per hall | PRJ-001 | 25 days | 2×8 crew | hist-prj-001-act-183 |
| Main power feeder cables — per hall | PRJ-001 | 10 days | 2×6 crew | hist-prj-001-act-184 |
| Distribution boards — per hall | PRJ-001 | 10 days | 2×6 crew | hist-prj-001-act-185 |
| Transformer & MV switchgear | PRJ-001 | 5 days | 1×4 crew | hist-prj-001-act-180 |
| Main LV switchgear | PRJ-001 | 3 days | 1×4 crew | hist-prj-001-act-181 |
| Generator & UPS installation | PRJ-001 | 3 days | 1×4 crew | hist-prj-001-act-182 |
| Underground LV cables & ducts | PRJ-001 | 5 days | 1×4 crew | hist-prj-001-act-179 |

**All LS (lump-sum) activities — durations used directly.** Data centre electrical scope is typically 3–4× a commercial office; all durations scaled by 2.5× with 10% margin:

- Cable trays (4 halls): 25 days × 2.5 × 1.1 = **69 days** (split across halls with parallel crews)
- Feeder cables (4 halls): 10 days × 2.5 × 1.1 = **28 days**
- Distribution boards (4 halls): 10 days × 2.5 × 1.1 = **28 days**

### 3.7 FIT-OUT & FINISHES

| Activity | Analog | Rate (per man-hr) | Per crew-day | Source |
|----------|--------|-------------------|--------------|--------|
| Internal partition walls | PRJ-001 | 1.406 m²/man-hr | 56 m²/day (10-man crew) | hist-prj-001-act-201 |
| Door frames & hardware | PRJ-001 | — | 10 days (LS) | hist-prj-001-act-202 |
| Raised access flooring | PRJ-001 | 7.292 m²/man-hr | 350 m²/day (6-man crew) | hist-prj-001-act-203 |
| Floor screeds | PRJ-001 | 0.938 m²/man-hr | 30 m²/day (4-man crew) | hist-prj-001-act-204 |
| Wall finishes (paint/tile) | PRJ-001 | 2.604 m²/man-hr | 167 m²/day (8-man crew) | hist-prj-001-act-207 |
| Anti-static flooring | PRJ-001 | 7.292 m²/man-hr | 350 m²/day (6-man crew) | hist-prj-001-act-205 (proxy — raised floor rate) |

**Polaris quantities:** Data halls are ~1,500 m² each with limited partition walls but extensive raised floor and anti-static finish. Admin/NOC has conventional office fit-out.

- Raised floor (4 halls): ~6,000 m² → 17 days with 1×6 crew (350 m²/day) → **19 days** (+10%)
- Wall finishes: admin/NOC only, ~1,500 m² → 9 days with 1×8 crew → **10 days** (+10%)

### 3.8 EXTERNAL WORKS

| Activity | Analog | Rate (per man-hr) | Per crew-day | Source |
|----------|--------|-------------------|--------------|--------|
| Access roads & parking | PRJ-001 | 1.302 lm/man-hr | 62.5 lm/day (6-man crew) | hist-prj-001-act-162 |
| External lighting | PRJ-001 | — | 5 days (LS) | hist-prj-001-act-163 |
| Landscaping & soft works | PRJ-001 | 3.125 m²/man-hr | 100 m²/day (4-man crew) | hist-prj-001-act-164 |
| Perimeter security fencing | PRJ-001 | — | 8 days (LS) | hist-prj-001-act-189 (security proxy) |

### 3.9 COMMISSIONING

All commissioning activities are lump-sum. Values from PRJ-001 (commercial office), scaled 2.0× for data centre complexity:

| Activity | Analog | Base | Polaris | Source |
|----------|--------|------|---------|--------|
| Electrical systems testing — per hall | PRJ-001 | 8 days | 12 days | hist-prj-001-act-217 |
| HVAC commissioning & balancing — per hall | PRJ-001 | 10 days | 15 days | hist-prj-001-act-215 |
| Fire alarm integrated test — per hall | PRJ-001 | 5 days | 7 days | hist-prj-001-act-218 |
| BMS/BAS integrated functional test | PRJ-001 | 8 days | 12 days | hist-prj-001-act-220 |
| Generator load-bank test | PRJ-001 | 5 days | 8 days | hist-prj-001-act-218 (proxy) |
| District heating commissioning (72-hr test) | Contract | — | 5 days | PDC-DH-001 |
| Acoustic & IEQ testing | PRJ-001 | 3 days | 5 days | hist-prj-001-act-222 |

---

## 4. NON-MEASURABLE ACTIVITIES (ANALOG DURATION DIRECTLY)

| Activity Category | Duration | Basis | Source |
|-------------------|----------|-------|--------|
| Architectural design | 25 days | Full design cycle with 14-day Engineer review | PRJ-001 scaled |
| Structural design | 20 days | Follows architectural freeze | PRJ-001 |
| MEP design | 25 days | Data centre complexity — 1.5× commercial | PRJ-001 scaled |
| Civil/external design | 15 days | Standard scope | PRJ-001 |
| Electrical design | 20 days | Data centre complexity | PRJ-001 scaled |
| Procurement (standard items) | 15–25 days | Tender/award/manufacturing cycle | PRJ-001 |
| Procurement (long-lead items) | Per register | PDC-LT-001 is authoritative | Project document |
| Engineer review cycles | 14 days (S1,S3) / 21 days (S2) | Contract Particular Conditions | PDC-PC-001 Rev C |
| Employer payment certification | 45 days | Contract | PDC-PC-001 Rev C |
| Permit/statutory approvals | Per condition | PDC-PP-001 | Project document |
| Finavia crane clearance | 21 days notice | Aviation restriction | PDC-PP-001 |

---

## 5. PROCUREMENT — CRITICAL FINDING

The Procurement Lead Time Register (PDC-LT-001) identifies:

| Item | Lead Time | Order-By Date | Status |
|------|-----------|---------------|--------|
| LT-01 Transformers | 52 weeks | 16 Jan 2026 | **NEGATIVE FLOAT** — order-by date is 6.4 weeks BEFORE Commencement (2 Mar 2026) |
| LT-02 MV Switchgear | 38 weeks | 25 Jun 2026 | Requires early PO |
| LT-03 Generators | 40 weeks | 11 Jun 2026 | Requires early PO |
| LT-04 Chillers/CRAH | 30 weeks | 19 Aug 2026 | Comfortable |
| LT-11 Structural Steel | 18 weeks | 12 Nov 2026 | Comfortable |

**LT-01 transformers must be ordered before Commencement.** This is the single most critical procurement action. NordBuild must either (a) place the transformer order prior to Commencement on an advance purchase agreement, or (b) accept that transformers will arrive 6.4 weeks after programme demand, pushing S1 sectional completion beyond May 2027. This is flagged as RISK-PROC-01 in the Basis of Schedule.

---

## 6. MARGIN AND ADJUSTMENT SUMMARY

| Adjustment | Value | Reason |
|------------|-------|--------|
| Base contingency (all quantity-driven durations) | +10% | First-build learning curve for data centre, Finnish winter productivity, 22-month programme compression |
| Data centre MEP scaling | 2.0–3.5× over commercial office analog | DC MEP density is fundamentally higher — this is scope scaling, not a risk margin |
| Winter productivity (Dec–Mar outdoor activities) | +15% increment | Frozen ground, reduced daylight, snow clearance (not applied separately — embedded in the 10% where winter overlap exists) |
| Summer shutdown (weeks 28–30) | Non-working | Finnish statutory — calendar already coded |
| Blasting hours (08:00–18:00) | -20% effective hours | 10 hrs vs 16 hrs available — rate already adjusted |

---

## 7. QUALIFICATIONS & EXCLUSIONS

1. **Transformer order-by date conflict:** LT-01 cannot be met from a 2-Mar-2026 Commencement. An advance purchase or early access arrangement is required.
2. **No direct data-centre analog exists** in NordBuild's history. All rates are from commercial/mixed-use buildings and scaled for DC density. Where scaling factors are applied, they are stated.
3. **BOQ provisional sums** (PS items in Section H — ELV/BMS) are carried at their stated value but the underlying scope is not yet firm. Any change to PS scope will affect both cost and duration.
4. **Grid connection staged release** in March 2027 (6.5 MVA for Hall 1) gates commissioning. If release slips, S1 cannot achieve sectional completion.
5. **District heating commissioning** requires heating season (Oct–Apr) and 72-hour uninterrupted test at ≥4 MW. This window constraint is embedded.
6. **Rates are productivity (cost-loaded input), not sell rates.** The historical package costs are shown for sanity-check only; the BOQ rates are authoritative for this project.
7. **Contractors' priced schedules** (Sähkö Katajisto, Voima Electric, Nordkraft) were reviewed for labour rate sanity but are subcontract tenders, not binding on the main programme.

---

*End of Productivity Rates Basis — Prepared for Polaris DC-1 Baseline Programme, Revision 0*
