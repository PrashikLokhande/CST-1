import logging

# Configure logging
logging.basicConfig(
    filename="exception_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def perform_math_operation(a, b, operation):
    """
    Performs a mathematical operation on two numbers and logs any exceptions.
    
    :param a: First number.
    :param b: Second number.
    :param operation: The mathematical operation ('add', 'subtract', 'multiply', 'divide').
    :return: The result of the operation or None if an exception occurs.
    """
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        else:
            raise ValueError(f"Unknown operation: {operation}")
    except Exception as e:
        logging.error(f"Error during operation '{operation}' with inputs ({a}, {b}): {e}")
        print(f"An error occurred: {e}. Check the log file for details.")
        return None

# Example usage
if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        result = perform_math_operation(num1, num2, op)
  
