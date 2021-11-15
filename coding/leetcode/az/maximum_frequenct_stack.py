from collections import Counter, defaultdict

class FreqStack:

    def __init__(self):
        self._freq = Counter()
        self._group = defaultdict(list)
        self._max_freq = 0

    def push(self, x):
        freq = self._freq[x] +  1
        self._freq[x] = freq
        if freq > self._max_freq:
            self._max_freq = freq
        self._group[freq].append(x)

    def pop(self):
        x = self._group[self._max_freq].pop()
        self._freq[x] -= 1
        if len(self._group[self._max_freq]) == 0:
            self._max_freq -= 1
        return x
