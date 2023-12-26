from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        maxAmount = nums[0]
        for i, _ in enumerate(nums):
            if i == 0 or i == 1:
                amount = nums[i]
            elif i == 2:
                amount = nums[2] + nums[0]
            else:
                amount = nums[i] + max(memo[i-2], memo[i-3])
            if amount > maxAmount:
                maxAmount = amount
            memo[i] = amount
        return maxAmount


nums = [1, 2, 3, 1]
out = Solution().rob(nums)
print(out)

nums = [2, 7, 9, 3, 1, 10, 12]
out = Solution().rob(nums)
print(out)

nums = [9]
out = Solution().rob(nums)
print(out)

nums = [9, 10]
out = Solution().rob(nums)
print(out)

nums = [1, 2, 1]
out = Solution().rob(nums)
print(out)
