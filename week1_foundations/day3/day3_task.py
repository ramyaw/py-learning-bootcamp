#Mini Project:
#Read a list of [test_name, retry_count (str)]
#Convert retry count to int safely
#Count how many tests were retried more than once
#Print a summary

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return -1

test_results = {
    "LoginTest": "1",
    "SignupTest": "2",
    "SearchTest": "3"
}

retry_counts = []
for test, retry in test_results.items():
    retry_int = convert_to_int(retry)
    print(f"{test} : {retry_int}")
    retry_counts.append(retry_int > 1)

count = sum(retry_counts)
print(f"Summary - Total tests that were retried : {count}")
