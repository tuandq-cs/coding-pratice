from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False

        memo = {}
        def solve(i: int, targetSum: int):
            if memo.get(targetSum):
                return False
            if targetSum == nums[i]:
                return True
            if targetSum < nums[i]:
                return False
            for j in range(i+1, len(nums)):
                if solve(j, targetSum-nums[i]):
                    return True
            memo[targetSum-nums[i]] = False
            return False
        for i in range(len(nums)):
            if solve(i, totalSum // 2):
                return True
        return False


nums = [1,5,11,5,6,3,3]
out = Solution().canPartition(nums)
print(out)

nums = [1,5,11,5]
out = Solution().canPartition(nums)
print(out)

nums = [1,2,3,5]
out = Solution().canPartition(nums)
print(out)

