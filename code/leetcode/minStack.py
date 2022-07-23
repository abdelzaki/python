from inspect import stack


class MinStack:

    def __init__(self):
        self.stack = list()
        self.minvalueStack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimalValue = min(
            val, self.minimalValue if len(self.minvalueStack) > 0 else val)
        self.minvalueStack.append(self.minimalValue)

    def pop(self) -> None:
        self.stack.pop()
        self.minvalueStack.pop()

    def top(self) -> int:
        value = self.stack[-1]
        return value

    def getMin(self) -> int:
