
class ThreeStacks:

    def __init__(self, depth):
        self._array = [None]*(3*depth)
        self._pointer = [0]*3
        self._depth = depth

    def push(self, stack, value):
        assert stack >= 0 and stack < 3
        index = self._pointer[stack] + stack * self._depth
        self._array[index] = value
        self._pointer[stack] += 1

    def pop(self, stack):
        assert stack >= 0 and stack < 3
        assert self._pointer[stack] != 0
        index = self._pointer[stack] - 1 + stack * self._depth
        value = self._array[index]
        self._array[index] = None
        self._pointer[stack] -= 1
        return value

stacks = ThreeStacks(10)

for i in range(3):
    stacks.push(0, i)

for i in range(5):
    stacks.push(1, i)

for i in range(2):
    stacks.push(2, i)

for i in range(3):
    print(stacks.pop(0))
print()

for i in range(5):
    print(stacks.pop(1))
print()

for i in range(2):
    print(stacks.pop(2))
