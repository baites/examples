
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


class SetOfStacks:
    def __init__(self, limit):
        self._stacks = [Stack()]
        self._limit = limit

    def push(self, value):
        current = self._stacks[-1]
        if len(current) > self._limit:
            self._stacks.append(Stack())
            current = self._stacks[-1]
        current.push(value)

    def pop(self):
        current = self._stacks[-1]
        value = current.pop()
        if len(current) == 0:
            del self._stacks[-1]
        return value

N = 10
s = Stack()

for i in range(N):
    s.push(i)

print(len(s))
print()
for i in range(N):
    print(s.pop())
print()
print(len(s))
print()

s = SetOfStacks(2)

for i in range(N):
    s.push(i)

print(len(s._stacks))
print()
for i in range(N):
    print(s.pop())
print()
print(len(s._stacks))
