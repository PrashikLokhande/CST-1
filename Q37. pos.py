def check_positive_number(value):
    """
    Checks if the input value is a positive number.
    Raises an exception if the value is not a positive number.

    :param value: The value to check.
    :raises ValueError: If the value is not a positive number.
    """
    if not isinstance(value, (int, float)):
        raise ValueError(f"Input must be a number. Received: {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"Input must be a positive number. Received: {value}")
    print(f"Input is a valid positive number: {value}")

# Example usage
if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        check_positive_number(num)
    except ValueError as e:
        print(f"Error: {e}")
