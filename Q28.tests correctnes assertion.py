def is_prime(num):
  """Checks if a number is prime.

  Args:
    num: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if num <= 1:
    return False
  if num <= 3:
    return True

  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False

  return True

import unittest

class TestIsPrime(unittest.TestCase):
  def test_prime_numbers(self):
    self.assertTrue(is_prime(2))
    self.assertTrue(is_prime(3))
    self.assertTrue(is_prime(5))
    self.assertTrue(is_prime(7))
    self.assertTrue(is_prime(11))
    self.assertTrue(is_prime(13))

  def test_non_prime_numbers(self):
    self.assertFalse(is_prime(1))
    self.assertFalse(is_prime(4))
    self.assertFalse(is_prime(6))
    self.assertFalse(is_prime(9))
    self.assertFalse(is_prime(10))
    self.assertFalse(is_prime(12))

if __name__ == '__main__':
  unittest.main()
  