from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1]*len(nums)
        for i in range(1, len(nums)):
            answers[i] = answers[i-1] * nums[i-1]
        cum_prod = 1
        for i in range(len(nums)-1, -1, -1):
            answers[i] *= cum_prod
            cum_prod *= nums[i]
        return answers


# General case
nums = [1, 2, 3, 4]
# cum_prod = 24
# answers = [24, 12, 8, 6]
answers = Solution().productExceptSelf(nums=nums)
print(answers)

# Corners cases
# n = 2
nums = [5, 7]
# cum_prod = 7
# answers = [7, 5]
answers = Solution().productExceptSelf(nums=nums)
print(answers)
# an item equal 0
nums = [-1, 1, 0, -3, 3]
answers = Solution().productExceptSelf(nums=nums)
print(answers)
