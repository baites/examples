
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


class Queue:

    def __init__(self):
        self._s1 = Stack()
        self._s2 = Stack()

    def push(self, value):
        while len(self._s1) > 0:
            self._s2.push(
                self._s1.pop()
            )
        self._s2.push(value)
        while len(self._s2) > 0:
            self._s1.push(
                self._s2.pop()
            )

    def pop(self):
        return self._s1.pop()


N = 10
q = Queue()

for i in range(N):
    q.push(i)

print()
for i in range(N):
    print(q.pop())
print()
