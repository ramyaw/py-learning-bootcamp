import json

summary = {
    "total": 3,
    "passed": 2,
    "failed": 1
}

with open("summary.json", "w") as f:
    json.dump(summary, f, indent=2)
