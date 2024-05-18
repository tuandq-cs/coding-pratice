from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1 for _ in range(n)]
        def recur(i: int, nums: List[int]) -> int:
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            m = nums[i] + recur(i+2, nums)
            m = max(m, recur(i+1, nums))
            memo[i] = m
            return memo[i]
        return recur(0, nums)