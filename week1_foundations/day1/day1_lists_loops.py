"""
Day 1 – Lists & Loops
Python fundamentals with a Java‑style thinking.

Tasks:
1. Create a list of test case names.
2. Print each with its index.
3. Use assertions (Python's built‑in `assert`) to validate expected behavior.
"""

# 1. Define list
test_cases = ["LoginTest", "SignupTest", "SearchTest", "CheckoutTest"]

# 2. Print each with index
for idx, name in enumerate(test_cases, start=1):
    print(f"{idx}. {name}")

# 3. Simple inline checks (like Java assertEquals)
assert len(test_cases) == 4, "Expected 4 test cases"
assert test_cases[3] == "CheckoutTest", "Last test case should be CheckoutTest"

print("✅ Day 1 checks passed!")
