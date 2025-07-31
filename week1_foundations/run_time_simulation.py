# Tuple: (test_name, duration in seconds)
results = [("Login", 2.1), ("Signup", 3.4), ("Search", 1.8), ("Checkout", 4.0)]

# Print all tests > 3s
for test_name, time in results:
    if time > 3.0:
        print(f"{test_name} took too long: {time}s")

# Find average run time
average = sum(a for _, a in results) / len(results)
print(f"⏱️ Avg run time: {average:.2f}s")

