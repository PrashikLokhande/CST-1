import logging

def log_function_call(func):
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
    result = func(*args, **kwargs)
    print(f"{func.__name__} returned: {result}")
    return result
  return wrapper

@log_function_call
def add(x, y):
  return x + y

@log_function_call
def subtract(x, y):
  return x - y

if __name__ == "__main__":
  result_add = add(5, 3)
  result_subtract = subtract(10, 4)