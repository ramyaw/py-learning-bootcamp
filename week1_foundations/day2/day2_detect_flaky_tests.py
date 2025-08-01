# test_name → list of statuses across runs
history = {
    "LoginTest": ["pass", "pass", "pass"],
    "SignupTest": ["fail", "pass", "fail"],
    "SearchTest": ["pass", "pass", "pass"],
    "CheckoutTest": ["fail", "fail", "fail"]
}

# Identify flaky tests
for test, statuses in history.items():
    if "pass" in statuses and "fail" in statuses:
        print(f"{test} is flaky ❗")