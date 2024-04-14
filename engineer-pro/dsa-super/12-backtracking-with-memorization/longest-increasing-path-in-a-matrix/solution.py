from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        def backtrack(x, y: int) -> int:
            if memo[x][y] != -1:
                return memo[x][y]
            longest = 0
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nX = x + d[0]
                nY = y + d[1]
                if (0 <= nX < m) and (0 <= nY < n) and matrix[x][y] < matrix[nX][nY]:
                    longest = max(longest, backtrack(nX, nY))
            memo[x][y] = longest + 1
            return longest + 1
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, backtrack(i, j))
        return ans