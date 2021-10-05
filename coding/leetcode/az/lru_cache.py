
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self._cache = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self._cache[key] = value
        self._cache.move_to_end(key)
        if len(self._cache) > self._capacity:
            self._cache.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)