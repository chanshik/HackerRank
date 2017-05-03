"""
Arrays: Left Rotation

https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""
import unittest


def array_left_rotation(arr, n, k):
    result = [arr[k]]
    result.extend(arr[k + 1:])
    result.extend(arr[0:k])

    return result


if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))

    answer = array_left_rotation(a, n, k)

    print(*answer, sep=' ')


class TestLeftRotation(unittest.TestCase):
    def test_left_rotation(self):
        self.assertEqual(
            [5, 1, 2, 3, 4],
            array_left_rotation([1, 2, 3, 4, 5], 5, 4)
        )
