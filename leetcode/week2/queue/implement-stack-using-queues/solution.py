from queue import Queue
from typing import List


class MyStack:

    def __init__(self):
        self.q = Queue(0)

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        # Time Complexity: O(n), because the constraint of just using pushBack, popFront operation
        for _ in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        v = self.q.get()
        return v

    def top(self) -> int:
        v = self.pop()
        self.push(v)
        return v

    def empty(self) -> bool:
        return self.q.empty()


def debug(ops: List[str], inps: List[List[int]]):
    obj = MyStack()
    out = [None]
    for i in range(1, len(ops)):
        if ops[i] == 'push':
            out.append(obj.push(inps[i][0]))
        elif ops[i] == 'pop':
            out.append(obj.pop())
        elif ops[i] == 'top':
            out.append(obj.top())
        else:
            out.append(obj.empty())
    print(out)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


ops = ["MyStack", "push", "push", "top", "pop", "empty"]
inps = [[], [1], [2], [], [], []]
# push 1: q = 1
# push 2: q = 1 <- 2, size = 2
# top: q = 1 <- 2, out = 2
# pop: q = 1, out = 2
# empty: size = 1 => out = False
# out = [null, null, 2, 2, False]
debug(ops, inps)

ops = ["MyStack", "empty"]
inps = [[], []]
debug(ops, inps)
