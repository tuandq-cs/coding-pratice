class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {}

        def recur(i: int):
            if i == 1:
                return 1
            if i == 2:
                return 2
            if memo.get(i):
                return memo[i]
            ways = recur(i - 1) + recur(i - 2)
            memo[i] = ways
            return ways
        return recur(n)


out = Solution().climbStairs(n=3)
print(out)

out = Solution().climbStairs(n=45)
print(out)
