"""
Even Tree 

https://www.hackerrank.com/challenges/even-tree
"""
import unittest


class EvenTree(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n

        self.edges = [[0] * (self.n + 1) for _ in range(self.n + 1)]
        self.node_counts = [1] * (self.n + 1)

    def add_edge(self, a, b):
        self.edges[a][b] = 1
        self.edges[b][a] = 1

    def find_even_tree(self):
        def find_leaf_nodes(n, edges):
            results = []

            for node in range(2, n + 1):
                if sum(edges[node]) == 1:
                    results.append(node)

            return results

        def remove_edge(edges, from_, to_):
            edges[from_][to_] = 0
            edges[to_][from_] = 0

        removed_edges = 0
        leaf_nodes = find_leaf_nodes(self.n, self.edges)

        while len(leaf_nodes) > 0:
            for node in leaf_nodes:
                if self.node_counts[node] > 0 and self.node_counts[node] % 2 == 0:
                    removed_edges += 1
                    self.node_counts[node] = 0

                    for to_node_idx in range(self.n + 1):
                        if self.edges[node][to_node_idx] == 1:
                            remove_edge(self.edges, node, to_node_idx)
                            break

            for node in leaf_nodes:
                for to_node_idx in range(self.n + 1):
                    if self.edges[node][to_node_idx] == 1:
                        self.node_counts[to_node_idx] += 1
                        remove_edge(self.edges, node, to_node_idx)
                        break

            leaf_nodes = find_leaf_nodes(self.n, self.edges)

        return removed_edges


if __name__ == '__main__':
    n, m = map(lambda x: int(x), input("").strip().split(" "))

    tree = EvenTree(m, n)

    for _ in range(m):
        from_, to_ = map(lambda x: int(x), input("").strip().split(" "))
        tree.add_edge(from_, to_)

    print(tree.find_even_tree())


class TestEvenTree(unittest.TestCase):
    def test_find_even_tree(self):
        tree = EvenTree(9, 10)
        edges = [
            (2, 1),
            (3, 1),
            (4, 3),
            (5, 2),
            (6, 1),
            (7, 2),
            (8, 6),
            (9, 8),
            (10, 8)
        ]

        for edge in edges:
            tree.add_edge(edge[0], edge[1])

        self.assertEqual(
            2,
            tree.find_even_tree()
        )
