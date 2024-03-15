import heapq
import math
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dis = [[math.inf for _ in range(n)] for _ in range(n)]
        dis[0][0] = grid[0][0]
        pq = []
        heapq.heappush(pq, (dis[0][0], (0, 0)))
        while len(pq) != 0:
            _, (x, y) = heapq.heappop(pq)
            for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nX = x + dir[0]
                nY = y + dir[1]
                if (0 <= nX < n) and (0 <= nY < n):
                    d = max(dis[x][y], grid[nX][nY])
                    if d < dis[nX][nY]:
                        dis[nX][nY] = d
                        heapq.heappush(pq, (d, (nX, nY)))
        return dis[n-1][n-1]
        # Time: O(n^2) + 4*n^2*Log(n^2) = O(n^2) * O(logn)