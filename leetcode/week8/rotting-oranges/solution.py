from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        numMin = 0
        def dfs(i: int, j: int):
            nonlocal numMin
            if grid[i][j] != 2:
                return
            grid[i][j] = 3
            isCounted = False
            for dir in ((0,-1), (0, 1), (1, 0), (-1, 0)):
                nI, nJ = i + dir[0], j + dir[1]
                if not (0 <= nI < m and 0 <= nJ < n and grid[nI][nJ] == 1):
                    continue
                if not isCounted:
                    numMin += 1
                    isCounted = True
                grid[nI][nJ] = 2
                dfs(nI, nJ)

        for i in range(m):
            for j in range(n):
                dfs(i, j)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return numMin
    
grid = [[2,1,1],[1,1,0],[0,1,1]]
out = Solution().orangesRotting(grid)
print(out)

grid = [[2,1,1],[0,1,1],[1,0,1]]
out = Solution().orangesRotting(grid)
print(out)

grid = [[0,2]]
out = Solution().orangesRotting(grid)
print(out)

grid = [
    [2,1,1],
    [1,1,1],
    [0,1,2]
]

