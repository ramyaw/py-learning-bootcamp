import json
from typing import Dict

# Constants
TEST_FILES = ["test1.json", "test2.json", "test3.json"]
TEST_TYPES = ["LoginTest", "SearchTest", "SignupTest"]


def count_test_failures(data: Dict) -> Dict[str, int]:
    """Count failures for each test type in a single test run"""
    return {
        test_type: 1 if data.get(test_type) == "fail" else 0
        for test_type in TEST_TYPES
    }


def process_test_files(file_paths: list) -> Dict[str, Dict[str, int]]:
    """Process multiple test files and aggregate failure counts"""
    failure_counts = {test_type: 0 for test_type in TEST_TYPES}

    for file_path in file_paths:
        with open(file_path, "r") as f:
            data = json.load(f)
            print(f"{data}")
            test_results = count_test_failures(data)

            for test_type, count in test_results.items():
                failure_counts[test_type] += count

    return {
        test_type: {"failures": count}
        for test_type, count in failure_counts.items()
    }


def main():
    # Process test files and get aggregated results
    test_results = process_test_files(TEST_FILES)

    # Print individual test results
    for test_type, result in test_results.items():
        print(f"{test_type}: {result['failures']}")

    # Print formatted JSON output
    print(json.dumps(test_results, indent=2))


if __name__ == "__main__":
    main()