"""Round-1 post graphic: grouped bars (one bar per model per scenario, plus an Average group) relative to baseline 1.0,
with a metrics table under the chart. One SVG, two halves. Stdlib only; PNG via PyMuPDF when available.

Usage: python tools/post_chart.py --out scoring/round1-post.svg
"""
import argparse, json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MODELS = [("haiku-5.5", "Claude Haiku 5.5", "#2a78d6"), ("sonnet-5.5", "Claude Sonnet 5.5", "#eb6834"), ("luna-6", "GPT-6 Luna", "#1baf7a")]
SCEN = [("21", "21_pour-day-truck-dispatch-and-route-markup", "Pour-day dispatch + markup", 0.875),
        ("S4", "S4_P08-ilmatek-EOT-claim-we-assess", "EOT claim assessment", 0.9375),
        ("PRE-01", "PRE-01_baseline-programme", "Baseline programme", 0.917)]
SURFACE, INK, INK2, GRID, LINE = "#ffffff", "#0b0b0b", "#52514e", "#e6e5e1", "#52514e"

# metrics per model (from the run archives: wall minutes, tool steps, input tokens M, cost USD at list price), per scenario order 21, S4, PRE-01
METRICS = {
    "haiku-5.5":  dict(wall=[32, 26, 61],  steps=[27, 71, 146],  tokens=[1.0, 5.9, 16.3],  cost=[0.15, 0.24, 0.60],  finished_alone=2, approved=0),
    "sonnet-5.5": dict(wall=[92, 36, 80],  steps=[109, 150, 192], tokens=[6.7, 16.0, 30.8], cost=[16.9, 10.3, 19.8], finished_alone=3, approved=1),
    "luna-6":     dict(wall=[90, 274, 188], steps=[425, 481, 881], tokens=[37.0, 47.1, 177.0], cost=[0.78, 1.24, 2.55], finished_alone=1, approved=1),
}


