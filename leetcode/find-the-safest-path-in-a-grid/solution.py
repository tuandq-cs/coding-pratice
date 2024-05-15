from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # n = 400 => n^2 = 160000, n^3 = 64000000
        # k is num of thieves => k * (n^2 - k) = k*n^2 - k^2
        n = len(grid)
        maxDis = n + n + 2
        thieves = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    thieves.append((i,j))
                else:
                    grid[i][j] = -1

        # bfs from thieves
        q = deque([])
        for i,j in thieves:
            q.append((i,j,0))
        while (len(q) > 0):
            i,j,dis = q.popleft()
            for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                nX, nY = i + dx, j + dy
                if 0 <= nX < n and 0 <= nY < n and (grid[nX][nY] == -1 or dis+1 < grid[nX][nY]):
                    grid[nX][nY] = dis+1
                    q.append((nX, nY, dis+1))
        # dfs from 0, 0 to n-1, n-1
        # res = self.dfs(0, 0, grid, visited, maxDis)
        pq = []
        pq.append((-grid[0][0],(0,0)))
        visited = [[0 for _ in range(n)] for _ in range(n)]

        while (len(pq) > 0):
            dis, (i, j) = heappop(pq)
            dis = -dis
            if i == n-1 and j == n-1:
                return dis

            visited[i][j] = 1
            for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                nX, nY = i + dx, j + dy
                if 0 <= nX < n and 0 <= nY < n and not visited[nX][nY]:
                    grid[nX][nY] = min(dis, grid[nX][nY])
                    visited[nX][nY] = 1
                    heappush(pq, (-grid[nX][nY], (nX, nY)))
        return 0
            

