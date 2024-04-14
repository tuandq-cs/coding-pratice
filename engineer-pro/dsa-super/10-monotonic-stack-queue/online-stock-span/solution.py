class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        while (len(self.stack) > 0 and self.stack[-1][0] <= price):
            self.stack.pop()
        i = j = self.i
        if len(self.stack) > 0:
            j = self.stack[-1][1] + 1
        else:
            j = 0
        self.stack.append((price, self.i))
        self.i += 1
        return i - j + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)