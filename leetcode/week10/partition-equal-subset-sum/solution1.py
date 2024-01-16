from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        targetSum = s // 2
        memo = [{} for _ in range(len(nums))]
        def solve(i: int, remainingSum: int):
            if remainingSum == 0:
                return True
            if i >= len(nums) or remainingSum < 0:
                return False
            if memo[i].get(remainingSum) is not None:
                return memo[i][remainingSum]
            ans = solve(i+1, remainingSum-nums[i]) or solve(i+1, remainingSum)
            memo[i][remainingSum] = ans
            return ans
        return solve(0, targetSum)
        
nums = [1,5,11,5]
out = Solution().canPartition(nums)
print(out)

nums = [1,5,11,5]
out = Solution().canPartition(nums)
print(out)

nums = [1,2,3,5]
out = Solution().canPartition(nums)
print(out)