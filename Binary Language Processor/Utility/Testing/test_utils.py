from Utility.utilities import print_colored

def test(func, test_val, expected_result):
    actual_result = func(test_val)
    if actual_result == expected_result:
        print_colored("Passed", color="green")
    else:
        print_colored("Failed at: " + str(test_val), color="red")
        print_colored("Expected Result: ", color="red")
        print(expected_result)
        print_colored("Actual Result: ", color="red")
        print(actual_result)