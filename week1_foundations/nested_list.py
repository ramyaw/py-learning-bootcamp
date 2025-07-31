# Each entry = [test_name, status, retry_count]
run_data = [
    ["Login", "pass", 0],
    ["Signup", "fail", 2],
    ["Search", "pass", 0],
    ["Checkout", "fail", 1]
]

for testName, status, retries in run_data:
    result = "✅" if status == "pass" else f"❌ (retries: {retries})"
    print(f"{testName} : {result}")
