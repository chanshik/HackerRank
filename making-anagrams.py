"""
Strings: Making Anagrams 

https://www.hackerrank.com/challenges/ctci-making-anagrams
"""
import unittest
from collections import Counter


def number_needed(a, b):
    cnt_a = Counter(a)
    cnt_b = Counter(b)

    needed = 0
    for key, cnt in cnt_a.items():
        if key not in cnt_b:
            needed += cnt
        else:
            needed += abs(cnt - cnt_b[key])

    for key, cnt in cnt_b.items():
        if key not in cnt_a:
            needed += cnt

    return needed


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    print(number_needed(a, b))


class TestMakingAnagrams(unittest.TestCase):
    def test_number_needed(self):
        self.assertEqual(
            4,
            number_needed("cde", "abc")
        )
