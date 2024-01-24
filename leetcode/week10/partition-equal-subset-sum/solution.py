from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        memo = {}
        def solve(i:int, s: int):
            if i >= len(nums) or s > totalSum // 2:
                return False
            if s == totalSum // 2:
                return True
            if memo.get(s) is not None:
                return memo[s]
            memo[s] = solve(i+1, s+nums[i]) or solve(i+1, s)
            return memo[s]
        return solve(0, 0)


nums = [1,5,11,5,6,3,3]
out = Solution().canPartition(nums)
print(out)

nums = [1,5,11,5]
out = Solution().canPartition(nums)
print(out)

nums = [1,2,3,5]
out = Solution().canPartition(nums)
print(out)

