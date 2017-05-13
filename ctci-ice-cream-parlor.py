"""
Binary Search: Ice Cream Parlor

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
"""
import unittest


def solve(m, arr):
    len_arr = len(arr)
    arr_idx = [(arr[idx], idx + 1) for idx in range(len(arr))]
    sorted_arr = sorted(arr_idx)

    for item, idx in sorted_arr:
        pair = m - item

        left = 0
        right = len_arr
        mid = int(len_arr / 2)
        while left < mid < right:
            mid_value = sorted_arr[mid][0]

            if mid_value == pair:
                return sorted([idx, sorted_arr[mid][1]])

            if mid_value > pair:
                right = mid
                mid = int((left + mid) / 2)

            elif mid_value < pair:
                left = mid
                mid = int((mid + right) / 2)


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))

        answer = solve(m, a)
        print(answer[0], answer[1])


class TestSolve(unittest.TestCase):
    def test_solve(self):
        answer = solve(8, [2, 1, 9, 4, 4, 56, 90, 3])

        self.assertEqual(
            [4, 5],
            answer
        )

        answer = solve(
            295,
            [678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561]
        )

        self.assertEqual(
            [7, 9],
            answer
        )
