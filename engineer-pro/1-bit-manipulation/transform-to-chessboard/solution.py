import math
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        memo = {}
        finalState = []
        fsOne = []
        for i in range(n):
            v = 0 << n
            for j in range(n):
                if (i*n + j) & 1 == 0:
                    setBit(v, j)
            fsOne.append(v)
        fsTwo = []
        for i in range(n):
            v = 0 << n
            for j in range(n):
                if (i*n + j) & 1 != 0:
                    setBit(v, j)
            fsOne.append(v)
        
            
        def solve(state: List[int]):
            hKey = ','.join(state)
            if memo.get(hKey) is not None:
                return memo[hKey]
            minMove = None
            nextStates = getNextState(state)
            for nS in nextStates:
                nM = solve(nS)
                if nM == -1:
                    continue
                if minMove == None or minMove > nM:
                    minMove = nM
            memo[hKey] = -1 if minMove is None else minMove
            return memo[hKey]
