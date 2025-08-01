import csv

with open("test_results.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["test_name"], row["status"])
