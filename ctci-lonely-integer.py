"""
Bit Manipulation: Lonely Integer

https://www.hackerrank.com/challenges/ctci-lonely-integer
"""
import unittest
from functools import reduce


def lonely_integer(arr):
    return reduce(lambda acc, x: acc ^ x, arr)


if __name__ == '__main__':
    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    print(lonely_integer(a))


class TestLonelyInteger(unittest.TestCase):
    def test_lonely_integer(self):
        self.assertEqual(
            1,
            lonely_integer([1]))

        self.assertEqual(
            2,
            lonely_integer([1, 1, 2])
        )

        self.assertEqual(
            2,
            lonely_integer([0, 0, 1, 2, 1])
        )
