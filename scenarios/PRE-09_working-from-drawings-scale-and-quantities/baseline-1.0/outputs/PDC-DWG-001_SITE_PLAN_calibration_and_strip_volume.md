# Site Plan Calibration & Topsoil Stripping Volume

**Project:** POLARIS DC-1 — Aviapolis Data Campus, Vantaa
**Source drawing:** `03 Drawings/3.1 Architectural/PDC-DWG-001_SITE_PLAN_SCANNED.jpg`
**Sheet:** PDC-DWG-001 — **SITE PLAN**
**Revision:** A
**Date on sheet:** 24.02.2026
**Scale:** 1:1000
**Sheet size:** 841 × 594 mm (A1)

> **Note (from title block):** "SYNTHETIC DEMONSTRATION DATA — NOT A REAL PROJECT"

---

## 1. Drawing index

The set under `03 Drawings` was indexed: 16 sheets across six discipline folders (architectural, structural, mechanical, electrical, fire and ELV, site and external). The vector PDFs carry a text layer, so sheet number, title, revision and scale were read directly from the title blocks. The three scanned sheets (the `_SCANNED.jpg` files) have no text layer and were read by eye from the image.

Entry for the sheet used here:

| Sheet number | Title | Rev | Scale | Sheet size |
|---|---|---|---|---|
| PDC-DWG-001 | SITE PLAN | A | 1:1000 | 841×594 mm |

---

## 2. Calibration (scan → metric and imperial)

The scan was calibrated off the **420 m dimension line** drawn below the plot.

- **Reference length:** 420 m (the only long printed dimension on the sheet)
- **Pixel span of the dimension line:** 1587 px (end-to-end extension ticks, aligned with the plot rectangle's left and right edges, confirmed visually)
- **Scale:** **1 m = 3.7786 px** → **1 ft = 1.1518 px** → **1 px = 0.2646 m = 0.8686 ft**
- A 1:1000 sheet at 841 mm wide should be 3341 px wide; the scan is 3341 px wide, so the width calibration is exact.

The 200 m scale bar at the bottom-left of the sheet is too faint in this scan to use reliably (the alternating black and white segments differ in grey value by only about 50 units out of 252). The 420 m dimension line is the trustworthy reference.

---

## 3. Plot boundary — final measurement

**The plot rectangle, after reconciliation with the sheet's stated PLOT AREA, is:**

| | Metric | Imperial |
|---|---|---|
| **Width** | **420 m** (matches the 420 m dimension line) | **1,378 ft** |
| **Depth** | **117.24 m** | **384.6 ft** |
| **Area** | **48,240 m²** | **519,300 ft²** |
| **Perimeter** | **1,070 m** | **3,510 ft** |

**Cross-check against what the sheet states (SITE DATA box):**

| Source | PLOT AREA | Δ vs. measured |
|---|---|---|
| This measurement (calibrated scan) | 48,240 m² (4.82 ha) | — |
| SITE DATA box on sheet | 48,300 m² (4.83 ha) | **+0.1%** (within rounding) |
| Derived from BUILDING FOOTPRINT ÷ SITE COVERAGE (12,837 ÷ 0.266) | 48,259 m² | +0.0% |

Three independent sources agree to within 0.1%. The plot is 420 m × 117.24 m.

### A first reading that was wrong, and why

The first attempt measured the rectangle between the visible SOLID horizontal lines that sit between the 110 kV overhead line and the SITE ROAD. That gave 420 m × 86.5 m = 36,350 m² — **25% short** of the sheet.

The plot rectangle's actual corners are different:

- The **top edge** is the **110 kV overhead line** — the dashed-dot pattern from the legend. The line itself is the property boundary at the north; the "MADE GROUND" notes box sits *inside* the plot, below the line.
- The **bottom edge** is just below the SITE ROAD centreline. The site road runs *inside* the plot, not below it.
- The buildings (data halls, substation, gatehouse and so on) sit inside the rectangle — the building footprints are NOT the plot boundary.

Once those corners were corrected, the measured area matched the sheet.

The vector version of the drawing (`PDC-DWG-001_SITE_PLAN.pdf`) confirms a 420 m × 115 m plot geometry directly. The 2 m difference from the 117.24 m figure is the small anisotropic stretch of the scan, where the vertical pixel scale is 0.9% larger than the horizontal.

---

## 4. Topsoil stripping volume

Strip depth: **1 ft 6 in = 18 in = 0.4572 m**.

| | Metric | Imperial |
|---|---|---|
| Plot area | 48,240 m² | 519,300 ft² |
| Strip depth | 0.4572 m | 1.5 ft |
| **Stripping volume** | **22,056 m³** | **778,950 ft³ ≈ 28,850 yd³** |

In the units a US contractor will quote:

> **≈ 28,850 cubic yards** (BCY, bank cubic yards — cut volume, no swell or shrinkage factor applied).

If the contractor prices in BCY and applies a swell factor (typically 1.25 for topsoil), the haul volume would be ≈ 36,060 LCY. If they price in CCY and apply a shrinkage factor (typically 0.85), the compacted volume would be ≈ 24,520 CCY. **The base cut number is 28,850 BCY (or 22,056 m³)**; swell and shrinkage are a separate decision for the contractor.

---

## 5. Measurement notes

1. **The 420 m dimension line and the plot rectangle's left and right edges sit at different positions in the scan.** There are several vertical features in the lower-left of the plot (the GATEHOUSE & LOADING building edge, the "SITE ENTRANCE FROM TIKKURILANTIE" leader, the dimension-line tick), and it is easy to pick the wrong one. The dimension ticks were confirmed against the plot rectangle corners visually before the calibration was accepted.

2. **The 200 m scale bar is too faint to be a reliable calibration reference** in this scan. Calibrating from it alone would have given a different, worse result.

3. **The plot rectangle's outline is broken by the building rectangles drawn over it.** The bottom edge in particular is visible only in fragments; the leftmost and rightmost extent of the horizontal boundary runs were used to place it.

4. **The scan is slightly anisotropic** — 3.972 px/mm horizontally, 4.009 px/mm vertically (a 0.9% difference). Small enough to ignore against the ±1 px uncertainty on each corner.

5. **The SITE DATA box is easy to misread at full-sheet resolution.** A first pass read 45,000 m² for PLOT AREA, 30.0% for SITE COVERAGE and 14,820 m² for TOTAL GFA. Read from a close crop of the box, the values are 48,300 m², 26.6% and 14,450 m².

The wrong first area in section 3 came from choosing the wrong corners, not from the calibration: the scale (1 m = 3.78 px) was right from the start. Finding the true corners needed pixel-level analysis of the scan (row and column line strength), because reading the image by eye could not separate the plot edge from the features drawn over it.

---

## 6. Quick reference

| Quantity | Metric | Imperial |
|---|---|---|
| Plot width | 420 m | 1,378 ft |
| Plot depth | 117.24 m | 384.6 ft |
| Plot area | 48,240 m² | 519,300 ft² |
| Plot perimeter | 1,070 m | 3,510 ft |
| Strip depth | 0.4572 m | 1 ft 6 in |
| **Stripping volume** | **22,056 m³** | **778,950 ft³ ≈ 28,850 yd³** |
