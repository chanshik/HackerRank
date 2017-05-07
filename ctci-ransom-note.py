"""
Hash Tables: Ransom Note

https://www.hackerrank.com/challenges/ctci-ransom-note
"""
import unittest
from collections import Counter


def ransom_note(magazine, ransom):
    words = Counter(magazine)

    for word in ransom:
        if word not in words or words[word] == 0:
            return False
        else:
            words[word] -= 1

    return True


if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')

    answer = ransom_note(magazine, ransom)
    if answer:
        print("Yes")
    else:
        print("No")


class TestRansomNote(unittest.TestCase):
    def test_ransom_note(self):
        self.assertEqual(
            True,
            ransom_note("give me one grand today night", "give one grand today")
        )

        self.assertEqual(
            False,
            ransom_note("give me one grand today night", "give one grand hello")
        )

        self.assertEqual(
            False,
            ransom_note("give me one grand today night", "give one grand grand today")
        )
