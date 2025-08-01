def test_grade(status):
    if status == "pass":
        return "A"
    elif status.casefold() == "fail":
        return "F"
    else:
        return "?"

print(test_grade("pass"))  # A
print(test_grade("skip"))  # ?
print(test_grade("Fail"))