"""
Merge Sort: Counting Inversions

https://www.hackerrank.com/challenges/ctci-merge-sort
"""
import unittest


def merge(arr, start, end, tmp):
    mid = int((start + end) / 2)
    left = start
    right = mid + 1
    tmp_idx = left
    count = 0

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            tmp[tmp_idx] = arr[left]
            left += 1
        else:
            tmp[tmp_idx] = arr[right]
            right += 1
            count += mid - left + 1

        tmp_idx += 1

    if left <= mid:
        arr[tmp_idx:end + 1] = arr[left:mid + 1]

    arr[start:tmp_idx] = tmp[start:tmp_idx]

    return count


def count_inversions(arr, start, end, tmp):
    mid = int((start + end) / 2)
    left_count = right_count = 0
    if start < mid:
        left_count = count_inversions(arr, start, mid, tmp)
    if mid + 1 < end:
        right_count = count_inversions(arr, mid + 1, end, tmp)

    merge_count = merge(arr, start, end, tmp)

    return left_count + right_count + merge_count


if __name__ == '__main__':
    t = int(input().strip())
    tmp = [None] * 10000000
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split(' ')))

        print(count_inversions(arr, 0, len(arr) - 1, tmp))


class TestCountInversions(unittest.TestCase):
    def test_count_inversions(self):
        self.assertEqual(
            0,
            count_inversions([1, 1, 1, 2, 2], 0, 4, [None] * 5)
        )

        self.assertEqual(
            4,
            count_inversions([2, 1, 3, 1, 2], 0, 4, [None] * 5)
        )
