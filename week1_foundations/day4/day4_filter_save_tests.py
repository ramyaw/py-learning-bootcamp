import csv

with open("test_results.csv", "r") as f:
    reader = csv.DictReader(f)
    failed = [row for row in reader if row["status"] == "fail"]

with open("day4_failed_tests.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["test_name", "status"])
    writer.writeheader()
    writer.writerows(failed)
