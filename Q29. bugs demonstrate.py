def factorial(n):
  if n == 0:
    return 1
  else:
    # Bug: n + 1 instead of n - 1
    # return n * factorial(n + 1)

    # Corrected:
    return n * factorial(n - 1)

# Example usage:
num = 5
result = factorial(num)
print("The factorial of", num, "is:", result)