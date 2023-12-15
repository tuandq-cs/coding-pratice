

from typing import List


class MyQueue:
    def __init__(self):
        self.inp_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.inp_stack.append(x)

    def pop(self) -> int:
        if len(self.out_stack) == 0:
            while (len(self.inp_stack) != 0):
                self.out_stack.append(self.inp_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        v = self.pop()
        self.out_stack.append(v)
        return v

    def empty(self) -> bool:
        return len(self.inp_stack) == 0 and len(self.out_stack) == 0


def debug(ops: List[str], inps: List[List[int]]):
    obj = MyQueue()
    out = [None]
    for i in range(1, len(ops)):
        if ops[i] == 'push':
            out.append(obj.push(inps[i][0]))
        elif ops[i] == 'pop':
            out.append(obj.pop())
        elif ops[i] == 'peek':
            out.append(obj.peek())
        else:
            out.append(obj.empty())
    print(out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


ops = ["MyQueue", "push", "push", "peek", "pop", "empty"]
inps = [[], [1], [2], [], [], []]
# inp_stack = []
# out_stack = [2]
# out = [null, null, null, 1, 1, False]
debug(ops, inps)
