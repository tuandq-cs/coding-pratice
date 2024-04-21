from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = [[]for _ in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        q = deque([])
        q.append(source)
        visited = [0 for _ in range(n)]
        visited[source] = 1
        while (len(q) > 0):
            u = q.pop()
            if u == destination:
                return True
            for v in adjList[u]:
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
        return False
        # Time: O(n) + O(m), m = n - 1 => O(n)
        # Space: O(n)
                