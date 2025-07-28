"""
Day 1 – Lists & Loops
Python fundamentals with a Java‑style thinking.

Tasks:
1. Create a list of test case names.
2. Print each with its index.
3. Use assertions (Python's built‑in `assert`) to validate expected behavior.
"""

# 1. Define list
test_cases = ["LoginTest", "SignupTest", "SearchTest"]

# 2. Print each with index
for idx, name in enumerate(test_cases, start=1):
    print(f"{idx}. {name}")

# 3. Simple inline checks (like Java assertEquals)
assert len(test_cases) == 3, "Expected 3 test cases"
assert test_cases[0] == "LoginTest", "First test case should be LoginTest"

print("✅ Day 1 checks passed!")
