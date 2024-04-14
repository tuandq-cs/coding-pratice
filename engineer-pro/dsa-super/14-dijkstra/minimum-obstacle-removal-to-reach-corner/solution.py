import heapq
import math
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cost = [[math.inf for i in range(n)] for _ in range(m)]
        cost[0][0] = 0
        pq = []
        heapq.heappush(pq, (0, (0, 0)))
        while (len(pq) != 0):
            _, (x, y) = heapq.heappop(pq)
            for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nX = x + dir[0]
                nY = y + dir[1]
                if (0 <= nX < m) and (0 <= nY < n):
                    c = cost[x][y] + grid[nX][nY]
                    if c < cost[nX][nY]:
                        cost[nX][nY] = c
                        heapq.heappush(pq, (c, (nX, nY)))
        return cost[m-1][n-1]