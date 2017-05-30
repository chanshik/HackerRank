"""
DFS: Connected Cell in a Grid

https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
"""
import unittest


def getBiggestRegion(grid):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    max_x = len(grid[0])
    max_y = len(grid)
    max_region = 0
    visited = [[0] * max_x for _ in range(max_y)]

    for row in range(max_y):
        for col in range(max_x):
            if visited[row][col] == 1:
                continue
            if grid[row][col] == 0:
                continue

            stk = [(row, col)]
            visited[row][col] = 1
            region_count = 0
            while len(stk) > 0:
                y, x = stk.pop(-1)
                region_count += 1
                if region_count > max_region:
                    max_region = region_count

                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= max_x:
                        continue
                    if ny < 0 or ny >= max_y:
                        continue
                    if visited[ny][nx] != 0:
                        continue

                    if grid[ny][nx] == 1:
                        visited[ny][nx] = 1
                        stk.append((ny, nx))

    return max_region


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for grid_i in range(n):
        grid_t = list(map(int, input().strip().split(' ')))
        grid.append(grid_t)

    print(getBiggestRegion(grid))


class TestBiggestRegion(unittest.TestCase):
    def test_get_biggest_region(self):
        grid = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ]

        self.assertEqual(
            5,
            getBiggestRegion(grid)
        )

    def test_one_region(self):
        grid = [
            [0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]

        self.assertEqual(
            8,
            getBiggestRegion(grid)
        )

    def test_diagonal_region(self):
        grid = [
            [1, 1, 1, 0, 1],
            [0, 0, 1, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0]
        ]

        self.assertEqual(
            9,
            getBiggestRegion(grid)
        )
