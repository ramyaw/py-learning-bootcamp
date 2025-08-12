from test_utils import count_pass_fail

suite2 = {
    "AddToCart": "fail",
    "RemoveItem": "pass",
    "ApplyCoupon": "pass"
}

print(count_pass_fail(suite2))
