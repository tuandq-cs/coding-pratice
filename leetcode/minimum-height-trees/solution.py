from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjSet = [set() for i in range(n)]
        for u, v in edges:
            adjSet[u].add(v)
            adjSet[v].add(u)
        # leaves
        leaves = deque([])
        for i in range(n):
            if len(adjSet[i]) <= 1:
                leaves.append(i)
        while (n > 2):
            n -= len(leaves)
            for _ in range(len(leaves)):
                u = leaves.popleft()
                v = adjSet[u].pop()
                adjSet[v].remove(u)
                if len(adjSet[v]) == 1:
                    leaves.append(v)
            
        res = []
        for i in leaves:
            res.append(i)
        return res