from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append(((i, j), 0))
        numMin = 0
        while len(q) != 0:
            (i, j), curMin = q.popleft()
            if grid[i][j] != 2:
                continue
            grid[i][j] = 3
            for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nI, nJ = i + dir[0], j + dir[1]
                if (0 <= nI < m and 0 <= nJ < n and grid[nI][nJ] == 1):
                    grid[nI][nJ] = 2
                    q.append(((nI, nJ), curMin + 1))
                    numMin = curMin + 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return numMin
        # Time: O(n)
        # Space: O(n) for queue


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
out = Solution().orangesRotting(grid)
print(out)

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
out = Solution().orangesRotting(grid)
print(out)


grid = [[0, 2]]
out = Solution().orangesRotting(grid)
print(out)

grid = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
out = Solution().orangesRotting(grid)
print(out)
