# Higher-order function
def apply_to_list(func, data_list):
    """
    Applies the given function to each element of the list.

    :param func: A function to apply to each element.
    :param data_list: A list of elements.
    :return: A new list with the function applied to each element.
    """
    return [func(item) for item in data_list]

# Example functions to be used
def square(x):
    """Returns the square of a number."""
    return x ** 2

def double(x):
    """Returns double the value of a number."""
    return x * 2

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

# Apply the square function
squared_numbers = apply_to_list(square, numbers)
print("Squared list:", squared_numbers)

# Apply the double function
doubled_numbers = apply_to_list(double, numbers)
print("Doubled list:", doubled_numbers)

# Use a lambda function
incremented_numbers = apply_to_list(lambda x: x + 1, numbers)
print("Incremented list:", incremented_numbers)
