class MinStack:

    def __init__(self):
        self._stack = []
        self._stack_min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._stack_min) == 0 or val < self._stack_min[-1]:
            self._stack_min.append(val)
        else:
            self._stack_min.append(self._stack_min[-1])

    def pop(self) -> None:
        val = self._stack.pop()
        self._stack_min.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()