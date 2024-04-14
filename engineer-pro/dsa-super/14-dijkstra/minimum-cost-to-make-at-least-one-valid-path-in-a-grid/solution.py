import heapq
import math
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 1: right
        # 2: left
        # 3: lower
        # 4: upper
        cost = [[math.inf for _ in range(n)] for _ in range(m)]
        cost[0][0] = 0
        pq = []
        heapq.heappush(pq, (0, (0, 0)))
        while (len(pq) != 0):
            _, (x, y) = heapq.heappop(pq)
            for i, d in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0))):
                nX = x + d[0]
                nY = y + d[1]
                if (0 <= nX < m) and (0 <= nY < n):
                    c = cost[x][y] + (0 if (i+1) == grid[x][y] else 1)
                    if c < cost[nX][nY]:
                        cost[nX][nY] = c
                        heapq.heappush(pq, (c, (nX, nY)))
        return cost[m-1][n-1]
    
grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
out = Solution().minCost(grid)
print(out)