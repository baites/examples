"""Implement pure python SinglyLinkedList."""

from collections.abc import Sized, Iterator, Iterable

class SinglyLinkedNode:
    """Implement a double linked node."""

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedListIter(Iterator):
    """Implement a list iterator."""
    def __init__(self, node):
        self._node = node
        self._stop_iter = False

    def __next__(self):
        if self._stop_iter:
            raise StopIteration
        if not self._node:
            self._stop_iter = True
            raise StopIteration
        value = self._node.value
        self._node = self._node.next
        return value


class SinglyLinkedList(Sized, Iterable):
    """Implement the actual list."""
    def __init__(self):
        """Constructor."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return list size."""
        return self._size

    def __iter__(self):
        """Return a list iterator."""
        return SinglyLinkedListIter(self._head)

    def push_front(self, value):
        """Push value in the front of the list."""
        node = SinglyLinkedNode(value)
        node.next = self._head
        self._head = node
        self._size += 1

    def pop_front(self):
        """Pop value from the front of the list."""
        if not self._head:
            raise EmptyList('Cannot pop front value.')
        node = self._head
        self._head = node.next
        node.next = None
        self._size -= 1
        return node.value

    def front(self):
        """Return value at the front of the list."""
        if not self._head:
            raise EmptyList('Cannot return front value.')
        return self._head.value
