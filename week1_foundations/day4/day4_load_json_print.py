import json

with open("summary.json", "r") as f:
    data = json.load(f)
    print("Summary:")
    print("Total:", data["total"])
    print("Passed:", data["passed"])
    print("Failed:", data["failed"])
