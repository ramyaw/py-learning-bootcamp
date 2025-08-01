# Dictionary: test case name → status
test_results = {
    "LoginTest": "pass",
    "SignupTest": "fail",
    "SearchTest": "pass"
}

# Conditional logic
for test, result in test_results.items():
    if result == "pass":
        print(f"{test}: ✅")
    elif result == "fail":
        print(f"{test}: ❌")
    else:
        print(f"{test}: ❓ Unknown status")

# Count pass/fail
passed = sum(1 for status in test_results.values() if status == "pass")
failed = len(test_results) - passed
print(f"\nSummary: {passed} passed, {failed} failed")
