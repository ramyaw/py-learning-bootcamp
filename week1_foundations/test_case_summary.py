test_cases = ["LoginTest", "SignupTest", "SearchTest", "CheckoutTest"]

print("Test case summary")
print(f"Total testcases : {len(test_cases)}")
print("Starts with 'S':")

for name in test_cases:
    if name.startswith("S"):
        print(f" - {name}")