import sys
from test_utils import count_pass_fail

# Simulate command line args
test_data = {
    "Login": "pass",
    "Search": "fail",
    "Checkout": "pass"
}

if len(sys.argv) > 1 and sys.argv[1] == "summary":
    summary = count_pass_fail(test_data)
    print("🧪 Summary:", summary)
else:
    print("Usage: python cli_test_summary.py summary")
