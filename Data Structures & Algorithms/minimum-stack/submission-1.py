class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currMin = 10000000

    def push(self, val: int) -> None:

        if self.minStack == []:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
                self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:

        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
