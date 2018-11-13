
class MinStack:
    def __init__(self):
        self._stack = []
        self._mins = []

    def push(self, value):
        minvalue = None
        if len(self._mins) > 0:
            minvalue = self._mins[-1]
        if not minvalue or value <= minvalue:
            self._mins.append(value)
        self._stack.append(value)

    def pop(self):
        value = self._stack.pop()
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def min_value(self):
        minvalue = None
        if len(self._mins) > 0:
            minvalue = self._mins[-1]
        return minvalue


items = [4, 3, 2, 1, 1, 3, 4]

s = MinStack()

for item in items:
    s.push(item)
    print(s.min_value())
print()
for item in items:
    print(s.pop(), s.min_value())
