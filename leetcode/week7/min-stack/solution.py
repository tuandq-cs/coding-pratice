class MinStack:

    def __init__(self):
        self.s = []
        self.minS = []

    def push(self, val: int) -> None:
        self.s.append(val)

        if len(self.minS) == 0 or val <= self.getMin():
            self.minS.append(val)

    def pop(self) -> None:
        ele = self.s.pop()
        if ele == self.getMin():
            self.minS.pop()

    def top(self) -> int:
        return self.s[len(self.s)-1]

    def getMin(self) -> int:
        return self.minS[len(self.minS)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
