from typing import List


class Solution:

    def dfs(self, i: int, j: int, path: set) -> int:
        path.add((i,j))
        m = 0
        for nI, nJ in self.adj[(i,j)]:
            if (nI, nJ) in path:
                continue
            copPath = path.copy()
            tmp = self.dfs(nI, nJ, copPath)
            m = max(m, tmp)
        return m + self.grid[i][j]


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        adj = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                adj[(i,j)] = []
                # look around 4 directions
                for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                    nI, nJ = i + dx, j + dy
                    if 0 <= nI < m and 0 <= nJ < n and grid[nI][nJ] != 0:
                        adj[(i,j)].append((nI, nJ))
        # dfs on each gold cells (max = 25)
        self.adj = adj
        self.grid = grid
        res = 0
        for i,j in adj:
            m = self.dfs(i, j, set())
            res = max(res, m)
        return res