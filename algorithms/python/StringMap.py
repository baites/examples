#! /usr/bin/env python

PRIME = 2**61-1


class StringMap:

    def __init__(self, size = 13):
        self._size = size
        self._list = [(None,) for i in range(size)]

    @staticmethod
    def _hfunc(string, basis, prime):
        hash = 0
        for i in reversed(range(len(string))):
            hash = hash * basis + ord(string[i]) % prime
        return value % size

    def _setitem(self, key, value, keyhash, count = 1):
        if self._list[keyhash][0] and self._list[keyhash][0] != '__deleted__':
            keyhash = (keyhash + count * (1 + count)) % self._size
            if count == 2*self._size:
                raise MemoryError('Map fully used, needs to be resized.')
            self._setitem(key, value, keyhash, count + 1)
        else:
            self._list[keyhash] = (key, value)

    def __setitem__(self, key, value):
        self._setitem(key, value,
            self._hfunc(key, self._size)
        )

    def _getitem(self, key, keyhash, count = 1):
        storedkey = self._list[keyhash][0];
        if key != storedkey:
            keyhash = (keyhash + count * self._hfunc(key, self._size)) % self._size
            return self._getitem(key, keyhash, count + 1)
        else:
            return self._list[keyhash][1]

    def __getitem__(self, key):
        return self._getitem(key,
            self._hfunc(key, self._size)
        )

    def _delitem(self, key, keyhash, count = 1):
        storedkey = self._list[keyhash][0];
        if key != storedkey:
            keyhash = (keyhash + count * self._hfunc(key, self._size)) % self._size
            self._delitem(key, keyhash, count + 1)
        else:
            self._list[keyhash] = ('__deleted__',)

    def __delitem__(self, key):
        self._delitem(key,
            self._hfunc(key, self._size)
        )


hmap = StringMap()
hmap['hola'] = 1
hmap['chau'] = 2
hmap['wolf'] = 3
hmap['dog'] = 4
hmap['cat'] = 5
hmap['lion'] = 6
hmap['elephant'] = 7
hmap['tiger'] = 8
hmap['bird'] = 9
hmap['human'] = 10
hmap['mom'] = 11
hmap['dad'] = 12
hmap['bye'] = 13
hmap['uch'] = 13

print(hmap._list)
#print(hmap['human'])

#del hmap['cat']
#print(hmap._list)
#hmap['cat'] = 5
#print(hmap._list)
