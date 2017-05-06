"""
Time Complexity: Primality

https://www.hackerrank.com/challenges/ctci-big-o
"""
import unittest
import math


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    upper_bound = int(math.sqrt(n) + 1)
    for i in range(3, upper_bound + 1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    p = int(input().strip())
    for a0 in range(p):
        n = int(input().strip())

        print("Prime" if is_prime(n) else "Not prime")


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(
            False,
            is_prime(12)
        )

        self.assertEqual(
            True,
            is_prime(5)
        )

        self.assertEqual(
            True,
            is_prime(7)
        )
