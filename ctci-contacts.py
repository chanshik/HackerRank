"""
Tries: Contacts

https://www.hackerrank.com/challenges/ctci-contacts
"""
import unittest


class ContactManager(object):
    def __init__(self):
        self.contacts = []
        self.partial_index = {}  # partial -> contacts

    def indexing(self, name):
        for idx in range(1, len(name) + 1):
            partial_name = name[0:idx]
            if partial_name in self.partial_index:
                self.partial_index[partial_name] += 1
            else:
                self.partial_index[partial_name] = 1

    def add(self, name):
        self.contacts.append(name)
        self.indexing(name)

        return len(self.contacts)

    def find(self, partial):
        if partial in self.partial_index:
            return self.partial_index[partial]

        return 0

    def cmd(self, op, contact):
        if op == 'add':
            return self.add(contact)
        elif op == 'find':
            print(self.find(contact))


if __name__ == '__main__':
    cm = ContactManager()

    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        cm.cmd(op, contact)


class TestContacts(unittest.TestCase):
    def test_operations(self):
        cm = ContactManager()

        cm.add("hack")
        cm.add("hackerrank")

        self.assertEqual(
            2,
            cm.find("hac")
        )

        self.assertEqual(
            0,
            cm.find("hak")
        )
