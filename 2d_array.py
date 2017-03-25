"""
https://www.hackerrank.com/challenges/2d-array

Context
Given a 2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in to be a subset of values with indices
falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Note: If you have already solved the Java domain's Java 2D Array challenge,
you may wish to skip this challenge.

Input Format

There are lines of input, where each line contains space-separated integers
describing 2D Array ; every value in will be in the inclusive range of to .

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19
"""


def solve(A):
    pattern = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1],
    ]
    pattern_len_row = len(pattern)
    pattern_len_col = len(pattern[0])
    max_value = -999999
    A_len_row= len(A)
    A_len_col = len(A[0])

    for row in range(A_len_row - pattern_len_row + 1):
        for col in range(A_len_col - pattern_len_col + 1):
            pattern_sum = 0

            for p_row in range(pattern_len_row):
                pattern_sum += sum(
                    [a * b for a, b in zip(
                        pattern[p_row], A[row + p_row][col:col + pattern_len_col])])

            if max_value < pattern_sum:
                max_value = pattern_sum

    return max_value


def main():
    A = []
    for _ in range(6):
        A.append(list(map(int, input("").strip().split())))

    print(solve(A))


if __name__ == '__main__':
    main()


import unittest


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(
            19,
            solve([
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0],
            ])
        )
