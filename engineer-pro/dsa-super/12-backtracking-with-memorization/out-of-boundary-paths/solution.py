class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(maxMove+1)]
        def backtrack(x, y, maxMove) -> int:
            if maxMove == 0:
                return 0
            if memo[maxMove][x][y] != -1:
                return memo[maxMove][x][y]
            numPaths = 0
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nX = x + d[0]
                nY = y + d[1]
                if 0 <= nX < m and 0 <= nY < n:
                    numPaths += backtrack(nX, nY, maxMove-1)
                else:
                    numPaths += 1
            memo[maxMove][x][y] = numPaths
            return numPaths
        return backtrack(startRow, startColumn, maxMove) % (10**9 + 7)