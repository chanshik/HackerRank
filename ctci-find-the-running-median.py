"""
Heaps: Find the Running Median

https://www.hackerrank.com/challenges/ctci-find-the-running-median
"""
import unittest
import heapq


class RunningMedian(object):
    def __init__(self):
        self.low_heap = []
        self.high_heap = []

    def get_median(self, v):
        high_len = len(self.high_heap)
        low_len = len(self.low_heap)

        if high_len == 0:
            heapq.heappush(self.high_heap, v)
            return v

        high_min = self.high_heap[0]

        if low_len == 0:
            if high_min <= v:
                heapq.heappush(self.high_heap, v)
                high_min = heapq.heappop(self.high_heap)
                heapq.heappush(self.low_heap, -high_min)
            else:
                heapq.heappush(self.low_heap, -v)

            return (self.high_heap[0] - self.low_heap[0]) * 0.5

        low_max = -self.low_heap[0]

        if high_len == low_len:
            if low_max <= v:
                heapq.heappush(self.high_heap, v)
            else:
                heapq.heappush(self.low_heap, -v)
                low_max = -heapq.heappop(self.low_heap)
                heapq.heappush(self.high_heap, low_max)

            return self.high_heap[0]

        else:
            if high_min <= v:
                heapq.heappush(self.high_heap, v)
                high_min = heapq.heappop(self.high_heap)
                heapq.heappush(self.low_heap, -high_min)
            else:
                heapq.heappush(self.low_heap, -v)

            return (self.high_heap[0] - self.low_heap[0]) * 0.5


if __name__ == '__main__':
    n = int(input().strip())
    median = RunningMedian()

    for _ in range(n):
        value = int(input().strip())

        print("{0:.1f}".format(median.get_median(value)))


class TestMedian(unittest.TestCase):
    def test_get_median(self):
        items = [12, 4, 5, 3, 8, 7]
        answer = [12.0, 8.0, 5.0, 4.5, 5.0, 6.0]

        median = RunningMedian()

        for idx in range(len(items)):
            self.assertEqual(
                answer[idx],
                median.get_median(items[idx])
            )

    def test_sample(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]

        median = RunningMedian()

        for idx in range(len(items)):
            self.assertEqual(
                answer[idx],
                median.get_median(items[idx])
            )
