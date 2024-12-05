import unittest

def test_calculator(num1, num2, operator, expected_result):
    result = calculate(num1, num2, operator)
    assert result == expected_result

if _name_ == '_main_':
    unittest.main()

# Example usage with test cases:
test_calculator(2, 3, '+', 5)
test_calculator(5, 2, '-', 3)
test_calculator(2, 3, '*', 6)
test_calculator(6, 2, '/', 3)
test_calculator(10, 0, '/', "Error: Division by zero")
test_calculator(2, 3, '$', "Invalid operator")