from typing import List


class Solution:
    def calcMax(self, i: int, j: int, grid: List[List[int]]):
        n = len(grid)
        m = 0
        for dx in range(3):
            nI = i + dx
            for dy in range(3):
                nJ = j + dy
                if 0 <= nI < n and 0 <= nJ < n:
                    m = max(m, grid[nI][nJ])
        return m

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                res[i][j] = self.calcMax(i, j, grid)
        return res