import heapq
import math
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        effort = [[math.inf for _ in range(n)] for _ in range(m)]
        effort[0][0] = 0
        pq = []
        # effort, (x, y)
        heapq.heappush(pq, (0, (0, 0)))
        while len(pq) != 0:
            _, (x, y) = heapq.heappop(pq)
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nX = x + d[0]
                nY = y + d[1]
                if (0 <= nX < m) and (0 <= nY < n):
                    e = max(effort[x][y], abs(heights[x][y] - heights[nX][nY]))
                    if e < effort[nX][nY]:
                        effort[nX][nY] = e
                        heapq.heappush(pq, (e, (nX, nY)))
        return effort[m-1][n-1]
                        
