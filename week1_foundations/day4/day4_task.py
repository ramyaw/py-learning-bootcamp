import json

# 1. Read multiple test run JSONs:
# {
#  "LoginTest": "pass",
#  "SearchTest": "fail",
#  "SignupTest": "pass"
# }
# 2. Count how many times each test failed across all runs
# 3. Write output:
# {
#  "LoginTest": {"failures": 0},
#  "SearchTest": {"failures": 2}
# }

login_test_failure = 0
search_test_failure = 0
signup_test_failure = 0

with open("test1.json", "r") as f:
    data = json.load(f)
    login_count = 1 if data["LoginTest"] == "fail" else 0
    search_count = 1 if data["SearchTest"] == "fail" else 0
    sign_count = 1 if data["SignupTest"] == "fail" else 0
    login_test_failure = login_count
    search_test_failure = search_count
    signup_test_failure = sign_count

with open("test2.json", "r") as f:
    data = json.load(f)
    login_count = 1 if data["LoginTest"] == "fail" else 0
    search_count = 1 if data["SearchTest"] == "fail" else 0
    sign_count = 1 if data["SignupTest"] == "fail" else 0
    login_test_failure += login_count
    search_test_failure += search_count
    signup_test_failure += sign_count

with open("test3.json", "r") as f:
    data = json.load(f)
    login_count = 1 if data["LoginTest"] == "fail" else 0
    search_count = 1 if data["SearchTest"] == "fail" else 0
    sign_count = 1 if data["SignupTest"] == "fail" else 0
    login_test_failure += login_count
    search_test_failure += search_count
    signup_test_failure += sign_count

print(f"LoginTest : {login_test_failure}")
print(f"SearchTest : {search_test_failure}")
print(f"SignUp Test : {signup_test_failure}")

test_results = {
    "LoginTest": {"failures": login_test_failure},
    "SearchTest": {"failures": search_test_failure},
    "SignUpTest": {"failures": signup_test_failure}
}
print(json.dumps(test_results, indent=2))


