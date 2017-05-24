"""
BFS: Shortest Reach in a Graph

https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
"""
import unittest


class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = [{} for _ in range(self.nodes)]

    def connect(self, from_, to_):
        self.edges[from_][to_] = 1
        self.edges[to_][from_] = 1

    def find_all_distances(self, start):
        d = [0] * self.nodes
        visited = {start: 1}
        q = [(start, 0)]

        while len(q) > 0:
            item = q.pop(0)
            node = item[0]
            distance = item[1]

            for idx in self.edges[node].keys():
                if idx in visited:
                    continue

                q.append((idx, distance + 6))
                d[idx] = distance + 6
                visited[idx] = 1

        results = []
        for node in range(self.nodes):
            if node == start:
                continue

            if d[node] == 0:
                results.append(-1)
            else:
                results.append(d[node])

        return results


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)

        for i in range(m):
            x, y = [int(x) for x in input().split()]
            graph.connect(x - 1, y - 1)

        s = int(input())
        results = graph.find_all_distances(s - 1)

        for result in results:
            print(result, end=' ')

        print("")


class TestGraph(unittest.TestCase):
    def test_find_all_distances(self):
        g = Graph(4)

        g.connect(0, 1)
        g.connect(0, 2)

        self.assertEqual(
            [6, 6, -1],
            g.find_all_distances(0)
        )

        g = Graph(3)

        g.connect(1, 2)

        self.assertEqual(
            [-1, 6],
            g.find_all_distances(1)
        )

    def test_distances(self):
        g = Graph(10)

        g.connect(2, 0)
        g.connect(9, 0)
        g.connect(9, 0)
        g.connect(2, 0)
        g.connect(0, 7)
        g.connect(4, 1)

        self.assertEqual(
            [6, -1, -1, -1, -1, -1, 12, -1, 12],
            g.find_all_distances(2)
        )
