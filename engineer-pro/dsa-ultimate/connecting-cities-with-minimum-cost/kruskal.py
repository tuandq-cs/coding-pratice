import heapq
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of cities
    @param connections: the connection info between cities
    @return: 
    """
    def getRoot(self, root: List[int], node: int):
        if root[node] == node:
            return node
        root[node] = self.getRoot(root, root[node])
        return root[node]


    def minimum_cost(self, n: int, connections: List[List[int]]) -> int:
        # min heaq
        pq = []
        for a, b, c in connections:
            heapq.heappush(pq, (c, a-1, b-1))
        root = [i for i in range(n)]
        cost = 0
        while len(pq) > 0:
            c, a, b = heapq.heappop(pq)
            u, v = self.getRoot(root, a), self.getRoot(root, b)
            if u == v:
                continue
            # join 2 group of cities
            cost += c
            root[u] = root[v]
        # check all cities is within 1 group
        setGroup = set()
        for i in range(n):
            setGroup.add(self.getRoot(root, i))
        return cost if len(setGroup) == 1 else -1
