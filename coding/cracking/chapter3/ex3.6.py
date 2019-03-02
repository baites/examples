
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def push(self, value):
        node = Node(value)
        node.next = self._head
        self._head = node
        self._size += 1

    def pop(self):
        node = self._head
        self._head = node.next
        node.next = None
        self._size -= 1
        return node.value

    def peek(self):
        return self._head.value


def sort(s):
    r = Stack()
    while len(s) > 0:
        value = s.pop()
        while len(r) > 0 and value > r.peek():
            s.push(r.pop())
        r.push(value)
    return r


import random


N = 10
s = Stack()

for i in range(N):
    s.push(random.randint(0,N-1))

r = sort(s)
for i in range(N):
    print(r.pop())
