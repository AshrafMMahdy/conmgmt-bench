"""Programme metrics for PRE-01 (and any XER): activity count, link count, relationship-type mix, open starts /
open ends, cycles, longest path length by duration (FS links, lags ignored) — enough to compare a programme's shape.
Usage: python tools/xer_metrics.py path/to/schedule.xer
"""
import sys, collections

def read_xer(path):
    tables, cur, cols = {}, None, None
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if parts[0] == "%T": cur = parts[1]; tables[cur] = []; cols = None
            elif parts[0] == "%F": cols = parts[1:]
            elif parts[0] == "%R" and cur and cols: tables[cur].append(dict(zip(cols, parts[1:])))
    return tables

def metrics(path):
    t = read_xer(path)
    tasks = {r["task_id"]: r for r in t.get("TASK", []) if r.get("task_type") not in ("TT_WBS",)}
    preds = [r for r in t.get("TASKPRED", []) if r["task_id"] in tasks and r["pred_task_id"] in tasks]
    succ = collections.defaultdict(list); pred = collections.defaultdict(list)
    for r in preds: succ[r["pred_task_id"]].append(r["task_id"]); pred[r["task_id"]].append(r["pred_task_id"])
    types = collections.Counter(r.get("pred_type", "?") for r in preds)
    milestones = [k for k, r in tasks.items() if r.get("task_type", "").startswith("TT_Mile") or r.get("task_type") in ("TT_FinMile", "TT_StartMile")]
    open_start = [k for k in tasks if not pred[k]]; open_end = [k for k in tasks if not succ[k]]
    # cycles + longest path (durations in hours / 8)
    dur = {k: float(r.get("target_drtn_hr_cnt") or 0) / 8 for k, r in tasks.items()}
    state, longest, cyc = {}, {}, False
    sys.setrecursionlimit(10000)
    def dfs(n):
        nonlocal cyc
        if state.get(n) == 1: cyc = True; return 0
        if state.get(n) == 2: return longest[n]
        state[n] = 1; best = 0
        for s in succ[n]: best = max(best, dfs(s))
        state[n] = 2; longest[n] = dur[n] + best; return longest[n]
    lp = max((dfs(k) for k in tasks), default=0)
    return {"activities": len(tasks), "milestones": len(milestones), "links": len(preds),
            "non_fs_share": round(1 - types.get("PR_FS", 0) / len(preds), 3) if preds else None,
            "relationship_types": dict(types), "open_starts": len(open_start), "open_ends": len(open_end),
            "has_cycle": cyc, "longest_path_days_fs_no_lag": round(lp, 1),
            "cost_loaded": any(float(r.get("target_cost") or 0) > 0 for r in t.get("TASKRSRC", []))}

if __name__ == "__main__":
    import json; print(json.dumps(metrics(sys.argv[1]), indent=2))
