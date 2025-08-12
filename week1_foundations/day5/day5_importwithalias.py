import test_utils as utils

data = {
    "TestA": ["pass", "fail", "pass"],
    "TestB": ["pass", "pass", "pass"],
    "TestC": ["fail", "fail", "fail"]
}

print(utils.get_flaky_tests(data))
