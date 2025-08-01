
def summarize_test_results(results: dict) -> dict:
    passed = sum(1 for v in results.values() if v == "pass")
    failed = sum(1 for v in results.values() if v == "fail")
    return {"passed": passed, "failed": failed}

test_results = {
    "LoginTest": "pass",
    "SignupTest": "fail",
    "SearchTest": "pass"
}

summary = summarize_test_results(test_results)
print(summary)  # Output: {'passed': 2, 'failed': 1}
