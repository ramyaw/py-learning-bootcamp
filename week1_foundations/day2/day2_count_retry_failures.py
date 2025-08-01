retries = {
    "LoginTest": 0,
    "SignupTest": 2,
    "SearchTest": 0,
    "CheckoutTest": 1
}

for test, count in retries.items():
    if count > 0:
        print(f"{test} retries = {count}")