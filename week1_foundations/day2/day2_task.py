# Write a script to:
# Print ✅ or ❌ next to each test
# Count pass/fail
# Save a summary to summary.txt like:
# Total: 5
# Passed: 3
# Failed: 2

test_results = {
    "LoginTest": "pass",
    "SignupTest": "fail",
    "SearchTest": "pass",
    "CartTest": "fail",
    "LogoutTest": "pass"
}

for test, status in test_results.items():
    result = "✅" if status == "pass" else f"❌"
    print(f"{test} : {result}")

passed_tests = sum(1 for status in test_results.values() if status == "pass")
total_tests = len(test_results)
failed_tests = total_tests - passed_tests

print(f"Total : {len(test_results)}")
print(f"Passed : {passed_tests}")
print(f"Failed : {failed_tests}")

# write to a file called summary.txt
with open('summary.txt', 'w') as f:
    f.write(f"Total: {total_tests}\n")
    f.write(f"Passed: {passed_tests}\n")
    f.write(f"Failed: {failed_tests}\n")
