# Convert status to severity
status_map = {
    "pass": "low",
    "fail": "high",
    "skip": "medium"
}

statuses = ["pass", "fail", "skip", "fail", "pass"]

severity = [(s, status_map[s]) for s in statuses]
print(severity)  # Output: ['low', 'high', 'medium', 'high', 'low']

# another approach using zip
severity = [status_map[s] for s in statuses]
for status, sev in zip(statuses, severity):
    print(f"Status: {status}, Severity: {sev}")
