test_cases = ["LoginTest", "SignupTest", "SearchTest", "CheckoutTest"]

reversed_cases = list(reversed(test_cases))
print(f" {reversed_cases}")

# with slicing
print(f"sliced: {test_cases[::-1]}")

# When used in start or end position (before the last colon): -1 means INDEX from end
print(f"sliced 1 : {test_cases[1:-1]}") # start from 1 (signuptest) and leave the last one and keep moving forward which is (searchTest)
print(f"sliced 2 : {test_cases[-3:-1]}") # start from last 3 (signupTest) and leave the last one and move forward which is (searchTest)
print(f"sliced 3 : {test_cases[-2:-1]}") # start from last 2 (searchTest) and leave the last one
print(f"sliced 4 : {test_cases[1::2]}") # start index 1 (SignupTest) and jump 2 from there (checkoutTest)
print(f"sliced 5 : {test_cases[1::3]}") # start index 1 (SignupTest) and jump 3 from there (which is nothing)

# When used in step position (after the last colon): -1 means DIRECTION/STEP
# `[start:end:step]`
print(f"sliced 6 : {test_cases[::-1]}") # start from last and keep jumping 1
print(f"sliced 7 : {test_cases[::-2]}") # start from last and jump to 2 from there
print(f"sliced 8 : {test_cases[::2]}") # start from first and jump to 2 from there
