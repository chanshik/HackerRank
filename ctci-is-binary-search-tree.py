"""
Trees: Is This a Binary Search Tree?

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
"""
import unittest


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree_(root):
    stk = [(root, 0, 10001)]

    while len(stk) > 0:
        node, min_value, max_value = stk.pop(-1)

        if node.data < 0:
            return False

        if node.left:
            if min_value < node.left.data < node.data:
                stk.append((node.left, min_value, node.data))
            else:
                return False

        if node.right:
            if node.data < node.right.data < max_value:
                stk.append((node.right, node.data, max_value))
            else:
                return False

    return True


class TestCheckBST(unittest.TestCase):
    def test_check_bst(self):
        root = Node(4)

        node = Node(2)
        node.left = Node(1)
        node.right = Node(3)

        root.left = node

        node = Node(6)
        node.left = Node(5)
        node.right = Node(7)

        root.right = node

        self.assertEqual(
            True,
            check_binary_search_tree_(root)
        )
