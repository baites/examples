"""Implement pure python DoublyLinkedList."""

from collections.abc import Sized, Iterator, Reversible

class DoublyLinkedNode:
    """Implement a double linked node."""

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedListIter(Iterator):
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


class DoublyLinkedListReversed(Iterator):
    """Implement a list reversed iterator."""
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
        self._node = self._node.prev
        return value


class DoublyLinkedList(Sized, Reversible):
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
        return DoublyLinkedListIter(self._head)

    def __reversed__(self):
        """Return a reversed list iterator."""
        return DoublyLinkedListReversed(self._tail)

    def push_front(self, value):
        """Push value in the front of the list."""
        node = DoublyLinkedNode(value)
        node.next = self._head
        if self._head:
            self._head.prev = node
        self._head = node
        self._size += 1
        if not self._tail:
            self._tail = self._head

    def pop_front(self):
        """Pop value from the front of the list."""
        if not self._head:
            raise EmptyList('Cannot pop front value.')
        node = self._head
        self._head = node.next
        self._head.prev = None
        node.next = None
        self._size -= 1
        return node.value

    def front(self):
        """Return value at the front of the list."""
        if not self._head:
            raise EmptyList('Cannot return front value.')
        return self._head.value

    def push_back(self, value):
        """Push value in the back of the list."""
        node = DoublyLinkedNode(value)
        node.prev = self._tail
        if self._tail:
            self._tail.next = node
        self._tail = node
        self._size += 1
        if not self._head:
            self._head = self._tail

    def pop_back(self):
        """Pop value from the back of the list."""
        if not self._head:
            raise EmptyList('Cannot pop back value.')
        node = self._tail
        self._tail = node.prev
        self._tail.next = None
        node.prev = None
        self._size -= 1
        return node.value

    def back(self):
        """Return value at the back of the list."""
        if not self._tail:
            raise EmptyList('Cannot return back value.')
        return self._tail.value
