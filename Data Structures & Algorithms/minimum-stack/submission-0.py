class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            min_so_far = val
        else:
            min_prev = self.stack[-1][1]
            min_so_far = min(val, min_prev)
        
        self.stack.append((val, min_so_far))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
