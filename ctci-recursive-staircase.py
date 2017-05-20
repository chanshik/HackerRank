"""
Recursion: Davis' Staircase

https://www.hackerrank.com/challenges/ctci-recursive-staircase
"""
import unittest


cache_dict = {}


def solve(n):
    global cache_dict

    if n in cache_dict:
        return cache_dict[n]

    result = 0
    for i in range(1, 4):
        if n - i == 0:
            result += 1
            break

        result += solve(n - i)

    cache_dict[n] = result

    return result


if __name__ == '__main__':
    s = int(input().strip())
    for a0 in range(s):
        n = int(input().strip())

        print(solve(n))


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(
            1,
            solve(1)
        )

        self.assertEqual(
            4,
            solve(3)
        )

        self.assertEqual(
            44,
            solve(7)
        )
