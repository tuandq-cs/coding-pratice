from collections import deque
from typing import List


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        def getStr(state: List[int]) -> str:
            return ''.join([f'{i}' for i in state])
        def neighbors(state: List[int]):
            res = []
            for i in range(4):
                for j in [-1, 1]:
                    newState = state.copy()
                    newState[i] = (newState[i] + j + 10) % 10
                    res.append(newState)
            return res
        sDeadend = set(deadends)
        q = deque([])
        q.append([0, 0, 0, 0])
        steps = 0
        while (len(q) > 0):
            for i in range(len(q)):
                comb = q.popleft()
                combStr = getStr(comb)
                if combStr in sDeadend:
                    continue
                sDeadend.add(combStr) # marked as visited
                if combStr == target:
                    return steps
                for nei in neighbors(comb):
                    q.append(nei)
            steps += 1
        return -1
                    