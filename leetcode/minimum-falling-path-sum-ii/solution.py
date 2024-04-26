import heapq
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(1, n):
            r = heapq.nsmallest(2, grid[i-1])
            for j in range(n):
                grid[i][j] += r[1] if grid[i-1][j] == r[0] else r[0]
        return min(grid[-1])