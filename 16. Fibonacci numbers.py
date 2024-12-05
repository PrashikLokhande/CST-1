def fibonacci(n):
  fib_numbers = [0, 1]
  for i in range(2, n):
    next_fib = fib_numbers[i-1] + fib_numbers[i-2]
    fib_numbers.append(next_fib)
  return fib_numbers

print(fibonacci(10))