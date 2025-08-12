from test_utils import count_pass_fail, get_flaky_tests

# Sample data
test_results = {
    "LoginTest": "pass",
    "SignupTest": "fail",
    "SearchTest": "pass",
    "CheckoutTest": "fail"
}

summary = count_pass_fail(test_results)
print("Summary:", summary)

run_history = {
    "LoginTest": ["pass", "pass"],
    "SignupTest": ["fail", "pass", "fail"],
    "SearchTest": ["pass", "pass"],
    "CheckoutTest": ["fail", "fail"]
}

flaky = get_flaky_tests(run_history)
print("Flaky tests:", flaky)
