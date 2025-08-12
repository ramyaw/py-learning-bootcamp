
def count_pass_fail(results: dict) -> dict:
    passed = sum(1 for v in results.values() if v == "pass")
    failed = sum(1 for v in results.values() if v == "fail")
    return {"passed": passed, "failed": failed}

def get_flaky_tests(history: dict) -> list:
    return [test for test, runs in history.items() if "pass" in runs and "fail" in runs]
