class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def solve(i: int, j: int):
            if not (0 <= i < n and 0 <= j < m):
                return 0
            if i == n-1 and j == m-1:
                return 1
            if memo.get(f"{i},{j}") is not None:
                return memo[f"{i},{j}"]
            numPaths = 0
            for d in ((1, 0), (0, 1)):
                nI, nJ = i + d[0], j + d[1]
                numPaths += solve(nI, nJ)
            memo[f"{i},{j}"] = numPaths
            return numPaths
        return solve(0, 0)


out = Solution().uniquePaths(m=3, n=7)
print(out)


out = Solution().uniquePaths(m=3, n=2)
print(out)

out = Solution().uniquePaths(m=1, n=1)
print(out)
