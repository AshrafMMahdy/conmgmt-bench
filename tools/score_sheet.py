"""Collect per-scenario score files into one results CSV.
Each scenario folder may hold scores/<run-name>.json: {"model":..,"date":..,"mode":..,"expectations":[0,0.5,1,...],
"key":{"found":n,"partial":n,"missed":n},"deliverables":"...","notes":"..."}.
Usage: python tools/score_sheet.py <run-name> > results.csv
"""
import csv, json, os, sys
run = sys.argv[1]; root = os.path.join(os.path.dirname(__file__), "..", "scenarios")
out = csv.writer(sys.stdout); out.writerow(["scenario", "model", "date", "mode", "expectations_score", "expectations_count", "key_found", "key_partial", "key_missed", "deliverables_produced", "notes"])
for folder in sorted(os.listdir(root)):
    p = os.path.join(root, folder, "scores", run + ".json")
    if not os.path.exists(p): continue
    d = json.load(open(p, encoding="utf-8")); e = d.get("expectations", []); k = d.get("key", {})
    out.writerow([folder.split("_")[0], d.get("model"), d.get("date"), d.get("mode"), round(sum(e) / len(e), 3) if e else "", len(e), k.get("found", ""), k.get("partial", ""), k.get("missed", ""), d.get("deliverables", ""), d.get("notes", "")])
