from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxAmount = -1
        for i, num in enumerate(nums):
            amount = num
            if i > 2:
                amount += self.rob(nums[:i-2])
            if i + 2 < len(nums):
                amount += self.rob(nums[i+2:])
            if amount > maxAmount:
                maxAmount = amount
        return maxAmount
        # Time complexity: O(n^3)


nums = [1, 2, 3, 1]
out = Solution().rob(nums)
print(out)

nums = [2, 7, 9, 3, 1]
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