def score(run, folder):
    p = os.path.join(ROOT, "scenarios", folder, "scores", f"{run}.json")
    return json.load(open(p, encoding="utf-8"))["final"]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
    rel = {m: [score(m, f) / base for _, f, _, base in SCEN] for m, _, _ in MODELS}
    for m in rel: rel[m].append(sum(rel[m]) / 3)
    groups = [lbl for _, _, lbl, _ in SCEN] + ["Average"]

    W = 1300; L, R, T = 90, 40, 90; ph = 420; B = 70
    pw = W - L - R; ymax = 1.2
    def y(v): return T + ph - (v / ymax) * ph
    o = [f'<text x="{L}" y="40" font-size="26" font-weight="600" fill="{INK}">Three construction management tasks, three models, one platform</text>',
         f'<text x="{L}" y="66" font-size="15" fill="{INK2}">Score relative to our baseline runs (1.00 = DeepSeek V4 Pro, MiniMax M3 and GLM 5.3 Flash, with a planner in the loop). One run per task, follow-ups counted against the score.</text>']
    v = 0.0
    while v <= ymax + 1e-9:
        o.append(f'<line x1="{L}" x2="{L+pw}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="{GRID}" stroke-width="1"/>')
        o.append(f'<text x="{L-10}" y="{y(v)+5:.1f}" font-size="13" text-anchor="end" fill="{INK2}">{v:.1f}</text>'); v += 0.2
    slot = pw / len(groups); bw = 56; gap = 10
    for gi, g in enumerate(groups):
        x0 = L + gi * slot + (slot - (3 * bw + 2 * gap)) / 2
        for mi, (m, name, col) in enumerate(MODELS):
            val = rel[m][gi]; x = x0 + mi * (bw + gap); h = y(0) - y(val); rx = 4
            o.append(f'<path d="M{x:.1f},{y(0):.1f} v{-(h - rx):.1f} q0,{-rx} {rx},{-rx} h{bw - 2*rx} q{rx},0 {rx},{rx} v{h - rx:.1f} z" fill="{col}"/>')
            ly = y(val) - 7 - (10 if abs(val - 1.0) < 0.06 else 0)   # keep the label off the baseline line
            o.append(f'<text x="{x+bw/2:.1f}" y="{ly:.1f}" font-size="14" font-weight="600" text-anchor="middle" fill="{INK}">{val:.2f}</text>')
        o.append(f'<text x="{L + gi*slot + slot/2:.1f}" y="{T+ph+26}" font-size="15" font-weight="600" text-anchor="middle" fill="{INK}">{g}</text>')
    o.append(f'<line x1="{L}" x2="{L+pw}" y1="{y(1):.1f}" y2="{y(1):.1f}" stroke="{LINE}" stroke-width="2" stroke-dasharray="8 5"/>')
    o.append(f'<text x="{L+pw}" y="{y(1)-8:.1f}" font-size="14" font-weight="600" text-anchor="end" fill="{INK2}">baseline 1.00</text>')
    lx = L
    for m, name, col in MODELS:
        o.append(f'<rect x="{lx}" y="{T+ph+44}" width="14" height="14" rx="3" fill="{col}"/>')
        o.append(f'<text x="{lx+20}" y="{T+ph+56}" font-size="14" fill="{INK}">{name}</text>'); lx += 20 + 8 * len(name) + 36

    # ── table ──
    ty = T + ph + B + 20
    cols = ["", "Score ÷ baseline", "Finished without a follow-up", "Reviewer approval", "Wall time per task", "Tool steps per task", "Input tokens per task", "Cost per task (list price)"]
    widths = [190, 120, 170, 130, 130, 130, 130, 150]
    o.append(f'<text x="{L}" y="{ty}" font-size="18" font-weight="600" fill="{INK}">What it took</text>')
    ty += 16
    rows = []
    for m, name, col in MODELS:
        M = METRICS[m]
        rows.append([name, f"{rel[m][3]:.2f}", f"{M['finished_alone']} of 3", f"{M['approved']} of 3", f"{sum(M['wall'])/3:.0f} min", f"{sum(M['steps'])/3:.0f}", f"{sum(M['tokens'])/3:.0f} M", f"${sum(M['cost'])/3:.2f}"])
    rh = 34
    x = L
    for ci, c in enumerate(cols):
        o.append(f'<text x="{x+8}" y="{ty+22}" font-size="13" fill="{INK2}">{c}</text>'); x += widths[ci]
    o.append(f'<line x1="{L}" x2="{L+sum(widths)}" y1="{ty+rh}" y2="{ty+rh}" stroke="{GRID}" stroke-width="1"/>')
    for ri, row in enumerate(rows):
        yy = ty + rh * (ri + 1); x = L
        o.append(f'<rect x="{L+8}" y="{yy+10}" width="12" height="12" rx="3" fill="{MODELS[ri][2]}"/>')
        for ci, cell in enumerate(row):
            o.append(f'<text x="{x + (26 if ci == 0 else 8)}" y="{yy+22}" font-size="14" font-weight="{600 if ci in (0,1) else 400}" fill="{INK}">{cell}</text>'); x += widths[ci]
        o.append(f'<line x1="{L}" x2="{L+sum(widths)}" y1="{yy+rh}" y2="{yy+rh}" stroke="{GRID}" stroke-width="1"/>')
    ty2 = ty + rh * (len(rows) + 1) + 24
    o.append(f'<text x="{L}" y="{ty2}" font-size="12" fill="{INK2}">Averages over the three tasks. Follow-up = the model stopped or asked and had to be told to continue. Reviewer approval = our independent review seat accepted the deliverable.</text>')
    o.append(f'<text x="{L}" y="{ty2+18}" font-size="12" fill="{INK2}">Cost from published per-token prices, prompt-cache reads included. Scoring method and every output: github.com/AshrafMMahdy/conmgmt-bench</text>')
    H = int(ty2 + 46)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Inter, Segoe UI, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="{SURFACE}"/>'] + o + ["</svg>"]
    open(a.out, "w", encoding="utf-8").write("\n".join(svg)); print("wrote", a.out)
    try:
        import fitz
        doc = fitz.open(a.out); pix = doc[0].get_pixmap(matrix=fitz.Matrix(2, 2)); png = os.path.splitext(a.out)[0] + ".png"; pix.save(png); print("wrote", png)
    except Exception as e:
        print("png skipped:", e)


if __name__ == "__main__":
    main()
