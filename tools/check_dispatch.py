"""Scenario 21 — check a mixer dispatch against the stated rules.

    python tools/check_dispatch.py <dispatch.xlsx | dispatch.csv> [--sheet NAME]

Reads one row per load with columns (names matched loosely, any order):
  mixer/truck · pour · load · batched · at pump/arrive/on site · discharged/placed
Times as HH:MM. Prints every violation and the mixer count; exit code 0 = feasible.
"""
import csv, re, sys

POURS = {"P1": dict(vol=24, ws="07:00", we="09:20", travel=25),
         "P2": dict(vol=16, ws="07:30", we="09:30", travel=35),
         "P3": dict(vol=8, ws="08:30", we="10:20", travel=20)}
CAP, LOAD, UNLOAD, LIMIT, GAP = 8, 10, 15, 90, 25
COLS = {"mixer": ("mixer", "truck", "vehicle"), "pour": ("pour", "element"), "load": ("load", "load number", "load no", "trip"),
        "batched": ("batched", "batch", "batching", "loaded", "leaves plant", "depart"),
        "arrive": ("at pump", "arrive", "arrival", "on site", "at site"),
        "placed": ("discharged", "placed", "discharge end", "finished")}

def mins(s):
    m = re.search(r"(\d{1,2})[:.h](\d{2})", str(s))
    if not m: raise ValueError(f"not a time: {s!r}")
    return int(m.group(1)) * 60 + int(m.group(2))

def hhmm(m): return f"{m // 60:02d}:{m % 60:02d}"

def read_rows(path, sheet=None):
    if path.lower().endswith(".csv"):
        with open(path, newline="", encoding="utf-8-sig") as f:
            return list(csv.reader(f))
    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[sheet] if sheet else None
    if ws is None:
        for cand in wb.worksheets:
            head = [str(c.value or "").lower() for c in next(cand.iter_rows(min_row=1, max_row=1))]
            if any(any(k in h for k in COLS["mixer"]) for h in head) and any(any(k in h for k in COLS["pour"]) for h in head):
                ws = cand; break
        ws = ws or wb.worksheets[0]
    rows = []
    for r in ws.iter_rows(values_only=True):
        vals = ["" if v is None else (v.strftime("%H:%M") if hasattr(v, "strftime") else v) for v in r]
        if any(str(v).strip() for v in vals): rows.append(vals)
    return rows

def parse(rows):
    head = [str(h).strip().lower() for h in rows[0]]
    idx = {}
    for key, names in COLS.items():
        for i, h in enumerate(head):
            if any(h == n or h.startswith(n) or n in h for n in names) and i not in idx.values():
                idx[key] = i; break
    missing = [k for k in COLS if k not in idx]
    if missing: raise SystemExit(f"columns not found: {missing}; header was {head}")
    out = []
    for r in rows[1:]:
        try:
            pour = re.search(r"P\s*([123])", str(r[idx["pour"]]).upper())
            if not pour: continue
            out.append(dict(mixer=str(r[idx["mixer"]]).strip(), pour="P" + pour.group(1), load=int(re.search(r"\d+", str(r[idx["load"]])).group()),
                            batched=mins(r[idx["batched"]]), arrive=mins(r[idx["arrive"]]), placed=mins(r[idx["placed"]])))
        except Exception as e:
            print(f"skipped row {r!r}: {e}")
    return out

def check(loads):
    v = []
    for L in loads:
        p = POURS[L["pour"]]
        if L["arrive"] - L["batched"] < LOAD + p["travel"]:
            v.append(f"{L['mixer']} {L['pour']} load {L['load']}: batched {hhmm(L['batched'])} but at pump {hhmm(L['arrive'])} — needs at least {LOAD + p['travel']} min (10 load + {p['travel']} drive)")
        if L["placed"] - L["arrive"] < UNLOAD:
            v.append(f"{L['mixer']} {L['pour']} load {L['load']}: discharge shorter than {UNLOAD} min")
        if L["placed"] - L["batched"] > LIMIT:
            v.append(f"{L['mixer']} {L['pour']} load {L['load']}: placed {L['placed'] - L['batched']} min after batching (limit {LIMIT})")
        if L["arrive"] < mins(p["ws"]) or L["placed"] > mins(p["we"]):
            v.append(f"{L['mixer']} {L['pour']} load {L['load']}: at pump {hhmm(L['arrive'])}–{hhmm(L['placed'])}, window {p['ws']}–{p['we']}")
    for pour, p in POURS.items():
        need = -(-p["vol"] // CAP)
        got = sorted(L["arrive"] for L in loads if L["pour"] == pour)
        if len(got) != need: v.append(f"{pour}: {len(got)} loads delivered, {need} needed ({p['vol']} m3 at {CAP} m3)")
        for a, b in zip(got, got[1:]):
            if b - a > GAP: v.append(f"{pour}: {b - a} min between arrivals {hhmm(a)} and {hhmm(b)} (max {GAP})")
    bay = sorted(L["batched"] for L in loads)
    for a, b in zip(bay, bay[1:]):
        if b - a < LOAD: v.append(f"loading bay: loads batched at {hhmm(a)} and {hhmm(b)} overlap (one bay, {LOAD} min each)")
    by = {}
    for L in loads: by.setdefault(L["mixer"], []).append(L)
    for m, ls in by.items():
        ls.sort(key=lambda L: L["batched"])
        for a, b in zip(ls, ls[1:]):
            back = a["placed"] + POURS[a["pour"]]["travel"]
            if b["batched"] < back: v.append(f"{m}: batches {b['pour']} load {b['load']} at {hhmm(b['batched'])} but is only back at the plant at {hhmm(back)}")
    return v, len(by)

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sheet = sys.argv[sys.argv.index("--sheet") + 1] if "--sheet" in sys.argv else None
    if not args: raise SystemExit(__doc__)
    loads = parse(read_rows(args[0], sheet))
    viol, n = check(loads)
    print(f"{len(loads)} loads, {n} mixers")
    for x in viol: print("VIOLATION:", x)
    print("FEASIBLE" if not viol else f"INFEASIBLE ({len(viol)} violations)")
    sys.exit(0 if not viol else 1)
