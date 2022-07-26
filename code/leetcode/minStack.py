


class MinStack:

    def __init__(self):
        self.stack = list()
        self.minvalueStack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimalValue = min(
            val, self.minvalueStack[-1] if self.minvalueStack  else val)
        self.minvalueStack.append(minimalValue)

    def pop(self) -> None:
        self.stack.pop()
        self.minvalueStack.pop()

    def top(self) -> int:
        value = self.stack[-1]
        return value

    def getMin(self) -> int:
        return self.minvalueStack[-1] if self.minvalueStack else 0
