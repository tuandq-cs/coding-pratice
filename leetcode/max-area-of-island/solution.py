from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int):
            grid[i][j] = -1
            area = 1
            for d in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                nI, nJ = i + d[0], j + d[1]
                if (0 <= nI < m) and (0 <= nJ < n) and grid[nI][nJ] == 1:
                    area += dfs(nI, nJ)
            return area
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res
                    