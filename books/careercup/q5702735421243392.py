
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DictWithLast:
    def __init__(self):
        self._map = {}
        self._tail = None

    def set(self, key, value):
        node = Node(value)
        if self._tail is None:
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._map[key] = node

    def get(self, key):
        return self._map[key].value

    def last(self):
        assert self._tail is not None
        return self._tail.value

    def delete(self, key):
        node = self._map[key]
        if len(self._map) == 1:
            self._tail = None
        elif node.next is None:
            node.prev.next = None
            self._tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        del self._map[key]


dlast = DictWithLast()

dlast.set(1, 'A')
dlast.set(2, 'B')
dlast.set(3, 'C')
print(dlast.get(3)) # print "C"
print(dlast.last()) # print "C"
dlast.delete(2)
print(dlast.last()) # print "C"
dlast.delete(3)
print(dlast.last()) # print "A"
dlast.delete(1)
print(dlast.last()) # Assert error!
