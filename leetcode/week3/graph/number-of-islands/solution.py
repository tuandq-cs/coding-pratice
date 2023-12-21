from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num = 0

        def dfs(i: int, j: int):
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] != "1":
                return

            grid[i][j] = '#'

            for direction in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nextI = i + direction[0]
                nextJ = j + direction[1]
                dfs(nextI, nextJ)

        def traverse(i: int, j: int):
            nonlocal num
            if grid[i][j] == "1":
                # Traverse until no directions has land
                dfs(i, j)
                num += 1
        for i in range(rows):
            for j in range(cols):
                traverse(i, j)
        return num


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
result = Solution().numIslands(grid)
print(result)

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
result = Solution().numIslands(grid)
print(result)
