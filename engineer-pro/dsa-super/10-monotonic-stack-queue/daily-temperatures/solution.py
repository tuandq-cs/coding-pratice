from typing import List


class Solution:
    def insert(self, i: int, temperatures: List[int], monoStack: List[int]):
        # remove those element has temp <= temp[i]
        while len(monoStack) > 0 and temperatures[monoStack[-1]] <= temperatures[i]:
            monoStack.pop()
        monoStack.append(i)

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        i = len(temperatures) - 1
        ans = [0] * len(temperatures)
        while (i >= 0):
            # add temp at i index into the monoStack
            self.insert(i, temperatures, monoStack)
            # because now, the i index is on the top of the stack
            # get the element next to the top, if there is no element, assign 0
            if len(monoStack) > 1:
                ans[i] = monoStack[len(monoStack)-2] - i
            i -= 1
        return ans