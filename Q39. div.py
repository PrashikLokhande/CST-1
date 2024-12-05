def safe_divide(a, b):
    """
    Performs division of two numbers with error handling.

    :param a: Numerator (dividend).
    :param b: Denominator (divisor).
    :return: The result of the division if successful, or an error message if an exception occurs.
    """
    try:
        result = a / b
        return f"The result of {a} divided by {b} is: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        print(safe_divide(numerator, denomin
