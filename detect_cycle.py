"""
Linked Lists: Detect a Cycle

https://www.hackerrank.com/challenges/ctci-linked-list-cycle
"""
import unittest


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    short_mover = head
    long_mover = head

    while short_mover is not None or long_mover is not None:
        for _ in range(2):
            if long_mover is None:
                return 0

            long_mover = long_mover.next

        short_mover = short_mover.next

        if short_mover == long_mover:
            return 1

    return 0


class TestDetectCycle(unittest.TestCase):
    def test_has_cycle(self):
        head = Node(1)

        self.assertEqual(
            0,
            has_cycle(head)
        )

        head = Node(1, Node(2, Node(3)))
        head.next.next.next = head.next

        self.assertEqual(
            1,
            has_cycle(head)
        )
