"""
Queues: A Tale of Two Stacks 

https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
"""


class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def peek(self):
        if len(self.outbox) == 0:
            self.reverse_to_outbox()

        return self.outbox[-1]

    def pop(self):
        if len(self.outbox) == 0:
            self.reverse_to_outbox()

        return self.outbox.pop(-1)

    def reverse_to_outbox(self):
        while len(self.inbox) > 0:
            self.outbox.append(self.inbox.pop(-1))

    def put(self, value):
        self.inbox.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
