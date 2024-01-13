class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2
            if memo.get(n) is not None:
                return memo[n]
            ways = dfs(n - 1) + dfs(n - 2)
            memo[n] = ways
            return ways
        return dfs(n)

out = Solution().climbStairs(4)
print(out)
