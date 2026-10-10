"""Leaderboard chart: one stacked column per scenario, one segment per model run, scores relative to baseline 1.0.

Reads scenarios/<id>/scores/<run>.json (final score 0..1+) and baseline-1.0/grading.md (expectations mean, key counts)
and writes an SVG. Relative score = run final / baseline outcome; a scenario without a baseline is plotted absolute
(1.00 = every expectation met) and marked with an asterisk.

Usage:  python tools/leaderboard_chart.py --runs haiku-5.5,sonnet-5.5 --scenarios 21,S4,PRE-01 --out scoring/round1.svg
Stdlib only. Colors: validated two-slot categorical palette (blue, orange, aqua, yellow ...), 2px surface gaps between
stacked segments, baseline reference line at 1.00, y axis 0..5 in 0.5 steps.
"""
import argparse, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scenarios")
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]   # fixed order, never cycled
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"


def folder_of(sid):
    for f in sorted(os.listdir(ROOT)):
        if f.split("_")[0] == sid: return os.path.join(ROOT, f)
    sys.exit(f"no scenario folder for {sid}")


def baseline_outcome(folder):
    """Expectations mean, averaged with the key score when the scenario has a key. None when no baseline exists."""
    p = os.path.join(folder, "baseline-1.0", "grading.md")
    if not os.path.exists(p): return None, None
    t = open(p, encoding="utf-8").read()
    m = re.search(r"\*\*Mean: ([0-9.]+)\*\*", t); exp = float(m.group(1)) if m else None
    k = re.search(r"\| found \| partial \| missed \|\n\|[-| ]+\|\n\| (\d+) \| (\d+) \| (\d+) \|", t)
    key = None
    if k:
        f, pa, mi = map(int, k.groups()); n = f + pa + mi
        key = (f + 0.5 * pa) / n if n else None
    model = re.search(r"Model: (.+?) ·", t); model = model.group(1) if model else "baseline"
    return (exp if key is None else (exp + key) / 2), model


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", required=True); ap.add_argument("--scenarios", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--ymax", type=float, default=5.0); ap.add_argument("--title", default="ConMgmt-Bench — score relative to baseline 1.0")
    a = ap.parse_args()
    runs = a.runs.split(","); sids = a.scenarios.split(",")
    rows = []   # per scenario: label, [(run, label, rel)], baseline model
    for sid in sids:
        folder = folder_of(sid); base, bmodel = baseline_outcome(folder); segs = []
        for r in runs:
            p = os.path.join(folder, "scores", f"{r}.json")
            if not os.path.exists(p): segs.append((r, r, None)); continue
            d = json.load(open(p, encoding="utf-8"))
            rel = d["final"] / base if base else d["final"]
            segs.append((r, d.get("model", r), rel))
        rows.append((sid + ("" if base else "*"), segs, bmodel))

    W, H, L, R, T, B = 760, 480, 70, 30, 60, 90
    pw, ph = W - L - R, H - T - B
    def y(v): return T + ph - (v / a.ymax) * ph
    slot = pw / len(rows); bw = min(72, slot * 0.5)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Inter, Segoe UI, Arial, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="{SURFACE}"/>',
         f'<text x="{L}" y="30" font-size="16" font-weight="600" fill="{INK}">{a.title}</text>',
         f'<text x="{L}" y="48" font-size="12" fill="{INK2}">Each column stacks the models run on that scenario; 1.00 = that scenario's published baseline run.</text>']
    v = 0.0
    while v <= a.ymax + 1e-9:
        o.append(f'<line x1="{L}" x2="{L+pw}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="{GRID}" stroke-width="1"/>')
        o.append(f'<text x="{L-8}" y="{y(v)+4:.1f}" font-size="11" text-anchor="end" fill="{INK2}">{v:.1f}</text>'); v += 0.5
    o.append(f'<text transform="translate(18,{T+ph/2:.0f}) rotate(-90)" font-size="12" text-anchor="middle" fill="{INK2}">score ÷ baseline</text>')
    for i, (label, segs, bmodel) in enumerate(rows):
        x0 = L + i * slot + (slot - bw) / 2; cum = 0.0
        for j, (run, mlabel, rel) in enumerate(segs):
            if rel is None: continue
            y1, y0 = y(cum + rel), y(cum); top = (j == len([s for s in segs if s[2] is not None]) - 1)
            h = max(0, y0 - y1 - (0 if j == 0 else 2))   # 2px surface gap between stacked segments
            rx = 4 if top else 0
            o.append(f'<path d="M{x0:.1f},{y0 - (0 if j==0 else 2):.1f} v{-(h - rx):.1f} q0,{-rx} {rx},{-rx} h{bw - 2*rx:.1f} q{rx},0 {rx},{rx} v{h - rx:.1f} z" fill="{PALETTE[j % len(PALETTE)]}"/>')
            if h >= 16: o.append(f'<text x="{x0+bw/2:.1f}" y="{(y0+y1)/2+4:.1f}" font-size="11" font-weight="600" text-anchor="middle" fill="#ffffff">{rel:.2f}</text>')
            cum += rel
        o.append(f'<text x="{x0+bw/2:.1f}" y="{y(cum)-6:.1f}" font-size="11" text-anchor="middle" fill="{INK}">Σ {cum:.2f}</text>')
        o.append(f'<text x="{x0+bw/2:.1f}" y="{T+ph+20}" font-size="12" font-weight="600" text-anchor="middle" fill="{INK}">{label}</text>')
        o.append(f'<text x="{x0+bw/2:.1f}" y="{T+ph+36}" font-size="10" text-anchor="middle" fill="{INK2}">baseline: {bmodel or "none"}</text>')
    o.append(f'<line x1="{L}" x2="{L+pw}" y1="{y(1):.1f}" y2="{y(1):.1f}" stroke="{INK2}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    o.append(f'<text x="{L+pw}" y="{y(1)-6:.1f}" font-size="11" text-anchor="end" fill="{INK2}">baseline 1.00</text>')
    lx = L
    for j, r in enumerate(runs):
        name = next((s[1] for row in rows for s in row[1] if s[0] == r and s[2] is not None), r)
        o.append(f'<rect x="{lx}" y="{H-28}" width="12" height="12" rx="2" fill="{PALETTE[j % len(PALETTE)]}"/>')
        o.append(f'<text x="{lx+18}" y="{H-18}" font-size="12" fill="{INK}">{name}</text>'); lx += 18 + 7 * len(name) + 28
    if any(r[0].endswith("*") for r in rows): o.append(f'<text x="{L+pw}" y="{H-18}" font-size="11" text-anchor="end" fill="{INK2}">* no published baseline: plotted absolute, 1.00 = every expectation met</text>')
    o.append("</svg>")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(o)); print("wrote", a.out)


if __name__ == "__main__":
    main()
