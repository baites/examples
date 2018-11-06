"""Implementing priority queue with updatable keys"""


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, item):
        return self.key < item.key

    def __repr__(self):
        return '({},{})'.format(
            self.key,
            self.value
        )


class PQueue:
    def __init__(self):
        self._heap = []
        self._index = {}

    def __contains__(self, value):
        return value in self._index

    def _swap(self, i, j):
        tmp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._index[self._heap[j].value] = i
        self._heap[j] = tmp
        self._index[tmp.value] = j

    def _sift_up(self, i):
        while i > 0:
            p = (i-1)//2
            if self._heap[i] < self._heap[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        mini = i
        l = 2*i + 1
        if l < self._size and\
            self._heap[l] < self._heap[mini]:
            mini = l
        r = 2*i + 2
        if r < self._size and\
            self._heap[r] < self._heap[mini]:
            mini = r
        if mini != i:
            self._swap(i, mini)
            self._sift_down(mini)

    def _update(self, key, value):
        i = self._index[value]
        item = self._heap[i]
        old_key = item.key
        item.key = key
        if key < old_key:
            self._sift_up(i)
        else:
            self._sift_down(i)

    def empty(self):
        return self._size == 0

    def push(self, key, value):
        if value in self._index:
            self._update(key, value)
            return
        self._heap.append(Item(key, value))
        self._size = len(self._heap)
        self._index[value] = self._size - 1
        self._sift_up(self._size - 1)

    def pop(self):
        if self._size == 0:
            raise IndexError('pop from empty queue')
        key = self._heap[0].key
        value = self._heap[0].value
        del self._index[value]
        item = self._heap.pop()
        self._size -= 1
        if self._size == 0:
            return key, value
        self._heap[0] = item
        self._index[item.value] = 0
        self._sift_down(0)
        return key, value
