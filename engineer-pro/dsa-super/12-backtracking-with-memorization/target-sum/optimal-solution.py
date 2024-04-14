from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = [{} for i in range(n)]
        def backtrack(i: int, curSum: int):
            if i == n:
                return 1 if curSum == target else 0
            if curSum in memo[i]:
                return memo[i][curSum]
            ans = 0
            ans += backtrack(i+1, curSum + nums[i])
            ans += backtrack(i+1, curSum - nums[i])
            memo[i][curSum] = ans
            return memo[i][curSum]
        return backtrack(0, 0)
        # Time: O(n*m), 1 <= n = nums.length <= 20, m is target range, -1000 <= m <= 1000
        # Worse case O(20*2000) = O(40000)